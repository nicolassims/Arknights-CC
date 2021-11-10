################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

#player-made screens
screen buttons():
        if (map[y - 1][x] < 1 and y != 0):
            textbutton "↑" action Return(value='F') xalign .9 yalign .7 text_size 200
            key "K_UP" action Return(value='F')
        if (map[y][x + 1] < 1 and x != len(map[0]) - 1):
            textbutton "→" action Return(value='R') xalign .97 yalign .83 text_size 200
            key "K_RIGHT" action Return(value='R')
        if (map[y + 1][x] < 1 and y != len(map) - 1):
            textbutton "↓" action Return(value='B') xalign .9 yalign .96 text_size 200
            key "K_DOWN" action Return(value='B')
        if (map[y][x - 1] < 1 and x != 0):
            textbutton "←" action Return(value='L') xalign .83 yalign .83 text_size 200
            key "K_LEFT" action Return(value='L')

screen mini_map_scr(map):
    frame:
        align (0.5, 0.5)
        grid len(map) len(map[0]):
            for i in range(len(map)):
                for j in range(len(map[0])):
                    if i == y and j == x:
                        $ tile = Solid("#FF0000", xmaximum=64, ymaximum=64)
                    elif map[i][j] < 1 and knowledgemap[i][j] == 1:
                        $ tile = Solid("#ffffff", xmaximum=64, ymaximum=64)
                    elif map[i][j] == 1 and knowledgemap[i][j] == 1:
                        $ tile = Solid("#008000", xmaximum=64, ymaximum=64)
                    else:
                        $ tile = Solid("#000000", xmaximum=64, ymaximum=64)

                    add tile

screen frontman():
    text "Choose a\nFrontman" xpos 0.7 xanchor 0.5 yalign 0.5 size 90 bold True outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]

screen go(op):
    textbutton "GO!" action [Hide("go"), Hide("setupstatus"), Return(op)] xpos 0.79 xanchor 0.5 yalign 0.94 text_size 90 text_bold True text_outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

screen setup(back):
    $ squaresize = 200
    $ spacesize = 20

    for i in range(12):
        transform:
            image "ui/shadow.png"
            anchor (0.5, 0.5)
            pos (20 + (i % 4) * (squaresize + spacesize) + squaresize / 2, 0.29 * (math.floor(i / 4.0) + 1) + 0.08)

    for i, op in enumerate(ops):
        $ portrait = Image(op.getparameter(PORTRAITS)[0])

        imagebutton:
            pos (20 + (i % 4) * (squaresize + spacesize) + squaresize / 2, 0.29 * (math.floor(i / 4.0) + 1) + 0.09)
            anchor (0.5, 1.0)
            idle Transform(portrait, fit="contain", xysize=(squaresize, 400), ypos=0)
            hover Transform(portrait, fit="contain", xysize=(squaresize + 50, 450), ypos=50)
            action [Hide("frontman"), Show("setupstatus", op=op, back=back), Show("go", op=op)]

screen setupstatus(op, back):
    image "ui/setupmenu.png"

    image "ui/classicons/" + op.getparameter(CLASS).lower() + ".png" xysize (140, 140) pos (0.915, 0.02)
    text op.getparameter(CODENAME) size 90 xpos 0.56 color "#FFF" bold True outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]
    text op.getparameter(SUBCLASS) + " " + op.getparameter(CLASS) size 50 pos (0.58, 0.1) color "#414342" bold True

    if (back):
        textbutton "Back" action [Hide("setupstatus"), Hide("go"), Jump("badmove")] xalign .65 yalign .85 xminimum 350 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" background Frame("gui/button/choice_idle_background.png")

    hbox:
        pos (0.6, 0.2)
        spacing 40
        vbox:
            spacing 20
            text "Level:" bold True size 40
            text "Health:" bold True size 40
            text "Attack:" bold True size 40
            text "Arts:" bold True size 40

        vbox:
            spacing 20
            text str(op.getparameter(LEVEL)) size 40
            text str(op.getparameter(HEALTH)) size 40
            text str(op.getparameter(ATK)) size 40
            text str(op.getparameter(ARTS)) size 40

        vbox:
            xpos 100
            spacing 20
            text "Cost:" bold True size 40
            text "Move:" bold True size 40
            text "Defense:" bold True size 40
            text "Arts Def:" bold True size 40

        vbox:
            xpos 90
            spacing 20
            text str(op.getparameter(COST)) size 40
            text str(op.getparameter(MOV)) size 40
            text str(op.getparameter(DEF)) size 40
            text str(op.getparameter(ARTSDEF)) size 40

    text "Fighting Style: " + op.getparameter(ELEMENT)[0] + "/" + op.getparameter(ELEMENT)[1] size 30 xanchor 0.5 pos (0.785, 0.51) color "#FFF" bold True

    textbutton op.getparameter(TALENT) action Show("talentblurb", id=int(op.getparameter(ID))) background Frame("gui/button/choice_idle_background.png") xanchor 0.5 xminimum 350 text_xalign .5 align (.785, .475)

    hbox:
        align(0.785, 0.69)
        xanchor 0.5
        spacing 60
        for x in op.getparameter(TECHS):
            imagebutton:
                idle Transform(x.getparameter(ICON), size=(200, 200), matrixcolor=InvertMatrix(0.0))
                hover Transform(x.getparameter(ICON), size=(200, 200), matrixcolor=InvertMatrix(1.0))
                action [Show("techblurb", op=op, id=int(x.getparameter(ID)), fullscreen=True)]

