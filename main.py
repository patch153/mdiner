from app import app

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000, use_reloader = True, threaded = True, debug = False)