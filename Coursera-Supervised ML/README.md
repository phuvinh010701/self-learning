# Supervised Machine Learning: Regession and Classification

---

## Week1

Machine learning algorithms:

* Supervised learning:

    * Regession
    * Classification

* Unsupervised learning:

    * Clustering: group similar data points together
    * Anomaly detection: Find unusual data
    * Dimentionality reduction: Compress data

* Semisupervised learning
* Reinforce learning

### Linear Regession: 

- Fitting straight line to data
- Regression model predicts numbers (Classification model predicts categories)

Model: f_wb(X) = Wx + b
W, b: parameters, weights, coefficients

- Cost funtionc: (get it better) Mean squared error



### Logistic Regession

- Classification problems
- Logistic function: 1/ (1 + e**(-f_wb))
- Cost functionc: Cross entropy: −∑(i, k)= yi-log(zi)+(1−yi)log(1−zi)

### Gradient Descent:

Optimize loss
