***[Sublime Text 3+](http://www.sublimetext.com/) Package. Install via an updated version of  [Package Control 2+](https://sublime.wbond.net/installation). Just **DON'T** install manually.

Description
------------------

Provides handy clipboard commands without keybindings.

To assign a new keybinding,

* look for the command name into "Commands.sublime-commands"
* Open ".../Packages/User/Default.sublime-keymap"
* Append there, for example for "paste as plain text":

```
, { "keys": ["ctrl+alt+v"], "command": "clipboard_commands_paste_plain_text" }
```

Source-code
------------------

https://github.com/SublimeText/ClipboardCommands