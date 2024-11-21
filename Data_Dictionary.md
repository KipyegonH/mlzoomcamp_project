# Data Dictionary

This document describes the features in the dataset **Default of Credit Card Clients**.

| **Column Name**              | **Type**   | **Description**                                                              | **Notes**                               |
|------------------------------|------------|------------------------------------------------------------------------------|----------------------------------------|
| `ID`                         | Integer    | Unique identifier for each client.                                           | Dropped during preprocessing.          |
| `LIMIT_BAL`                  | Numeric    | Amount of given credit (NT dollar).                                          | Includes individual and family credit. |
| `SEX`                        | Categorical| Gender of the client (`1` = male, `2` = female).                             | Mapped to `male` and `female`.         |
| `EDUCATION`                  | Categorical| Client's education level (`1` = graduate, `2` = university, etc.).           | Mapped to descriptive labels.          |
| `MARRIAGE`                   | Categorical| Marital status (`1` = married, `2` = single, etc.).                          | Mapped to descriptive labels.          |
| `AGE`                        | Numeric    | Client's age in years.                                                       | -                                      |
| `PAY_0` to `PAY_6`           | Categorical| Repayment status in months (e.g., `-1` = paid in full, `1` = payment delay). | Renamed to `PAY_1` to `PAY_6`.         |
| `BILL_AMT1` to `BILL_AMT6`   | Numeric    | Bill statement amount (NT dollar) for the past six months.                   | -                                      |
| `PAY_AMT1` to `PAY_AMT6`     | Numeric    | Amount paid (NT dollar) in the past six months.                              | -                                      |
| `default_payment`            | Categorical| Default payment indicator (`0` = no default, `1` = default).                 | Target variable.                       |

### Notes:
- Categorical variables were encoded for modeling purposes.
- Irrelevant or redundant columns, such as `ID`, were dropped during preprocessing and column with romans numbers dropped from the raw data first.
- Column `default payment next month` was renamed to `default_payment`.

For further details about the dataset, refer to the [UCI repository description](https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip).
