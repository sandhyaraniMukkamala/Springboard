# Capstone Project II #

Kiva Loan Delay analysis
____________________________________________________________________________________________________________________________

## Goal: ##

Understand why there are delays between:

- "posted_time" - time when a loan is posted
- "funded_time" - time when a loan is 100% funded by lenders
- "disbursed_time" - time when a loan is disbursed by the field agent to the borrower

### Method: ###

There is a tendency to an increase on fund delay over time, since a loan is posted and until it is funded and disbursed. To analyize this problem, after making feature selection and engineering, treated this as a classification issue where a loan is either classfied as "high delay" or "low delay".

## Conclusion: ##

Reached 0.80 AUC and a 0.72 score on test dataset with a Random Forest Classifier. "total number of lenders", "amount of the loan", "the lender term" and "the currency policy" are the most relevant features that explain loan delays. When relating to the EDA made, we see that some features are more helpful to predict when a loan will be delayed more than the desirable time, others to when it will have a smaller delay. For instance, the the two most important ones (loan amount and total number of lenders), which are positively correlated, help the explainability of the model in the sense that they contribute to higher delayed loans. Or, for instance, if it is a loan for Paraguay. Any loan with a high value on these features will be a motive of concern from the start, in the sense that they are good indicators of a higher delay. On the other hand, if, for instance, the loan has a shared currency policy, or it belongs to the 'Personal Use' sector, or the partner id is nº136, there is a good chance that the loan will be funded "on time". Considerations must also be taken regarding the correlation between these important variables, before concluding if a loan with this or that feature may be problematic, as explained in the documentation.
