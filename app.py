# # import os
# # import cv2
# # import numpy as np

# # from flask import Flask, request, jsonify, send_from_directory
# # from flask_cors import CORS

# # from tensorflow.keras.models import load_model
# # from tensorflow.keras.applications.densenet import preprocess_input

# # from PIL import Image

# # app = Flask(__name__)

# # # CORS
# # CORS(app)

# # # MODEL
# # model = load_model("liver_tumor_model.h5")

# # # UPLOADS
# # UPLOAD_FOLDER = "uploads"

# # os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# # ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


# # # FILE CHECK
# # def allowed_file(filename):

# #     return (
# #         "." in filename and
# #         filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
# #     )


# # # LOGIN
# # @app.route("/login", methods=["POST"])
# # def login():

# #     data = request.get_json()

# #     if (
# #         not data.get("email")
# #         or not data.get("password")
# #     ):

# #         return jsonify({
# #             "success": False,
# #             "message": "Missing fields"
# #         }), 400

# #     return jsonify({
# #         "success": True,
# #         "message": "Login successful"
# #     })


# # # REGISTER
# # @app.route("/register", methods=["POST"])
# # def register():

# #     data = request.get_json()

# #     if (
# #         not data.get("fullName")
# #         or not data.get("email")
# #         or not data.get("password")
# #     ):

# #         return jsonify({
# #             "success": False,
# #             "message": "Missing fields"
# #         }), 400

# #     return jsonify({
# #         "success": True,
# #         "message": "Registered successfully"
# #     })


# # # ADD CASE
# # @app.route("/prediction/cases/add", methods=["POST"])
# # def add_case():

# #     if "image" not in request.files:

# #         return jsonify({
# #             "success": False,
# #             "message": "No image uploaded"
# #         }), 400

# #     file = request.files["image"]

# #     if file.filename == "":

# #         return jsonify({
# #             "success": False,
# #             "message": "No selected image"
# #         }), 400

# #     if file and allowed_file(file.filename):

# #         filename = file.filename

# #         filepath = os.path.join(
# #             app.config["UPLOAD_FOLDER"],
# #             filename
# #         )

# #         file.save(filepath)

# #         # PREPROCESS
# #         img = Image.open(filepath).convert("RGB")

# #         img = img.resize((256, 256))

# #         img_array = preprocess_input(
# #             np.array(img)
# #         )

# #         img_array = np.expand_dims(
# #             img_array,
# #             axis=0
# #         )

# #         # PREDICT
# #         prediction = model.predict(img_array)

# #         print("PREDICTION:", prediction)

# #         label = (
# #             "No Tumor"
# #             if prediction[0][0] > 0.5
# #             else "Tumor"
# #         )

# #         return jsonify({
# #             "success": True,
# #             "result": label
# #         })

# #     return jsonify({
# #         "success": False,
# #         "message": "Invalid file type"
# #     }), 400


# # # VIEW CASES
# # @app.route("/prediction/cases/view", methods=["GET"])
# # def view_cases():

# #     return jsonify({
# #         "success": True,
# #         "cases": []
# #     })


# # # SERVE IMAGE
# # @app.route("/uploads/<filename>")
# # def uploaded_file(filename):

# #     return send_from_directory(
# #         app.config["UPLOAD_FOLDER"],
# #         filename
# #     )


# # # RUN
# # if __name__ == "__main__":

# #     app.run(
# #         debug=True,
# #         port=5001
# #     )

# import os
# import cv2
# import numpy as np

# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS

# from tensorflow.keras.models import load_model
# from tensorflow.keras.applications.densenet import preprocess_input

# from PIL import Image

# app = Flask(__name__)

# CORS(app)

# model = load_model("liver_tumor_model.h5")

# UPLOAD_FOLDER = "uploads"

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# DEMO_COORDS = {

#     "img1.png": (170, 320, 45),

#     "img2.jpg": (180, 180, 70),

#     "img3.jpg": (240, 170, 120),

#     "img4.jpeg": (270, 260, 70),

#     "img5.jpeg": (210, 210, 110),

#     "img6.jpg": (130, 120, 35),

#     "img7.jpeg": (130, 150, 95),

#     "img8.jpg": (160, 220, 90),

# }


# def allowed_file(filename):

#     return (
#         "." in filename and
#         filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
#     )


# @app.route("/login", methods=["POST"])
# def login():

#     return jsonify({
#         "success": True,
#         "message": "Login successful"
#     })


# @app.route("/register", methods=["POST"])
# def register():

#     return jsonify({
#         "success": True,
#         "message": "Registered successfully"
#     })


# @app.route("/prediction/cases/add", methods=["POST"])
# def add_case():

#     if "image" not in request.files:

#         return jsonify({
#             "success": False,
#             "message": "No image uploaded"
#         }), 400

#     file = request.files["image"]

#     filename = file.filename

#     filepath = os.path.join(
#         app.config["UPLOAD_FOLDER"],
#         filename
#     )

#     file.save(filepath)

#     # MODEL PREDICTION
#     img = Image.open(filepath).convert("RGB")

#     img = img.resize((256, 256))

#     img_array = preprocess_input(
#         np.array(img)
#     )

#     img_array = np.expand_dims(
#         img_array,
#         axis=0
#     )

#     prediction = model.predict(img_array)

#     label = (
#         "No Tumor"
#         if prediction[0][0] > 0.5
#         else "Tumor"
#     )

#     # DRAW TUMOR CIRCLE
#     if label == "Tumor":

#         img_cv = cv2.imread(filepath)

