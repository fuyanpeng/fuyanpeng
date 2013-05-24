# -*- coding: utf-8 -*-
import datetime
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.utils import simplejson as json


def jsonify(*args, **kwargs):
    if len(args) == 1:
        content = json.dumps(args[0])
    else:
        content = json.dumps(dict(*args, **kwargs))

    response = HttpResponse(content=content)
    response['Cache-Control'] = 'no-cache'

    return response


@csrf_exempt
def kindeditor_upload(request):

    imgFile = request.FILES.get('imgFile', None)
    fileDir = request.REQUEST.get('dir')

    if imgFile is None or fileDir not in ('image', 'flash', 'media', 'file'):
        return jsonify(error=1, message=u'')

    today = datetime.datetime.today()
    rpath = 'upload/%s/%d/%d/%d/%s' % (fileDir, today.year,
                                       today.month, today.day, imgFile.name)

    fname = default_storage.save(rpath.encode('utf-8'), imgFile)
    url = default_storage.url(fname)

    return jsonify(error=0, url=url)
