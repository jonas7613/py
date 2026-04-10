from flask import Flask, jsonify
app = Flask(__name__)
courses = {
    1: {"course_name": "Data Structures", "credits": 4},
    2: {"course_name": "Cyber Security", "credits": 5}
}
@app.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = courses.get(course_id)
    if course:
        return jsonify(course)
    else:
        return jsonify({"error": "Course not found"}), 404
if __name__ == "__main__":
    app.run(port=5003)