

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
    s "Everything looks sooo good!"
    "I nod in agreement."
    mc "How about we split up, and then we can meet up at the registers when we have what we want?"
    s 1r "Sounds good!"
    show sayori at thide
    hide sayori
    "With that, Sayori runs off in a random direction, and I start browsing the stands closest to me."
    show black with wipeleft
    hide black with wipeleft
    "5 minutes later, we meet up at the registers, ready to pay for our food."
    "I got myself a bowl of ramen, while Sayori has a plate of sushi."
    show sayori 1a at t11
    "We take our food to the registers and get ready to pay for it, but then I notice Sayori has her purse out."
    mc "Ah..."
    show sayori 1b
    mc "Don't trouble yourself, Sayori..."
    mc "I can take care of it."
    s 1c "I'm not helpless, you know!"
    s 1h "I'll do it!"
    show sayori 1g
    mc "Sayori, you need to think about yourself sometimes."
    mc "Save your money for something else, okay?"
    s 1c "B-but..."
    show sayori 1g
    "Sayori looks at me with upturned eyes."
    show sayori 1f
    "She's really insistent upon this, isn't she?"
    "I know she wants to prove herself, what with me handling a lot of burdens in our relationship."
    "But at the same time, she needs to spend her money on herself and not me."
    "Suddenly, I find myself in a bit of a dilemma..."
    menu:
        "What should I do?"
        "Let Sayori pay for lunch.":
            $ sayori_happiness = sayori_happiness + 1
            $ cb_save_reset()
            call mod_day1_s_pay
        "Pick up the tab for her.":
            $ sayori_happiness = sayori_happiness - 3
            $ cb_save_reset()
            call mod_day1_mc_pay
    return

label mod_day1_s_pay:
    "I find myself unable to resist the look Sayori's giving me."
    show sayori 1g
    "I sigh."
    mc "Alright, fine. You win. You can take care of it this time around."
    show sayori 1x
    "Sayori perks up upon hearing this."
    s 1s "Yaaay!"
    s 1e "You're too nice, [player]~"
    "Seeing her smile makes me smile too."
    show sayori 1d
    "She gives me a little hug, then steps up to the register and pays for our food."
    "After that, I find us a table and we sit down."
    call mod_day1_an_converge
   
label mod_day1_mc_pay:
    mc "Don't worry about that, Sayori. I'll take care of it."
    show sayori 1k
    "Sayori dejectedly looks downward."
    s "Aw... but I wanted to..."
    "I pat her on the shoulder."
    show sayori 1g
    mc "It's alright. Like I said, save your money for something else, okay?"
    show sayori 1d
    "She looks up and gives me a weak smile."
    "I fish my wallet out of my pocket and pay for our food."
    "As I do, I start to feel bad."
    show sayori 1f
    "Maybe she wanted to prove herself more than I thought, and I just crushed that for her."
    "I can still see her looking upset out of the corner of my eye."
    show sayori 1g
    mc "...here, I'll let you cover the tip, alright?"
    show sayori 1a
    "Sayori's expression lights up at this offer."
    "She hands me a bill and a few coins, and I drop them into the tip jar."
    "I then find us a table and we sit down."
    call mod_day1_an_converge

label mod_day1_an_converge:
    show black with wipeleft
    hide black with wipeleft
    show sayori 1a at t11
    "As we're eating, Sayori takes notice of the wasabi on her plate."
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
    $ renpy.pause(2)
    show sayori 1t
    show sayori 1v with alphadissolve2
    "Almost immediately, her face turns red."
    s 1w "{i}Hahh...hahh...{/i}"
    s 1p "{i}{b}Spicyyyyy!!!{/b}{/i}" with hpunch
    "Sayori reaches for her water bottle, almost fumbling and spilling it."
    "As she guzzles the water, I can't help but chuckle a little at the scene."
    mc "If you had let me finish, I would've told you it was spicy..."
    s 5a "S-sorry..."
    s 5b "Guess my curiosity got the best of me, hehe~"
    "I smile thinking about how we always had little moments like this when we were younger."
    "However, now the enjoyment is somewhat dulled knowing the pain Sayori's feeling."
    "Still, best to make the most of it I guess."
    "I playfully pinch Sayori's cheek."
    show sayori 5c
    mc "You're cute sometimes. You know that, Sayori?~"
    show sayori 5b
    s "Ehehe...~"
    show sayori 1d
    stop music fadeout 2.0
    "With that ordeal over, we finish our lunches, and then get ready to see what else there is to do at the festival."
    "Sayori seems excited, so I want to do everything I can to give her a good time."