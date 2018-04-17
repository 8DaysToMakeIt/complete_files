
image sayori_sway:
    subpixel True
    "cg/s_kill.png"
    zoom 0.7
    xpos 0.51
    rotate -1.5    
    block:
        ease 5.0 xpos 0.49 rotate 1.5
        ease 5.0 xpos 0.51 rotate -1.5    
        repeat

label mod_day1_main:
    $ sayori_happiness = 3
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the festival."
    "Of all the days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I considered going to her house to wake her up, but decided that's a little {i}too{/i} much."
    "Meanwhile, the preparations for the event should be nearly complete."
    "I managed to carry all the cupcakes myself by carefully stacking two trays."
    "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with Sayori and Natsuki at the festival."
    "But knowing Monika, I'm sure the event will be great, too."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"
    m "You're the first one here!"
    m "Thanks for being early."
    mc "That's funny, I thought at least Yuri would be here by now."
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that have all the poems we're performing."
    "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    "So, that's the one I'll be performing."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah, she overslept again..."
    mc "That dummy."
    mc "You'd think that on days this important, she'd try a little harder..."
    "I say that, but I suddenly remember what Sayori told me yesterday..."
    "And I suddenly feel awful, knowing it's not nearly that simple for her."
    "I only said it because it's the way I'm used to thinking."
    "But..."
    "Maybe I should have gone to wake her up after all?"
    menu:
        "What should I do?"
        "Go wake her up.":
            $ sayori_happiness = sayori_happiness + 1
            show expression Text("[sayori_happiness]"):
                ypos 0.5
            call mod_day1_wakeup
        "Let her sleep in.":
            $ sayori_happiness = sayori_happiness - 3
            show expression Text("[sayori_happiness]"):
                ypos 0.5
            call mod_day1_ignore
        "Wait outside her house.":
            $ sayori_happiness = sayori_happiness - 1
            show expression Text("[sayori_happiness]"):
                ypos 0.5
            call mod_day1_waitoutside
    return 

label mod_day1_wakeup:
    $ cb_save_reset()
    "If I let Sayori sleep in, she'd feel really bad for waking up late."
    "Besides, I'm a bit worried considering what she said yesterday."
    mc "...you know what?"
    m "Hmm?"
    mc "I actually am a bit worried about Sayori now. I'll go check up on her."
    m 1b "Alrighty then! Just don't leave me here alone for too long~"
    scene black with wipeleft
    "After hearing Monika's words I immediately exit the clubroom, and begin walking to Sayori's house."
    stop music fadeout 2.0
    scene bg house with wipeleft
    "After a few minutes of walking I reach Sayori's house."
    "I ring the bell once, but don't get an answer."
    "I decide to just enter; she's sleeping after all."
    scene black with wipeleft_scene
    mc "Sayori?"
    "She really is a heavy sleeper."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    "That really is something a boyfriend would do..."
    "In any case..."
    "It just feels right."
    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    scene sayori_bedroom with wipeleft
    mc "Sayori?"
    mc "You awake?"
    "As I peek in I notice Sayori sleeping in her bed."
