import time
import RPi.GPIO as GPIO

from nanohttp import Controller, RestController, json


class ForwardControllers(RestController):
    @json
    def get(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(36,GPIO.OUT)
        GPIO.setup(38,GPIO.OUT)
        GPIO.setup(35,GPIO.OUT)
        GPIO.setup(37,GPIO.OUT)
        GPIO.output(36,True)
        GPIO.output(38,False)
        GPIO.output(35,True)
        GPIO.output(37,False)
        time.sleep(0.4)
        GPIO.cleanup()
        return {'status':'ok'}


class BackwardControllers(RestController):
    @json
    def get(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(36,GPIO.OUT)
        GPIO.setup(38,GPIO.OUT)
        GPIO.setup(35,GPIO.OUT)
        GPIO.setup(37,GPIO.OUT)
        GPIO.output(36,False)
        GPIO.output(38,True)
        GPIO.output(35,False)
        GPIO.output(37,True)
        time.sleep(0.4)
        GPIO.cleanup()
        return {'status':'ok'}


class LeftControllers(RestController):
    @json
    def get(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(36,GPIO.OUT)
        GPIO.setup(38,GPIO.OUT)
        GPIO.setup(35,GPIO.OUT)
        GPIO.setup(37,GPIO.OUT)
        GPIO.output(36,False)
        GPIO.output(38,True)
        GPIO.output(35,True)
        GPIO.output(37,False)
        time.sleep(0.4)
        GPIO.cleanup()
        return {'status':'ok'}


class RightControllers(RestController):
    @json
    def get(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(36,GPIO.OUT)
        GPIO.setup(38,GPIO.OUT)
        GPIO.setup(35,GPIO.OUT)
        GPIO.setup(37,GPIO.OUT)
        GPIO.output(36,True)
        GPIO.output(38,False)
        GPIO.output(35,False)
        GPIO.output(37,True)
        time.sleep(0.4)
        GPIO.cleanup()
        return {'status':'ok'}


class Root(Controller):
    forward = ForwardControllers()
    backward = BackwardControllers()
    left = LeftControllers()
    right = RightControllers()

