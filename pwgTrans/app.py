#!flask/bin/python
from flask import Flask,jsonify,abort,make_response,request
import urllib,re,requests,sys,piwigo,time,urlparse

#URL of your Piwigo Api
piwigourl = 'http://example.com/ws.php?format=json'


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

# Api for chrome extension to upload image information
@app.route('/pwgtrans/api/v1.0/images',methods=['POST'])
def create_task():
    if not request.json or not 'image' in request.json:
        abort(400)

    
    


    image = {
        'id': images[-1]['id'] + 1,
        'image': request.json['image'],
        'category': request.json.get('category', 58),
        'name': request.json.get('name', "local"),
        'author': request.json.get('authur', ""),
        'comment': request.json.get('comment', ""),
        'level': request.json.get('level', 0),
        'tags': request.json['tags'],
    }
     # get image file type from image url
    imgurl = request.json['image']
    parse = urlparse.urlparse(imgurl)
    path = parse.path
    filetype = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', path)
    # use time stample to define image local file name to prevent collusion
    ticks = str(time.time())
    if len(filetype):
        print('filtye ttttttt')
        image['image'] = ticks + filetype[0]
        '''image['name'] = image['name']+filetype[0]'''
        print(image['image'])

        images.append(image)
        imageurl = image.get('author')
        imagename = image.get('image')
        downloadimage(imageurl,imagename)
        return jsonify({'image': image}), 201
    else:
        print('filtye ffffffff')
        return jsonify({'error':'Can not get filetype'})


def downloadimage(imageurl,imagename):
    testfile = urllib.URLopener()
    testfile.retrieve(imageurl, imagename,reporthook=dlprogress)



'''dl progress'''
def dlprogress(count,blockSize,totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write('%2d%%' % percent)
    sys.stdout.write("\b\b\b")
    sys.stdout.flush()
    if(count*blockSize >= totalSize):
        '''download finished'''
        uploadtoPiwigo()



def uploadtoPiwigo():
    site = piwigo.Piwigo('http://example.com')
    site.pwg.session.login(username='piwigouser',password="password")
    print(images[-1]['tags'])
    site.pwg.images.addSimple(image=images[-1]['image'],category=images[-1]['category'],name=images[-1]['name'],author=images[-1]['author'],comment=images[-1]['comment'], tags=images[-1]['tags'])





if __name__ == '__main__':

    app.run(host='0.0.0.0')
