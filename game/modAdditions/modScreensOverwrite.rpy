screen main_menu(m = mmm):
    style_prefix "mm"
    tag menu
    viewport:
        xinitial .5
        draggable True
        edgescroll 800,500
        fixed:
            fit_first True
            add bgs[0]
            vbox:
                yalign 1.0 yoffset -40 spacing 0
                button:
                    xoffset 40
                    at btn
                    add "0GUI/start.png"
                    action Start()
                button:
                    xoffset -96
                    at btn
                    add "0GUI/load.png"
                    action ShowMenu("load")
                button:
                    xoffset 0
                    at btn
                    add "0GUI/settings.png"
                    action ShowMenu("preferences")
                button:
                    xoffset 40
                    at btn
                    add "0GUI/quit.png"
                    action Quit(confirm=not main_menu)
            fixed:
                align 0.26,0.9
                fit_first True
                add "0GUI/mm/ZL.png"

                button:
                    tooltip zoe_log
                    padding 0,0 focus_mask True
                    at mm_girls
                    add "0GUI/mm/Z.png"
                    action NullAction()
                button:
                    tooltip leanne_log
                    padding 0,0 focus_mask True
                    at mm_girls
                    add "0GUI/mm/L.png"
                    action NullAction()
            button:
                tooltip irene_log
                align 0.66,0.96
                padding 0,0 focus_mask True
                at mm_girls
                add "0GUI/mm/I.png"
                action NullAction()
            fixed:
                align 0.8,0.96
                fit_first True
                add "0GUI/mm/NC.png"

                button:
                    tooltip coral_log
                    padding 0,0 focus_mask True
                    at mm_girls
                    add "0GUI/mm/C.png"
                    action NullAction()
                button:
                    tooltip norah_log
                    padding 0,0 focus_mask True
                    at mm_girls
                    add "0GUI/mm/N.png"
                    action NullAction()
            text "Find the girls on the beach by moving your mouse!" align .5,0.1

            imagebutton:
                action [ui.callsinnewcontext("galleryNameChange"), Show("sceneCharacterMenu")]
                idle Transform("modAdditions/images/cloud.png", zoom=0.4)
                hover Transform(im.MatrixColor("modAdditions/images/cloud.png", im.matrix.brightness(0.2)), zoom=0.4)
                align (0.65, 0.025)
                background None
                hover_background None