#    play music "bgm/5_sayori.ogg" fadeout 2.0
    "Seeing her like that is kind of heartwarming..."
    "But I can't be thinking like that right now. How can I wake her up...?"
    "I decide to just gently shake her."
    mc "Come on Sayori, wake up."
    show sayori 1bp at t11 with hpunch
    "A few shakes later, Sayori opens her eyes sleepily."
    play music silverlining_d fadein 2.0
    s "Mngh... wh-wha...?"
    mc "It's time for the festival!"
    show sayori 4bm
    "Upon hearing those words Sayori shuffles a bit in her bed."
    show sayori 1bd
    "She then gives me a small smile."
    s "Right... the festival... we'll be spending all day together..."
    "She slowly rises from her bed, rubbing her eyes."
    "I guess a small smile is all she can give right now."
    "But it doesn't matter."
    "I promised I'd help her get better, even if it's small steps at a time."
    "I'll always be by her side."
    mc "I'll give you some privacy now."
    s 1bk "Y-yeah..."
    scene black with wipeleft
    "I step outside her room and close the door."
    "At this point, I'm alone with my thoughts."
    "A part of me is anxious about the festival, but another part of me is worrying about Sayori."
    "I linger on that latter thought."
    "She doesn't even know what she's feeling herself, but I have to help her."
    "She thinks she's in this alone, but she's wrong."
    "She has me now."
    "{cps=35}I love her and I'm willing to do whatever it takes to--{/cps}{nw}"
    "The door swings open and out comes Sayori."
    scene sayori_bedroom wipeleft
    show sayori 1 at t11
    s "Well... I guess I'm ready."
    mc "Alright then, lets get going. Monika did tell me not to keep her waiting after all."
    "Upon hearing Monika's name she suddenly smiles."
    s 4r "Well let's go then! I can't wait to see the festival!"
    "Her happy act was enough to get me to smile. But I know that it was just a facade down under."
    "However, that thought only strengthened my determination."
    "One day, she'll be able to truly smile again. But this time, it won't be fake."
    scene bg residential_day with wipeleft_scene
    "I can't help but worry about Sayori as we walk back to the literature club together."
    "Eventually, my thoughts get to me."
    mc "Sayori?"
    show sayori 1c at t11
    s "What's up?"
    stop music fadeout 2.0
    "I look around, checking to see if anyone else is near us."
    mc "Sayori... how are you really feeling?"
    show sayori 1k
    "She looks around as well, and sighs when she notices we're alone."
    s 1l "I-I don't really know..."
    play music harshreality fadein 2.0
    s "I appreciate you caring enough to wake me up..."
    s "But you're just wasting your time on me..."
    "I grab her by the shoulders and look her in the eyes."
    show sayori 1h
    mc "Listen Sayori. I would never consider the time we spend to be a waste."
    mc "I love you after all."
    show sayori 1t
    mc "I want to do anything I can do to help you. Even if you don't understand what you're feeling."
    mc "Please...trust in me. I only want what's best for both of us."
    show sayori 1t:
         ease 0.5 zoom 2.4 ypos 2.6
    scene black with wipeleft
    "I pull her into a hug."
    "After a few moments, her arms tightly wrap around me."
    s "I-I know I've said this a lot to you, but..."
    s "...thank you."
    "I let go of her, but she still holds onto me."
    mc "You don't need to thank me. I'm only treating you how I should have."
    mc "Anyways... I guess we shouldn't leave Monika alone for any longer..."
    s "Yeah..."
    stop music fadeout 2.0
    "Sayori slowly lets go of me, and we resume walking back to school."
    "After just a few more minutes, we're back in the clubroom."
    scene bg club_day with wipeleft_scene 
    show monika 1b at t11
    play music sunnyday fadeout 2.0
    m "Welcome back!"
    m 1d "Is Sayori doing alright?"
    mc "{cps=30}Yeah, she--{/cps}{nw}"
    show monika 1b at t22
    show sayori 1h at t11
    s "I just wasn't feeling well on Friday."
    s 1r "I'm fine now, see?~"
    "Sayori gives Monika a big smile."
    show sayori at t31
    "I smile with her, but it's hard to do knowing what's happening in the depths of her mind."
    "I push a desk so that it's right up against another one. Sayori takes a seat, and I sit down next to her."
    show monika at thide
    hide monika
    show sayori 1d at t11
    "She rests her head on the desktop and I put an arm around her."
    show sayori 1f at t11
    "With her face out of Monika's view, her expression slowly loses its brightness."
    "The contrast between the truth and facade hurts me to my core."
    "But I can change this. I'll do all I can for her."
    "But the only thing I can do in the mean time is wait for Yuri and Natsuki."
    call mod_day1_morning_converge