screen talentblurb(id):
    python:
        id -= 1
        talenttext = "{b}" + opdex[id][CODENAME] + "'s Talent: " + opdex[id][TALENT] + "{/b}\n"

        talentext += gettalentblurb(id + 1)

    imagebutton:
        xfill True
        yfill True
        idle "ui/empty.png"
        action [Hide("talentblurb")]

    frame:
        align (0.5, 0.5)
        margin (200, 100)
        padding (100, 50)
        text talenttext xalign 0.5

screen techblurb(op, id, fullscreen):
    python:
        id -= 1
        techtext = "{b}" + op.getparameter(CODENAME) + "'s Tech: " + techdex[id][NAME] + "{/b}\n"
        techtext += "Gain SP by " + techdex[id][GAINTYPE].lower() + ".\n"

        currentsp = 0
        for tech in op.getparameter(TECHS):
            if (tech.getparameter(ID) - 1 == id):
                currentsp = tech.getparameter(POINTS)

        techtext += "Current SP: " + str(currentsp) + "/" + str(tech.getparameter(COST)) + "."

        charges = tech.getparameter(CHARGES)
        if (charges > 1):
            techtext += " Holds " + str(charges) + "."

        techtext += "\n"

        techtext += gettechblurb(id)

    if (fullscreen):
        imagebutton:
            xfill True
            yfill True
            idle "ui/empty.png"
            action [Hide("techblurb")]

    frame:
        align (0.5, 0.5)
        margin (200, 100)
        padding (100, 50)
        text techtext xalign 0.5

screen battle():
    python:
        screenwidth = 1920
        spacesize = 20
        totalspace = spacesize * 10
        squaresize = (screenwidth - totalspace) / 9

    text str(mydp) + " DP" xpos 0.1 size 90 bold True outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]
    text str(otherdp) + " DP" xpos 0.9 xanchor 1.0 size 90 bold True outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]

    for i, op in enumerate(battlefield):
        $ color = "#FFF"
        if (ownedfield[i] == True):
            $ color = gui.hover_color
        elif (ownedfield[i] == False):
            $ color = "#E0A366"

        add Solid(color, xpos = 20 + i * (squaresize + spacesize), ypos = 800, xysize = (squaresize, squaresize))

        text str(battlefieldPoints(i)) size 180 color (0, 0, 0, 60) xpos 60 + i * (squaresize + spacesize) ypos 800 xysize (squaresize, squaresize)

        if (op != None):
            bar:
                xpos 20 + i * (squaresize + spacesize) + squaresize / 2
                ypos 800 + squaresize / 2
                xanchor 0.5
                xsize squaresize - 20
                range int(opdex[op.getparameter(ID) - 1][HEALTH] * (10 + op.getparameter(LEVEL)) * 5)
                value op.getparameter(HEALTH)
                right_bar gui.muted_color
                left_bar "#F69122"

            if (op.getparameter(ALLY)):
                text str(op.getparameter(HEALTH)) + "HP" xanchor 0.5 xpos 20 + i * (squaresize + spacesize) + squaresize / 2 ypos 797 + squaresize / 2 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

            bar:
                xpos 20 + i * (squaresize + spacesize) + squaresize / 2
                ypos 850 + squaresize / 2
                xanchor 0.5
                xsize squaresize - 20
                range 10
                value op.getparameter(MOVEPOINTS) * 10
                right_bar gui.muted_color
                left_bar "#459426"

            if (op.getparameter(ALLY)):
                text str(op.getparameter(MOVEPOINTS)).rstrip(".0") + "MOV" xanchor 0.5 xpos 20 + i * (squaresize + spacesize) + squaresize / 2 ypos 847 + squaresize / 2 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

            add Transform(Image(op.getparameter(PORTRAITS)[0]),
                          fit="contain",
                          xysize=(squaresize, 1000),
                          anchor=(0.5, 1.0),
                          xpos = 20 + i * (squaresize + spacesize) + squaresize / 2,
                          ypos = 800 + squaresize / 2,
                          xzoom = 1 if op.getparameter(ALLY) else -1)

            text orderstring(actionlist.index(op)) xanchor 0.5 xpos 20 + i * (squaresize + spacesize) + squaresize / 2 ypos 800 + squaresize / 2 - 50 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

            if (op == actor):
                add Transform(Image("ui/cursor.png"), anchor=(1.0, 1.0), xpos = 20 + i * (squaresize + spacesize) + squaresize / 2, ypos = 700, xzoom = 0.25, yzoom = 0.25)

