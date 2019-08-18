from securit.app import app
from securit.sensors import GPIO

if __name__ == "__main__":
    app.run(use_reloader=False, host='0.0.0.0')
    GPIO.cleanup()
    app.logger.info('GPIO pins were cleaned!')