label mod_day1_waitoutside:
    $ cb_save_reset()
    "She should be able to wake up on her own."
    "She deserves it after everything that went on yesterday."
    "But, I can't just leave her to walk to school alone."
    "What kind of person would do that?"
    mc "...you know what?"
    m "Hmm?"
    mc "I'm gonna go to Sayori's house and wait for her to wake up."
    m 3a "Alright, just don't take too long!"
    scene black with wipeleft_scene
    "As she finishes her sentence I exit the clubroom and begin walking to Sayori's house."
    scene bg residential_day with wipeleft_scene
    "I soon arrive at her house and wait at the door. It would be rude if I went in, right?"
    "I check my phone, Natsuki texted me that she was going to be a bit late today."
    "After a half hour, Sayori opens the door and steps out."
    show sayori 1k at t11
    mc "Hey Sayori!"
    s 1l "Hey..."
    show sayori 1k
    "Her eyes are red and puffy."
    "Knives of guilt dig into me -- she had clearly spent some time crying."
    "I should have been with her this morning..."
    mc "Sayori...!"
    s 1l "Don't worry about it!"
    s "Let's just go to school and work on the pamphlets."
    show sayori 2d
    "Sayori forces a smile."
    stop music fadeout 2.0
    mc "Sayori... anyone can see right through you right now."
    show sayori 1u
    "Sayori's smile disappears."
    "She looks like she's going to burst into tears again..."
    "Oh god..."
    "{i}What have I done?{/i}"
    mc "Sayori..."
    mc "I'm...I'm sorry."
    show sayori 1t
    "Tears well up in Sayori's eyes."
    s 1v "I..."
    show sayori 1w with hpunch
    play music downpour fadein 2.0
    "She bursts into tears, her hands in her face."
    s "I thought..."
    s 1v "I thought you didn't care anymore..."
    "The guilt digs into my heart now."
    show sayori 1v:
        ease 0.5 zoom 2.4 ypos 2.6
    scene black with wipeleft_scene
    play music downpour fadein 2.0  
    "I grab on to her and hug her tightly."
    "What am I doing? I don't know anything about her condition... and yet I left her all alone."
    mc "I never realized..."
    "She isn't hugging me back."
    s "Please..."
    s "Don't do this to me..."
    s "I don't deserve your attention..."
    s "I don't deserve anything...!"
    mc "Don't say that!"
    "I finally feel the guilt overcome me."
    "This was my fault."
    "I could have been with her, and comforted her that I was here."
    "All I can do now is make up for my own failure."
    "I have to make this right."
    mc "I won't leave you anymore."
    mc "I meant what I said yesterday."
    mc "I will take care of you, no matter what."
    "Sayori begins to hug me back, lightly."
    mc "..we need to get going. We don't want to keep the rest of the club waiting, do we?"
    "Sayori nods her head."
    scene bg residential_day with wipeleft_scene
    show sayori 1u at t11
    "I let go of her. But I wanted to hold onto her for longer..."
    "She still looks down, though."
    "I really hope she's okay."
    window hide
    $ renpy.pause(2)
    stop music fadeout 4.0
    show sayori 1t with alphadissolve2
    show sayori 1d with alphadissolve2
    window show
    "As we walk, Sayori's facade slowly reconstructs itself, and soon she's back to smiling."
    "A few minutes later, we arrive in the clubroom."
    stop music fadeout 2.0
    scene bg club_day with wipeleft_scene
    play music sunnyday fadein 2.0
    "Her facade isn't as bright as it usually is, but that's my fault..."
    play music sunnyday fadein 2.0
    show monika 1b at t11
    m "Welcome back!"
    m 1a "Yuri and Natsuki still haven't arrived, so we've got some waiting to do."
    m 1d "Is Sayori alright?"
    mc "Yeah, she's fine."
    mc "She just wasn't feeling well on Friday, so she stayed home to rest. She's still recovering a bit, but she can make it through the festival."
    mc "Right, Sayori?"
    show sayori 1d at t31
    "Sayori gives her a light smile and nods."
    "I flash Sayori a smile, but I can't even muster up a real one myself..."
    "I push a desk right up against another one, let Sayori take a seat, and sit down next to her."
    show monika at thide
    hide monika
    show sayori 1k at t11
    "She rests her head on the desktop, and I instinctively wrap my arm around her head."
    "I still feel terrible for making her think I forgot about her..."
    "But now, I have to be there for her. I can't make the same mistake twice."
    "So for now, we might as well relax while we wait for Yuri and Natsuki."
    call mod_day1_morning_converge
    
