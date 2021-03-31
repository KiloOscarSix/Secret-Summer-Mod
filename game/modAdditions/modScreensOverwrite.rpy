screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    #code
    if main_menu:

        imagebutton idle "gui/start_idle.png" hover "gui/start_hover.png" focus_mask True action Start()

        imagebutton idle "gui/load_idle.png" hover "gui/load_hover.png" focus_mask True action ShowMenu("load")

        imagebutton idle "gui/option_idle.png" hover "gui/option_hover.png" focus_mask True action ShowMenu("preferences")

        imagebutton idle "gui/patreon_idle.png" hover "gui/patreon_hover.png" focus_mask True action OpenURL ("https://www.patreon.com")

        imagebutton idle "gui/discord_idle.png" hover "gui/discord_hover.png" focus_mask True action OpenURL ("https://www.patreon.com")

        imagebutton idle "gui/logo_idle.png" hover "gui/logo_hover.png" focus_mask True action OpenURL ("https://www.patreon.com")

        textbutton "Scene Gallery" action [ui.callsinnewcontext("galleryNameChange"), Show("sceneGalleryMenu")] text_style "modTextButtonHeader"

        if renpy.variant("pc"):
            imagebutton idle "gui/quit_idle.png" hover "gui/quit_hover.png" focus_mask True action Quit(confirm=not main_menu)

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"
            
    # imagebutton:
    #     action [ui.callsinnewcontext("galleryNameChange"), Show("sceneCharacterMenu")]
    #     idle Transform("modAdditions/images/cloud.png", zoom=0.4)
    #     hover Transform(im.MatrixColor("modAdditions/images/cloud.png", im.matrix.brightness(0.2)), zoom=0.4)
    #     align (1.0, 0.025)
    #     background None
    #     hover_background None