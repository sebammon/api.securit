from securit import app
from securit.sensors import GPIO

if __name__ == "__main__":
    try:
        app.run(use_reloader=False, host='0.0.0.0')
    except KeyboardInterrupt:
        GPIO.cleanup()
