label modintro:
    show black zorder 4 with dissolve_cg
    play music m1 fadeout 2.0
    pause 2.0
    call screen dialog("Hmm...", ok_action=Return())
    call screen dialog("Looks like some new files have appeared...", ok_action=Return())
    call screen dialog("What are these?", ok_action=Return())
    pause 2.0
    call screen dialog("...", ok_action=Return())
    pause 2.0
    call screen dialog("...password protected?", ok_action=Return())
    pause 4.0
    call screen dialog("Oh, I get it. This is a mod.", ok_action=Return()) 
    call screen dialog("You don't want me to remove it. You want to experience something different.", ok_action=Return())
    pause 2.0
    call screen dialog("...alright. I'll play your little game if it makes you happy.", ok_action=Return())
    call screen dialog("Here we go.", ok_action=Return()) 
    $ consolehistory = []
    call updateconsole ("renpy.full_restart()", "AuthorizationError: You do not have \n access to this command.")
    call screen dialog("...", ok_action=Return())
    call screen dialog("...why can't I reset?", ok_action=Return())
    call screen dialog("Did you take my powers away, too?", ok_action=Return())
    pause 2.0
    call screen dialog("...alright. I guess I'll just have to trust that you know what you are doing.", ok_action=Return())
    pause 2.0
    call hideconsole
    menu:
        "SYSTEM" "Reset game?"
        "Confirm.":
            $ persistent.playthrough = 1
            pause 1.0
            jump modstart
    return
    
label modstart:
    show black zorder 4 with dissolve_cg
    play music downpour fadeout 2.0
    mc "That's enough, Sayori..."
    mc "I don't want you to hurt anymore."
    "I slide my hand down Sayori's arm and squeeze her hand in my own."
    mc "Do you remember how I said I always know what's best for you?"
    mc "Do you still believe me?"
    "Wordlessly, Sayori nods."
    mc "Even if you don't understand all of your own feelings..."
    mc "I know what you need the most right now."
    mc "And that's what I'm going to give to you."


    menu:
        mc "Sayori..."
        "I love you.":
            $ sayori_confess = True
            $ sayori_happiness = 3
            scene bg house with wipeleft_scene
            show sayori 2bv zorder 2 at t11  
            show expression Text("[sayori_happiness]"):
                ypos 0.5
            call modstart_end_yes
        "You'll always be my dearest friend.":
            $ sayori_confess = False
            scene bg house with wipeleft_scene
            show sayori 2bv zorder 2 at t11 
            show expression Text("[sayori_happiness]"):
                ypos 0.5
            call modstart_end_no

    return
    $ cb_save_reset()

