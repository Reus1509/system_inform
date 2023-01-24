all_classes = {}
all_students = {}
id_student = 1

def create_student():
    surname = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    otch = input("Введите отчество ученика: ")
    birth = input("Введите дату рождения ученика: ")
    tel = input("Введите телефон ученика: ")
    adress = input("Введите адрес ученика: ")
    class_name = input("Введите номер класса ученика: ")
    global all_classes
    if class_name not in all_classes:
        create_cl(class_name)
    all_classes[class_name].append(id_student)
    st_data = [surname, name, otch, birth, tel, adress, class_name]
    global all_students
    all_students[id_student] = st_data
    global id_student
    id_student += 1

def create_cl(name_class=False):
    if not name_class:
        name_class = input("Введите номер класса: ")
    all_classes[name_class] = []

def edit_student():
    pass

def delete_student():
    pass

def change_class():
    pass