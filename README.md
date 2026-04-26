# 📊 Hidden Data Corruption Detection System
 Overview
This project simulates a data replication system using nested data structures and demonstrates how improper copying (shallow copy) can lead to hidden data corruption. It uses Python along with NumPy and Pandas to analyze data, detect anomalies, and predict system stability.

 Objective
* Simulate structured multi-zone data
* Demonstrate corruption caused by shallow copy
* Analyze data using NumPy and Pandas
* Detect anomalies and clusters
* Predict system stability using a risk model

 Key Concepts
* Nested Data Structures (list + dictionary)
* Shallow Copy vs Deep Copy
* Data Corruption
* Risk Modeling
* Anomaly Detection
* Stability Analysis
* 
 Features
* User-driven data input
* Personalized dataset (based on roll number)
* Demonstration of hidden corruption
* DataFrame-based analysis
* Manual correlation calculation
* Anomaly and cluster detection
* Final system risk classification

 How to Run
1. Open terminal / command prompt
2. Navigate to project folder
3. Run the program:

Input Requirements
* Number of zones
* Roll number
* Metrics for each zone:
  * Traffic
  * Pollution
  * Energy
* 5 history values per zone

Output Includes
* BEFORE vs AFTER mutation (corruption proof)
* DataFrame view of dataset
* Risk scores for each zone
* Anomalies detected
* Cluster patterns
* Stability index
* Final system decision

Important Observation
Shallow copy does not duplicate nested structures, so modifying copied data also changes the original data, causing hidden corruption.

 Technologies Used
* Python
* NumPy
* Pandas
* Math & Copy modules

 Conclusion
This project successfully demonstrates how improper data copying can lead to hidden corruption and how analytical techniques can be used to detect and evaluate system risks effectively.


---