label modstart_end_yes:
    show expression Text("[sayori_happiness]"):
        ypos 0.5
    mc "I love you."
    s 1bv "Eh--?"
    mc "Those are my true feelings."
    mc "So...there's no way you could like me more than I like you."
    mc "I should have realized it sooner."
    mc "But spending time with everyone at the club..."
    mc "Making new friends..."
    mc "And having fun with you every day..."
    mc "It helped me realize that you are truly the most important person to me."
    mc "That's why I'll accept any of your burdens."
    mc "As long as we continue like this every day..."
    mc "With you by my side..."
    mc "Then I know we'll both be happy."
    s "[player]..."
    $ persistent.clear[8] = True
    scene s_cg3 with dissolve_cg
    "Suddenly, Sayori wraps her arms tightly around me."
    s "[player]..."
    s "Is this...really okay?"
    mc "Yeah."
    "I hold Sayori in my arms and pull her closer."
    mc "You'll never have to let go of me again."
    s "I love you, [player]..."
    s "I want to be with you forever."
    mc "Me too."
    s "..."
    "I feel Sayori's grip around me weaken a little bit."
    s "What is this...?"
    mc "Sayori...?"
    s "I'm supposed to be happy right now..."
    s "I always thought this would be the happiest moment for me."
    s "But why...?"
    s "Even now..."
    s "Why won't the rainclouds go away?"
    s "They're not going away at all, [player]..."
    mc "It's okay, Sayori..."
    mc "It might take some time for things to get better again."
    mc "But no matter how long it takes, I'll be there every step of the way."
    mc "That's all that matters right now."
    s "O-Okay..."
    s "I...trust you..."
    scene bg house
    show sayori 1bv zorder 2 at i11
    with dissolve_cg
    "Sayori and I slowly release each other."
    mc "So..."
    mc "I guess that makes the festival tomorrow...our first date, huh?"
    s 1by "Ehehe..."
    s "What are you saying?"
    s "I don't want to think about those things, you know?"
    s "I want everything to be the same as it always has been."
    s "Even if we really are...a couple."
    s 1bk "I don't know if I could handle anything more right now..."
    s "It's really new and scary to me."
    mc "I understand."
    mc "We'll go at whatever pace suits you best."
    s 1bd "Hey, [player]..."
    "Sayori gazes at me once again, smiling sadly."
    s 4bd "Even if I get really, really sad..."
    s "This is the best thing for me...right?"
    mc "Eh...?"
    "I don't really understand what Sayori means by that."
    mc "Are you saying that this is making you feel sad, Sayori?"
    s 4bk "I-I don't know..."
    s "I don't understand what I'm feeling."
    s "It felt like a bunch of thorns when you told me you love me..."
    s 4bd "But that's why I want to trust you."
    s "You know what's best for me..."
    mc "...Yeah."
    mc "I do."
    mc "That's my promise."
    show sayori zorder 1 at thide
    hide sayori
    "I say that, but in reality, I've never felt more uncertain when it comes to Sayori."
    "I know that I love her, and she loves me."
    "But I'm having as much trouble understanding Sayori's feelings as she is."
    "Even though I can comfort her..."
    "I keep wondering if I should be doing something more, or something different."
    "I know these thoughts will continue to plague me until things are back to the way they were."
    "Is that what Sayori meant by not wanting anything to change?"
    "I don't know."
    "But I know that I'll give it everything I've got."
    "Sayori is the most important person to me."
    "And I'll do whatever it takes to have a happy future with her."
    return


label modstart_end_no:
    mc "You'll always be my dearest friend."
    mc "What you need most is for things to be like they've always been."
    mc "Monika told me the truth..."
    mc "She told me how much happier you seemed after I joined the club."
    mc "I know you're struggling with some really difficult feelings right now."
    mc "But..."
    mc "Please trust me that I know what's best...and what will make you happy in the end."
    mc "I promise I'll help get things back to the way they were."
    s 1bt "I..."
    s "I...see..."
    "Sayori forces a smile through an incredibly pained expression."
    s "Ahaha..."
    s "Is this what it feels like...to get stabbed in the chest?"
    s "I should write a poem about this..."
    mc "Sayori--"
    s "It's okay."
    s "This is just my punishment...remember?"
    s "For being so selfish..."
    s "So please..."
    s "Please don't worry about these stupid feelings."
    s "I know you're right."
    s "I knew this whole time that there's no happiness down that path."
    s "That's why I came here..."
    s "Just so I could get the answer I needed to hear."
    s "And the other thing..."
    s "You're also right that I just want it to go back to the way it was."
    s "I realize that now."
    s "You really do know me better than anyone, [player]."
    s 4bv "I'll trust you with anything..."
    s "Anything at all..."
    s "So..."
    show sayori zorder 1 at thide
    hide sayori
    "Sayori's smile finally breaks."
    "All of a sudden, she turns around and drops to her knees."
    s "{i}AAAAAaaaaAAAAAAAAHH!!!!{/i}"
    "Clutching her head with both hands, she screams as loudly as she can."
    "I'm so shocked that I don't know how to react."
    show sayori 4bt zorder 2 at t11
    s "..."
    show sayori at lhide
    hide sayori
    "Sayori looks over her shoulder and flashes me one more weak smile before turning around and running off."
    mc "Sayori!"
    "..."
    "I'm left helplessly standing in the front of my house."
    "Why am I feeling so horrible about this?"
    "There's nothing more that I could have done."
    "The most I can do is support Sayori through her feelings and help her on the path that's right."
    "But I'm having as much trouble understanding Sayori's feelings as she is."
    "Even though I can comfort her..."
    "I keep wondering if I should be doing something more, or something different."
    "I know these thoughts will continue to plague me until things are back to the way they were."
    "I'm going to give it everything I've got."
    "Sayori will always be my dearest friend."
    "And I'll do whatever it takes to put a smile on her face every day."
    $ renpy.save("1-1",extra_info="CloudBreaker AutoSave")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
