# AgroSphere

AgroSphere is a web-based platform designed to link farmers and buyers, providing a collaborative space for the agricultural community. It offers features such as real-time chat, a news feed for product postings, reactions, comments, favorites, and easy sharing options.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction

AgroSphere is aimed at creating a seamless connection between farmers in rural areas and buyers in urban areas. The platform facilitates communication, product showcasing, and collaboration, fostering a stronger agricultural community.

## Features

1. **User Authentication:**

   - Users can create accounts with email, password, username, passport, and address.
   - Existing farmers can directly request links to buyers.
2. **Chat Functionality:**

   - Real-time group chat for farmers and buyers with shared interests.
   - Private messaging for one-on-one communication.
3. **News Feed:**

   - Farmers can post their products on the news feed.
   - Users can comment on and react to news feed items.
4. **Favorites:**

   - Users can add news feed items to their favorites.
5. **Sharing:**

   - Share icon for easy copying and sharing of news feed item URLs.

## Setup

To set up AgroSphere locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/agrosphere.git
   cd agrosphere

   ```
2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Apply migrations and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Run the development server:

   ```bash
   python manage.py runserver
   ```
5. Visit http://127.0.0.1:8000/newsfeed/news-feed/ in your web browser.

## Usage

1. Create a user account or log in.
2. Explore the chat, news feed, and other features.
3. Post products on the news feed and engage with the community.

## Technologies Used

- Django
- Django Channels
- Bootstrap
- Other relevant technologies...

## Contributing

We welcome contributions! Feel free to fork the repository, create issues, or submit pull requests. Follow our [Contribution Guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Sample Screenshots:**

[Include sample screenshots here, showcasing different features of your application.]
