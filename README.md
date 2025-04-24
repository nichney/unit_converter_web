# Unit Converter Web

A web-based unit conversion application. This project allows users to easily convert between various units of measurement through a user-friendly interface.

https://roadmap.sh/projects/unit-converter

## Features

- **Responsive Design**: The application is designed to work seamlessly on both desktop and mobile devices.
- **Unit Categories**: Supports conversions for:
  - Length
  - Weight
  - Temperature
  - Volume
- **Dynamic Backend**: Powered by Python for accurate calculations and scalability.
- **Clean UI**: Styled with CSS for a modern and intuitive user experience.

## How to Run Locally

   ```bash
   git clone https://github.com/nichney/unit_converter_web.git
   cd unit_converter_web
   pipenv shell
   pip install -r requirements.txt
   uvicorn app:app --reload --bind 0.0.0.0 --port 8080
   ```
