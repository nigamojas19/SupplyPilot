# AI-Driven-Supply-Chain-Analytics
An end-to-end supply chain analytics project for Super Mart, a fictional FMCG company. Raw order data is loaded into a Supabase (PostgreSQL) database with n8n workflow automation, then analysed in Quadratic, an AI-powered spreadsheet, using SQL and natural-language prompts to calculate delivery KPIs such as Line Fill Rate, Volume Fill Rate, On-Time (OT), In-Full (IF) and OTIF.

Built by following the codebasics tutorial. Setup notes, fixes and my own analysis are documented below.

Problem statement

Super Mart's supply chain team needs to know how well it fulfils customer orders. Order data arrives as files and is hard to analyse by hand. This project:

Automates getting the data into a database.
Makes it queryable with SQL.
Uses AI-assisted analysis to calculate the key service-level KPIs and surface insights.
Tech stack
Tool	Role
n8n	Workflow automation: extracts the data files and loads them into PostgreSQL
Supabase (PostgreSQL)	Cloud database that stores dimension and fact tables
Quadratic	AI spreadsheet that connects to Postgres, runs SQL and builds KPIs/charts
SQL / Python	Querying and calculations inside Quadratic
Architecture
Data files (CSV / Excel)
        │
        ▼
   n8n workflow  ──►  Supabase (PostgreSQL)  ──►  Quadratic (SQL + AI prompts)
 (extract & load)      (session pooler)            KPIs, charts, insights
Database schema
Table	Description
dim_customers	Customer details
dim_products	Product details
dim_target_orders	Target on-time / in-full / OTIF percentages per customer
fact_order_line	Order-line level data (ordered vs delivered quantities, dates)
fact_orders_aggregate	Order-level data with on_time, in_full and otif flags
KPIs calculated
KPI	Meaning
Line Fill Rate (LIFR)	Share of order lines delivered in full
Volume Fill Rate (VOFR)	Delivered quantity as a share of ordered quantity
On-Time (OT) %	Share of orders delivered on or before the agreed date
In-Full (IF) %	Share of orders delivered with the complete quantity
OTIF %	Share of orders that were both on time and in full

# Setup
1. Supabase
Create a project at supabase.com.
Create the tables and import the CSV files (Table Editor → Import data).
Click Connect and copy the Session pooler credentials (host, port, database, user, password).
2. n8n
Install Node.js LTS (v22 or v24), then run npm install -g n8n, or use Docker.
Start with n8n and open http://localhost:5678.
Add a Postgres credential using the Supabase session pooler details.
Build or import the workflow that extracts the files and inserts them into Supabase.
3. Quadratic
Create a new file at quadratic.ai.
Go to Connections → Add connection → Postgres and use the same Supabase credentials.
Insert a Postgres cell (press / in a cell) and write SQL.

# Challenges and fixes
Problem	Cause	Fix
npm install -g n8n failed with a node-gyp / Visual Studio error	Node.js v26 is too new, so a dependency had no prebuilt binary	Installed Node.js LTS and removed the half-installed n8n folder
CSV import failed with date/time field value out of range: "13-03-2025"	Dates were DD-MM-YYYY, but Postgres expects MM-DD-YYYY by default	Converted dates to YYYY-MM-DD with pandas before importing (or imported as text and converted with to_date(col, 'DD-MM-YYYY'))
Supabase direct connection could not be reached	The direct connection is IPv6-only on the free plan	Used the Session pooler connection string

# Key insights
Total Order Lines	25,777
Line Fill Rate	65.99%
Volume Fill Rate	96.62%
Total Orders	13,595
On Time Delivery %	59.23%
In Full Delivery %	52.61%
On Time In Full %	28.75%
# Screenshots
<img width="1877" height="1042" alt="image" src="https://github.com/user-attachments/assets/1ce7f243-6319-496d-b013-cd15244aa9bc" />

Supabase:
<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/fbf9bbda-dd03-495b-b285-9bdf48a6f6a9" />

<img width="1600" height="950" alt="image" src="https://github.com/user-attachments/assets/ef105561-c1bd-4fb0-b44a-9331e606394e" />

Insights:
<img width="1124" height="344" alt="image" src="https://github.com/user-attachments/assets/04be6280-7942-4651-b06b-2b2c9a6074c8" />

n8n workflow Supabase tables Quadratic dashboard

Repository structure
├── README.md
├── images/                 # screenshots used in this README
├── n8n/
│   └── workflow.json       # exported n8n workflow (credentials removed)
└── sql/
    └── queries.sql         # SQL prompts and equivalent queries used in Quadratic

# Data and credits
Tutorial and dataset: codebasics
The dataset is provided by codebasics for learning only. It is not included in this repository.
