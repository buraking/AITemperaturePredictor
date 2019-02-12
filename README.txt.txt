Beijing temperature predictor AI 
 
 
Introduction 
 
Due to the massive climate changes happening, i’ve decided to work on an AI that is to predict the temperature based on two different datasets going from 2010 all the way up to 2015. 
The data contains detailed information on the overall weather changes on hourly basis. 
 
Problem definition 
 
As for now the data contained the information needed up until december 31 2015. 
In order to predict the temperature within at least 6 months i will be using two different machine learning models. 
Then based on the results and scores from each model, i will have to determine which is best for the given data. 
Since the data most likely isn’t perfect, certain cleaning strategies and filtering will be needed to enhance the AI to its full potential. 
 
 
The data 
 
The data are split into two different datasets. 
One being from the year of 2010-2014 and another being from 2010-2015, but more detailed and more insignificant factors. 
The first thing i did to handle the data was to get rid of “NaN” values and replace them with a numerical value based on the average. I then shaped the data, to get a better and more structured understanding on the data within the dataset. 
Another thing worth doing, was having different visualization of the data, this could be a histogram of the different columns to show when the data within the different columns is mostly apparent.  Afterwards i ran a check on which columns was telling a lot about the temperature in Beijing. This helped me filter out and narrow the data that i would want my AI to work with. I came to the conclusion the 6 features i wanted to work with was: “year”, “month”, “hour”, “DEWP (Dew point)” and “HUMI (Humidity)”.  
 
Linear regression 
 
Since the dataset was informed to be used for regression it only seemed obvious to at least try this model out.  
In order to validate the model, i split the data into a training set and a test, to have the AI first work on the training set and then afterwards working with the actual test set. I then ran the regression method, and checked on certain error levels and general score by the AI. At first the score was rather low, down to 0.72 i then decided to find a second dataset with more details and ran the AI again. The score now increased 0.95. Which is a good enough score to start working on future outcomes. 
After polishing the AI i tested if it could predict 6 month ahead of the last given data. 
On June 11 2016 the AI predicted a temperature of 31 degrees Celsius. This is one degree, compared to the actual result. 
 
Decision Tree 
 
Even though that the Linear Regression model had a satisfying performance, both in prediction score and actual prediction on unknown data, i still needed a secondary model to compare with. 
I decided to go with a Decision Tree instead. 
Up until using the actual regression method for Decision Tree i pretty much did the same procedure as with Linear Regression.  
When it comes to Decision Tree i made forest of 4 different trees for the AI to train with. 
After having checked the AI with the training and the test data i ran a check to see how well it did. 
The best score the decision tree was able to put out was 0.93, which is good enough, for testing future outcomes.  
I therefore tried to see how well it predicted the temperature the same date as in Linear Regression. 
The result ended up being 30 degrees Celsius at best, which was actually correct and 27 degrees Celsius at worst.  
 
 
Conclusion 
 
After running the two different Machine Learning techniques we see that both are pretty much equally suited for to calculate this task, with a slight edge to the Linear Regression model. 
However if a more complicated output is expected, the Linear Regression model might not be the right one for the job. 
Another possibility is to using deep learning for this, but the dataset used for this task, most likely wasn’t fitting enough to uphold the requirements. 
However a world wide dataset with a similar, but significantly more detailed data is available. 
This could be used to solve the same task, and even more difficult tasks of equal relevance. 