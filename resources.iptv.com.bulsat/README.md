# resources.iptv.com.bulsat
Add-on for [Kodi](https://kodi.tv), this addon will generate .m3u and .xml files for channel stream and epg data from [www.bulsat.com](http://www.bulsat.com).

### Disclaimer
This plugin is not officially commisioned/supported by Bulsatcom. The trademark "Bulsatcom" is registered by "Bulsatcom"

## Requirements
* Active user registration in [www.bulsat.com](http://www.bulsat.com)
* [Kodi](https://kodi.tv) media player
* [IPTV Simple Client - win](http://kodi.wiki/view/Add-on:IPTV_Simple_Client) / [IPTV Simple Client - ubuntu](http://kodi.wiki/view/Ubuntu_PVR_add-ons) to watch IPTV on [Kodi](https://kodi.tv)
* [Request](http://kodi.wiki/view/Add-on:Requests) add-on, this is service add-on to make web requests.
* Channel [logos](https://github.com/vastril4o/kodi/raw/master/logos.zip) for [IPTV Simple Client](http://kodi.wiki/view/Add-on:IPTV_Simple_Client)

## Prepare Kodi
```
Settings > System (enable Exper mode)
```
```
Add-ons > Unknow sources > enabled
```
```
Manage Dependencies > Request (only cheking if it is installed)
```
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/6.jpg)

## Installation add-on (resources.iptv.com.bulsat)
* Download add-on [zip](https://github.com/vastril4o/kodi/raw/master/resources.iptv.com.bulsat.zip)
* Install add-on
```
Add-ons/Add-ons Browser/Install from zip file/ (select downloaded zip)
```
* Settings
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/1.jpg)
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/2.jpg)
* Run add-on to generate files

## Installation / Setup add-on (IPTV Simple Client)
* Enable IPTV Simple Client if you missing TV section in Kodi or skip this
```
Add-ons/My add-ons/PVR clients/PVR IPTV Simple Client > Enable
```
If this add-on is missing, go to [IPTV Simple Client - win](http://kodi.wiki/view/Add-on:IPTV_Simple_Client) / [IPTV Simple Client - ubuntu](http://kodi.wiki/view/Ubuntu_PVR_add-ons) wiki page
* Settings
* Point to generated .m3u file
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/3.jpg)
* Point to generated .xml.gz file
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/4.jpg)
* Point to extracted [logos](https://github.com/vastril4o/kodi/raw/master/logos.zip) folder
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/5.jpg)

## Issues (known)
* Logos in [www.bulsat.com](http://www.bulsat.com) are in .svg format which is unsuported by [Kodi](https://kodi.tv)
* Channel .m3u stream urls expiring on every 2 hours, so you need to run add-on again to generate valid .m3u streem
