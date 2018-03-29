
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
    "The more I think about it, the more I feel the need to do something..."
    menu:
        "What should I do?"
        "Go wake her up.":
            $ sayori_happiness = sayori_happiness + 1
            $ cb_save_reset()
            call mod_day1_wakeup
        "Let her sleep in.":
            $ sayori_happiness = sayori_happiness - 3
            $ cb_save_reset()
            call mod_day1_ignore
        "Wait outside her house.":
            $ sayori_happiness = sayori_happiness - 1
            $ cb_save_reset()
            call mod_day1_waitoutside
    return 

label mod_day1_wakeup:
    mc "...you know what?"
    m "Hmm?"
    mc "I actually am a bit worried about Sayori now. I'll go check up on her."
    m 1b "Alrighty then! Just don't leave me here alone for too long~"
    scene black with wipeleft
    "After hearing her words I immediately exit the club and school, and begin walking to Sayori's house."
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
    play music "bgm/5_sayori.ogg" fadeout 2.0
    "Looking at her sleeping like that, it's kinda heartwarming... I wonder what she is dreaming of?"
    "But now I gotta focus. How can I wake her up...?"
    "After some thinking, I decide to just gently shake her."
    mc "Come on Sayori, wake up."
    show sayori 1bp at t11 with hpunch
    s "Mmph... wh-wha...?"
    mc "It's time for the school festival!"
    "I take a deep gulp, and I feel like I might regret what I say next a bit..."
    mc "You know... time for our first date."
    show sayori 4bm
    "After hearing those words Sayori shuffles a bit in her bed."
    show sayori 1bd
    "She then gives me a small smile."
    s "W-well, thank you [player]."
    s 1be "I'm glad you cared enough about me to do this..."
    "She slowly rises from her bed, rubbing her eyes as she does so."
    "I guess a small smile is all she can give right now."
    "But it doesn't matter."
    "I promised I'd help her get better. Even if it's small steps at a time."
    "I'll always be by her side."
    mc "I'll give you some privacy now."
    s 1bk "Y-yeah..."
    scene black with wipeleft
    "I step outside her room and close the door."
    "At this point, I'm alone with my thoughts."
    "A part of me is anxious about the festival, but another part of me is worrying about Sayori."
    "I linger at that thought."
    "She doesn't even know what she's feeling herself."
    "But I have to help her."
    "She thinks she's in this alone. But she's wrong."
    "She has me now."
    "{cps=35}I love her and I'm willing to do whatever it takes to--{/cps}{nw}"
    "The door swings open and out comes Sayori."
    scene sayori_bedroom wipeleft
    show sayori 1 at t11
    s "Well... I guess I'm ready."
    mc "Alright then, lets get going. Monika did tell me not to keep her lonely after all."
    "When she hears Monika's name she suddenly smiles."
    s 4r "Well let's go then! I can't wait to see the festival!"
    "Her happy act was enough to get me to smile. But I know that deep down she was still depressed."
    "But that thought only strengthened my determination."
    "One day, she'll actually smile like this, without any of the lurking shadows."
    scene bg residential_day with wipeleft_scene
    "As we walk back to school I can't help but wonder how she's really feeling."
    mc "Sayori?"
    show sayori 1c at t11
    s "What's up?"
    "I look around, trying to see if anyone's around."
    "The coast is clear."
    mc "Sayori... How are you really feeling?"
    show sayori 1k
    "She looks around as well, and sighs when she notices we're alone."
    s 1l "I-I don't really know... I appreciate you caring enough to wake me up..."
    s "But you're just wasting your time on me..."
    "I grab her by the shoulders and look her in the eyes."
    show sayori 1h
    mc "Listen Sayori. I would never consider the time we spend to be a waste."
    mc "I love you after all."
    show sayori 1t
    mc "I want to do anything I can do to help you. Even if you don't understand what you're feeling."
    mc "Please...trust in me. I only want what's best for both of us."
    scene black with wipeleft
    "I pull her into a hug."
    "After a few moments, her arms tightly wrap around me."
    stop music fadeout 2.0
    s "I-I know I've said this a lot to you, but..."
    s "...thank you."
    "I let go of her, but she still holds onto me."
    mc "You don't need to thank me. I'm only treating you how I should have."
    "Anyways... I guess we shouldn't leave Monika alone for any longer..."
    "Sayori slowly lets go of me, and we resume walking back to school."
    "After just a few more minutes, we're back in the clubroom."
    scene bg club_day with wipeleft_scene 
    show monika 1b at t11
    play music lctheme fadeout 2.0
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
    "I push a desk so that it's right up against another one, let Sayori take a seat, then sit down right next to her."
    show monika at thide
    hide monika
    show sayori 1d at t11
    "She rests her head on the desktop and I put an arm around her."
    show sayori 1f at t11
    "With her face out of Monika's view, I see her expression slowly lose its brightness."
    "It hurts to see her like this, and I know she's suffering... but I'm going to try my hardest to help that go away in the coming days."
    call mod_day1_morning_converge

