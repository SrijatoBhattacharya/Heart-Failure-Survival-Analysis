# Heart Failure Clinical Survival Analysis 🫀📊

### Clinical Objective
To determine if pre-existing diabetes significantly reduces the survival time of patients diagnosed with heart failure. This project utilizes Kaplan-Meier survival curves and Log-Rank statistical testing to analyze clinical trial data and validate the mortality impact of the diabetic cohort versus the non-diabetic cohort.

### The Dataset
The analysis was performed on a publicly available clinical dataset of 299 heart failure patients. 
**Key Features Analyzed:**
* `time`: Follow-up period (in days)
* `DEATH_EVENT`: Patient outcome (1 = deceased, 0 = survived/censored)
* `diabetes`: Binary indicator of pre-existing condition (1 = Diabetic, 0 = Non-Diabetic)

### Tech Stack
* **Language:** Python 3
* **Data Wrangling:** Pandas
* **Statistical Modeling:** Lifelines (`KaplanMeierFitter`, `logrank_test`)
* **Visualization:** Matplotlib

### Methodology & Results
The patient data was segmented into two cohorts based on diabetes status. A Kaplan-Meier estimator was fitted to both groups to visualize the probability of survival over a 250+ day period. 

To ensure mathematical rigor, a Log-Rank test was executed to determine if the visual divergence between the curves was statistically significant.

*(Note for Srijato: Drag and drop your `survival_curve.png` image file right here so it displays on your profile)*

**Conclusion:** The Log-Rank test returned a **P-value of 0.8405**. Because the p-value is significantly greater than the standard alpha threshold of 0.05, we conclude that there is **no statistically significant difference** in survival times between the diabetic and non-diabetic cohorts in this specific dataset. Pre-existing diabetes was not the primary driver of mortality for these heart failure patients.
