label mod_day1_evening:
    show screendark zorder 999
    show bg residential_evening with wipeleft_scene
    play music jazztrack fadeout 2.0
    window show
    "The festival extends through the afternoon and into the evening."
    "I'm surprised that we got to see the entire festival."
    "Sayori and I had probably covered just about every area of the school looking for things to do."
    "We even saw the other club members a few times."
    "As we walk home, I barely feel tired at all..."
    show sayori 1d zorder 3 at t11
    "...but all the activities have clearly taken their toll on Sayori."
    "She is more shuffling along than actually walking, and is leaning on me for support."
    mc "You doing alright, Sayori?"
    s 1e "Mmm..."
    "She's clinging tightly to my arm."
    "Thank goodness we're close to her house; it doesn't look like she'll be able to go much further."
    show sayori 1k
    "But... she's had time to dwell on her own thoughts lately."
    "It hasn't done her any good."
    show sayori 1y
    "Maybe she'd want to spend the night with me instead. She does seems happier when I'm around..."
    menu:
        "What should I do?"
        "Let Sayori sleep over.":
            $ sayori_happiness = sayori_happiness + 1
            $ cb_save_reset()
            show expression Text("[sayori_happiness]"):
                ypos 0.5
            call mod_day1_sleepover
        "Drop Sayori off at her house.":
            $ sayori_happiness = sayori_happiness - 4
            $ cb_save_reset()
            show expression Text("[sayori_happiness]"):
                ypos 0.5
            call mod_day1_dropoff
    return

label mod_day1_sleepover:
    mc "Hey, Sayori?"
    "Sayori looks up at me."
    s 1x "Yeah?"
    "I can't let her stay on her own again."
    mc "Do you want to come over to my house tonight?"
    show sayori 1e with alphadissolve2
    "Sayori immediately blushes hearing what I said."
    mc "Don't get the wrong idea... I'm just trying to look after you."
    "Sayori gives a small smile."
    s 1y "Don't worry, I didn't."
    s 2e "But you don't need to do this, you know..."
    "She always thinks of other people's feelings rather than her own..."
    "It would be a redeeming quality, but she doesn't need to redeem anything to me."
    mc "I'm doing this because I want to do what's best for you."
    mc "Besides, when was the last time we had a sleepover?"
    show sayori 1y
    "She, again, gives me a small smile."
    s 1c "A few years ago..."
    s 1e "But I still remember it like it was yesterday."
    "I stare off into the distance, reminiscing about the past."
    "Times like when we were stuck after climbing a tree as children, or playing together by the river near our houses..."
    window hide
    show bg residential_evening_blur zorder 998 with Dissolve(8.0)
    show bg residential_evening zorder 0 with Dissolve(0.2)
    show sayori 1l
    window show
    s "Ah-"
    "I snap back to reality, and realize I've been staring into Sayori's eyes."
    "She must have been thinking about our childhood in the same way."
    "She looks away, realizing what was happening."
    mc "Ahaha..."
    mc "Don't worry about it."
    "There was a moment of silence."
    s 1r "Ok, I'll go to...{i}your...{/i}"
    "She yawns heavily."
    show sayori 1d
    "God, she must be really tired."
    "It took me until now for me to realize she was stumbling on her feet."
    mc "Come on, I'll give you a hand."
    show sayori 1o at hop
    hide sayori with alphadissolve
    "I hoist Sayori up in my arms, and proceed to take her home."
    show sayori 1d at t11:
        zoom 2.4 ypos 2.3
    "Sayori almost giggles."
    s 1e "You really don't have to..."
    "She yawns again, more heavily than last time."
    mc "I'm not having you fall asleep mid-walk."
    mc "Plus, you don't exactly weigh much."
    show sayori 1o
    "Sayori takes a moment to think that comment over."
    s 1l "I think that was a compliment, right?"
    mc "Of course."
    show sayori 1s
    "She smiles properly, for the first time since she told me everything."
    s "Thanks..."
    s "Ehehe..."
    window hide
    $ renpy.pause(3)
    show sayori 1q with alphadissolve2
    window show
    "She falls asleep in my arms."
    "I smile, seeing my house just ahead of us."
    "Thank god we don't have nosy neighbors."
    hide sayori with alphadissolve
    show bg kitchen_night with Dissolve(2.0)
    "As quietly as I can, I take her upstairs and into my room."
    show bg bedroom_night with Dissolve(2.0)
    "I place her down on my bed, taking extra care to cover her with any blankets that I can find."
    s "[player]?"
    "Sayori looks up at me from underneath three layers of blankets."
    "She still has the smile I saw from earlier on."
    mc "Yeah?"
    s "You don't need to set up another--"
    "She yawns again."
    mc "Don't worry about it, I will."
    s "No..."
    "I hear her shift to the other side of the bed."
    "Thank god I bought a double bed."
    show sayori 1y at t11 with alphadissolve2
    s "Just get in..."
    hide sayori with alphadissolve
    "I smile and do as she asks, pulling the covers back over us."
    "I place my head on the pillow, closing my eyes."
    scene black
    show bg longfadebedroom
    stop music fadeout 5.0
    "I think today was a good day."
    "And maybe..."
    "{i}Just maybe...{/i}"
    "{i}I made one of those rain clouds go away.{/i}"
    "..."
    jump mod_day2_main

