In this project, we made a project similar to the medium site, where we can add our blog posts, add sections such as tags and categories, and filter them according to these sections. Additional sections such as user login, login and registration have been added.and we made a request where we can edit the user profile

Can be edited locally with 127.0.0.1/admin
## Usage

**Preferably use `virtualenv`:**

```bash
# Create a virtual environment
virtualenv medium_clone_vnv

# Activate the virtual environment
todo_vnv\Scripts\activate
pip install -r requirements.txt
# Apply the migrations to the database 
py manage.py migrate 
py manage.py createsuperuser # Follow the prompts to add an admin user
py manage.py makemigrations
py manage.py migrate
py manage.py runserver   		
```
![Ekran görüntüsü 2024-08-07 134826](https://github.com/user-attachments/assets/7954f18e-cabc-436c-99f9-f2155936bf26)
![Ekran görüntüsü 2024-08-07 134902](https://github.com/user-attachments/assets/f7916578-44c0-4fd0-b857-40ac542a1951)
![Ekran görüntüsü 2024-08-07 134844](https://github.com/user-attachments/assets/c4d66d38-0573-4a75-8864-db66e41894f5)
![Ekran görüntüsü 2024-08-07 134819](https://github.com/user-attachments/assets/e8177150-c07a-4e48-a0ce-2f036effb068)
![Ekran görüntüsü 2024-08-07 135329](https://github.com/user-attachments/assets/d7d82627-9feb-43cd-b380-2f7039895cab)
![Ekran görüntüsü 2024-08-07 135319](https://github.com/user-attachments/assets/1abc66cf-a7b3-4e64-896b-4495fa099382)
![Ekran görüntüsü 2024-08-07 135501](https://github.com/user-attachments/assets/cafe112b-2ac8-465b-9d61-6a135f5a0e85)
![Ekran görüntüsü 2024-08-07 135448](https://github.com/user-attachments/assets/1e380717-4839-4383-9711-5dc12f31a91b)
![Ekran görüntüsü 2024-08-07 135436](https://github.com/user-attachments/assets/2923a1de-cf8e-4193-84fa-15dd545b0323)
![Ekran görüntüsü 2024-08-07 135350](https://github.com/user-attachments/assets/6d0aa70e-307e-4095-8a3e-058831ea267a)
![Ekran görüntüsü 2024-08-07 135338](https://github.com/user-attachments/assets/a23b8707-7164-4e2e-aaef-8231316d2a4a)
