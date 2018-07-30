Support this project :) [buy me a coffe whit PayPal](http://www.paypal.me/VasilValchev/2)

![alt text](https://github.com/vasildev/resources.iptv.bsc/blob/master/icon.png)
# resources.iptv.bsc
[Add-on](https://github.com/vasildev/resources.iptv.bsc/raw/master/resources.iptv.bsc.zip) for [Kodi](https://kodi.tv), this addon will generate .m3u and .xml files for channel stream and epg data from [www.bulsat.com](http://www.bulsat.com)

### Disclaimer
This plugin is not officially commisioned/supported by Bulsatcom. The trademark "Bulsatcom" is registered by "Bulsatcom", visit [www.bulsat.com](http://www.bulsat.com)

## Screenshot
![alt text](https://github.com/vasildev/resources.iptv.bsc/blob/master/resources/screenshot1.jpg)
![alt text](https://github.com/vasildev/resources.iptv.bsc/blob/master/resources/screenshot2.jpg)
![alt text](https://github.com/vasildev/resources.iptv.bsc/blob/master/resources/screenshot3.jpg)

## Requirements
* Active user registration in [www.bulsat.com](http://www.bulsat.com)
* [Kodi](https://kodi.tv) media player
* [IPTV Simple Client - win](http://kodi.wiki/view/Add-on:IPTV_Simple_Client) / [IPTV Simple Client - ubuntu](http://kodi.wiki/view/Ubuntu_PVR_add-ons) to watch IPTV on [Kodi](https://kodi.tv)
* [Request](http://kodi.wiki/view/Add-on:Requests) add-on, this is service add-on to make web requests.
* [IPTV BSC](https://github.com/vasildev/resources.iptv.bsc/raw/master/resources.iptv.bsc.zip) add-on zip.

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
![alt text](https://github.com/vasildev/resources.iptv.bsc/blob/master/resources/6.jpg)

## Installation add-on (resources.iptv.bsc)
* Download add-on [zip](https://github.com/vasildev/resources.iptv.bsc/raw/master/resources.iptv.bsc.zip)
* Install add-on
```
Add-ons > Add-ons Browser > Install from zip file > select downloaded zip
```
* Settings
![alt text](https://github.com/vasildev/resources.iptv.bsc/blob/master/resources/1.jpg)
![alt text](https://github.com/vasildev/resources.iptv.bsc/blob/master/resources/2.jpg)
* Run add-on to generate files

## Installation / Setup add-on (IPTV Simple Client)
* Enable [IPTV Simple Client - win](http://kodi.wiki/view/Add-on:IPTV_Simple_Client) / [IPTV Simple Client - ubuntu](http://kodi.wiki/view/Ubuntu_PVR_add-ons) if you missing TV section in Kodi or skip this
```
Add-ons > My add-ons > PVR clients > PVR IPTV Simple Client > enable
```
* Settings
![alt text](https://github.com/vasildev/resources.iptv.bsc/blob/master/resources/3.jpg)
![alt text](https://github.com/vasildev/resources.iptv.bsc/blob/master/resources/4.jpg)
![alt text](https://github.com/vasildev/resources.iptv.bsc/blob/master/resources/5.jpg)
You can find all channel logo png files in /resources/logos/256 which are also contained in downloaded zip.

## Issues (known)
* Logos in [www.bulsat.com](http://www.bulsat.com) are in .svg format which is unsuported by [Kodi](https://kodi.tv)
* Channel .m3u stream urls expiring on every 2 hours, so you need to run add-on again to generate valid .m3u streem
* Add bugs or problems on project [issue](https://github.com/vasildev/resources.iptv.bsc/issues) page