label mod_day1_dropoff:
    "I glance at Sayori, and notice her signs of fatigue."
    mc "Alright Sayori, we're almost home. Let's keep moving."
    window hide
    $ renpy.pause(2)
    show sayori 1k with alphadissolve2
    window show
    "As we resume walking I notice her sluggish pace."
    mc "Are you feeling alright? How tired are you?"
    s 1e "I-I'm...alright..."
    mc "Are you sure?"
    show sayori 1d
    "She nods her head."
    window hide
    $ renpy.pause(2)
    show sayori 1u with alphadissolve2
    show sayori 1f with alphadissolve2
    "As we walk closer and closer to Sayori's house I notice her pace slowing down even more."
    "I guess she must be pretty tired."
    show sayori 1k
    show black with wipeleft_scene
    hide black
    "After a few moments we arrive in front of Sayori's house."
    mc "Alright now, you better get some rest."
    "I pat Sayori on the back as she walks to the front door."
    show sayori 1y
    "She raises her palm at me, as if she was too tired to properly wave goodbye."
    "I wave back at her."
    mc "Have a nice night."
    show sayori at thide
    hide sayori
    "As I walk away I hear Sayori close the front door."
    stop music fadeout(5.0)
    show black with Dissolve(5.0)
    "I reminisce on the way back to my house."
    "It's been quite a while since we've spent time together like that, just the two of us."
    "Thinking about it, we don't hang out too much anymore."
    "We were inseparable as kids, but I guess we drifted apart..."
    window hide
    $ renpy.pause(3.0)
    window show
    "{i}...or was it me?{/i}"
    "Have I slowly been changing without noticing it?"
    "Maybe I could have picked up on Sayori's signs of depression..."
    "Maybe this could have been different."
    window hide
    $ renpy.pause(3.0)
    window show
    "I sigh to myself as I approach my front door."
    "Maybe I'm overthinking this..."
    scene bg bedroom_night with Dissolve(2.0)
    "As I walk into my room I leave my jacket on the door and collapse onto my bed."
    "I blankly stare at the ceiling."
    window hide
    $ renpy.pause(5.0)
    window show
    "Man, it's kinda hard to not think about things right now."
    "I glance over at my desk, I could get on my PC..."
    "But then again, I could really use some sleep; this day's been pretty busy for me."
    "I look over at my clock, it's about 8..."
    "I close my eyes for a while and my mind wanders."
    show black
    window hide
    $ renpy.pause(5.0)
    window show
    show sayori 1y at t11:
        alpha 0.2
    "Sayori."
    "The only thoughts I have right now are of Sayori."
    show sayori 1u
    "Was it really the right choice to just leave her at her own home?"
    show sayori 1v
    "Was it really the right choice to just leave her alone with her thoughts?"
    show sayori at thide
    hide sayori
    $ renpy.pause(2.0)
    show sayori 1w at t11:
        alpha 0.0
        linear 5.0 alpha 0.2
    "I try to think of other things but I can think of only Sayori right now."
    "Damn, I just can't sleep like this."
    show sayori at thide
    hide sayori
    hide black with Dissolve(2.0)
    "I get up and wash my face in the bathroom."
    "I feel a bit better now, but..."
    "..."
    "God, {i}what's wrong with me?{/i}"
    $ renpy.pause(1.0)
    "Maybe I should think about the better parts of the day..."
    show sayori 1x:
        alpha 0.0
        xcenter 640
        ycenter 500
        zoom 0.0
        linear 5.0 alpha 0.2 zoom 1.0
    $ renpy.pause(5.0)
    show sayori at thide
    hide sayori
    scene bg bedroom_night with wipeleft_scene
    "I drag myself out of the bathroom and take a quick peek at the time."
    "It's only been a few minutes, but it feels like I've been thinking about Sayori for hours..."
    "Maybe I have, though?"
    "I've spent the entire day worrying about her."
    "It can't be selfish for me to think about other things, right?"
    "Ah, screw it... I'm going to sleep."
    scene black
    show bg longfadebedroom
    "I tuck myself into bed and close my eyes."
    "I can worry about this stuff tomorrow."
    "And with those last thoughts, my mind sinks away into my dreams."
    window hide
    scene black with wipeleft_scene
    $ sayori_happiness = 1
    python:
        if sayori_happiness > 0:
            renpy.jump("mod_day1_nightevent")
        else:
            renpy.jump("mod_day2_main")

