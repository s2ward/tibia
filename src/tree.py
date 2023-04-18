import os
from functools import reduce


branch = '├──'
pipe = '│'
end = '└──'
dash = '──'

root_folder = '/home/s2w/tibia/npc'
repo_url = 'https://github.com/s2ward/tibia/blob/main/npc'


class Tree(object):
    def __init__(self, tag):
        self.tag = tag


class Node(Tree):
    def __init__(self, tag, *nodes):
        super(Node, self).__init__(tag)
        self.nodes = list(nodes)


class Leaf(Tree):
    pass


def _draw_tree(tree, level, file, last=False, sup=[]):
    def update(left, i):
        if i < len(left):
            left[i] = '&nbsp;&nbsp;&nbsp;&nbsp;'
        return left

    prefix = ''.join(reduce(update, sup, ['{}&nbsp;&nbsp;&nbsp;'.format(pipe)] * level))
    if isinstance(tree.tag, tuple):
        tag, url = tree.tag
        tree_line = prefix + (end if last else branch) + '{}&nbsp;'.format(dash) + tag + f" [↗]({url})"
    else:
        tree_line = prefix + (end if last else branch) + '{}&nbsp;'.format(dash) + str(tree.tag)

    file.write(tree_line + '  \n')

    if isinstance(tree, Node):
        if not tree.nodes:  # check for empty nodes
            return
        level += 1
        for node in tree.nodes[:-1]:
            _draw_tree(node, level, file, sup=sup)
        _draw_tree(tree.nodes[-1], level, file, True, [level] + sup)



def draw_tree(trees, filename):
    with open(filename, 'w') as file:
        for tree in trees[:-1]:
            _draw_tree(tree, 0, file)
        _draw_tree(trees[-1], 0, file, True, [0])


def build_tree(folder, only_empty=False, only_unverified=False):
    def process_folder(folder):
        nodes = []

        for entry in sorted(os.listdir(folder)):
            entry_path = os.path.join(folder, entry)

            if os.path.isdir(entry_path):
                node = Node(entry, *process_folder(entry_path))
                if node.nodes:
                    nodes.append(node)
            elif only_empty and not entry.endswith('_EMPTY.txt'):
                continue
            elif only_unverified and not entry.endswith('_UNVERIFIED.txt'):
                continue
            else:
                entry_url = os.path.join(repo_url, os.path.relpath(entry_path, root_folder)).replace("\\", "/").replace(" ", "%20")
                leaf = Leaf((entry, entry_url))
                nodes.append(leaf)

        return nodes

    return Node(os.path.basename(folder), *process_folder(folder))

import itertools

# Build trees
all_files_tree = build_tree(root_folder)
empty_files_tree = build_tree(root_folder, only_empty=True)
unverified_files_tree = build_tree(root_folder, only_unverified=True)

# Draw trees and save them to files
draw_tree([all_files_tree], 'all_files_tree.md')
draw_tree([empty_files_tree], 'empty_files_tree.md')
draw_tree([unverified_files_tree], 'unverified_files_tree.md')
