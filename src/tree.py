import os
from functools import reduce
import json

branch = '├──'
pipe = '│'
end = '└──'
dash = '──'

root_folder = '../npc'
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

def load_file_mapping(file_mapping_path):
    with open(file_mapping_path, 'r') as file:
        return json.load(file)

file_mapping = load_file_mapping("api/file_mapping.json")

def _draw_tree(tree, level, file, last=False, sup=[], is_root=False):
    def update(left, i):
        if i < len(left):
            left[i] = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        return left

    if not is_root:
        prefix = ''.join(reduce(update, sup, ['{}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.format(pipe)] * level))

        if isinstance(tree.tag, tuple):
            tag, url = tree.tag
            tag = tag.replace('_', ' ').replace(',', '&#44;')  # Replace underscores and commas
            tree_line = prefix + (end if last else branch) + '{}&nbsp;&nbsp;'.format(dash) + f'<strong>{tag}</strong>' + f" [↗]({url})"
        else:
            tree_line = prefix + (end if last else branch) + '{}&nbsp;&nbsp;'.format(dash) + f'<strong>{tree.tag.replace("_", " ")}</strong>'

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
            _draw_tree(tree, 0, file, is_root=True)
        _draw_tree(trees[-1], 0, file, True, [0], is_root=True)

def build_tree_from_mapping(mapping, base_url, only_empty=False, only_unverified=False, only_verified=False):
    def process_mapping(mapping, path_parts):
        nodes = []

        for key, value in mapping.items():
            current_path = os.path.join(*path_parts, key)
            current_url = os.path.join(base_url, current_path).replace("\\", "/").replace(" ", "%20")

            if isinstance(value, dict):
                node = Node((key, current_url), *process_mapping(value, path_parts + [key]))  # Store directory name as tuple
                if node.nodes:
                    nodes.append(node)
            else:
                if only_empty and value != "EMPTY":
                    continue
                elif only_unverified and value != "UNVERIFIED":
                    continue
                elif only_verified and value != "VERIFIED":
                        continue
                
                leaf = Leaf((key, current_url))
                nodes.append(leaf)

        return nodes

    return Node(os.path.basename(root_folder), *process_mapping(mapping, []))

def post_process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for i, line in enumerate(lines):
            # Remove "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" from the beginning of each line
            line = line.replace("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", "", 1)

            # Replace the first character of the first line with ".&nbsp;&nbsp;"
            if i == 0:
                line = ".&nbsp;&nbsp;" + line[1:]

            file.write(line)

def add_navigation(filename, current_tree_index):
    navigation = [
        f'1. All Transcripts: [↗](./all_transcripts.md)',
        f'2. Verified Transcripts: [↗](./verified_transcripts.md)',
        f'3. Empty Transcripts: [↗](./empty_transcripts.md)',
        f'4. Unverified Transcripts: [↗](./unverified_transcripts.md)',
    ]

    # Remove link for the current tree
    navigation[current_tree_index] = navigation[current_tree_index].split(" [↗]")[0]

    with open(filename, 'r') as file:
        content = file.read()

    with open(filename, 'w') as file:
        file.write('\n'.join(navigation) + '\n\n' + content)

# Build trees
all_files_tree = build_tree_from_mapping(file_mapping, repo_url)
verified_files_tree = build_tree_from_mapping(file_mapping, repo_url, only_verified=True)
empty_files_tree = build_tree_from_mapping(file_mapping, repo_url, only_empty=True)
unverified_files_tree = build_tree_from_mapping(file_mapping, repo_url, only_unverified=True)

# Draw trees and save them to files
draw_tree([all_files_tree], '../doc/all_transcripts.md')
draw_tree([verified_files_tree], '../doc/verified_transcripts.md')
draw_tree([empty_files_tree], '../doc/empty_transcripts.md')
draw_tree([unverified_files_tree], '../doc/unverified_transcripts.md')

# Post-process files
post_process_file('../doc/all_transcripts.md')
post_process_file('../doc/verified_transcripts.md')
post_process_file('../doc/empty_transcripts.md')
post_process_file('../doc/unverified_transcripts.md')

# Add navigation
add_navigation('../doc/all_transcripts.md', 0)
add_navigation('../doc/verified_transcripts.md', 1)
add_navigation('../doc/empty_transcripts.md', 2)
add_navigation('../doc/unverified_transcripts.md', 3)