label mod_day1_ignore:
    $ cb_save_reset()
    "Nah, I think I'll let her get some rest."
    show monika at thide
    hide monika
    "She must be a bit tired after everything she went through yesterday."
    "In the meantime, I take a good look around the room."
    "The walls are still a bit bare, but I figure it'd be easier to take care of that when the others arrive."
    show monika 5a at t11
    m "Hey, do you want to check out the pamphlets?"
    m "I think I did a great job with them!"
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desk."
    mc "Oh yeah, this looks good."
    mc "Something like this will definitely help people take the club more seriously."
    m 2b "Yeah, I thought so too!"
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize everyone's poems from the ones they performed during our practice."
    show monika 1a
    "After I'm done looking, I put the pamphlet back down, take a seat at one of the desks, and stretch."
    mc "This is going to be great!"
    show monika 2a
    "Monika simply smiles and nods."
    show black with wipeleft
    scene bg club_day with wipeleft
    "10 minutes pass."
    show black with wipeleft
    scene bg club_day with wipeleft
    "20 minutes pass."
    show black with wipeleft
    scene bg club_day with wipeleft
    "Then 30."
    stop music fadeout 2.0
    "Geez, Sayori really is a heavy sleeper, isn't she?"
    "I get out my phone to text her that she should probably wake up, but right as I'm about to start, the clubroom door flies open."
    play music sunnyday fadeout 2.0
    show sayori 1p at t31
    s "{i}*Haaah... haaahh...*{/i}"
    s "I-I'm so sorry I'm late, [player]!"
    show sayori at t11
    s 1m "I didn't miss anything, did I?"
    show monika 1a at t31
    m "Nope."
    m 1b "The festival hasn't even started yet."
    show sayori 1o
    "Monika pats Sayori on the shoulder, clearly able to tell how distressed she is."
    show sayori 1k
    show monika at thide
    hide monika
    "Still panting, Sayori walks over to the desk next to mine and slumps down into the seat, resting her head on the desktop."
    "A tinge of guilt runs through me; she was probably waiting for me to greet her as she left her house..."
    "...or maybe she needed me to wake her up after all."
    "I pause for a moment, then pull my desk right up to hers and put an arm around her."
    "It's the least I can do."
    show sayori 1y
    "Sayori does her best to smile, but I can tell how hurt she is that I wasn't there for her."
    show sayori 1t
    "She's on the verge of tears. I can tell how hard she's trying to not break down in front of Monika."
    show sayori 1v
    "I start gently rubbing her back in an attempt to console her."
    "I know she doesn't want to show her true self in front of the others yet, so I do what I can do to help while we wait for the others to arrive."
    call mod_day1_morning_converge

label mod_day1_morning_converge:
    show black with wipeleft
    scene bg club_day with wipeleft
    show sayori 1y at t11
    "After about 15 minutes, the door flies open and Natsuki steps into the room with Yuri in tow."
    show sayori 1a at t33
    show natsuki 1d at t32
    show yuri 1a at t31
    n "Alright, it's festival time!"
    "Sayori perks up upon seeing them enter the room."
    show natsuki 1a
    s 1x "Hey, Natsuki! Hey, Yuri!"
    show sayori 1a
    y 1b "Hello, Sayori."
    y 1f "I know you left early on Friday, and I wanted to ask... is everything alright?"
    s 1x "I just wasn't feeling well... I'm fine now!"
    show yuri 1a
    s 4r "Let's just get this thing started!"
    show yuri 1c
    "Yuri nods, and begins helping Monika set up the banners."
    show yuri at thide
    hide yuri
    show natsuki at t21
    show sayori 1a at t22
    "Meanwhile, Natsuki inspects the cupcakes to ensure I haven't ruined any of them."
    show natsuki at thide
    hide natsuki
    show black with wipeleft
    hide black with wipeleft
    show monika 4b at t21
    m "Hey... I printed the booklets using the school printers... would you mind proofreading them, [player]?"
    m 2b "I didn't really check for mistakes, but I have my laptop so if there are any, I can just fix them."
    mc "Sure thing."
    show monika 1a
    "I pick up the booklet from my desk and hold it between me and Sayori."
    mc "Wanna look it over together?"
    show sayori 1q
    "Sayori nods, and we start reading."
    show black with wipeleft
    call mod_day1_afternoon
    
    
    
