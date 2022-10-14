# Steam account switcher 
_(linux only now, but you can PR to add windows registry support)_

Allows to switch steam account without having to log out and log in again.


## How it works

Just replace `Registry.HKCU.Software.Valve.Steam.AutoLoginUser` variable with another steam account name, 
so next time you start steam it will log in with that account.

## How to use

`python main.py`

If steam is currently running, you will need to re-enter it after running script.  
**Don't click on `Log out of account` button, otherwise you will need to log in again**

Example output:
```
Current account: svinerus

Choose an account:
0: svinerus (Дед)
1: svinerus2 (Дед)
> 1

Kill steam? [Y/n]: Y 
```


#### todo
- pip pkg
- windows support