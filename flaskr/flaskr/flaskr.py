from flask import Flask, current_app, Response, send_file,  request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)  # create the application instance :)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    try:
        if filename.endswith('.jpg'):  # Or any other binary file type
            with open(os.path.join(app.static_folder, filename), 'rb') as f:
                image_binary = f.read()
            encoded_image = base64.b64encode(image_binary).decode('utf-8')
            return Response(encoded_image, mimetype='image/jpeg')
        return app.send_static_file(filename)
    except FileNotFoundError:
        return {"error": "File not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500
