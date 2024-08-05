from empl import Company


api = Company("https://x-clients-be.onrender.com")


def test_get_list_of_employees():
    name = "Yana"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0


def test_add_new_employee():
    name = "Yana"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Yana99", "B")
    assert new_employee["id"] > 0

    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
    assert resp[0]["firstName"] == "Yana99"
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == "B"


def test_get_employee_by_id():
    name = "Yana"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Yana99", "Ba")
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "Yana99"
    assert get_info["lastName"] == "Ba"


def test_change_employee_info():
    name = "Yana"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Yana99", "Bab")
    id_employee = new_employee["id"]

    update = api.update_employee_info(id_employee, "Babar", "yana.babarikova@gmail.com")
    assert update["id"] == id_employee
    assert update["email"] == "yana.babarikova@gmail.com"
    assert update["isActive"] == True