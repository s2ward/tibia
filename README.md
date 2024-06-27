### Updated Documentation

# Tibia  

A repository for all things Tibia.  

### Where are the NPCs?  

They are here!
- [/data/npcs/text/]]([https://github.com/s2ward/tibia/data/npcs/text](https://github.com/s2ward/tibia/tree/main/data/npcs/text))

- Talesoftibia.com: [Open Source](https://talesoftibia.com)
- Discord: [Explorer Society](https://discord.gg/JRvjSuU99U)
- Search Transcripts: [NPSearch](https://www.talesoftibia.com/npsearch)   
- Search Books: [LIBSearch](https://www.talesoftibia.com/libsearch)  
- Research: [talesoftibia](https://www.talesoftibia.com/blog)), [reddit](https://www.reddit.com/r/SolvingTibia) 
- All Transcripts: [↗](./docs/npc_trees/all_transcripts.md)  

The `data/npcs/text/` directory and its content is used by [NPSearch](https://www.talesoftibia.com/npsearch)  
The `data/books/book_database.json` contains 1370~ books and is used by [LIBSearch](https://www.talesoftibia.com/libsearch)

### Tales of Tibia: Project Overview

1. [Tales of Tibia: Project Overview](#tales-of-tibia-project-overview)
   1. [What is Tales of Tibia?](#what-is-tales-of-tibia)
2. [The Search Tools](#the-search-tools)
   1. [How to Contribute](#how-to-contribute)
   2. [Project Structure](#project-structure)
3. [Data and Image Endpoints](#data-and-image-endpoints)
   1. [resources.talesoftibia.com](#resourcestalesoftibiacom)
4. [Hotkey Mania: Detailed Guide](#hotkey-mania-detailed-guide)
   1. [What is Hotkey Mania?](#what-is-hotkey-mania)
   2. [How Hotkey Mania Works](#how-hotkey-mania-works)
   3. [Setting Up Hotkey Mania](#setting-up-hotkey-mania)
   4. [Using Hotkey Mania](#using-hotkey-mania)
5. [NPC Transcripts: Contribution Guide](#npc-transcripts-contribution-guide)
   1. [Collection Process](#collection-process)
   2. [Basic Format](#basic-format)
   3. [Grouping Conversations](#grouping-conversations)
   4. [Additional Tips](#additional-tips)
   5. [Helper Script](#helper-script)
6. [Adding new NPCs and Books: Contribution Guide](#adding-new-npcs-and-books-contribution-guide)
   1. [NPCs](#npcs)
   2. [Books](#books)
7. [Contributors](#contributors)
8. [Legal Note](#legal-note)

## What is Tales of Tibia?

Tales of Tibia is a passion-project that provides tools and resources for the Tibia gaming community, to be able to read the various tales in Tibia, be it from books, NPC conversations or from user-generated research.

The main components are:

1. **npsearch**: A tool for searching and viewing NPC transcripts.
2. **libsearch**: A tool for searching and viewing in-game books.
   - See tools here: [GitHub](https://github.com/s2ward/toolsoftibia)
3. **Magic Web Explorer**: A map tool with cyclopedia, catered to explore the Magic Web.
   - See tool here: [GitHub](https://github.com/s2ward/magic-web)
4. **Blog**: A collection of updates, mysteries, stories, guides, and research.  
5. **GitHub**: A repository of NPC transcripts and book data for community contributions.  
   - See repository here: [GitHub](https://github.com/s2ward/tibia)

## The Search Tools

For a simple demonstration, visit [services](https://talesoftibia.com/services/).  

The NPC and book data is sourced from various Tibia community resources, [this project](https://github.com/s2ward/tibia/issues/51), and compiled into a structured database. When adding new data, it's then automatically validated, processed, and published for use. 

1. **Data Collection**: 
   - NPC transcripts are sourced from tibiasecrets.com, community contributions, and a custom [hotkey spamming](#how-hotkey-mania-works) method. Some transcripts from English and Brazilian Wiki are also used.   
     - New transcripts come from hotkey spamming, and is the most reliable method.   
   - Book data is compiled from English and Brazilian Tibia Wikis, with additional harmonization, metadata and missing books added.

2. **Data Processing**:
   - Automated workflows process and validate the data.
   - GitHub Actions update file mappings, sync NPC data, and generate tree views upon approved pull requests.
   - All `data/npcs/text/*.txt` files are compiled into `data/npcs/npc_transcript_database.json` and published to GitHub Pages and Cloudflare R2.  

3. **User Interface**:
   - The search interfaces, designed by GABRO, mimic Tibia's aesthetic.
   - npsearch and libsearch fetch data from JSON files hosted on Cloudflare R2 to perform client-side searches.

## How to Contribute

1. **NPC Transcripts**:  
   
See [NPC Transcripts: Contribution Guide](#npc-transcripts-contribution-guide) for more detailed guidelines.  
But in essence, you can contribute by:
- Checking the [docs/npc_trees/unverified_empty_transcripts.md](https://github.com/s2ward/tibia/blob/main/docs/npc_trees/unverified_empty_transcripts.md) list for missing transcripts.
- Use the "[Hotkey Mania](#hotkey-mania-detailed-guide)" method for complete* documentation.  
- Create a pull request with your changes.
   - You may also send missing data on e.g. Discord or Reddit. It will be highly appreciated.  

2. **Book Data**:
   - Contributions to the book database are welcome, read how-to here: [instructions](#books)  

3. **Tool Development**:
   - Raise an issue, reach out via Discord or Reddit to discuss new tool ideas or features.

## Project Structure

1. **GitHub Repository**:
   - `data/npcs/text/`: Contains NPC transcripts (used by npsearch).
   - `data/books/book_database.json`: Contains book data (used by libsearch).
   - `src/`: Python scripts for data processing and validation.
   - `.github/workflows/`: GitHub Actions for automated processes.

2. **Directory Structure**:
   
```
tibia/
├── data/
│   ├── books/
│   │   ├── book_database.json
│   │   └── book_image_mapping.json
│   ├── npcs/
│   │   ├── npc_metadata.json
│   │   ├── npc_transcript_database.json
│   │   ├── npc_verification_mapping.json
│   │   └── text/
│   │       └── [NPC text files organized by <area>/<subarea>]
├── docs/
│   ├── npc_trees/
│   │   └── [NPC tree structures]
│   └── [other documentation files]
├── .github/
│   └── workflows/
│       ├── deploy_resources.yml
│       ├── update_and_process_npc_data.yml
│       ├── update_npc_status_on_pr_merge.yml
│       └── validate_npc_file_structure.yml
├── src/
│   ├── scripts/
│   │   ├── gha/
│   │   │   ├── generate_book_image_mapping.py
│   │   │   ├── generate_npc_status_report.py
│   │   │   ├── update_npc_location_metadata.py
│   │   │   ├── generate_npc_trees.py
│   │   │   ├── compile_npc_transcript_database.py
│   │   │   ├── update_npc_file_and_verification_mapping.py
│   │   │   ├── update_project_status.py
│   │   │   └── validate_npc_file_structure.py
│   │   ├── utils/
│   │   │   ├── mapper_to_tibiamaps.py
│   │   │   └── sanitize.py
│   └── [other source code modules]
├── hotkeys.json
└── [other project files]
```


1. **GitHub Workflows**:
   - Pull requests trigger validation checks. 
     - [validate_npc_file_structure.yml](https://github.com/s2ward/tibia/blob/main/.github/workflows/validate_npc_file_structure.yml)
   - Approved changes update file mappings, sync data, compile NPC database, and regenerate documentation. 
     - [update_and_process_npc_data.yml](https://github.com/s2ward/tibia/blob/main/.github/workflows/update_and_process_npc_data.yml)
   - Changes are then published to GitHub Pages, and Cloudflare R2 on resources.talesoftibia.com
     - [deploy_resources.yml](https://github.com/s2ward/tibia/blob/main/.github/workflows/deploy_resources.yml)
   - Another workflow creates a notification on Discord, as well as an update to individual contributions on [GitHub](https://github.com/s2ward/tibia/issues/51)
     - [update_npc_status_on_pr_merge.yml](https://github.com/s2ward/tibia/blob/main/.github/workflows/update_npc_status_on_pr_merge.yml)

## Data and Image Endpoints

The database and images are hosted by Cloudflare in an [R2 Bucket](https://developers.cloudflare.com/r2/), which is accessible on a dedicated subdomain, `resources.talesoftibia.com`  

## resources.talesoftibia.com

Prepend `https://resources.talesoftibia.com` to the following paths:

1. **JSON Data**
   - NPC conversations, metadata, books, and book images:
     - `/data/npcs/npc_transcript_database.json`
     - `/data/npcs/npc_metadata.json`
     - `/data/npcs/npc_verification_mapping`
     - `/data/books/book_database.json`
     - `/data/books/book_image_mapping.json`

2. **Images**
   - NPC, book, spell, and creature images, padded to square in .png format:
     - `/images/npcs/`
     - `/images/books/`
     - `/images/spells/`
     - `/images/creatures/`

Example: [https://resources.talesoftibia.com/images/npcs/Planestrider.png](https://resources.talesoftibia.com/images/npcs/Planestrider.png)

## Hotkey Mania: Detailed Guide

### What is Hotkey Mania?

[Hotkey Mania](https://github.com/s2ward/tibia/blob/main/hotkeys.json) is a custom-made hotkey preset designed to efficiently find hidden single-word keywords when interacting with NPCs in Tibia. It's a powerful tool for documenting NPC responses and uncovering hidden transcripts.
With it I've already uncovered really [obscure and hidden keywords](https://talesoftibia.com/blog/2024-02-17-obscure-svargrond-transcripts/), even a [new source](https://talesoftibia.com/blog/2023-04-28-new-source-of-holy-water/) of holy water, and documented close to 500 NPCs. A lot of really strange and interesting things have been found.  

You can use it to get first look into unseen content, potentially impactful for the lore and mysteries, it's addictive and fun.  

See it in action (41s):  
[Watch it on YouTube](https://youtu.be/YMx6i2K9K00?t=41)

What:
- Contains strings of unique words with a maximum of 255 characters each.
- Populates Action-Bar buttons for quick clicking.
- Three hotkey presets: "NPC1", "NPC2", and "NPC3". 
- Includes deliberately duplicated words spread randomly across buttons.
- A bit over 1000 buttons in total.

Content of the hotkey presets:
1. 15,000 words that NPCs respond to and answer with.
2. 10,000 most commonly used English words.
3. 15,000 words found in Tibia's in-game books.
4. Known multi-word keywords.  

### How Hotkey Mania Works

1. The preset populates your Action-Bar buttons with strings of words.
2. When interacting with an NPC, you can rapidly click through these buttons.
3. This method allows you to "ask" the NPC thousands of words in a short time.
4. Any responses can be saved to a text file for documentation.

With Hotkey Mania, you can typically cover all preset words while saving the transcripts in about 15-60 minutes per NPC.  

### Setting Up Hotkey Mania

Follow these steps to import the Hotkey Mania preset into your Tibia client:

1. **Locate your Tibia configuration folder**:
   - On Windows: `%LOCALAPPDATA%\Tibia\packages\Tibia\conf\`
   - Tip: In Tibia, go to Settings > "Open screenshots folder" to find `Tibia\packages\Tibia`, then navigate to the `conf` folder.

2. **Prepare for import**:
   - Close Tibia client (important).
   - Backup your existing `clientoptions.json` file (important) place it on e.g. your desktop or cloud storage.

3. **Edit clientoptions.json**:
   - Open `clientoptions.json` in a text editor.
   - Find this block of text, copy it in its entirety with spaces included, and use e.g. CTRL + F to find:
     ```json
                     }
                 ]
             }
         }
     ```
   - Add a comma after the closing brace of the `hotkeys` object:
     ```json
                     }
                 ]
             }, 
             ^-- Add comma here
         }
     ```

4. **Import Hotkey Mania**:
   - Download the [hotkeys.json](https://github.com/s2ward/tibia/blob/main/hotkeys.json) file from the Tales of Tibia GitHub repository.
   - Copy the entire contents of `hotkeys.json`.
   - Paste the copied content immediately after the comma you added in step 3.

5. **Validate your changes**:
   - Copy the entire contents of your modified `clientoptions.json`.
   - Paste it into a JSON validator like [jsonlint.com](https://jsonlint.com/).
   - Ensure the JSON is valid before saving. It will be green if it's good.  

6. **Save and test**:
   - Save the modified `clientoptions.json`.
   - Launch Tibia and check if the new hotkeys are available.  
   - Don't make changes while Tibia is running.  

### Using Hotkey Mania

1. In Tibia, cycle through the hotkey presets using CTRL + J.
2. When talking to an NPC, rapidly click through the Action-Bar buttons.
3. Save any new responses to a text file for later documentation.

### Legal Note

Hotkey Mania does not violate any Tibia rules or Terms of Service. It's essentially importing and restoring hotkeys within the game's existing functionality.

# NPC Transcripts: Contribution Guide

To get a good sense of how to gather transcripts and tackle this challenge, I'll show you my process.  

## Collection Process

1. **Basic Queries**: Start with these standard questions:
   - hi, how are you, name, job, time, news, rumours/rumors, bye

2. **Follow Blue Keywords**: 
   - Follow the blue keywords that the NPC's provide.  

3. **Try Nearby Names**: 
   - Test NPC names and creatures in the vicinity (e.g., Sam, Oswald, Frodo)

4. **Quest Research**: 
   - Check the Tibia Wiki for any quests involving this NPC

5. **Item and Quest Dialogues**: 
   - Attempt using item names or specific quest dialogue options

6. **Copy-Paste Responses**: 
   - Some 2-word keywords might be hidden and not highlighted in blue
   - Try combinations that make sense in context

7. **Hotkey Spamming**: 
   - I use this last, after steps 1-6
   - It's faster once you're familiar with most responses
   - If you find a new response, backtrack to identify the trigger word

Always save responses in a text file as you find them.

## Basic Format

When contributing NPC transcripts to the transcript project, it's important to follow a consistent structure. This ensures that the information is easily readable, searchable, and maintainable. Here's a comprehensive guide on how to structure your NPC transcript contributions.

Use the following format for each interaction:

```
Player: <your keyword>
NPC: <npc response>
Player: job
NPC: I'm an example!  
```

Further, there are some other additional rules to follow:  

**Expected Format**: 
   - No empty lines between dialogues.
   - No lines that don't start with `Player:` or `NPC:`.
   - Only one NPC per file.
   - No timestamps or level indicators.
   - Use "Player" instead of your character name.
   - Use NPC names as they appear in the game.  

## Grouping Conversations

Group related queries together. This makes it easier to navigate the transcript and find specific information.
In this example, there are headers in `#`, these should not be included in the final transcript.  

Think of how you would like to read it, don't scramble the transcripts, there should be a flow to it.  
Not all NPCs are the same, some are more chatty, some speak of very little things, some are almost solely quest-related. There is no one-size-fits-all, it will differ.  

Here's a recommended, general structure:

```
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

### Example Transcript

## Introduction Queries
> Player: (idle)  
Oswald: Come here adventurers! Come say hi! (example transcript)  
Player: hi  
Oswald: Oh, hello Player. What is it? Why do you disturb me?  
Player: name  
Oswald: My name is Oswald, but let's proceed, I'm a very busy man.  
Player: job / important  
Oswald: I'm honoured to be the assistant of the great, the illustrious, the magnificent Durin!  
Player: time  
Oswald: It is nearly tea time, so please hurry!  

## About Oswald's Role
> Player: assistant  
Oswald: I've got a job of great responsibility - I keep annoying persons away from my boss.  
Player: annoying  
Oswald: Better don't ask, you wouldn't like the answer.  
Player: Durin  
Oswald: Just between you and me, he can be quite a tyrant.  
Player: tyrant / how are you  
Oswald: If there weren't so many people harassing me, life would be great.  
Player: harassing  
Oswald: You don't need not ask me about that, you are perfect in it.  
Player: sell  
Oswald: Hey, I'm not a shopkeeper, I'm an important man!  

## General Queries
> Player: help  
Oswald: I'll inform the higher officials of your needs.  
Player: monster  
Oswald: AHHHH!!! WHERE??? WHERE???  
Player: dungeon  
Oswald: If you want to see dungeons, simply refuse to pay your taxes.  
Player: sewer  
Oswald: Our sewer system is very modern, but crowded with rats and wannabe heroes.  
Player: god  
Oswald: I think the gods are too busy to care about us mortals, hmm... that makes me feel godlike, too.  
Player: king  
Oswald: Ah, yes, yes, hail to King Tibianus! Long live the king and so on...  

## About Other NPCs
> Player: sam  
Oswald: A simple shopkeeper with minor intelligence.  
Player: benjamin  
Oswald: What do you expect from ex-soldiers? He's nuts! He had way too many blows on the head.  
Player: gorn  
Oswald: He sells his scrolls far too expensive.  
Player: quentin  
Oswald: I heard he was a ladies' man in younger days. Nowadays, it is rumoured that he likes to wear women clothes now and then.  
Player: bozo  
Oswald: Isn't he the artist formerly known as the prince?  
Player: eclesius  
Oswald: Eclesius... Eclesius... I think they say about him that he accidentally turned his assistant into a frog. So you better pay attention!  
Player: lynda  
Oswald: Sweet as honey, but cold as a fish. The only thing that can soften her heart is this awfully expensive Venorean ice cream.  

## Chained Conversations 
> Player: gamel  
Oswald: This man lives in the darkness like a rat and he is also as handsome as one. He surely is up to no good and often consorts with sinister strangers.  
Player: sinister strangers  
Oswald: Just last week, a one-eyed man, who had a room at Frodo's, met him in the middle of the night.  

## Rumors and Gossip
> Player: rumour / gossip / news  
Oswald: You know a rumour? TELL ME! TELL ME! TELL ME!  
Player: mud  
Oswald: I heard Sam dated a female mud-wrestler once.  
Player: weapon  
Oswald: It's rumoured that Sam does not forge all weapons himself. Instead he is buying them from his cousin, who is married to a cyclops.  
Player: magic  
Oswald: I overheard a conversation of officials in which they claimed that magic will be forbidden soon.  
Player: power / rebellion  
Oswald: There are people who talk about a rebellion against King Tibianus.  
Player: spell  
Oswald: I heard about a sorcerer who was toasted by a misfired spell of himself.  
Player: excalibug  
Oswald: It's beyond all doubt that certain sinister elements in our city have certain knowledge about this myth.
Player: goshnar  
Oswald: They say he isn't truly dead. He was... or is a necromant after all.  
Player: necromant nectar  
Oswald: You aren't the first one to ask about that. Am I the only one that prefers wine to such disgusting stuff?  

## Quest-Related Conversation Should always be at the very end.  
> Player: invitation (The Thieves Guild Quest)  
Oswald: I am deeply sorry, there are no invitations left. I hope you didn't lose yours.  
Player: yes  
Oswald: You strange people lose everything, don't you? If you need another one, it'll cost you dearly. 5000 gold, deal or no deal?  
Player: no  
Oswald: I thought as much.  
Player: yes  
Oswald: Excellent! Here is your invitation!  

## Farewell
> Player: thank you  
Oswald: You are... uhm... welcome. Are you already done?  
Player: bye / farewell  
Oswald: Finally!  
Player: (vanish)   
Oswald: Begone!   

## Additional Tips

1. **Multiple Keywords**: If an NPC gives the same response to multiple keywords, list them all:
   
   > Player: offer / goods / buy  
   Santa Claus: I sell the finest swords in all the land!  

2. **Special Interactions**: If there are special conditions for certain dialogues (e.g., quest stages, level requirements), note them:

   > Player: hi (with garlic necklace)  
   Vladruc: Cough... Cough (example)  


3. **Quest Progression**: If responses change based on quest progress, note the different stages:

   > Player: mission (before quest acceptance)   
   Santa Claus: Are you interested in helping our village?  
   Player: mission (after quest acceptance)  
   Santa Claus: Have you cleared the forest of those strange creatures yet?  
   Player: mission (after quest completion)  
   Santa Claus: Thanks again for your help! Our village is safe thanks to you.  


4. **Seasonal or Event-Specific Dialogue**: If the NPC has special dialogue during in-game events, mini world changes or seasons, group these separately:

   > Player: solstice (Colors of Magic)  
   Lugri: Ah yes, the Summer Solstice Festival is our biggest celebration of the year!


5. **Gaps**: If there are gaps in the transcript, the search engine will not accept them:

   > Player: 
   
   NPC: ...


6. **Custom text** If you feel like you need to write a clarification, use a very short sentence within parentheses of the Player prompt. 

   > Player: hi (below level 999)  
   Cipfried: You are too young to be here.


Remember, the goal is to create a comprehensive and easily navigable transcript. By following this structure, you'll help make the NPC transcripts more readable and maintainable.  

### Helper Script

To remove timestamps, level indicator, to change your name from 'Character name' into 'Player' and check that you have the correct format, you can use the following Python script: [src/scripts/utils/sanitize.py](https://github.com/s2ward/tibia/blob/main/src/scripts/utils/sanitize.py)

For example:  
- `python3 sanitize.py yourworkfile.txt Playername`
- `python3 sanitize.py yourworkfile.txt 'Cony Island'`

## Adding new NPCs and Books: Contribution Guide

When a new update arrives, new NPCs and new books are often added to the game. This guide explains how to contribute new NPCs and books.

### NPCs  

1. Create a new folder for the NPC under the appropriate town and subarea. e.g., `data/npcs/text/Town/Subarea/NPC_Name.txt`.
2. Add the NPC .txt file(s), it can be an empty file.  
3. Update the `npc_metadata.json` file with the new NPC data.

```json
    {
        "name": "Planestrider",
        "job": "Unknown",
        "race": "Unknown",
        "gender": "Unknown",
        "location": "Roshamuul",
        "subarea": "The Cube (Location)",
        "map": "https://tibiamaps.io/map#33938,32496,14:2",
        "version": "12.31.9667",
        "quests": [
            {
                "quest-name": "Opticording Sphere Quest",
                "quest-url": "https://tibia.fandom.com/wiki/Opticording_Sphere_Quest"
            }
        ],
        "dialogues": [
            "I am and never was. The first final piece of a puzzle, put back into its box. But how many boxes are there, how many will there ever be? All of them. There will be all of them."
        ],
        "coordinates": [
            33938,
            32496,
            14
        ]
    }
```

4. Add NPC images without names above the NPC to the `img/npc/` folder. e.g. `Planestrider.png`

### Books

1. Open the `data/books/book_database.json` file.
2. Locate the area where the new book should be added, e.g. a new book in Thais should be among the Thais books. For new areas, add a new section - and use naming convention from [Tibias official map](https://www.tibia.com/library/?subtopic=maps)  

3. Add the new book data in the following format: 
```json
    {
        "name": "The_Dream_Machine",
        "author": "?",
        "description": "About the dream machine.",
        "locations": [
            "Dream Realm -> Dream Master"
        ],
        "libraries": [
            "Dream Realm Library"
        ],
        "version": "7.9",
        "related-articles": [
            {
                "article-name": "Dream Machine",
                "article-url": "https://tibia.fandom.com/wiki/Dream_Machine"
            }
        ],
        "next-book": "_NONEXT",
        "previous-book": "_NOPREV",
        "img": [
            "Book_(Brown)"
        ],
        "text": "The dream machine draws its energy ...",
        "map": [
            "https://tibiamaps.io/map#32845,32227,14:2"
        ],
        "type": "book",
        "locations-wip": [
            {
                "mainarea": "Main Continent - Southern Wilderness",
                "area": "Dream Realm",
                "subarea": "Dream Master"
            }
        ]
    }
``` 
See example [here](https://github.com/s2ward/tibia/commit/40561dd8e459b3c0413337fae05eb24626cf81ec)

- "img": for example, books can be added to the `imgages/books/` folder. `New_Book_Sprite.png` 
  - There are already a lot of book sprites in the folder, so you can use one of those unless it's a completely new sprite.
  - You can download creature and spell sprites from [spell library](https://www.tibia.com/library/?subtopic=spells) and [creature library](https://www.tibia.com/library/?subtopic=creatures) and upload them to the corresponding folder, e.g. `images/creature/`

 or `images/spell/`.
- Previous book and next book should be `_NONEXT` and `_NOPREV` respectively if there are no previous or next books. But if it's part of a series, e.g. 'Tibia History 1' and 'Tibia History 2', then you should link them together, where the first book has `_NOPREV` but the name of the second book in `next-book`. The second book has the first book's name as `previous-book` and `_NONEXT` as `next-book`.
- "type" can be either creature, book, or spell. 
- "locations-wip" is a work in progress field, it's not used yet but will be used for a future feature.

That's it!  

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
- Cony Island with 450 contributions.  
- LucH (Cookie12345678) with 50 contributions.
- [Roc.ky](https://tibia.fandom.com/wiki/User:RockyLaRo) with 10 contributions.   
- elkolorado with 4 contributions.
- BrunoBrockweldAlves With 1 contribution.

As well as some from Tibiasecrets.com Discord community.

## Research:  

- [469](https://article.talesoftibia.com/469/1/)
- [Island Dianscher, 469]([https://www.reddit.com/r/TibiaMMO/comments/15832tv/lore_warlocks_draconia_trolls_the_mysterious/](https://talesoftibia.com/blog/2024-06-08-island-dianscher/))
- [getting-started]([https://s2ward.github.io/docs/getting-started/](https://talesoftibia.com/blog/2024-06-14-getting-started-with-lore-and-mysteries/))

# Legal Note

All NPC transcripts & books are the work of CipSoft GMBH. This project is fan-based work and does not claim ownership of the content.

For more detailed information or to get involved, join the community on [Discord](https://discord.gg/JRvjSuU99U) or [Reddit](https://www.reddit.com/user/s2w). 
