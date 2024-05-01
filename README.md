# Tibia  

A repository for all things Tibia.  

- TalesOfTibia.com: [Open Source](https://github.com/s2ward/talesoftibia.com)
- Discord: [Explorer Society](https://discord.gg/JRvjSuU99U)
- Search Transcripts: [NPSearch](https://www.talesoftibia.com/npsearch)   
- Search Books: [LIBSearch](https://www.talesoftibia.com/libsearch)  
- Research: [s2ward/docs](https://github.com/s2ward/docs), [reddit](https://www.reddit.com/r/SolvingTibia)   
- All Transcripts: [↗](./doc/all_transcripts.md)  

The `npc/` directory and its content is used by [NPSearch](https://www.talesoftibia.com/npsearch)  
The `api/books.json` contains 1370~ books and is used by [LIBSearch](https://www.talesoftibia.com/libsearch)

## How to contribute to [NPSearch](https://www.talesoftibia.com/npsearch)  

A great way to contribute is by checking [unverified or empty](./doc/unverified_empty_transcripts.md) transcripts and pick one.  
You may look into "Hotkey Mania" below to ask thousands of words per minute if you want to document an entire NPCs transcripts. 

By searching in the tree view from above link, you can quickly get to your NPC you are looking for. (CTRL + F "A Prisoner").  

1. When you have your transcript(s), paste your content in an NPC file in this format:  

```
Player: <your keyword>  
NPC: <npc response>  
```

We also strive to group up what makes sense.

```markdown
# Introduction Queries
hi, name, job, time

# Miscellaneous Queries
army, news, rumors

# Queries About Places
thais, venore, carlin

# Queries About Other Characters
sam, frodo, oswald

# Chained Conversations
Follow the flow as NPC leads with new keywords

# Quest-Related Conversations
- holy orchid (Wizard Outfits Quest)

# Ending the Conversation
bye
```

Example: [Chester Kahs](https://github.com/s2ward/tibia/blob/main/npc/Thais/Chester_Kahs.txt)

If they have the same response for e,g, 'offer', 'goods' and 'buy', use format:  
Player: offer / goods / buy

2. Create a pull-request.
Note: You can ask for collaborator access in discord/reddit or in a pull-request. 

If you want to contribute but have no idea how, you may also send the transcripts through:  
- [discord](https://discord.gg/JRvjSuU99U) (preferred)  
- [reddit](https://www.reddit.com/user/s2w)

### Tree views  
- All Transcripts: [↗](./doc/all_transcripts.md)   
- Verified Transcripts: [↗](./doc/verified_transcripts.md)   
- Empty transcripts: [↗](./doc/empty_transcripts.md)  
- Unverified transcripts: [↗](./doc/unverified_transcripts.md)  
- Empty or Unverified transcripts: [↗](./doc/unverified_empty_transcripts.md)  

npc/ directory structure: [npc/town/subarea/npc.txt](https://github.com/s2ward/tibia/tree/main/npc)
```
├── Yalahar
│   ├── A_Beautiful_Girl.txt
│   ├── Beregar
│   │   ├── Bolfona.txt
│   │   ├── Harog.txt
│   │   └── ...
│   ├── Beregar_Mines
│   │   ├── ...
... 
And so on.  
```

### Accessible Resources at `resources.talesoftibia.com`

- **JSON Data**
  - NPC conversations, metadata, books, and book images:
    - `/data/npcs/transcripts.json`
    - `/data/npcs/npc-data.json`
    - `/data/books/books.json`
    - `/data/books/book-images.json`

- **Images**
  - NPC, book, spell, and creature images, padded to square in .png format:
    - `/images/npcs/`
    - `/images/books/`
    - `/images/spells/`
    - `/images/creatures/`


# Hotkey Mania

To find tricky, hidden single-word keywords, I've made a hotkey preset you can import into your personal hotkey file.  

Link: [hotkeys.json](https://github.com/s2ward/tibia/blob/main/hotkeys.json)  

### See it in action on YouTube --> [here!](https://youtu.be/YMx6i2K9K00?t=41) <--

It consists of strings of unique words with a maximum of 255 characters.  
- These strings are populated to Action-Bar buttons. 
- Duplicate words by design randomly spread out between buttons

There are currently three hotkey presets: "NPC1", "NPC2" and "NPC3". You can cycle through them using CTRL + J.  
The content of the hotkey presets are as follows (in order):  

- 15 000 words that **NPC**s respond to and answer with.  
- 10 000 most **common**ly used english words.  
- 15 000 words we find in **books** of Tibia.  

When talking to NPCs, you can click-spam all of these actionbar buttons in approx 10-30 minutes _while_ saving the transcripts into a .txt

### How to import your hotkeys to your pre-existing hotkey file  

For windows, your hotkeys reside here, in a file named `clientoptions.json`  

- Windows: `%LOCALAPPDATA%\Tibia\packages\Tibia\conf\` 

You can go to settings in Tibia and click 'Open screenshots folder' to get into `Tibia\packages\Tibia` and then open `conf` folder.  

### Step by step how-to:  

1. Close Tibia (**important**)
2. Backup clientoptions.json (**important**)
3. Open clientoptions.json with a text-editor.  
4. Copy the whole block below (including spaces) and search for it (CTRL + F)
```
                    }
                ]
            }
        }
```
Add a comma `,` and paste the contents of clientoptions.json
```
                    }
                ]
            }, 
            x<-- there
        }
```
To confirm that the new clientoptions.json is correct, copy-paste the entirety of your clientoptions.json into [json validater](https://jsonlint.com/) to check if it's valid. 

### Is this legal?  

Yes. It violates no rules/ToS. You are effectively just importing/restoring hotkeys.  

# Contributors

### Top transcript contributors:  

- 🥇 [tibiasecrets.com](https://tibiasecrets.com/transcripts/) with a whopping 410 contributions of excellent quality. 
- 🥈 [tibiawiki.br](https://tibiawiki.com.br/) with 250~ contributions.  
- 🥉 [tibia.fandom.com/](https://tibia.fandom.com/) with 100~ contributions.  

### Top books contributors: 

- 🥇 [tibiawiki.br](https://tibiawiki.com.br/) ~1260 books in library
- 🥈 [tibia.fandom.com/](https://tibia.fandom.com/) ~1220 books in library
- 🥉 s2w (Cony Island) Merged and added books to reach ~1370 books in library

### Individual contributors: 

You can view all individual contributions in [Contributions Table](https://github.com/s2ward/tibia/issues/51#issuecomment-1506364610)  

Roughly:
- Cony Island with 200 contributions.  
- LucH (Cookie12345678) with 50 contributions.  
- elkolorado with 4 contributions.
- BrunoBrockweldAlves With 1 contribution.

As well as some from Tibiasecrets.com discord community.

## Research:  

- [469](https://s2ward.github.io/docs/469/1/)
- [Island Dianscher, 469](https://www.reddit.com/r/TibiaMMO/comments/15832tv/lore_warlocks_draconia_trolls_the_mysterious/)
- [getting-started](https://s2ward.github.io/docs/getting-started/)



# Getting started with the world of Tibia Lore & Mysteries.  

### 1. What is the lore? 

The lore of Tibia is truly unique and nothing like you've seen in any other game.  
It can provide answers to *every single mystery* in Tibia, both big and small. Once you've learnt something new, five more mysteries arise you've never even heard or thought of. You'll see that 99% percent of the mysteries are never even discussed online.   
Once you've understood a concept, it'll completely change the way you look at Tibia *forever*.  This is described by the content-creators as different *meta*-levels, and they are explained in a multitude of different ways.   

A mystery in Tibia can have several [solutions](https://www.google.com/search?q=definition+of+solve), just like a riddle. 
One solution will feel correct, but then somehow another answer pops up that feels even better. It's important to have an open and flexible mindset. Follow Tibia.  

The lore is deeply contextual, and every NPC, ground item, book and quest serves a purpose. This includes seemingly insignificant details like short books containing only a title or quests that may appear as fool's errands.  

With tens of thousands of mysteries in Tibia, the lore offers various explanations and intricate riddles to unravel them all.  

## 2. How does the lore work?

The lore works in several different ways depending on what you like to do. Some people like to focus on single characters such as Ferumbras, others might dedicate all their time to deciphering 469- and others like to try everything in the Serpentine Tower.  

What I found to work best when unveiling the lore is as follows:

- Have fun
	- Self explanatory. If you don't have fun doing it, then it is not for you.

- Contained lore
	- This is the lore of a city or a place, where there are several stories told from the views of its inhabitants. 
Minotaurs in Mintwallin might describe the events that occur(ed) there from their point of view, their legends and their upbringing. The deathly city of Ankrahmun might have competely different views and ways of describing their lore and upbringings. You can explore every single nook and cranny of a place to get a contained picture. 

Many mysteries can be explained in contained lore, but far, far from all.  

An example of a contained mystery in Ankrahmun Pt. [1](https://www.reddit.com/r/TibiaMMO/comments/owjfs6/the_dark_secret_of_ankrahmun_how_to_unfolded_a/) and Pt. [2](https://www.reddit.com/r/TibiaMMO/comments/owjwbt/the_dark_secret_of_ankrahmun_how_to_unfolded_a/)

After and only after you've searched every nook and cranny of a contained place, you will feel there are some loose ends you cannot explain within. These leads will *only* emerge once you've properly explored a place, read their books, completed their quests & talked to its inhabitants. This is the only way of feeling and seeing the importance of certain 'mundane' leads that others don't care to even think about, because frankly It's impossible. This is when we get to the next section.  

- Overlapping lore 
	- After following leads from contained lore, you might find yourself reading the philosophies from another race & place. They will use different words to describe certain effects and events. A common example is Divination, Dream magic & Spells. Each of them being the same thing. However, figuring this out is not as easy as it might sound.  
	- The genesis and groundwork for all lore was engineered by Knightmare. All succeeding lore and content is built upon this groundwork and thus, in a similar way as Knightmare started it. 
	- > [Interview](https://forums.tibiabr.com/threads/378403-TibiaBR-entrevista-Knightmare?p=5353142#post5353142) with Knightmare 2010: "People tend to think what they read in (real life) history books is the one and only, true and definite history of the world. **Well it isn't**. What we read in books was pictured out by historians from several source texts that they took as reference. Those texts are **often biased and sometimes forged, sometimes based on misconceptions or hearsay**. Instead of providing a definite history without doubts of blind spots, I try to give the players **source material**. **In most cases they have to picture out the course of events on their own**. It's their choice which text or NPC they believe. **It's up to them to cross reference texts to figure out what truly happened**."

We find several historians within Tibia that will tell you their research, but keep in mind- it is not the true and definite history of the world of Tibia. After exploring every nook and cranny of your leads in another 'contained place', you will find some similarities- while they're not exactly the same, there is a reason behind it. The texts are often forged and based on legends, misconceptions and lies. The NPCs you stumble upon might be lying and have an ulterior motive. They might also tell you everything they know- which likely is not the true version because oftentimes they read the works of other historians. 

- Scattered lore
	- This is when you start to see commonalities everywhere, or the hints are all over the place. The lore of Tibia is heavily interconnected and you might find bits and pieces scattered all over. A lot of the older mysteries are scattered and the hints are thin and far between.  

This is where we get to the last section which is the most difficult yet extremely rewarding. 

- Solving mysteries
	- Cross-referencing several contained places, you might stumble upon that little something, that something which you cannot stop thinking about.. You are sitting on information that does not make sense at all if you take the words for granted, yet you are constantly pointed towards this information. There are too many connections to ignore and you can *feel* it just like you feel the leads of a contained place, you can now feel the culmination of all these different leads and a riddle emerges that cannot be seen nor emerge in any other way. Discussing, putting all these leads on a paper or mind-map and trying to reason about it might make something *click*. And now you are laughing your ass off because the answers are oftentimes funny and completely unexpected. The dopamine release is like nothing else. 

Congratulations, you now know what really transpired. You have now reached another meta-level which you can use to solve even more riddles & mysteries of your already visited places or succeeding ones. Oftentimes you get the answer to what you initially thought were completely unrelated mysteries.  

Here we follow the leads of a contained place into another contained place and answer a riddle in a most unexpected way. Remember, a riddle can have several different solutions.  

[Hugo Demonbunny](https://www.reddit.com/r/SolvingTibia/comments/p36umb/serpentine_tower_hugo_demonbunny_the_hyena_king/)

### 3. Where do I start? 

- By jumping in!
	-	I recommend to choose a place you have an interest in. 
	-	Demona warlocks? Ab'dendriel elves? Ankrahmun pharaoh? Thais vampires? Venore trade syndicate? Kazordoon dwarves?
	-	If you want some tip on where to go for you first, I'd suggest Kazordoon as it has a lot of mysteries that are not too difficult- and it gets you started. Consider speaking to Emperor Kruzak- and then visiting every nook and cranny of the mines that Malech is guarding. And maybe the surrounding surface.  
	-	Visit their libraries in-game, talk to the NPCs- they usually have a lot to tell you without even trying keywords in the dark. A couple of keywords I tell every NPC is 'job', 'name', '\<name of city>'
	-	Perhaps try to complete a quest without spoilers. I recommend Jakundaf Desert Dungeon or The Hidden City of Beregar. This is not only fun, it also teaches you to *think* like the content-creators leads you on. Try to think *how* was something completed. A good example of this is the Paradox Tower quest and Dreamers Challenge.

Do what you feel like. Do what you think is fun.  

## Common pitfalls 

1. Thinking that a reward is around every corner.
	- The thrill of figuring something out or seeing something new might convince you that there is a physical reward just around the corner. While it might be fun to try and come up with ideas, it's easy to get stuck in this phase. The lore is *HUGE* and the mysteries are endless. My opinion is that any mechanical quest / physical reward will emerge just like the solution to the various riddles and mysteries.  
2. Getting put down by the lack of confirmation.
	- We are given source material instead of a definite history without doubts of blind spots. It can be demotivating at times, but after solving a couple of riddles yourself- you will understand why the lore cannot be done any other way. Would we have ANY mystery to solve otherwise?  
3. Involving real life into the lore. 
	- There are countless allusions within Tibia. They serve as a way to lighten up the mood to a rather gloomy and dark world, and many enjoy finding them. The content-creators have stated numerous times that everything can be solved within Tibia. An explicit exception to this is the Mysterious Ornate Chest quest- where we have to know some binary, use a graphical program such as Paint, and visit tibia.com. 
	- Kaballah, Hebrew Gematria and Aleister Crowley will not get you anywhere.  
4. Discarding lore as allusions. 
	- I have seen many people discard certain characters or places as *only* allusions. 
	- I've seen people think that Hugo Chief from Venore is just be an allusion to Hugo Boss- and then missing out on one of the richest (also lore-wise) characters in Tibia. 
5. Only getting your information through the internet
	- It's paramount to visit the places in-game. It's a LOT of fun, highly immersive and there are hundreds of details you only find visually and contextually. Some examples of such are the covers of the books in Demona- they can tell you from which time they've been written.. Or their oranges they have on their tables, or in which container/place/library you find certain books such as the **basket** (lead) containing "Only a flute can master the snakes". 
	- Every. single. thing. is put there for a reason and frankly it's frighteningly consistent. 
6. Distractions
	- Knightmare introduced distractions as to not give away and avert from the obvious, the mundane details such as the **basket**  can tell you more than you ever imagined. 
	- > [Knightmare](https://forums.tibiabr.com/threads/378403-TibiaBR-entrevista-Knightmare?p=5353142#post5353142): "There are so many secrets hidden in my areas that never ever where found, only the obvious things seems to attract peoples attention and possibly distract it from other things that would be too obvious else ;o)"
	- It's paramount to explore every angle and think about every item. Keep asking yourself questions and try to find explanations for them. The lore is frighteningly consistent
7. Believeing that things introduced in the same update will give you answers. 
	- As seen again and again, such as the tower of Caramellia- or Opticording Sphere, quests and mysteries are introduced spanning updates over several years. Tibia lore has been 'cooking' for over 25 years, it's a great time to begin now!  
8. Forcing a theory
	- You will get many ideas along the way, you might have a theory that you'll do your darndest to fit in. This could make you ignore contradictions and only focus on the bits that fit into your theory. Again, a flexible mindset is paramount.
9. Spending all your time on a mystery where you don't have all the clues yet. 
	- The answer is out there and you will find it when you least expect it. Follow all the leads! 
10. Thinking that a mystery cannot be solved
	- A lot of people assume a mystery can't be solved due to lazy developers or that they don't agree with how Cip is running things. This is absolutely not the case. If you ever stumble upon an inconsistency, you've stumbled upon a great mystery that can be explained. One example of such is [The First Dragon](https://www.tibiaqa.com/710/why-is-the-first-dragon-called-first-dragon-and-not-garsharak). While there might not be a physical reward for every single mystery, the riddles can be solved and their existence can be answered.

### Most Importantly

Have fun!

--- 

## Workflows

On pull-request, an [automatic job](https://github.com/s2ward/tibia/tree/main/.github/workflows/validate.yml) will make sure that the format is correct by running src/validate.py

When maintainer approves, .github/worflows/publish-conversations.yaml will run and update api/file-mappings.json, doc/<tree views> and api/conversations.json based on changes.  
Tree views doc/*_transcripts.md will be generated and updated based on api/file-mappings.json.  
All NPC.txt files including incoming changes creates api/conversations.json.  
Upon merge by a repository maintainer, the transcript will deploy to GitHub pages where [NPSearch](https://talesoftibia.com/npsearch) fetches the jsons. 


All NPC transcripts & books are the work of CipSoft GMBH.  
I do not own them, this is merely fan-based work.  
