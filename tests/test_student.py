from student.student import Student

def test_init():
    name = "Ada Lovelace"
    level = "sophomore"
    courses = ["mathematics", "foundations of computing"]

    ada = Student(name, level, courses)

    assert ada.name == name
    assert ada.level == level
    assert ada.courses == courses

def test_add_class():
    new_class = 'Intro to Feminism'
    charles = Student("Charles Babbage", "senior", ["mechanical engineering"])
    charles.add_class(new_class)

    assert len(charles.courses) == 2
    assert new_class in charles.courses

def test_get_num_classes():
    george = Student("George Byron", "senior", ["advanced poetry"])

    assert george.get_num_classes() == 1

def test_summary():
    anne = Student(
        "Anne Byron",
        "senior",
        ["theory of religion", "theory of morality"]
    )

    assert anne.summary() == "Anne Byron is a senior enrolled in 2 classes"

def test_get_student_with_more_classes_student_b():
    charles = Student("Charles Babbage", "senior", ["mechanical engineering"])
    ada = Student(
        "Ada Lovelace",
        "sophomore",
        ["mathematics", "foundations of computing"]
    )
    # act
    student_b = charles.get_student_with_more_classes(charles, ada)
    assert student_b == ada

def test_get_student_with_more_classes_student_a():
    charles = Student("Charles Babbage", "senior", ["mechanical engineering"])
    ada = Student(
        "Ada Lovelace",
        "sophomore",
        ["mathematics", "foundations of computing"]
    )
    # act
    student_a = charles.get_student_with_more_classes(ada, charles)
    assert student_a == ada    

def test_add_class_empty_list_courses():
    # act/arrange
    charles = Student("Charles Babbage", "senior")
    #assert
    assert charles.courses == []