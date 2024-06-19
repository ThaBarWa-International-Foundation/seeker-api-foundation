## Seeker API Foundation

This project serves as the foundation for building APIs used within the Seeker collection of tools. These tools aim to empower curious individuals to accelerate their learning by harnessing and integrating technological advancements.

### Features

* **Flask Framework:** Leverages the lightweight and flexible Flask framework for building RESTful APIs.
* **Modular Design:** Encourages modularity, allowing for easier development and maintenance of API functionalities.
* **Testing Framework:** Includes testing capabilities using `pytest` for ensuring code quality and reliability.

### Installation

**Prerequisites:**

* Python 3.12 or later ([https://www.python.org/downloads/](https://www.python.org/downloads/))

**Using Poetry:**

1. Create a virtual environment using Poetry:

   ```bash
   poetry init
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

### Usage

**Running the Development Server:**

1. Start the development server:

   ```bash
   poetry run flask run
   ```

   This will typically launch the server at `http://127.0.0.1:5000/`. You can access the API endpoints from this address using tools like Postman or curl.

**Testing:**

To run the test suite:

```bash
poetry run pytest
```

This will execute unit tests to ensure the API functions as expected.

### Contributing

We welcome contributions to this project! Please refer to the following resources for guidelines and instructions:

* **Contribution Guidelines:** (**To be added** - Create a separate file outlining contribution guidelines)
* **Issue Tracker:** (**To be added** - Provide a link to your issue tracker, like GitHub Issues)

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Inspiration

This project is inspired by the official Flask tutorial: [https://palletsprojects.com/p/flask/](https://palletsprojects.com/p/flask/)
