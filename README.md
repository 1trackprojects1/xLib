# Welcome to the xLib Framework
>AIO Framework for exploiting libssh. Used for loading bots to a CNC botnet. Like
Mirari & QBot.

## Interface & ToolPlay
This is a CLI output of the program.
```
root@trackprojects:~# python xLib.py 
[*] Welcome to xLib CLI. [*]
| Exploit : LIBSSH Auth Bypass | Version : 0.2.6 |
--------------------------------------------------
Enter payload: id 
--------------------------------------------------
[+] Found : 6221 devices!
[-] Exploited!
```

## Installation
First you need to install a few modules to prevent errors like this that will prevent you from running the script.
```
root@trackprojects:~# python xLib.py 
Traceback (most recent call last):
  File "xLib.py", line 14, in <module>
    import shodan
ImportError: No module named shodan
```
To do this run the following commands on your system. <br>
```pip install json```<br>
```pip install socket```<br>
```pip install paramiko```<br>
```pip install shodan```<br>
These will install all the modules required to run this script. Once all this is done run this command to finnaly start the xLib Framework.<br>
```python xLib.py```

## TODOs Are Listed Bellow:
TODOs | Status
------|-------
autoLoad Support | [ :+1: ]
Proxy Support | [ :-1: ]
xList Support | [ :-1: ]
Custom Payload Support | [ :+1: ]
