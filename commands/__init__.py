import sys
import os

__all__ = ["commands_list",]

_commands = sorted([
        "exit",
        "help",
        "load",
        ])

commands_list = {}

for command in _commands:
#    print "[*] debug: cwd: %s" % os.getcwd()
    module = __import__(("commands." + command), fromlist=[command.title()])
    klass = getattr(module, command.title())

    commands_list[command] = klass

commands_list['quit'] = commands_list['exit']
commands_list['?'] = commands_list['help']
