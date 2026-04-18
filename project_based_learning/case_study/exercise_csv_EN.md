# Exercise: Employee Records Reconciliation

## Scenario

You work on the **Data Governance** team at *Industrie Digitali S.p.A.*, an Italian company with approximately 1,000 employees across several offices nationwide.

The company relies on three separate information systems, each managed by a different department, that maintain their own employee registry:

1. **sistema_hr.csv** — Export from the Human Resources management system, used by the HR office for contracts, onboarding, and organisational management.
2. **gestionale_paghe.csv** — Export from the payroll system, used by the Finance and Administration office for salaries and pay slips.
3. **anagrafica_aziendale.csv** — Export from the central company registry, used by General Management for reporting and internal communications.

Over time, due to manual data entry, migrations, and misalignment between departments, the three systems have become **out of sync**: not every employee appears in every file, and each system follows its own formatting conventions.

Management has asked you to perform a **full reconciliation** to understand the true state of the employee records.

---

## Objectives

### 1. Load the three files correctly
Each file uses a different format. Before any analysis you need to identify and handle differences in:
- delimiter (which character separates the columns?)
- date format
- salary format (decimals, rounding)
- name structure (one column or two? in what order?)
- employee ID (which prefix? which format?)
- language and style of column headers

### 2. Identify a linking key
The three files do not use the same employee ID. Find a field that is present in all three files and can serve as a **unique join key** to match records across them.

### 3. Build the complete registry
Starting from the three files, build a single DataFrame containing all 1,000 employees with no duplicates.

### 4. Find the discrepancies
Answer the following questions:

- How many employees appear in **all three** files?
- How many employees are **missing** from each file? Which ones?
- Are there employees present in **only one** of the three files?
- Are there employees present in **exactly two** files? If so, which combination?

### 5. Produce a summary report
Generate a clear output (table, DataFrame, or file) that shows, for each employee, which systems they appear in and which they are absent from.

---

## Hints

- Start by opening each file in a text editor (or with `head` in the terminal) to inspect the format **before** writing any code.
- The `pd.read_csv()` function accepts a `sep` parameter to specify the delimiter.
- Set operations (`set`, intersection, difference, union) are very useful for this kind of analysis.
- Think about which field is truly **unique and consistent** across all three files — not all of them are.
- Note: one of the files does not include a phone number. This is not a mistake; it is a characteristic of the source system.

---

## Deliverable

Produce a notebook (`.ipynb`) or a script (`.py`) that:

1. Loads the three files into three separate DataFrames.
2. Determines the linking key across the files.
3. Computes and prints the number of employees in each of the following categories:
   - present in all three files
   - missing from each file (with a list of names)
   - present in only one file
   - present in exactly two files
4. (Optional) Produces a final CSV file with the complete registry and a column indicating presence in each system (e.g. `in_hr`, `in_payroll`, `in_registry`).

Good luck!
