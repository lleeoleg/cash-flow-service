# Django CashFlow Manager

Веб-приложение для управления движением денежных средств с удобным интерфейсом, фильтрацией по категориям, типам и статусам, а также CRUD-операциями для справочников и записей.

---

##  Функциональность

- Добавление, редактирование и удаление записей ДДС
- Справочники: Типы, Категории, Подкатегории, Статусы
- AJAX-загрузка категорий и подкатегорий
- Валидация данных на клиенте и сервере
- Интерфейс на Bootstrap 5
- Панель управления всеми справочниками и ДДС

---

## Запуск проекта

### Установка зависимостей

git clone https://github.com/lleeoleg/cash-flow-service.git
cd cash-flow-service
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate для Windows
pip install -r requirements.txt

база данных уже включена в проект;
она находится в корне проекта (db.sqlite3);
её не нужно создавать с нуля — просто использовать.
### Доступ администратора

- Логин: `admin`
- Пароль: `admin`

Скрины проекта: 
<img width="1438" height="708" alt="Снимок экрана 2025-07-25 в 22 47 44" src="https://github.com/user-attachments/assets/4d20019a-7335-42a4-a3b0-85998a7eba8b" />
<img width="1435" height="771" alt="Снимок экрана 2025-07-25 в 22 48 19" src="https://github.com/user-attachments/assets/5c4483b8-1b53-43aa-8cfe-4a11734c768f" />
<img width="1440" height="547" alt="Снимок экрана 2025-07-25 в 22 48 50" src="https://github.com/user-attachments/assets/0f6bc685-c519-4c6b-bd0e-0d08801402cf" />
<img width="1437" height="800" alt="Снимок экрана 2025-07-25 в 22 48 36" src="https://github.com/user-attachments/assets/604aeeda-d223-427b-acc5-5f3dd4e0ed00" />
<img width="1433" height="432" alt="Снимок экрана 2025-07-25 в 23 10 05" src="https://github.com/user-attachments/assets/d8029c7c-3516-4ff7-b2dc-b72d74a7984f" />




