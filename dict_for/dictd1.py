Employee = {
    "employee_id" : 102,
    "name" : "Dikshant",
    "course" : "data analytics"
}


for employee_data in Employee:
    print(f"employee_data = {employee_data}, type of employee_dat = {type(employee_data)}, keyvalue = {Employee.get(employee_data)}")

