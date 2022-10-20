import easygui

lang=easygui.enterbox("Write a sentence")
lang.split()
easygui.msgbox("You wrote"+" \" " + lang+" \"")

selection=lang
reply=easygui.choicebox("Choose your word to study", choices=selection.split())
easygui.msgbox("Today's word:\n%s"%(reply))