screen battleui():
    use battle()

    vbox:
        xalign .5 yalign .3
        hbox:
            textbutton "Attack" action Return(value='attack') xminimum 350 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" background Frame("gui/button/choice_idle_background.png")
            textbutton " Tech " action Return(value='tech') xminimum 350 text_xalign .5 text_size 60 text_color "#826926" text_hover_color "#c98022" background Frame("gui/button/choice_idle_background.png")
        hbox:
            textbutton " Move " action Return(value='move') xminimum 350 text_xalign .5 text_size 60 text_color "#437128" text_hover_color "#459426" background Frame("gui/button/choice_idle_background.png")
            textbutton " Item " action Return(value='item') xminimum 350 text_xalign .5 text_size 60 text_color "#295272" text_hover_color "#256799" background Frame("gui/button/choice_idle_background.png")
        hbox:
            textbutton "Deploy" action Return(value='deploy') xminimum 350 text_xalign .5 text_size 60 text_color "#772372" text_hover_color "#B739B0" background Frame("gui/button/choice_idle_background.png")
            textbutton " Pass " action Return(value='pass') xminimum 350 text_xalign .5 text_size 60 text_color gui.accent_color text_hover_color gui.hover_color background Frame("gui/button/choice_idle_background.png")

#location is an int from 0-8
#minrange is an int
#maxrange is an int >= minrange
#aoe is a boolean
#target is one of "op", "empty", or "both"
#deploying is an int, with 0 representing not deploying
screen targeting(location, minrange, maxrange, aoe, target, deploying):
    use battle()

    python:
        screenwidth = 1920
        spacesize = 20
        totalspace = spacesize * 10
        squaresize = (screenwidth - totalspace) / 9

    textbutton "Back" action Jump("badmove") xalign .5 yalign .4 xminimum 350 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" background Frame("gui/button/choice_idle_background.png")

    if (aoe):
        $ print("HANDLE THIS!")

    for i, op in enumerate(battlefield):
        if (((target == "op" and op != None)#if we're targeting an operator, and there's an operator on this battlefield slot...
            or (target == "empty" and op == None)#or we're targeting an empty square, and there's no operator on this battlefield slot...
            or target == "both")#or if we're targeting either
            and (deploying == 0 or deploying > 0 and ownedfield[i] == True and mydp >= deploying + i * 10)#or if not deploying, or if you are deploying, and own that tile, and have enough dp to spend...
            and location + minrange <= i <= location + maxrange):#and the possible target is within our targeting range...
            imagebutton:
                pos (20 + i * (squaresize + spacesize), 800)
                xysize (squaresize, squaresize)
                idle (Solid((155, 81, 81, 200)) if target != "empty" else Solid((67, 113, 40, 200)))#choose a red color if you can target an operator
                hover (Solid((208, 59, 61, 200)) if target != "empty" else Solid((69, 148, 38, 200)))#choose a green color if you can target the ground
                action Return(value=[i])

            if (deploying > 0):
                text str(deploying + i * 10) + "\nDP" size 80 color (255, 255, 255, 255) xpos 50 + i * (squaresize + spacesize) ypos 800 xysize (squaresize, squaresize)

