**🚀 CSV to PostgreSQL Pipeline with Airflow and Docker**
This project implements a scalable data pipeline that loads one or more CSV files into a PostgreSQL database using Apache Airflow. It uses csvsql to automatically generate SQL schemas from CSV headers, supports parallel processing, and runs entirely within Docker.

**✨ Features**
✅ Accepts multiple CSV files
✅ Auto-generates PostgreSQL schema with csvsql
✅ Loads data into PostgreSQL
✅ Parallel processing using Airflow
✅ Fully containerized with Docker and Docker Compose

**🛠 Technologies Used**
Apache Airflow – Workflow orchestration

PostgreSQL – Target relational database

csvsql (from csvkit) – Schema generation

Docker – Containerized runtime environment

**⚙️ Configuration**
The only required configuration is setting the CSV delimiter in the DAG file.

In dags/load_to_database.py, set:

delimiter = ','
You can change this to ';', '\t', or any other delimiter that matches your CSV files.

**📂 Project Structure**
.
├── airflow/                      # Airflow environment setup
│   ├── Dockerfile                # Custom Airflow Docker image
│   └── airflow.cfg               # Airflow configuration
│
├── dags/                         # DAG files
│   └── load_to_database.py       # Main DAG that processes CSV files
│
├── data/                         # Folder to place your CSV files
│   └── your_files.csv
│
├── docker-compose.yml            # Docker Compose setup
└── README.md

**▶️ Usage**
1. Add Your CSV Files
   Place one or more .csv files into the data/ folder.

2. Set Your Delimiter
   Open dags/load_to_database.py and adjust the delimiter variable if needed.

3. Build and Run the Pipeline
   In the root directory, run:
`docker-compose up --build
`
4. Access Airflow UI
   Navigate to http://localhost:8082

5. Trigger the DAG
   Run the load_to_database DAG to start processing your files.

**👤 Made By**
Abdelghafour AIT ADDI
📧 aitaddiabdelghafour@gmail.com

