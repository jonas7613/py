from flask import Flask, jsonify
app = Flask(__name__)
students = {
    1: {"name": "Jonathan", "dept": "CSE"},
    2: {"name": "Arun", "dept": "ECE"}
}
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = students.get(student_id)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404
if __name__ == "__main__":
    app.run(port=5001)