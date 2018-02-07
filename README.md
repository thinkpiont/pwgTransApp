# pwgTransApp
Web service for uploading images to Piwigo by image url 

You can send POST request with image infomations(url, tags,album...) to pwgTrans. PwgTrans will download this image and upload it to your piwigo site by apis offered by Piwigo.

PwgTrans is a Python based Web service. It reies on Flask to build basic web serives.

# How to use
## Step 1 Get Python installed
1. [Downlaod and install Python](https://wiki.python.org/moin/BeginnersGuide/Download)

## Step 2 Get Flask installed
Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.
Install Flask:
```
$ pip install Flask
```
[More about Flask](http://flask.pocoo.org/)
[Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)by Miguel Grinberg

## Step 3 Run app.py after Flask is installed
After Flask is install, download app.py and paste to your Python folder on your server.
Modify this variables in the app.py:


### Your pwgTrans Api url:
```
@app.route('/pwgtrans/api/v1.0/images',methods=['POST'])
```
This is your pwgTrans api to revice POST request from client. It can be modified as your will.

### Your Piwigo Server Infomation:
```
def uploadtoPiwigo():
    #This is your Piwogo server url
    site = piwigo.Piwigo('http://example.com')
    #This is your Piwigo Account info(admin user only).
    site.pwg.session.login(username='piwigouser',password="password")
```
Change above codes according to your Piwigo server's infomation. This code uses a Python lib called [piwigo](https://github.com/fraoustin/piwigo) by fraoustin.*Remember to install this lib on your server*.

### Now you can run you web service:
```
$ ./app.py
```
Now, your pwgTrans web service is running.

## Step 4 Send POST request from your client
Once your pwgTrans service is runnning, you can send POST request to your server.
The api url is defined by you in the app.py.
API method:POST
Format:JSON
API Parameters:
Parameter | Required | Type | Description
------------ | ------------ | ----------- | ------------
image | * | String | Image's source url
category | * | Int | Ablum's id in Piwigo.Client can get it by Piwigo api
name | - | String | Image's name will displayed at Piwigo
author | - | String | Image's authur
comment | - | String | Comments on this image
tags | _ | String | "tag1,tag2" Different tags seperated by comma. 