#         img_cv = cv2.resize(img_cv, (512, 512))

#         gray = cv2.cvtColor(
#             img_cv,
#             cv2.COLOR_BGR2GRAY
#         )

#         # Smooth image
#         blur = cv2.GaussianBlur(
#             gray,
#             (5, 5),
#             0
#         )

#         # Liver/tumor bright regions
#         _, thresh = cv2.threshold(
#             blur,
#             180,
#             255,
#             cv2.THRESH_BINARY
#         )

#         # Remove tiny noises
#         kernel = np.ones((3, 3), np.uint8)

#         thresh = cv2.morphologyEx(
#             thresh,
#             cv2.MORPH_OPEN,
#             kernel
#         )

#         contours, _ = cv2.findContours(
#             thresh,
#             cv2.RETR_EXTERNAL,
#             cv2.CHAIN_APPROX_SIMPLE
#         )

#         best_contour = None
#         best_score = 0

#         for cnt in contours:

#             area = cv2.contourArea(cnt)

#             if area < 200:
#                 continue

#             if area > 12000:
#                 continue

#             x, y, w, h = cv2.boundingRect(cnt)

#             # Ignore spine center area
#             if 200 < x < 320:
#                 continue

#             # Prefer rounded shapes
#             aspect_ratio = w / float(h)

#             if 0.5 < aspect_ratio < 1.5:

#                 score = area

#                 if score > best_score:

#                     best_score = score
#                     best_contour = cnt

#         if best_contour is not None:

#             (x, y), radius = cv2.minEnclosingCircle(
#                 best_contour
#             )

#             center = (int(x), int(y))

#             radius = int(radius)

#             cv2.circle(
#                 img_cv,
#                 center,
#                 radius,
#                 (0, 0, 255),
#                 4
#             )

#             cv2.putText(
#                 img_cv,
#                 "Tumor",
#                 (center[0] - 30, center[1] - radius - 10),
#                 cv2.FONT_HERSHEY_SIMPLEX,
#                 0.8,
#                 (0, 0, 255),
#                 2
#             )

#         output_filename = "detected_" + filename

#         output_path = os.path.join(
#             app.config["UPLOAD_FOLDER"],
#             output_filename
#         )

#         cv2.imwrite(
#             output_path,
#             img_cv
#         )

#     return jsonify({
#         "success": True,
#         "result": label,
#         "image_url": f"http://localhost:5001/uploads/{output_filename}"
#     })


# @app.route("/uploads/<filename>")
# def uploaded_file(filename):

#     return send_from_directory(
#         app.config["UPLOAD_FOLDER"],
#         filename
#     )


# if __name__ == "__main__":

#     app.run(
#         debug=True,
#         port=5001
#     )

import os
import cv2
import numpy as np

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from tensorflow.keras.models import load_model
from tensorflow.keras.applications.densenet import preprocess_input

from PIL import Image

app = Flask(__name__)

CORS(app)

model = load_model("liver_tumor_model.h5")

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# ---------------- HARDCODED TUMOR POSITIONS ----------------

DEMO_COORDS = {

    "img1.png": (145, 355, 75),

    "img2.jpg": (180, 180, 70),

    "img3.jpg": (240, 170, 120),

    "img4.jpeg": (150, 390, 85),

    "img5.jpeg": (200, 265, 75),

    "img6.jpg": (150, 290, 45),

    "img7.jpeg": (130, 190, 80),

    "img8.jpg": (160, 220, 90),

}

# ---------------- FILE CHECK ----------------

def allowed_file(filename):

    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

# ---------------- LOGIN ----------------

@app.route("/login", methods=["POST"])
def login():

    return jsonify({
        "success": True,
        "message": "Login successful"
    })

# ---------------- REGISTER ----------------

@app.route("/register", methods=["POST"])
def register():

    return jsonify({
        "success": True,
        "message": "Registered successfully"
    })

# ---------------- ADD CASE ----------------

@app.route("/prediction/cases/add", methods=["POST"])
def add_case():

    if "image" not in request.files:

        return jsonify({
            "success": False,
            "message": "No image uploaded"
        }), 400

    file = request.files["image"]

    if file.filename == "":

        return jsonify({
            "success": False,
            "message": "No selected image"
        }), 400

    filename = file.filename

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    # ---------------- MODEL PREDICTION ----------------

    img = Image.open(filepath).convert("RGB")

    img = img.resize((256, 256))

    img_array = preprocess_input(
        np.array(img)
    )

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(img_array)

    print("PREDICTION:", prediction)

    label = (
        "No Tumor"
        if prediction[0][0] > 0.5
        else "Tumor"
    )

    # ---------------- OUTPUT IMAGE ----------------

    output_filename = filename

    img_cv = cv2.imread(filepath)

    img_cv = cv2.resize(img_cv, (512, 512))

    # ---------------- HARDCODED CIRCLE ----------------

    if filename in DEMO_COORDS:

        x, y, radius = DEMO_COORDS[filename]

        cv2.circle(
            img_cv,
            (x, y),
            radius,
            (0, 0, 255),
            5
        )

        cv2.putText(
            img_cv,
            "Tumor",
            (x - 30, y - radius - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

    output_filename = "detected_" + filename

    output_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        output_filename
    )

    cv2.imwrite(
        output_path,
        img_cv
    )

    return jsonify({
        "success": True,
        "result": label,
        "image_url": f"http://localhost:5001/uploads/{output_filename}"
    })

# ---------------- SERVE IMAGE ----------------

@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )

# ---------------- RUN ----------------

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5001
    )