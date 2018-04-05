init python:
    menu_trans_time = 1
    splash_message_default = "This game is a fan mod, not associated with Team Salvato."
    splash_messages = [
    "You are my sunshine,\nMy only sunshine",
    "I missed you.",
    "Play with me",
    "It's just a game, mostly.",
    "This game is not suitable for children\nor those who are easily disturbed?",
    "sdfasdklfgsdfgsgoinrfoenlvbd",
    "null",
    "I have granted kids to hell",
    "PM died for this.",
    "It was only partially your fault.",
    "This game is not suitable for children\nor those who are easily dismembered.",
    "Don't forget to backup Monika's character file."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    alpha 0.5
    "mod_assets/raineffect.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "mod_assets/loadraineffect.png"
    menu_bg_move

image menu_fade:
    "white"
    menu_fadeout

image menu_lightning:
    subpixel True
    alpha 0.0
    xcenter 640
    ycenter 360
    block:
        choice:
            "mod_assets/lightning.png"
        choice:
            "mod_assets/lightning2.png"
        function playthunder
        parallel:
            choice:
               xpos 0.4
            choice:
               xpos 0.5
            choice:
               xpos 0.6
            choice:
               xpos 0.7
            choice:
               xpos 0.8
            choice:
               xpos 0.9
        parallel:
            choice:
               ypos 0.6
            choice:
               ypos 0.7
            choice:
               ypos 0.8
            choice:
               ypos 0.9
        choice:
            pause 3.0
        choice:
            pause 4.5
        choice:
            pause 6.2
        choice:
            pause 9.1
        choice:
            pause 11.2
        alpha 0.3
        pause 0.05
        alpha 0.0
        pause 0.05
        alpha 1.0
        pause 0.03
        alpha 0.8
        pause 0.02
        alpha 0.6
        pause 0.02
        alpha 0.4
        pause 0.02
        alpha 0.4
        pause 0.02
        alpha 0.2
        pause 0.02
        alpha 0.0
        repeat

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "sayori 1t"
    xpos 0.2
    ycenter 350
    zoom 0.8
    rotate 0.2   
    block:
        choice:
           "sayori 1v" with alphadissolve
        choice:
           "sayori 1tq" with alphadissolve
        choice:
           "sayori 1t" with alphadissolve
        choice:
           "sayori 4w" with alphadissolve
        choice:
           pass
        ease 3.0 xpos 0.198 rotate -0.2
        ease 3.0 xpos 0.202 rotate 0.2
        repeat    

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "mod_assets/main_menu.png"
    menu_nav_move

image menu_logo:
    "mod_assets/modlogo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

style bottomR:
    xpos 0.7
    ypos 0.9

image debug_version:
    Text("version 20180404_playtest", style="bottomR")

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    ypos -500
    parallel:
        xoffset 0 yoffset 0
        linear 0.5 xoffset 100 yoffset 400
        repeat
    #parallel:
    #    ypos 0
    #    time 0.65
    #    ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True

    topleft
    ypos -500
    parallel:
        xoffset 0 yoffset 0
        linear 1.5 xoffset 100 yoffset 400
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image intro2:
    truecenter
    "white"
    0.5
    "mod_assets/cblogo.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "mod_assets/warning_bedroom.png"
image tos2 = "bg/warning2.png"


label splashscreen:

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run:
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    pass

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")

    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "This game is a fan mod of {i}Doki Doki Literature Club{/i} by Team Salvato."
        "The original game is available at http://ddlc.moe. Do not play {i}Doki Doki CloudBreaker!{/i} unless you have played DDLC previously."
        "Additionally, certain eventualities in {i}Doki Doki CloudBreaker!{/i} may result in emotional distress. Those with depression, anxiety, or other conditions may not be able to play safely."
        "Do not play this mod if you are not certain if it may be safe for you."
        menu:
            "By playing {i}Doki Doki CloudBreaker!{/i}, I understand that this is a fan mod not associated with Team Salvato, and I accept any potential risks upon myself at no fault of Team CloudBreaker."
            "I agree.":
                pass
        $ persistent.first_run = True
        scene sayori_bedroom
        with Dissolve(1.5)
        pause 1.0
        scene white


    python:
        s_kill_early = None
        if persistent.playthrough == 0:
            try: renpy.file("../characters/sayori.chr")
            except: s_kill_early = True
        if not s_kill_early:
            if persistent.playthrough <= 2 and persistent.playthrough != 0:
                try: renpy.file("../characters/monika.chr")
                except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            if persistent.playthrough <= 1 or persistent.playthrough == 4:
                try: renpy.file("../characters/natsuki.chr")
                except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                try: renpy.file("../characters/yuri.chr")
                except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            if persistent.playthrough == 4:
                try: renpy.file("../characters/sayori.chr")
                except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]
            a = range(1,12)
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload



    $ config.allow_skipping = False

    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        pause 1.0
        show end with dissolve_cg
        pause 3.0
        $ config.allow_skipping = True
        return


    if s_kill_early:
        show black
        play music "bgm/s_kill_early.ogg"
        pause 1.0
        show end with dissolve_cg
        pause 3.0
        scene white
        show expression "images/cg/s_kill_early.png":
            yalign -0.05
            xalign 0.25
            dizzy(1.0, 4.0, subpixel=False)
        show white as w2:
            choice:
                ease 0.25 alpha 0.1
            choice:
                ease 0.25 alpha 0.125
            choice:
                ease 0.25 alpha 0.15
            choice:
                ease 0.25 alpha 0.175
            choice:
                ease 0.25 alpha 0.2
            choice:
                ease 0.25 alpha 0.225
            choice:
                ease 0.25 alpha 0.25
            choice:
                ease 0.25 alpha 0.275
            choice:
                ease 0.25 alpha 0.3
            pass
            choice:
                pass
            choice:
                0.25
            choice:
                0.5
            choice:
                0.75
            repeat
        show noise:
            alpha 0.1
        with Dissolve(1.0)
        show expression Text("Now everyone can be happy.", style="sayori_text"):
            xalign 0.8
            yalign 0.5
            alpha 0.0
            600
            linear 60 alpha 0.5
        pause
        $ renpy.quit()


    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.confesslofi
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.25
    hide intro with Dissolve(0.5, alpha=True)
    show intro2 with Dissolve(0.5, alpha=True)
    pause 2.25
    hide intro2 with Dissolve(0.5, alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    if persistent.playthrough == 0:
        $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        if persistent.yuri_kill >= 1380:
            $ persistent.yuri_kill = 1440
        elif persistent.yuri_kill >= 1180:
            $ persistent.yuri_kill = 1380
        elif persistent.yuri_kill >= 1120:
            $ persistent.yuri_kill = 1180
        elif persistent.yuri_kill >= 920:
            $ persistent.yuri_kill = 1120
        elif persistent.yuri_kill >= 720:
            $ persistent.yuri_kill = 920
        elif persistent.yuri_kill >= 660:
            $ persistent.yuri_kill = 720
        elif persistent.yuri_kill >= 460:
            $ persistent.yuri_kill = 660
        elif persistent.yuri_kill >= 260:
            $ persistent.yuri_kill = 460
        elif persistent.yuri_kill >= 200:
            $ persistent.yuri_kill = 260
        else:
            $ persistent.yuri_kill = 200
        jump expression persistent.autoload

    
    elif False: # anticheat != persistent.anticheat:
            stop music
            scene black
            "The save file could not be loaded."
            "Are you trying to cheat?"
            $ s_name = "Sayori"
            show sayori 1bb at t11
            s "Hey, [player]."
            s 1bd "I appreciate you trying to save me from whatever might have happened."
            s 1bc "But you knew that wasn't going to work, right?"
            call updateconsole ("cloudbreaker.gamemode()", "Game mode 'oneshot' is active. Saves \nare deleted and rendered invalid \nafter each major choice.")
            s 1bu "Am I really worth fighting {i}that much{/i} for?"
            hide sayori with wipeleft
            "Please load a different (valid) save file in order to continue playing 'Doki Doki CloudBreaker!'"
            $ renpy.full_restart(transition=None, label="splashscreen")
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return

label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        $ persistent.yuri_kill += 200


    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

label autoload_yurikill:
    if persistent.yuri_kill >= 1380:
        $ persistent.yuri_kill = 1440
    elif persistent.yuri_kill >= 1180:
        $ persistent.yuri_kill = 1380
    elif persistent.yuri_kill >= 1120:
        $ persistent.yuri_kill = 1180
    elif persistent.yuri_kill >= 920:
        $ persistent.yuri_kill = 1120
    elif persistent.yuri_kill >= 720:
        $ persistent.yuri_kill = 920
    elif persistent.yuri_kill >= 660:
        $ persistent.yuri_kill = 720
    elif persistent.yuri_kill >= 460:
        $ persistent.yuri_kill = 660
    elif persistent.yuri_kill >= 260:
        $ persistent.yuri_kill = 460
    elif persistent.yuri_kill >= 200:
        $ persistent.yuri_kill = 260
    else:
        $ persistent.yuri_kill = 200
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = "/mod_assets/St4-confession.mp3"
    return

label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return

label readonly:
    scene black
    "The game cannot be run because you are trying to run it from a read-only location."
    "Please copy the DDLC application to your desktop or other accessible location and try again."
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
