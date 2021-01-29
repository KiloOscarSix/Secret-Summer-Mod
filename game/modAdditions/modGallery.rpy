init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, pageNum, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = pageNum
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = os.path.join("/images/", "{}".format(thumbnail))
            galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

default galleryPageNumber = 1
default scopeDict = {}

define galleryMenu = [
    ["All", "/images/a120.webp"],
]

define Unknown = GalleryItem("All", 1, "galleryScene1", "a120.webp")
define Unknown = GalleryItem("All", 1, "galleryScene2", "a191.webp")
define Unknown = GalleryItem("All", 1, "galleryScene3", "b35.webp")
define Unknown = GalleryItem("All", 1, "galleryScene4", "b149.webp")
define Unknown = GalleryItem("All", 1, "CH4RID", "d26.webp")
define Unknown = GalleryItem("All", 1, "CH4HIKE", "d141.webp")
define Unknown = GalleryItem("All", 1, "galleryScene5", "e26.webp")
define Irene = GalleryItem("All", 1, "galleryScene6", "f167.webp")

label galleryNameChange:
    default persistent.p_name = ""
    if persistent.p_name == "":
        scene bg
        show mc
        with dissolve
        $ persistent.p_name = renpy.input("What is the name of the MC?")

    $ scopeDict = {"p_name":persistent.p_name}
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        style "modFixed"
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        style "modFixed"
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))
            style "modImageButton"

    fixed:
        style "modFixed"
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            style "modGrid"
            cols 4
            spacing 50
            align (0.5, 0.5)

            for i in galleryMenu:
                vbox:
                    imagebutton:
                        action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                        idle Transform(i[1], zoom=0.2)
                        hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                        style "modImageButton"
                    text i[0]:
                        style "modTextBody"
                        xcenter 0.5


screen sceneCharacterMenu(galleryCharacter="All"):

    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        style "modFixed"
        xysize (1536, 98)
        pos (85, 14)

        text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        style "modFixed"
        spacing 20
        pos (1666, 39)

        imagebutton:
            if galleryPageNumber == 1:
                # action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
                action [Hide("sceneGalleryMenu"), ShowMenu("main_menu")]
            else:
                action Function(galleryDecreasePageNumber)
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))
            style "modImageButton"

        if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
            imagebutton:
                action Function(galleryIncreasePageNumber)
                idle "/modAdditions/images/nextButton.png"
                hover im.MatrixColor("/modAdditions/images/nextButton.png", im.matrix.brightness(0.2))
                style "modImageButton"

    fixed:
        xysize (1875, 789)
        pos(19, 115)
        style "modFixed"

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)
            style "modGrid"

            for galleryItem in galleryItems:
                if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                    imagebutton:
                        action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                        idle Transform(galleryItem.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(galleryItem.thumbnail, 15), zoom=0.2)
                        style "modImageButton"