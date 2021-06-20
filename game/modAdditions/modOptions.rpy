define gr = "{color=#0f0}"
define red = "{color=#f00}"
define blue = "{color=#00f}"

default NorahPath = "{color=#0f0}[Norah Path]"
default ZoePath = "{color=#0f0}[Zoe Path]"
default CoralPath = "{color=#0f0}[Coral Path]"
default LeannePath = "{color=#0f0}[Leanne Path]"
default IrenePath = "{color=#0f0}[Irene Path]"

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        grid 3 2:
            spacing 20

            textbutton "Norah Path" action [ToggleVariable("NorahPath", true_value="{color=#0f0}[Norah Path]", false_value="")]
            textbutton "Zoe Path" action [ToggleVariable("ZoePath", true_value="{color=#0f0}[Zoe Path]", false_value="")]
            textbutton "Coral Path" action [ToggleVariable("CoralPath", true_value="{color=#0f0}[Coral Path]", false_value="")]
            textbutton "Leanne Path" action [ToggleVariable("LeannePath", true_value="{color=#0f0}[Leanne Path]", false_value="")]
            textbutton "Irene Path" action [ToggleVariable("IrenePath", true_value="{color=#0f0}[Irene Path]", false_value="")]

        textbutton "Change In-Game Names" action ui.callsinnewcontext("changeIngameNames") text_style "modTextButtonHeader"

        textbutton "Change Gallery Names" action ui.callsinnewcontext("changeGalleryNames") text_style "modTextButtonHeader"

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)

label changeGalleryNames:
    scene bg
    show mc
    with dissolve

    $ persistent.p_name = renpy.input("What is the name of the MC?").strip()
    return

label changeIngameNames:
    scene bg
    show mc
    with dissolve

    $ p_name = renpy.input("What is the name of the MC?").strip()

    hide mc
    show j
    with dissolve

    $ rel_f = renpy.input("The oldest man of the house is the MC's ??? (Default will be landlord. 1/7)", default="landlord").strip() or "landlord"

    hide j
    show c
    with dissolve

    $ rel_s = renpy.input("This is 18-year-old Coral. She is your ??? (Default will be roommate. 2/7)", default="roommate").strip() or "roommate"

    hide c
    show lz
    with dissolve

    $ rel_b = renpy.input("This is 23-year-old Leanna, the redhead and 22-year-old Zoe with the black hair. You are their ??? (Default will be roommate. 3/7)", default="roommate").strip() or "roommate"

    hide lz
    show i
    with dissolve

    $ rel_sm = renpy.input("This is 37 year-old Irene, the new wife of the landlord. And also your ??? (Default will be landlady. 4/7)", default="landlady").strip() or "landlady"

    hide i
    show n
    with dissolve

    $ rel_m = renpy.input("This is 41-year-old Norah, the ex-wife of the landlord. And also the MC's ??? (Default will be landlady. 5/7)", default="landlady").strip() or "landlady"

    $ m_nik = renpy.input("What does the MC call her? (Default will be her name.)", default="Norah").strip() or "Norah"

    hide n
    show fam
    with dissolve

    $ rel_fam = renpy.input("What are the people of this household called together? (Default will be unit. 7/7)", default="unit").strip() or "unit"

    return