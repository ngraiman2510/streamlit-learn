import streamlit as st

if "students" not in st.session_state:
    st.session_state.students = []

if "student_name" not in st.session_state:
    st.session_state.student_name = ""
if "student_mark" not in st.session_state:
    st.session_state.student_mark = 0


def getGrade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    name = st.session_state.student_name.strip()
    mark = st.session_state.student_mark

    if not name:
        st.session_state.form_error = "Please enter a student name."
        return
    if mark <= 0 or mark > 100:
        st.session_state.form_error = "Please enter a valid mark between 1 and 100."
        return

    grade = getGrade(mark)
    st.session_state.students.append({"name": name, "mark": mark, "grade": grade})
    st.session_state.form_success = f"Added {name} with mark {mark} and grade {grade}"

    ## Clearing the form fields after submission
    st.session_state.student_name = ""
    st.session_state.student_mark = 0


## constructing a form to add student grades
with st.form("my_form"):
    st.write("Add Student Grade")
    st.text_input("Student Name", key="student_name")
    st.number_input("Grade", min_value=0, max_value=100, step=1, key="student_mark")
    st.form_submit_button("Add Student", on_click=add_student)

if "form_error" in st.session_state:
    st.error(st.session_state.pop("form_error"))
if "form_success" in st.session_state:
    st.success(st.session_state.pop("form_success"))

## displaying the student grades in a table
if st.session_state.students:
    st.write("Student Grades:")
    st.table(st.session_state.students)
    average, highest, lowest = st.columns(3)
    average.metric(
        "Average",
        f"{sum(student['mark'] for student in st.session_state.students) / len(st.session_state.students):.2f}",
    )
    highest.metric(
        "Highest", f"{max(student['mark'] for student in st.session_state.students)}"
    )
    lowest.metric(
        "Lowest", f"{min(student['mark'] for student in st.session_state.students)}"
    )
