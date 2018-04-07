label mod_day2_main:
    show black
    show mod_logo with Dissolve(2.0)
    show thanks_text with Dissolve(2.0)
    $ renpy.pause(2.0)
    "Team Cloudbreaker thanks you for testing this early version of {i}Doki Doki CloudBreaker!{/i}."
    "Please report any criticism, issues, or general comments back to us."
    "Additionally, please don't release information about the game to anyone outside the development or playtest teams."
    "We want to keep everything a surprise for the final release. :)"
    "Until next time, remember to {cps=20}{i}{b}Watch the Skies{/b}{/i}{/cps}, and good night."
    $ renpy.full_restart(transition=Dissolve(2.0), label="splashscreen")
    
