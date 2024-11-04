# 🌟 WorkBrew - Cafe & Workspace Suggestion App 🍵💻

## 📚 About the Project
**WorkBrew** is a web application built using Django, Python, and PostgreSQL that allows users to explore and discover cafes and workspaces suitable for professionals. Users can browse through a list of venues, view details about them, and leave reviews based on their experiences.

## 🔑 Key Features
- **User Authentication** 🔑: Users can create accounts, log in, and manage their profiles.
- **Venue Listing** 🔍: Users can browse through a list of cafes and workspaces, view their details, and filter/search based on various criteria.
- **Venue Reviews** ✨: Authenticated users can leave reviews for the venues they have visited, including ratings, comments, and images.
- **Dashboard** 📊: Users can view their own reviews and manage their account settings.
- **Admin Panel** 🛠️: Administrators can manage the venues, reviews, and user accounts through a dedicated admin interface.

## 🛠️ Tech Stack
- **Backend**: Django (Python), PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Django built-in authentication system
- **Database**: PostgreSQL
- **Deployment**: Aiven, Render

## 🚀 Getting Started

### 📋 Prerequisites
- Python (version 3.x) 🐍
- PostgreSQL 🗃️
- pip (Python package manager) 📦
- virtualenv (optional but recommended) 🐳

### 📲 Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/workbrew.git
   ```
2. Create a virtual environment (optional but recommended):
   ```
   cd workbrew
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Set up the PostgreSQL database:
   - Create a new database
   - Update the `DATABASES` setting in the `settings.py` file with your database credentials
5. Run the database migrations:
   ```
   python manage.py migrate
   ```
6. Create a superuser account:
   ```
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```
   python manage.py runserver
   ```
   The application should now be accessible at `http://localhost:8000/`.

## 🤝 Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

1. Fork the repository 🍴
2. Create your feature branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Create a new Pull Request 🔃

## 📄 License
This project is licensed under the [MIT License](LICENSE.txt).

## 🙏 Acknowledgements
- [Django](https://www.djangoproject.com/) 🐍
- [PostgreSQL](https://www.postgresql.org/) 🗃️
- [Bootstrap](https://getbootstrap.com/) (or any other CSS framework of your choice) 💅
