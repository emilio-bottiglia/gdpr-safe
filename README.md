# gdpr-safe
This app begins running a series of dedicated file scanners—one for DOC files, one for PDF files, one for CSV files, one for XLSX files, and one for TXT files. Each scanner processes its own file type independently, displaying a progress bar as it searches through every matching file and extracts text to look for predefined keywords. As each scanner completes its work, the app logs the file paths and any detected keywords into a single report.csv, which the admin is instructed to retrieve when all scanning is finished.

I originally built this application in 2018 as part of my 4th‑year college project towards a degree BSc (Hons) in Digital Forensics and Cyber Security at the Institute of Technology Blanchardstown (now TUD), where the project—“GDPR: A Technical Evaluation for Determining an Adequate Level of Protection”—focused on GDPR compliance.
Below are some images showing app flowchart, this app in action and a sample report.
<img width="603" height="730" alt="flowchart" src="https://github.com/user-attachments/assets/3b01c69c-a6f6-4a91-95da-30f6cae1b687" />


<img width="1890" height="912" alt="scanner" src="https://github.com/user-attachments/assets/900f041a-9802-4ad1-99da-408ef92f639b" />


<img width="1229" height="419" alt="csv_rep" src="https://github.com/user-attachments/assets/81c97f1b-027a-4a1c-81d6-872ef1c50f6e" />
