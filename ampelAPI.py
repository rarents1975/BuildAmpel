from flask import Flask
from flask import jsonify
import RPi.GPIO as GPIO
import time

LEDRED = 18
LEDYELLOW = 27
LEDGREEN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEDYELLOW, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LEDGREEN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LEDRED, GPIO.OUT, initial=GPIO.LOW)

app = Flask(__name__)

@app.route('/api/led/red')
def led_red():
    GPIO.output(LEDRED,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(LEDRED,GPIO.LOW)
    return jsonify(ledred=GPIO.input(LEDRED))
    GPIO.cleanup

@app.route('/api/led/yellow')
def led_yellow():
    GPIO.output(LEDYELLOW,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(LEDYELLOW,GPIO.LOW)
    return jsonify(ledyellow=GPIO.input(LEDYELLOW))
    GPIO.cleanup

@app.route('/api/led/green')
def led_green():
    GPIO.output(LEDGREEN,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(LEDGREEN,GPIO.LOW)
    return jsonify(ledgreen=GPIO.input(LEDGREEN))
    GPIO.cleanup

#@app.route('/api/led/toggle')
#def led_togggle():
#    GPIO.output(LED,not GPIO.input(LED))
#    return jsonify(led=GPIO.input(LED))

#GPIO.cleanup

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
