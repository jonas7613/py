from flask import Flask, jsonify
import requests
app = Flask(__name__)
enrollments = {
    1: {"student_id": 1, "course_id": 2},
    2: {"student_id": 2, "course_id": 1}
}
STUDENT_SERVICE_URL = "http://localhost:5001/students"
COURSE_SERVICE_URL = "http://localhost:5003/courses"
@app.route("/enrollment/<int:enroll_id>", methods=["GET"])
def get_enrollment(enroll_id):
    enrollment = enrollments.get(enroll_id)

    if enrollment:
        student_res = requests.get(f"{STUDENT_SERVICE_URL}/{enrollment['student_id']}")
        course_res = requests.get(f"{COURSE_SERVICE_URL}/{enrollment['course_id']}")
        result = enrollment.copy()
        if student_res.status_code == 200:
            result["student"] = student_res.json()
        else:
            result["student"] = "Student not found"
        if course_res.status_code == 200:
            result["course"] = course_res.json()
        else:
            result["course"] = "Course not found"
        return jsonify(result)
    else:
        return jsonify({"error": "Enrollment not found"}), 404
if __name__ == "__main__":
    app.run(port=5002)