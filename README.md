# Onetimepass Extension for ulauncher

Generate TOTP tokens for two factor authentication.

## Settings
There are only a few settings available

*generate pin keyword*   
default: one   
This is the keyword to activate this ulauncher. If you type a argument after the keyword it will be used to filter the providers.

*providers*   
default:
This field contains provider's information with a name and a secret seperated by a equals sign with a space.
Example:
```
google=123123 facebook=321321 github=121212
```

## Requirements
For this extension the onetimepass python library is needed.
```
pip3 install onetimepass
```

## Disclaimer
This software is delivered free of charge and without warranty.
Make sure you always make backup keys for your accounts.
I am not responsible for any loss of data.

## Licenses
All rights off third party libraries or images remain to the original authors.

Big thanks to the following authors
* ulauncher
* onetimepass (totp library)
* ulauncher-2fa
