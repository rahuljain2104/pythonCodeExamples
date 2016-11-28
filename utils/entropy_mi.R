# this file calculates and return entropy/mutual information for the variables

# install.packages("entropy")


#setwd("D:\\codes\\datasets\\kaggle\\Titanic")
#
#train <- read.csv('train.csv')
#x = train$Survived
#y = train$Sex
#z = train$Pclass

# head(train)
# str(train)

check <- function(x) {
    if (x > 0) {
        result <- "Positive"
    }
    if (x < 0) {
        result <- "Negative"
    }

    return(result)
}
