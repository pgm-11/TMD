# Telegram Media Downloader (beta)
 
With this app you can download all media on a Telegram group as long as you have the link to the group. 

This app does not have a graphical UI and therefore requires basic knowledge of how to use the console/terminal.

*Tested on Macbook with M3 Pro & iPhone XS/15 Pro Max (used Pytp App to execute the script)*

## Download

[Click here to download the latest version](https://github.com/pgm-11/TMD/archive/refs/heads/main.zip) or just clone this repository.


## Requirements
- Telegram Account
- [Install Python on your Device](https://www.python.org/downloads/)
- Find out how to use the console on your computer/phone
- Create a Telegram App

## Set up a Telegram app
For this app it is necessary that you set up a Telegram app. This is quite simple and quick to do. 

**Authenticate yourself with your number on the following page and create a App. (It is possible that the creation of the app only works on mobile devices, just try it out.)**
```text
https://my.telegram.org/apps
```

Once the app has been created, the `App-ID` and `App-HASH` are important. *Do not pass these to third parties.*


## Configuration
1. Create an `.env` file in the same folder. You can copy the content of `example.env` file and fill the two variables `App-ID` and `App-HASH`.
2. Install all python requirements in the directory `pip3 install -r requirements.txt`


## Usage
```bash
python3 downloader.py
```

Now follow the instructions.

## Todos
- [ ] Adding a graphical UI
- [ ] Download media from groups without a public link
- [ ] Removing the limitation



