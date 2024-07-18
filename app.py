from extensions import app
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

if __name__ == "__main__":
    from routes import *
    app.run(debug=True)
    print("app is running")