label mod_day1_waitoutside:
    "I think I should let her wake up for herself."
    "She deserves it after everything that went on yesterday."
    "But, I shouldn't just leave her to walk to school alone."
    "What kind of person would do that?"
    mc "Monika?"
    m "Yes?"
    mc "I think I'm going to go and wait for Sayori to wake up."
    m 1b "Alright!"
    m 3a "Don't take too long, though!"
    scene black wipeleft_scene
    "I exit the school building and walk to Sayori's house."
    scene bg residential_day with wipeleft_scene
    "About half an hour after I arrive, Sayori walks through the door, dressed for school, with a sullen look on her face."
    show sayori 1k at t11
    mc "Hey Sayori!"
    s 1l "Hey..."
    show sayori 1k
    "She looks like she's been crying again..."
    "Did I do this?"
    mc "Ah..."
    s 1l "Don't worry about it!"
    s 1k "Let's just go to school and work on the pamphlets."
    "Come on, Sayori."
    "I'm not dumb, and neither are you."
    "I can see right through this."
    show sayori 1g
    mc "I can see when you are putting up an image..."
    mc "Please..."
    show sayori 1u
    mc "Don't do that..."
    "She looks like she's going to burst into tears again..."
    "Oh god..."
    "{i}What have I done?{/i}"
    mc "Please tell me what's wrong..."
    show sayori 1t
    "She looks at me with a faded smile and tears welling up in her eyes."
    s 1v "I..."
    show sayori 1w with hpunch
    "She bursts into tears, her hands in her face."
    s "I thought..."
    s 1v "I thought you didn't care anymore..."
    "A pit of guilt sat in my stomach."
    scene black with wipeleft_scene
    play music t9 fadeout 2.0  
    "I grab on to her and pull her into a tight hug."
    "I don't even know how tight I was squeezing."
    "But I wasn't letting this go on any longer."
    mc "I never realized..."
    "She started struggling again."
    "She wasn't hugging back, either."
    s "Please..."
    s "Don't do this to me..."
    s "I don't deserve your attention..."
    s "I don't deserve anything..."
    mc "Don't speak like that!"
    "At this point I was almost crying too."
    "What had I done?"
    "What could I have done differently?"
    mc "I will never leave you."
    mc "I meant what I said yesterday."
    mc "I will take care of you, no matter what."
    mc "And besides, I still get to spend time with the others at the club!"
    mc "That is what I want."
    "Sayori begins to hug back, lightly."
    mc "We need to get going. We don't want to keep the rest of the club waiting, do we?"
    "Sayori nods her head."
    scene bg residential_day with wipeleft_scene
    show sayori 1u at t11
    "We stop hugging and start walking."
    "She still looks down, though."
    "I really hope she's okay."
    "A few minutes later, we arrive in the clubroom."
    scene bg club_day with wipeleft_scene
    play music lctheme fadeout 2.0
    "During our walk there, Sayori was able to build her facade back up... at least a little bit."
    "I don't blame her. I'm the only one who's seen her darker side."
    show monika 1b at t11
    m "Welcome back!"
    m 1a "Yuri and Natsuki still haven't arrived, so we've got some waiting to do."
    m 1d "Is Sayori alright?"
    mc "Yeah, she's fine."
    mc "She just wasn't feeling well on Friday, so she stayed home to rest. She's still recovering a bit, but she can make it through the festival."
    mc "Right, Sayori?~"
    show sayori 1d at t31
    "Sayori simply smiles and nods."
    "I smile with her, but it's hard to do that knowing what's happening in the depths of her mind..."
    "With that conversation over, I push a desk so that it's right up against another one, let Sayori take a seat, and then sit down next to her."
    show monika at thide
    hide monika
    show sayori 1k at t11
    "She rests her head on the desktop and I put an arm around her."
    "I still feel terrible for making her think I forgot about her..."
    "But there's no taking that back at this point."
    "So for now, we might as well relax while we wait for Yuri and Natsuki."
    call mod_day1_morning_converge
    
label mod_day1_ignore:
    "Nah, I think I'll let her get some rest."
    show monika at thide
    hide monika
    play music lctheme fadeout 2.0
    "She must be a bit tired after everything she went through yesterday."
    "In the meantime, I take a good look around the room."
    "The walls are still a bit bare, but I figure it'd be easier to take care of that when the others arrive."
    show monika 5a at t11
    m "Hey, do you want to check out the pamphlets?"
    m "They came out really nice!"
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desk."
    mc "Oh yeah, they really did."
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
    show sayori 1p at t31
    s "{i}*Haaah... haaahh...*{/i}"
    s "I'm so sorry I'm late, MC!"
    show sayori at t11
    s 1m "I didn't miss anything, did I?"
    show monika 1a at t31
    m "Nope."
    m 1b "The festival hasn't even started yet, so you have plenty of time."
    show sayori 1o
    "Monika pats Sayori on the shoulder, clearly able to tell how distressed she is."
    show sayori 1k
    show monika at thide
    hide monika
    "Still panting, Sayori walks over to the desk next to mine and slumps down into the seat, resting her head on the desktop."
    "I suddenly feel really bad; she had probably been waiting for me to greet her as she left her house..."
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
    "Yuri nods, then moves to help Monika hang the banner up."
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
    m "Hey, I printed the booklets using the school printers... would you mind proofreading them, [player]?"
    m 2b "I didn't really check for mistakes, but I have my laptop so if there are any, I can just fix them."
    mc "Sure thing!"
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
    play music td
    show s_kill_bg
   # show s_kill:
   #     truecenter
   #     zoom 0.7 xalign 0.5 yalign 0.05
   #     pause 0.5
    show sayori_sway
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
    pause 2.0
    show sayori_sway
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