label mod_day1_dead:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the festival."
    "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I considered going to her house to wake her up, but decided that's a little too much."
    "Meanwhile, the preparations for the event should be nearly complete."
    "I managed to carry all the cupcakes myself by carefully stacking two trays."
    "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."
    "But knowing Monika, I'm sure the event will be great, too."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    mc "That's funny, I thought at least Yuri would be here by now."
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that has all the poems we're performing."
    "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    "So, that's the one I'll be performing."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah, she overslept again..."
    mc "That dummy."
    mc "You'd think that on days this important, she'd try a little harder..."
    "I say that, but I suddenly remember what Sayori told me yesterday..."
    "And I suddenly feel awful, knowing it's not nearly that simple for her."
    "I only said it because it's the way I'm used to thinking."
    "But..."
    "Maybe I should have gone to wake her up after all?"
    m 1k "Ahaha."
    m 4b "You should take a little responsibility for her, [player]!"
    "Well, she's not wrong about that."
    "I sigh. She's probably going to be here soon anyway."
    "After a couple moments of awkward silence, Monika speaks up again."
    m 5 "Hey, do you want to check out the pamphlets?"
    m "They came out really nice!"
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desks."
    mc "Oh yeah, they really did."
    mc "Something like this will definitely help people take the club more seriously."
    m "Yeah, I thought so too!"
    m 3g "But, um... Sayori sent me a different poem last night."
    m "I'm not sure what it means... I was going to do something, but I feel like you know her better than I do."
    m "Maybe you could take a look?"
    "I nod, then quickly flip through the pages."
    show monika zorder 1 at thide
    hide monika
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    mc "What's this...?"
    stop music fadeout 2.0
    "I flip to Sayori's poem."
    "It's different from the one she practiced."
    "It's one that I haven't read before..."
    call showpoem (poem_s3, music=False)
    mc "Ah--"
    "What is this...?"
    "Reading the poem, I get a pit in my stomach."
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "What's wrong?"
    mc "Ah, I..."
    "This poem feels completely different from everything else Sayori's written."
    "But more than that..."
    mc "{i}T-this isn't right...!{/i}"
    mc "{i}I'm going to go get Sayori.{/i}"
    m "Ah--"
    m 1d "{cps=30}Should I go with you--{/cps}{nw}"
    scene bg corridor with wipeleft
    "I've already left the classroom."
    "I quicken my pace."

    scene bg residential_day with wipeleft_scene
    "What was I thinking?"
    "I should have tried a little bit harder for Sayori."
    "It's not a big deal to at least wait for her, or help her wake up."
    "Even the simple gesture of walking her to school makes her really happy."
    "Besides..."
    "I told her yesterday that things will be the same as they always have been."
    "That's all she needs, and what I want to give her."

    scene bg house with wipeleft
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    mc "Sayori?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    "Isn't that more like something a boyfriend would do?"
    "In any case..."
    "It just feels right."
    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    window hide(None)
    window auto
    play music lefthanging
    show s_kill_bg
    show sayori_sway
   # show s_kill:
   #     truecenter
   #     zoom 0.7 xalign 0.5 yalign 0.05
   #     pause 0.5
    $ renpy.pause(3)
    "What the hell...?"
    "{i}What the hell??{/i}"
    "Is this a nightmare?"
    "It...has to be."
    "This isn't real."
    "There's no way this can be real."
    "Sayori wouldn't do this."
    "Everything was normal up until a few days ago."
    "That's why I can't believe what my eyes are showing me...!"
    scene black with dissolve_cg
    "I suppress the urge to vomit."
    "Just yesterday..."
    "I told Sayori I would be there for her."
    "I told her I know what's best, and that everything will be okay."
    "Then why...?"
    "Why would she do this...?"
    "How could I be so helpless?"
    "What did I do wrong?"
    "Turning down her confession..."
    "That has to have been what pushed her over the edge."
    "Her agonized scream still echoes in my ears."
    "Why did I do that to her when she needed me the most?"
    "Why was I so selfish?"
    "This is my fault--!"
    "My swarming thoughts keep telling me everything I could have done to prevent this."
    "If I just spent more time with her."
    "Walked her to school."
    "And gave her what I know she wanted out of our relationship..."
    "...Then I could have prevented this."
    "I know I could have prevented this!"
    "Screw the Literature Club."
    "Screw the festival."
    "I just...lost my best friend."
    "Someone I grew up with."
    "She's gone forever now."
    "Nothing I do can bring her back."
    "This isn't some game where I can reset and try something different."
    "I had only one chance, and I wasn't careful enough."
    "And now I'll carry this guilt with me until I die."
    "Nothing in my life is worth more than hers..."
    "But I still couldn't do what she needed from me."
    "And now..."
    "I can never take it back."
    "Never."
    "Never."
    "Never."
    "Never."
    "Never..."
    window hide
    stop music fadeout 2.0
    pause 2.0
    show sayori_sway
    play music introtrack fadein 2.0
    call screen dialog("Well... you did it. You killed her.", ok_action=Return())
    call screen dialog("Honestly, I'm surprised.", ok_action=Return())
    call screen dialog("Did you {i}really{/i} think turning down her confession would make it any better?", ok_action=Return())
    call screen dialog("I mean, you saw her reaction.", ok_action=Return())
    call screen dialog("Did it look like you made her any happier?", ok_action=Return())
    call screen dialog("Not to mention that from what I'm seeing, it looks like you didn't even unlock the contents of the mod.", ok_action=Return())
    call screen dialog("Sigh...", ok_action=Return())
    pause 2.0
    call screen dialog("I guess we're going to have to try this again, aren't we?", ok_action=Return())
    call screen dialog("Here we go... and please, don't screw it up this time.", ok_action=Return())
    menu:
        "SYSTEM" "Reset game?"
        "Confirm.":
            $ persistent.playthrough = 1
            pause 1.0
            $ renpy.full_restart(transition=None, label="splashscreen")

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