#source is an operator object
#target is an operator object
#hits is an int
#atkbuff is a float, with 1 as default
#elements is an array of element strings, usually just one
#effect is either zero or a tech object
screen useattack(source, targets, hits, atkbuff, elements, effect):
    use battle()

    $ damagereport = ""

    for tech in source.getparameter(TECHS):
        if (tech.getparameter(GAINTYPE) == "Attacking"):
            $ tech.setparameter(POINTS, min(tech.getparameter(COST) * tech.getparameter(CHARGES), tech.getparameter(POINTS) + tech.getparameter(GAINPER)))

    $ incapacitated = []

    for target in targets:
        python:
            for tech in target.getparameter(TECHS):
                if (tech.getparameter(GAINTYPE) == "Defending"):
                    tech.setparameter(POINTS, min(tech.getparameter(COST) * tech.getparameter(CHARGES), tech.getparameter(POINTS) + tech.getparameter(GAINPER)))

            effectiveness = effectiveness(elements, target.getparameter(ELEMENT))
            power = (source.getparameter(ARTS) if source.getparameter(USESARTS) else source.getparameter(ATK)) * atkbuff * effectiveness
            defense = (target.getparameter(ARTSDEF) if source.getparameter(USESARTS) else target.getparameter(DEF))

            dmg = 0
            for hit in range(hits):
                dmg += max(1, 0.05 * power, power - defense)

                if (source.getparameter(ID) == KROOS and renpy.random.random() <= 0.2):#KROOS TALENT, Kroos' talent
                    if ("{b}Kroos gets serious!{/b} " not in damagereport):
                        damagereport += "{b}Kroos gets serious!{/b} "
                    else:
                        damagereport = damagereport.replace("{b}Kroos gets serious!{/b} ", "{b}Kroos gets {i}deadly{/i} serious!{/b} ")
                    dmg *= 1.6

            dmg = int(min(target.getparameter(HEALTH), dmg))
            target.setparameter(HEALTH, target.getparameter(HEALTH) - dmg)

            if (source.getparameter(ID) == ROCKSICK):#ROCKSICK TALENT, Rocksick's talent
                max = maxhp(source)
                healthgained = min(max - source.getparameter(HEALTH), max / 10)
                source.setparameter(HEALTH, source.getparameter(HEALTH) + healthgained)
                damagereport += "{b}Rocksick regenerates, gaining " + str(healthgained) + " health!{/b} "

            damagereport += ("Ally " if source.getparameter(ALLY) else "Foe ")
            damagereport += source.getparameter(CODENAME) + " dealt " + str(dmg) + " damage to the "
            damagereport += ("ally " if target.getparameter(ALLY) else "foe ")
            damagereport += target.getparameter(CODENAME)
            damagereport += hitsStrings(hits)
            damagereport += "! "
            damagereport += effectivestring(effectiveness, elements, target.getparameter(ELEMENT))

            if (effect != 0):
                effectnum = effect.getparameter(EFFECT)
                if (effectnum == 1):#draining health, used by rocklaw. Uses effectpower1 as percentage of damage done.
                    max = maxhp(source)
                    source.setparameter(HEALTH, min(max, source.getparameter(HEALTH) + dmg * effect.getparameter(EFFECTPOWER1)))
                    damagereport += source.getparameter(CODENAME) + " drains " + str(dmg) + " health! "

            if (target.getparameter(HEALTH) <= 0):
                damagereport += ("Ally " if target.getparameter(ALLY) else "Foe ") + target.getparameter(CODENAME) + " incapacitated!"
                incapacitated.append(target)

    imagebutton:
        xfill True
        yfill True
        idle "ui/empty.png"
        action [Return(value=incapacitated)]

    frame:
        align (0.5, 0.3)
        margin (200, 100)
        padding (100, 50)
        text damagereport xalign 0.5

#source is an operator object
#target is an operator object
screen usetech(op):
    use battle()

    hbox:
        spacing 50
        align (0.5, 0.1)
        for tech in op.getparameter(TECHS):
            $ ready = tech.getparameter(POINTS) >= tech.getparameter(COST)
            imagebutton:
                idle Transform(tech.getparameter(ICON), size=(200, 200), matrixcolor=(InvertMatrix(0) if ready else SaturationMatrix(0)))
                hover Transform(tech.getparameter(ICON), size=(200, 200), matrixcolor=InvertMatrix(1) if ready else SaturationMatrix(0))
                hovered Show("techblurb", op=op, id=int(tech.getparameter(ID)), fullscreen=False)
                unhovered Hide("techblurb")
                action ([Return(value=tech), Hide("techblurb")] if ready else NullAction())

    textbutton "Back" action Jump("badmove") xalign .5 yalign .4 xminimum 350 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" background Frame("gui/button/choice_idle_background.png")

screen useitem():
    use battle()

    if (len(inventory) == 0):
        frame:
            align (0.5, 0.4)
            margin (200, 100)
            padding (100, 50)
            text "You don't have any items!" xalign 0.5

        imagebutton:
            xfill True
            yfill True
            idle "ui/empty.png"
            action [Jump("badmove")]

screen deploy():
    use battle()

    $ opsinbank = 0

    for op in ops:
        if op not in battlefield:
            $ opsinbank += 1

    if (opsinbank == 0):
        frame:
            align (0.5, 0.4)
            margin (200, 100)
            padding (100, 50)
            text "You have no undeployed operators!" xalign 0.5

        imagebutton:
            xfill True
            yfill True
            idle "ui/empty.png"
            action [Jump("badmove")]
    else:
        image Transform("bgs/tactics.png", matrixcolor=SaturationMatrix(0), xsize=1920, ysize=1080)
        use setup(back=True)
