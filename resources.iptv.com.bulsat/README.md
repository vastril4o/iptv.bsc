# resources.iptv.com.bulsat
Add-on for [Kodi](https://kodi.tv), this addon will generate .m3u and .xml files for channel stream and epg data from [www.bulsat.com](http://www.bulsat.com).

## Requirements
* Active user registration in [www.bulsat.com](http://www.bulsat.com)
* [Kodi](https://kodi.tv) media player
* [IPTV Simple Client - win](http://kodi.wiki/view/Add-on:IPTV_Simple_Client) / [IPTV Simple Client - ubuntu](http://kodi.wiki/view/Ubuntu_PVR_add-ons) to watch IPTV on [Kodi](https://kodi.tv)
* [Request](http://kodi.wiki/view/Add-on:Requests) add-on, this is service add-on to make web requests.
* Channel [logos](https://github.com/vastril4o/kodi/raw/master/logos.zip) for [IPTV Simple Client](http://kodi.wiki/view/Add-on:IPTV_Simple_Client)

## Installation add-on (resources.iptv.com.bulsat)
* Prepare [Kodi](https://kodi.tv) for installation
```
Settings > System
```
```
Expert mode
```
```
Add-ons > Unknow sources > enabled
```
```
Manage Dependencies > Request
```
If you can`t find [Request](http://kodi.wiki/view/Add-on:Requests), you need to install it first
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/6.png)
* Install add-on from [zip](https://github.com/vastril4o/kodi/raw/master/resources.iptv.com.bulsat.zip)
* Settings
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/1.png)
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/2.png)
* Run add-on again to generate files

## Installation / Setup add-on (IPTV Simple Client)
* Enable IPTV Simple Client if you missing TV section in Kodi, else skip this. Add-on location:
```
Add-ons/My add-ons/PVR clients/PVR IPTV Simple Client > Enable
```
If this add-on is missing, go to [IPTV Simple Client - win](http://kodi.wiki/view/Add-on:IPTV_Simple_Client) / [IPTV Simple Client - ubuntu](http://kodi.wiki/view/Ubuntu_PVR_add-ons) wiki page
* Settings
* Point to generated .m3u file
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/3.png)
* Point to generated .xml.gz file
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/4.png)
* Point to extracted folder from this zip: [logos](https://github.com/vastril4o/kodi/raw/master/logos.zip)
![alt text](https://github.com/vastril4o/kodi/blob/master/resources.iptv.com.bulsat/resources/5.png)

## Issues (known)
* Logos in [www.bulsat.com](http://www.bulsat.com) are in .svg format which is unsuported by [Kodi](https://kodi.tv), only .png
* Channel .m3u stream cookie is expiring on every 2 hours, so you need to run add-on again to generate valid .m3u streem fail
