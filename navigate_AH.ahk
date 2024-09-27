#Requires AutoHotkey v2.0

Log_Item(name, filename) {
	; Click "Market Price"
	MouseMove(313, 101)
	Click()
	Sleep(1000)

	; Enter an item into the AH search bar
	CoordMode("Mouse", "Screen")
	x:= 219
	y:= 54
	MouseMove(x, y)
	Sleep(100)
	Click()
	Sleep(1000)
	Send("{Backspace 20}")
	Sleep(1000)
	Send("{Backspace 20}")
	Sleep(1000)
	Send(name)
	Sleep(1000)
	Send("{Enter}")
	Sleep(3000)
	Send("{Enter}")

	; Start recording the screen while clicking "Next" 13 times
	Send("{LWin down}{Shift down}r{Shift up}{LWin up}")
	Sleep(5000)
	MouseMove(271, 174)
	Click("down")
	Sleep(1000)
	MouseMove(1000, 675)
	Click("up")
	Sleep(1000)
	MouseMove(590, 33)
	Click()
	Sleep(6000)
	MouseMove(675, 136)

	Loop 13 {
		Click()
		Sleep(750)
	}
	Send("{Alt down}{Tab}{Alt up}")
	Sleep(500)
	MouseMove(615, 30)
	Click()

	; Save the video to the right destination
	Sleep(6000)
	Send("^s")
	Sleep(6000)
	Send(filename)
	Send("{Tab}")
	Sleep(500)
	Send("{Tab}")
	Sleep(500)
	Send("{Enter}")
	Sleep(500)
	Send("{Left}")
	Sleep(500)
	Send("{Enter}")
	Sleep(5000)

	; Close Snipping Tool
	Send("{Alt Down}{F4}{Alt Up}")
	Sleep(5000)
}

Home:: {
	Log_Item("Spell Trace", "vid1")
	Log_Item("Sol Erda Fragment", "vid2")
}

Log_Item("Spell Trace", "vid1")
Log_Item("Sol Erda Fragment", "vid2")
