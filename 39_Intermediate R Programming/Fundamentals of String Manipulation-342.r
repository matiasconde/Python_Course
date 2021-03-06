## 1. Working With Strings ##

library(readr)
scores <- read_csv("scores.csv")

## 2. Subsetting Strings by Position ##

match_month <- str_sub(scores$match_date, -4,-1)

## 3. Splitting Strings ##

match_matrix <- str_split(scores$match_date, " ", simplify = TRUE)

scores <- scores%>%
    mutate(match_month = match_matrix[,2])

## 4. Calculating Average Goals Per Month ##

total_goals <- scores$home_goals + scores$away_goals

scores <- scores %>%
    mutate(total_goals = total_goals)

avg_monthly_goals <- scores %>%
    group_by(match_month) %>%
    summarize(mean(total_goals))

## 5. Combining Strings ##

lose_country <- if_else(scores$win_country == scores$home_country, scores$away_country, scores$home_country)

scores <- scores %>%
    mutate(lose_country = lose_country)

team_results <- str_c(scores$win_country, scores$lose_country, sep = " beat ")

## 6. String Manipulations for Reformatting Match Dates ##

match_matrix <- str_split(scores$match_date, " ", simplify = TRUE)

match_day <- match_matrix[,1]


## 7. Padding Strings ##

match_matrix <- str_split(scores$match_date, " ", simplify = TRUE)
match_day <- match_matrix[,1]

match_day <- str_pad(match_day, 2, side = "left", pad = "0")

scores <- scores %>%
    mutate(match_day = match_day)

match_day_length <- str_length(match_day)

## 8. Creating New Variables ##

win_goals <- if_else(scores$win_country == scores$home_country, scores$home_goals, scores$away_goals)

lose_goals <- if_else(scores$win_country == scores$home_country, scores$away_goals, scores$home_goals)

scores <- scores %>%
    mutate(win_goals = win_goals, lose_goals = lose_goals)


## 9. Combining Strings to Create Match Summaries ##

match_summary <- str_c(scores$win_country, "beat", scores$lose_country, "on", scores$match_month, scores$match_day, "2014 with scores of", scores$win_goals, "to", scores$lose_goals, sep=" ") 

