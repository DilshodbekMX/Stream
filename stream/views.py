import cv2
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators import gzip


@gzip.gzip_page
def index(request):

    return render(request=request, template_name="index.html")


def videoStream(request,camera_ip):
    return StreamingHttpResponse(gen(camera_ip), content_type='multipart/x-mixed-replace; boundary=frame')
def find_camera(ids):

    cameras=['http://192.168.1.5:8080/video']

    return cameras[int(ids)]


def gen(camera):
    cam = find_camera(camera)
    came = IPWebCam(cam)
    while True:
        frame = came.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


class IPWebCam(object):
    def __init__(self, camera_ip):
        self.url = cv2.VideoCapture(camera_ip)

    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):
        success, imgNp = self.url.read()
        resize = cv2.resize(imgNp, (640, 480), interpolation=cv2.INTER_LINEAR)
        ret, jpeg = cv2.imencode('.jpg', resize)
        return jpeg.tobytes()