label mod_day1_nightevent:
    $ renpy.pause(5)
    window show
    "Suddenly, I'm woken up by the sound of my doorbell ringing repeatedly."
    show screendark zorder 999
    show bg bedroom_night with Dissolve(3.0)
    "I groggily sit up and look out the window... it's still dark, save for the light coming from the streetlamps."
    show bg kitchen_night with Dissolve(2.0)
    "I trudge out of my room, almost fall down the stairs, and eventually arrive and the front door."
    "Whoever's there is alternating between frantically ringing the doorbell and pounding on the door."
    "However, I've already figured out who it is at this point."
    play music downpour fadein 5.0
    "I open the door..."
    show sayori 4w at t11:
        zoom 2.0 ypos 2.0
        linear 0.5 zoom 2.4 ypos 2.3
    s "[player]...!"
    scene black with Dissolve(1.0)
    "Sayori quickly throws her arms around me and squeezes me tightly, tears streaming down her face."
    mc "Whoa... Sayori, what's wrong...?"
    s "{cps=20}M-my thoughts... they were being really mean to me...{/cps}"
    s "Th-they won't get out of my head..."
    s "Help me, [player]..."
    mc "..."
    "I gently wrap my arms around Sayori and start stroking her hair."
    "She continues crying into my chest."
    mc "{i}Shh... it's okay...{/i}"
    mc "I'm here..."
    show screendark zorder 999
    show sayori 1v at t11:
        zoom 2.4 ypos 2.3
    "Sayori looks up at me, then tries to say something..."
    s "[player]..."
    show sayori 1w with alphadissolve:
        zoom 1.9 ypos 2.275
    "...but she's unable to finish, and breaks down sobbing again."
    hide sayori with Dissolve(0.5)
    "She cries into my shirt more and more, only able to speak fragments in between her sobbing."
    s "I... I can't do it... not alone..."
    s "I'm so scared..."
    mc "Shhh..."
    mc "It's alright... I'm here now..."
    window hide
    $ renpy.pause(5.0)
    window show
    "It's been a few minutes, and Sayori hasn't stopped crying."
    "In that time, I had moved over to the couch so that she wouldn't have to be stuck standing up."
    "But now I'm starting to think that maybe getting her some sleep would help more..."
    mc "Hey, Sayori..."
    show sayori 1v at t11:
        zoom 2.4 ypos 2.3
    mc "How about we sleep together for the rest of the night?"
    show sayori 1e with alphadissolve:
        zoom 1.9 ypos 2.275
    "She wipes some of the tears from her eyes and nods."
    "I can tell she wants to say something too, but can't."
    hide sayori with Dissolve(0.5)
    "I slowly stand up so I don't jar her too much, then carry her upstairs and into my bedroom."
    scene bg bedroom_night with Dissolve(2.0)
    show screendark zorder 999 with Dissolve(1.0)
    "Once we arrive, I try to tuck Sayori in, but she stays latched on to me."
    show sayori 1v at t11:
        zoom 2.4 ypos 2.3
    mc "Come on, Sayori..."
    mc "I just need to let you go so I can tuck you in." 
    mc "{cps=10}{i}I won't leave you.{/i}{/cps}"
    "I try to pry myself free from Sayori's grasp."
    show sayori 1p with alphadissolve:
        zoom 2.0 ypos 2.4
    "She lets out a little squeak and clings to me even tighter in response."
    mc "..."
    "It's clear at this point that she does not want to let go, so I decide to just climb into bed with her attached to me and then pull the covers over us."
    "But if leaving her alone hurt her that badly, I don't blame her."
    mc "Sayori, I..."
    hide sayori with Dissolve(0.5)
    "I gently wrap my arms around her."
    mc "...I'm sorry."
    mc "I love you."
    "Sayori doesn't say anything but I can feel her start to relax."
    stop music fadeout(5.0)
    scene black with Dissolve(5.0)
    "I close my eyes and wait for sleep to fall over me."
    "All I can do is shout at myself inside my head."
    "How selfish was I?"
    "To leave Sayori alone as she was drowning in her depressive thoughts?"
    "I feel a tear roll down my cheek."
    "I wanted to cry in anger and sorrow, but I couldn't put Sayori through that."
    "I made her suffer enough as it is."
    "Feeling guilty and emotionally tarnished, I try my hardest to fall asleep."
    "Maybe I can..."
    "Make this better..."
    "{cps=10}{i}Tomorrow...{/i}{/cps}"
    jump mod_day2_main