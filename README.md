

**Project Highlights:**

- **Data Exploration:** 🧹 Employed one-way ANOVA to identify features most relevant to rainfall prediction and utilized the IQR method to remove outliers, ensuring cleaner and more accurate data.
- **Feature Engineering:** 🛠️ Leveraged time series forecasting, and transformed date features into sine and cosine values for month and day to improve model performance. Utilized a column transformer to handle nearly 25 input columns effectively.
- **Model Development:** 🤖 Designed an artificial neural network (ANN) with a ReLU activation function, optimizing the model to deliver accurate rainfall predictions.

**Challenges Faced:**

- **Handling Complex Data:** 📊 With nearly 25 input columns, tracking and processing each feature was intricate. I employed a column transformer to manage this complexity and ensure smooth data input for the model.
- **Deployment Difficulties:** 🚀 Deploying the model posed its own set of challenges. I used Flask to deploy the model, which required careful handling of each input column and integration with the prediction system. The deployment process was a valuable learning experience, ensuring that the model could handle real-time inputs effectively.


