from project import add_student, search_student, delete_student, load_students


def test_add_student():
    add_student("Test", "999", 4.0)
    students = load_students()
    assert any(s["id"] == "999" for s in students)


def test_search_student():
    result = search_student("Test")
    assert isinstance(result, list)


def test_delete_student():
    delete_student("999")
    students = load_students()
    assert not any(s["id"] == "999" for s in students)
