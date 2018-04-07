

label mod_day1_afternoon:
    scene bg corridor with wipeleft_scene
    stop music fadeout 2.0
    show sayori 1a at t11
    "After the Literature Club's event, we decided to split up for the rest of the festival, since there is so much to do and everyone has their own interests."
    "We had a pretty good turnout, and a lot of people seemed excited watching us recite our poems."
    "Some of them even tried their hand at reciting them, as Monika had planned."
    "This gave us all hopes of finding new members, but only time will tell."
    "We'll have to see how it all plays out tomorrow."
    show black with wipeleft
    scene bg courtyard with wipeleft_scene
    "As we walk around in the courtyard, we observe the numerous food stands set up around the place."
    show sayori 1x at hop
    "Sayori excitedly looks around."
    s "Everything looks sooo good! I want to try and eat everything!"
    "I give her a concerned glance, but nod in agreement."
    "Is she saying this based on her own feelings? Or is this just another part of her facade?"
    "No no, I can't get distracted by things like that. This is our time together."
    mc "How about we split up, and we can meet up at the registers later."
    s 1r "Sounds good!"
    show sayori at thide
    hide sayori
    "With that, Sayori runs off in a random direction, and I start browsing the stands closest to me."
    show black with wipeleft
    hide black with wipeleft
    "5 minutes later, we meet up at the registers, ready to pay for our food."
    "I got myself a bowl of ramen, and spot Sayori with a container of sushi."
    show sayori 1a at t11
    "We take our food to the registers. I take my wallet out to bay for both of us, but then I notice Sayori has her purse out."
    mc "Don't trouble yourself, Sayori..."
    show sayori 1b
    mc "I can take care of it."
    s 1c "No, I can do it!~"
    "She gives me a nervous laugh. Something's brewing in her mind..."
    show sayori 1g
    mc "Don't worry about it, it's just a favor."
    mc "Save your money for something else, okay?"
    s 1c "B-but..."
    show sayori 1g
    "Sayori looks at me with upturned eyes."
    show sayori 1f
    "She's really insistent upon this, isn't she?"
    "Could she be trying to be more independent?"
    "But, she needs to spend her money on herself and not me."
    "This is making me feel on the spot..."
    menu:
        "What should I do?"
        "Let Sayori pay for lunch.":
            $ sayori_happiness = sayori_happiness + 1
            show expression Text("[sayori_happiness]"):
                ypos 0.5
            call mod_day1_s_pay
        "Pick up the tab for her.":
            $ sayori_happiness = sayori_happiness - 3
            show expression Text("[sayori_happiness]"):
                ypos 0.5
            call mod_day1_mc_pay
    return

label mod_day1_s_pay:
    $ cb_save_reset()
    "I can't resist the look Sayori is giving me."
    show sayori 1g
    "I sigh."
    mc "Alright, fine. You win. You can take care of it this time around."
    show sayori 1x
    "Sayori perks up upon hearing this."
    s 1e "You're too nice, [player]~"
    show sayori 1d
    "She gives me a small, but seemingly genuine smile, and lightly hugs me."
    "I watch as she steps up to the register and pays for our food."
    "I look around the courtyard, and spot a table near the booths."
    "I motion for Sayori to follow me, and we sit."
    call mod_day1_an_converge
   
label mod_day1_mc_pay:
    $ cb_save_reset()
    "It's alright, it's just a favor after all. Right?"
    mc "Don't worry about it, Sayori. I'll take care of it."
    show sayori 1k
    "Traces of disappointment appear on her face."
    s "Aw..."
    "I give her a quick shoulder pat I have to show her that I care about her."
    show sayori 1g
    mc "It's alright. You should worry more about yourself than doing me a favor."
    show sayori 1d
    "She looks up and gives me a weak smile."
    "I hand the cashier some yen, and pay for the meal."
    "My worries about Sayori start acting up."
    show sayori 1f
    "She probably wanted to do this by herself..."
    "I see her upset expression out of the corner of my eye."
    show sayori 1g
    mc "Alright... I'll let you pay for the tip. It's the least I can let you do."
    show sayori 1a
    "It's also the least I can do to make it up to her."
    "Regardless, Sayori's expression lights up at this offer."
    "She hands me a bill and a few coins, and I drop them into the tip jar."
    "I motion for Sayori to follow me, and we sit."
    call mod_day1_an_converge

label mod_day1_an_converge:
    show black with wipeleft
    hide black with wipeleft
    show sayori 1a at t11
    "As we're eating, I see Sayori take notice of the wasabi on her plate."
    s 1c "Hey, [player]..."
    show sayori 1b
    mc "Hmm?"
    s 1c "What's this green stuff? I've never really tried it..."
    show sayori 1b
    mc "Oh, that? That's wasabi."
    mc "It adds some flavor to the sushi, and I think it also helps prevent food poisoning..."
    show sayori 1n
    mc "You can put it directly on the sushi, or mix it into the soy sauce and dip the sushi in that..."
    "Somewhere along the line, Sayori stopped listening to me."
    show sayori 1r
    "I see her scoop up the entire lump of wasabi with one of her chopsticks and put it into her mouth."
    show sayori 1q
    s "{i}Mmmf...!{/i}"
    play music t7 fadein 5.0
    window hide
    $ renpy.pause(2)
    show sayori 1t
    show sayori 1v with alphadissolve2
    window show
    "Almost immediately, her face turns red."
    s 1w "{i}Hahh...hahh...{/i}"
    s 1p "{i}{b}Spicyyyyy!!!{/b}{/i}" with hpunch
    "Sayori frantically reaches for her water bottle, almost fumbling and spilling it."
    "As she guzzles the water, her face suddenly glows, turning even redder."
    s "{i}Mmmpmfh!{/i}"
    show sayori 1m
    "Sayori spits out the water and frantically gasps for air."
    "I can't help but chuckle a little at the scene."
    mc "If you had let me finish, I would've told you it was spicy..."
    s 5a "S-sorry..."
    s 5b "Guess my curiosity got the best of me, hehe~"
    "I smile; we always had little moments like this when we were younger."
    "There's some good emotion in this nostalgia, but I can't seem to identify it."
    "Something about it makes it sink into my gut, like I can't truly experience it..."
    "Could my own feelings and worry for Sayori be mixing together?"
    "Where are these doubts and emotions coming from?"
    "{i}No...{/i}I can't fall victim to my own negativity and worries. I have to keep myself together."
    "I playfully pinch Sayori's cheek."
    show sayori 5c
    mc "It's moments like this with you... that make me truly feel happy Sayori."
    show sayori 5b
    "Sayori blushes."
    s "Ehehe...~"
    show sayori 1d
    stop music fadeout 2.0
    "After that incident, we quickly finish our lunch, and begin exploring the festival a bit more."
    "Sayori seems really excited, so I have to do my best for her."
    window hide
    scene black with wipeleft_scene
    call mod_day1_evening