## Kaggle Description

Nothing ruins the thrill of buying a brand new car more quickly than seeing your new insurance bill. The sting’s even more painful when you know you’re a good driver. It doesn’t seem fair that you have to pay so much if you’ve been cautious on the road for years.

Porto Seguro, one of Brazil’s largest auto and homeowner insurance companies, completely agrees. Inaccuracies in car insurance company’s claim predictions raise the cost of insurance for good drivers and reduce the price for bad ones.

**In this competition, you’re challenged to build a model that predicts the probability that a driver will initiate an auto insurance claim in the next year.** While Porto Seguro has used machine learning for the past 20 years, they’re looking to Kaggle’s machine learning community to explore new, more powerful methods. A more accurate prediction will allow them to further tailor their prices, and hopefully make auto insurance coverage more accessible to more drivers.

Download data from here:
https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/data


## Data Description

Data Description

In this competition, you will predict the probability that an auto insurance policy holder files a claim.

In the train and test data, features that belong to similar groupings are tagged as such in the feature names (e.g., ind, reg, car, calc). In addition, feature names include the postfix bin to indicate binary features and cat to indicate categorical features. Features without these designations are either continuous or ordinal. Values of -1 indicate that the feature was missing from the observation. The target columns signifies whether or not a claim was filed for that policy holder.
File descriptions

    train.csv contains the training data, where each row corresponds to a policy holder, and the target columns signifies that a claim was filed.
    test.csv contains the test data.
    sample_submission.csv is submission file showing the correct format.

	
**This was my first Kaggle competition and I was able to get my leaderboard score 0.26418 (Highest was 0.29698).**