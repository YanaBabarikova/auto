from EmployeeApi import EmployeeApi
from EmployeeSQL import EmployeeSQL
import allure

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeSQL("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

@allure.title("Создание организации")
@allure.description("Проверка, что созданная компания отображается в списке")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_get_employee():
    with allure.step("Создать компанию"):
        name = "SkyPro_tester"
        descr = "Образовательные услуги"
        result = api.create_company(name, descr)
        new_id = result["id"]

    with allure.step("получаем список сотрудников компании через API"):
        api_result = api.get_employee(new_id)
    
    with allure.step("получаем список сотрудников компании из БД"):
        my_params = str(new_id)  
        db_result = db.get_employees(my_params)

    with allure.step("проверка соотвествия списка полученного из API списку из БД"):
        assert len(api_result) == len(db_result)


@allure.title("Создание организации")
@allure.description("Проверка создания сотрудника у конкретной компании")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_add_new():
    with allure.step("Создать компанию"):
        name = "SkyPro_tester"
        descr = "Образовательные услуги"
        result = api.create_company(name, descr)
        new_id = result["id"]

    with allure.step("Взаимодействие с списком сотрудников компании через API (cоздание нового сотрудника)"):
        employee_company = api.get_employee(new_id)
        len_before = len(employee_company)

    with allure.step("Создание сотрудника"):
        first_name = 'Яна'
        last_name = 'Заяц'
        middle_name = 'Руслановна'
        company_id = new_id
        email = 'tester@gmail.com'
        phone = '7(915)536-02-93'

        new_employee = api.create_employee(first_name, last_name, middle_name, company_id, email, phone) 
        id_employee = new_employee["id"]

    with allure.step("Взаимодействие с списком сотрудников компании через API (удаление нового сотрудника)"):
        employee_company = api.get_employee(new_id)
        len_after = len(employee_company)

        db.delete(id_employee) 

    with allure.step("Проверить, что появился 1 новый"):
        assert len_after - len_before == 1

    with allure.step("Проверка id нового сотрудника"):
        for employee in employee_company:
            if employee["id"] == id_employee:
                assert employee["firstName"] == first_name
                assert employee["lastName"] == last_name
                assert employee["middleName"] == middle_name
                assert employee["companyId"] == new_id
                assert employee["phone"] == phone
                assert employee["id"] == id_employee


@allure.title("Обращение к сотруднику по id")
@allure.description("Проверка данных у сотрудника по id")
@allure.feature("READ")
@allure.severity("blocker")
def test_get_one_employee():
    with allure.step("Создать компанию"):
        name = "РSkyPro_tester"
        descr = "Образовательные услуги"
        result = api.create_company(name, descr)
        new_id = result["id"]

    with allure.step("cоздаем сотрудника"):
        first_name = 'Яна'
        last_name = 'Заяц'
        middle_name = 'Руслановна'
        company_id = new_id
        email = 'tester@gmail.com'
        phone = '7(915)536-02-93'

        db.create(first_name, last_name, middle_name, company_id, email, phone)
        max_id = db.get_max_id()

    with allure.step("Получение сотрудника по id"):
        new_employee = api.employee_id(max_id)

    with allure.step("Удаление сотрудника по id"):
        db.delete(max_id)
