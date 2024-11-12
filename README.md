# invoiceapi

## Features
  #### Post and PUT operations for invoice and invoice details using a single endpoint
  #### API documentation
## Technologies Used
#### Django
#### Django REST Framework
#### Python
## Prerequisites
#### Python 3.x
#### pip (Python package installer)

## Setup Instructions
#### 1. Clone the Repository
`git clone https://github.com/rahulmakhijasg8/invoiceapi.git`

`cd invoiceapi(project-directory)`

#### 2. Create a Virtual Environment
`python -m venv venv`

`venv\Scripts\activate` (for windows)

`source venv/bin/activate` (for macos)

#### 3. Install Dependencies
`pip install -r requirements.txt`

#### 4. Run Migrations
`python manage.py makemigrations`

`python manage.py migrate`

#### 5. Create a Superuser (Optional)
To access the Django admin interface, create a superuser:
`python manage.py createsuperuser`

#### 6. Run the Development Server
`python manage.py runserver`

Open your browser and navigate to http://127.0.0.1:8000/api/invoices to access the API metods.

#### API Endpoints
    GET /api/invoices/ - Lists all the invoices along with all the invoice details.
    POST /api/invoices/ - Create a new invoice along with invoice details using the json format described in the assignment file
    PUT /api/invoices/{invoice_id} - Updates invoice or invoice details or both of the objects corresponding the invoice_id


