#Requires AutoHotkey v2.0
#Persistent  ; Keeps the script running
#SingleInstance force  ; Prevents running multiple instances
Run "C:\Users\pilklover420\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Nexon\MapleStory.lnk"

F1::  ; Assigning the hotkey to F1. You can change it to whatever key you prefer
{
    Send, {Left}    ; Left arrow key
    Sleep, 100      ; Small delay (100 ms)
    Send, {Enter}   ; Enter key
    Sleep, 100
    Send, {Down 4}  ; Down arrow key pressed 4 times
    Sleep, 100
    Send, {Enter}   ; Enter key
    Sleep, 100
    Send, {Escape}  ; Escape key
    Sleep, 100
    Send, {Right}   ; Right arrow key
    Sleep, 100
    Send, {Down 4}  ; Down arrow key pressed 4 times
    Sleep, 100
    Send, {Enter}   ; Enter key
}

; TODO: Move mouse to search bar
; 	Type in items we want to search
;	Start recording screen
;	Click right 13 times
;	End recording and save as movie.mov
;	Quit game
;	Run python script
;	Write status somewhere?
