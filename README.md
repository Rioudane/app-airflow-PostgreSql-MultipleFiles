# 📊 CSV to MySQL ETL Pipeline with Airflow & Docker (Dynamic CSV Support)

This project builds a fully automated ETL pipeline using **Apache Airflow**, **Docker**, and **MySQL**.

🔥 It automatically:
- Detects a single `.csv` file inside the `data/` folder (mounted via Docker)
- Derives the MySQL table name from the CSV file name (e.g., `medical_records.csv` → `medical_records`)
- Generates the SQL schema using `csvkit`
- Creates the table in MySQL
- Loads the data using `pandas`

---

## 🧱 Tech Stack

- 🌀 Apache Airflow (workflow orchestration)
- 🐬 MySQL 8.0 (relational database)
- 🐳 Docker & Docker Compose (containerization)
- 📦 csvkit (`csvsql` for schema generation)
- 🐼 pandas (CSV ingestion)

---

## 📁 Folder Structure

.
├── airflow/
│ └── Dockerfile # Custom Airflow image with csvkit
├── dags/
│ └── csv_to_mysql_dag.py # The Airflow DAG
├── data/
│ └── your_file.csv # Put your CSV here!
├── docker-compose.yml
├── plugins/
├── logs/
└── README.md

---

## ⚙️ How It Works

1. **Dynamic Detection**  
   The DAG scans `/opt/airflow/data/` for the first `.csv` file it finds.

2. **Table Name Derivation**  
   The table name is extracted from the CSV filename (e.g., `sales_data.csv` → `sales_data`).

3. **Schema Generation**  
   `csvsql` converts the CSV file into a `CREATE TABLE` SQL script.

4. **Table Creation**  
   MySQLHook executes the schema and creates the table.

5. **Data Loading**  
   `pandas.read_csv()` reads the CSV and loads it into MySQL using SQLAlchemy.

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/your-username/csv-to-mysql-airflow.git
cd csv-to-mysql-airflow
2. Add your CSV
Put a single .csv file into the data/ directory.
Example: data/medical_records.csv

3. Start Docker Compose

docker-compose up --build
Airflow UI: http://localhost:8081
Login: admin / admin

▶️ Trigger the DAG
Open Airflow UI

Locate the DAG: csv_to_mysql_dag

Click ▶️ "Trigger DAG"

View execution via Graph View

🧪 Example Query
After the DAG completes, connect to MySQL:

docker exec -it Mysql_container mysql -uroot -proot -e "USE data_ingestion; SHOW TABLES;"
You should see your table named after the CSV file.

💡 Limitations
🚫 Only one .csv file should be placed inside the data/ folder.

🚫 Does not support file validation or schema conflict detection (can be added later).

👨‍💻 Author
Made by ABDELGHAFOUR AIT ADDI 
Email: aitaddiabdelghafour@gmail.com
