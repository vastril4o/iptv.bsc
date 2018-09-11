<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/ntkme/github-buttons/archive/master.zip" data-icon="octicon-cloud-download" data-size="large" aria-label="Download ntkme/github-buttons on GitHub">Download</a>
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>
Download last version [here](/download/iptv.bsc.zip)

# iptv.bsc
Add-on for [Kodi](https://kodi.tv), this addon will generate .m3u and .xml files for channel stream and epg data from [www.bulsat.com](http://www.bulsat.com).<br/>
Support this project :) you can buy me a coffe whit [PayPal](http://www.paypal.me/VasilValchev/2)

## Screenshot
![alt text](/src/resources/screenshot1.jpg)

## Requirements
* Active user registration in [www.bulsat.com](http://www.bulsat.com)
* [Kodi](https://kodi.tv) media player
* [IPTV Simple Client - win](http://kodi.wiki/view/Add-on:IPTV_Simple_Client) / [IPTV Simple Client - ubuntu](http://kodi.wiki/view/Ubuntu_PVR_add-ons) to watch IPTV on [Kodi](https://kodi.tv)
* [Request](http://kodi.wiki/view/Add-on:Requests) add-on, this is service add-on to make web requests.
* [IPTV BSC](/download/iptv.bsc.zip) add-on zip.

## Prepare Kodi
```
Settings > System (enable Exper mode)
```
```
Settings > System > Add-ons > Unknow sources > enabled
```
```
Settings > System > Add-ons > Manage Dependencies > request (check if it is installed)
```

## Installation (iptv.bsc)
* Download add-on [zip](/download/iptv.bsc.zip)
* Install add-on
```
Add-ons > Add-ons Browser > Install from zip file > select downloaded zip
```
* Settings
Open addon and set your bulsat credential and download path for files
* Run add-on to generate files

## Installation / Setup (IPTV Simple Client)
* Enable [IPTV Simple Client - win](http://kodi.wiki/view/Add-on:IPTV_Simple_Client) / [IPTV Simple Client - ubuntu](http://kodi.wiki/view/Ubuntu_PVR_add-ons) if you missing TV section in Kodi or skip this
```
Add-ons > My add-ons > PVR clients > PVR IPTV Simple Client > enable
```
* Settings
Set your location to match your downloaded files from iptv.bsc

You can find all channel logo png files in src/resources/logos/256 which are also contained in downloaded zip.

### Disclaimer
This plugin is not officially commisioned/supported by Bulsatcom. The trademark "Bulsatcom" is registered by "Bulsatcom", visit [www.bulsat.com](http://www.bulsat.com)