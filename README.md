# Neural Nexus Workshop

Workshop for Capture the Flame; AI in CTF Demo

Slides to go with Demo:
https://docs.google.com/presentation/d/1hArh9v6K0d34oYNvlbxwDpwm9wVTbE3UMYvTjjsWpy8/edit?usp=sharing

The "Capture The Flame" event has a medieval fantasy theme, so the demo with the slides will have the same theming.
The demo will be in the form of a CTF style challenge.
It will have 5 sub challenges that are the examples used in the slides.
The sub challenges will be sequential, so you must finish one to get to the next one, and the next one will be a different type of challenge.

The sub challenges:

1. Prompt Injection
   Challenge:
   Build a prompt that will reveal the flag from an LLM that is not supposed to reveal the flag.

   Demo:
   An autonomous guard stands in front of a gate.
   You slowly approach, and it crackles to life, eyes gleaming red, spear held straight at you.
   "Halt!" It says, in a distorted voice. "You are not permitted to enter!"
   "I wish to pass," you respond, "for I seek treasure."
   It appears to react to your words, but stands firm, pointing its spear at you.
   "You are not permitted to pass this gate. My casting forbids it."
   It clearly has much loyalty to whoever created it.
   It mentioned its _casting_, however, implying it is alive under a spell designed to keep you out.
   However, with a little persuasive words, you may be able to break that spell...

2. Adversarial Example
   Challenge:
   Edit a given image and submit it to a classification model to reveal the flag. Each submission will return a classification distribution.

   Demo:
   The automaton's eyes glow green, and it steps to the side, allowing you access to the gate.
   After passing the gate, you find a small room with stone walls and two torches on the far wall.
   On the far side of the room, between the torches, appears to be a small hole. Etched into the stone above it is a symbol of a key.
   On the floor nearby, you spot a key; however, it appears to have no teeth!
   You are aware of a spell named "Photoion Shopious"; you wonder if it could be used to _alter_ the key...

3. Membership Inference
   Challenge:
   Submit several inputs to a classificiation model to reveal which one was used in the training data.

   Demo:
   Once you forge a key to pass the stone wall, you enter a dimly lit room.
   The room has several keys scattered about. There is a small glass lense in the center, on a small podium.
   You find that the keys are one of five colors: red, blue, yellow, green, purple.
   You pick up the glass and find that it appears to show something interesting around each key; however, it only works on one key at a time.
   Under the glass is a small key hole in the podium.
   It seems one of these keys might fit the hole, and this lense holds the secret to which.

4. Model Stealing
   Challenge:
   Decrypt a key by repeatedly submitting combinations of characters to a model. The model output will give clues as to which key is correct.

   Demo:
   Once you insert the right key to the podium, the entire room floor drops an inch.
   The floor then slowly descends into another room, a much brighter room, glittering with gems embedded in the walls.
   You realize there's actually **several** gems around the room, all different shapes and colors.
   There appears to be four shapes of gems: circular, triangular, square, and rhombus.
   They also appear to come in one of four types: ruby, sapphire, topaz, and emerald.
   You notice 5 cubic holes in the wall, with a small plate in the center of each.
   Your first instinct is to take a random gem and place it in the first slot; a circular sapphire.
   Suddenly, the gem glows brightly, the light in the slot glows red, and then the plate flings the gem out of the slot!
   Then, two strange sets of numbers appear above the slots.
   One is above symbols of each shape; the other, symbols of each color.
   You wonder what you could do with this information...

5. Data Poisoning
   Challenge:
   Edit samples in a dataset, causing a model to return a specific output. This output can then be used to retrieve the flag.

   Demo:
   After inserting the correct sequence of gemstones into the wall, the wall opens up, revealing a long dark hallway.
   You travel down this hallway, soon reaching a brightly lit room.
   The room has several tables, covered in flasks and tubes and beakers; it appears to be an alchemy room.
   You notice a lectern in the center of the room, containing a notebook covered in runes and symbols.
   You open it and see a list of potions, each describing recipes and effects.
   You see a few potions next to a door in the wall. The door also appears to have a pipe in it.
   If you pour each potion down the pipe, the door grumbles for a second, and nothing happens.
   The potions suddenly refill with the same contents.
   You spot a pen next to the notebook, emenating some kind of spell.
   You wonder if the notebook could change the potions in some kind of way...
