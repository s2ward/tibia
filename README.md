# Tibia  

A repository for all things Tibia.  

Research: [s2ward/docs](https://github.com/s2ward/docs)

NPC transcript layout: [npc/{town}/{npc}.txt](https://github.com/s2ward/tibia/tree/main/npc)

```
├── npc
│   ├── Chaochai
│   │   └── Lizard_Prisoner_EMPTY.txt
│   ├── Chazorai
│   │   └── Chrak_EMPTY.txt
│   ├── Cormaya
│   │   ├── A_Majestic_Warwolf.txt
│   │   ├── Dedoras.txt
│   │   ├── Ghostly_Wolf.txt
│   │   ├── Gurbasch.txt
│   │   ├── Hawkhurst.txt
│   │   ├── Pemaret.txt
│   │   ├── Yoem.txt
│   │   └── Ysbasra_EMPTY.txt
│   ├── Darashia
... 
And so on.  
```

Where _EMPTY.txt are empty files.  

## How to contribute to [NPSearch](https://talesoftibia.com/pages/tools.html)  

![search](https://user-images.githubusercontent.com/25346191/230612401-1b6207c6-10de-4df6-8732-90c79c74a644.gif)

Create a pull-request and edit any NPC within [npc](https://github.com/s2ward/tibia/tree/main/npc) folder.  
Add your transcripts and GitHub will automagically take care of the rest.  

![CONTRIBUTE](https://user-images.githubusercontent.com/25346191/230709346-7346a63c-83f5-42af-bc60-ed4aa9900388.gif)

A great way to contribute is by going into npc/{town}/{npc}_EMPTY.txt and paste your transcript there without your Tibian name, timestamp nor level.  

```
Player: {your keyword}  
NPC: {npc response}  
```

And raise a pull-request on main branch.  

On pull-request, an [automatic job](https://github.com/s2ward/tibia/tree/main/.github/workflows/publish-conversations.yml) will make sure that the format is correct by running src/validate.py.  
If validation succeeds, another job will run which will convert all transcripts including your new contribution into api/conversations.json.   
Upon merge by a repository maintainer, the transcript will deploy to GitHub pages where [NPSearch](https://talesoftibia.com/pages/tools.html) fetches the .json and uses it for search using src/search.js  

If you want to contribute but have no idea how, you may also send the transcripts through:  
- [discord](https://discord.gg/JRvjSuU99U) (preferred)  
- [reddit](https://www.reddit.com/user/s2w) 

Note that it will take a bit longer for you new contribution to be searchable if you don't make a pull-request.  

# hotkeys.json  

![image](https://user-images.githubusercontent.com/25346191/230845416-bfe24fe7-62df-48be-abbc-760926d835bb.png)

To find all the tricky and secret single-word keywords, I've made a hotkey preset you can import into your pre-existing hotkey file.   

It consists of strings of unique words with a maximum of 255 characters which is the length limit for one message in Tibia.  
These strings are populated to Action-Bar buttons. Effort has been made to make all words unique, but there will be duplicates, it's not 100% perfect but pretty close. All words have been shuffeled to make words spread out instead of having loads of commonly 'responed-to' words in one button to make it easier when two or more words are in one button.  

There are currently three hotkey presets: "NPC1", "NPC2" and "NPC3". You can cycle through them using CTRL + J.  
The content of the hotkey presets are as follows (in order):  

- 15 000 words that **NPC**s respond to and answer with.  
- 10 000 most **common**ly used english words.  
- 15 000 words we find in **books** of Tibia.  

When talking to NPCs, you can click-spam all of these actionbar buttons in approx 10 minutes! No more copy-pasting for hours and hours lasting a whole day. If ten people do 10 NPCs in 6 days, we'd finish all NPCs with excellent quality and can then find and move on to multi-word keywords. Such as 'gabel is a rebel' 'magic crystal lugri deathcurse' or 'one eyed stranger'  

### How to import your hotkeys to your pre-existing hotkey file  

For windows, your hotkeys reside here:  

- Windows: %APPDATA%\Tibia\packages\Tibia\conf\\**clientoptions.json**  

You can go to settings in Tibia and click 'Open screenshots folder' to quickly find %APPDATA%\Tibia\packages\Tibia and browse to the correct folder.  

IMPORTANT!!!  
###Make a backup of your current hotkeys before proceeding!  

Copy your current clientoptions.json and name it clientoptions.json.backup  
This way you can quickly rename it back in case you did something wrong. Otherwise you might lose all your current hotkeys.   

#### Close Tibia before doing any work on the clientoptions.json file.  

## Step by step how-to:  

1. Open clientoptions.json with a text-editor.  
2. Paste the contents of hotkeys.json here:  

![image](https://user-images.githubusercontent.com/25346191/230849013-b8a6e683-dac7-40a3-bd47-f2590f98cee8.png)  
Above picture is where you start your paste, picture below is the end of the paste, just make sure to paste between the correct curly brackets { and brackets [.  

3. Confirm that the new .json is correct. Copy-paste the entirety of your clientoptions.json into [json validater](https://jsonformatter.curiousconcept.com/) to check if it contains any errors.  

![image](https://user-images.githubusercontent.com/25346191/230849815-bce6120d-5e3d-4c68-8bbd-8fb4d5482a35.png)

In this specific case, you'd have to put a single } at the end of the file. If there are no errors, your clientoptions.json is correct and will work.   

![addhotkey](https://user-images.githubusercontent.com/25346191/230851330-89ad7a76-6e0f-4ef3-a9fc-898bac5c3e57.gif)

Congratulations.  
You now have a never-before done and completely legal new edge in finding unheard of new mysteries.  

#### Is this legal?  

Yes. It violates no rules/ToS. You are effectively just importing/restoring hotkeys.  

### Top transcript contributors:  

- 🥇 [tibiasecrets.com](https://tibiasecrets.com/transcripts/) with a whopping 410 contributions of excellent quality. 
- 🥈 [tibiawiki.br](https://tibiawiki.com.br/) with 250~ contributions.  
- 🥉 [tibia.fandom.com/](https://tibia.fandom.com/) with 100~ contributions.   

### Individual contributors: 

- Cony Island (Simula, s2w) with 5 contributions.  
- Your name?  

# Research:  

---

- [469](https://s2ward.github.io/docs/469/1/)

- [getting-started](https://s2ward.github.io/docs/getting-started/)

---

# Getting started with the world of Tibia Lore & Mysteries.  

## 1. What is the lore? 

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

# Common pitfalls 

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

# Most Importantly

Have fun!

--- 

All NPC transcripts & books are the work of CipSoft GMBH.  
I do not own them, this is merely fan-based work.  
