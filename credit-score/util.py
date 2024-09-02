import pandas as pd
from sklearn.impute import KNNImputer


class DataFrameTransformer:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.__number_columns = df.select_dtypes("number").columns
        self.__categorical_columns = df.select_dtypes("object").columns.drop(
            "Credit_Score"
        )

    @property
    def number_columns(self):
        return self.__number_columns

    def categorical_columns(self):
        return self.__categorical_columns

    def delete_col(self, cols):
        """
        Drops a specified column from the DataFrame and its associated index variable.
        """
        self.df.drop(columns=cols, inplace=True)

        for col in cols:
            if col in self.categorical_columns:
                self.categorical_columns = self.categorical_columns.drop(col)
            else:
                self.number_columns = self.number_columns.drop(col)

    def drop_redundant_columns(self):
        self.delete_col(["Name", "ID", "SSN"])

    def transform_dtypes(self):
        problem_columns_float = [
            "Annual_Income",
            "Changed_Credit_Limit",
            "Outstanding_Debt",
            "Total_EMI_per_month",
            "Amount_invested_monthly",
            "Monthly_Balance",
        ]
        problem_columns_int = ["Num_of_Loan", "Num_of_Delayed_Payment", "Age"]

        self.df[problem_columns_float] = self.df[problem_columns_float].apply(
            pd.to_numeric, errors="coerce"
        )
        self.df[problem_columns_float] = self.df[problem_columns_float].astype(
            "float64"
        )
        self.df.loc[:, problem_columns_float].fillna(
            value=self.df[problem_columns_float].median(),
            inplace=True,
        )
        self.df[problem_columns_int] = self.df[problem_columns_int].apply(
            pd.to_numeric, errors="coerce"
        )
        self.df[problem_columns_int] = self.df[problem_columns_int].astype(
            pd.Int32Dtype()
        )
        self.df.loc[:, problem_columns_int].fillna(
            value=self.df[problem_columns_int].median(), inplace=True
        )
        return self.df

    def throw_outliers(self):
        return self.df.drop(
            self.df[
                (self.df["Age"] < 0)
                | (self.df["Age"] > 100)
                | (self.df["Num_Bank_Accounts"] < 0)
                | (self.df["Num_of_Loan"] < 0)
                | (self.df["Num_of_Delayed_Payment"] < 0)
                | (self.df["Delay_from_due_date"] < 0)
            ].index
        )

    def transforming_columns(self):
        split_credit_history = self.df["Credit_History_Age"].str.extract(
            r"(\d+)\sYears\sand\s(\d+)\sMonths"
        )

        total_months = split_credit_history[0].astype(
            pd.Int32Dtype()
        ) * 12 + split_credit_history[1].astype(pd.Int32Dtype())

        self.df["Credit_History_Age"] = total_months

        loan_types = [
            "Not Specified",
            "Credit-Builder Loan",
            "Personal Loan",
            "Debt Consolidation Loan",
            "Student Loan",
            "Payday Loan",
            "Mortgage Loan",
            "Auto Loan",
            "Home Equity Loan",
        ]

        self.df["Type_of_Loan"].fillna("", inplace=True)
        for suffix in loan_types:
            self.df["Type_of_Loan_" + suffix] = self.df["Type_of_Loan"].apply(
                lambda x: suffix in x.split(", ")
            )

        self.delete_col(["Type_of_Loan"])
        self.number_columns = self.number_columns.drop("Credit_History_Age")
        self.number_columns = self.number_columns.append(
            pd.Index(["Credit_History_Age"])
        )

        self.df = pd.get_dummies(
            self.df,
            columns=[
                "Month",
                "Occupation",
                "Credit_Mix",
                "Payment_of_Min_Amount",
                "Payment_Behaviour",
            ],
            drop_first=True,
        )

    def apply_all(self):
        self.drop_redundant_columns()
        self.transform_dtypes()
        self.throw_outliers()
        self.transforming_columns()
        return self.df


class Credit_Dataset:
    def __init__(self, train, test):
        self.train = DataFrameTransformer(train).apply_all()
        self.test = DataFrameTransformer(test).apply_all()

    def impute_all(self, model=KNNImputer(n_neighbors=1)):

        if "Customer_ID" in self.train.columns:
            self.train.drop("Customer_ID")
        train_features = {
            "columns": self.train.columns,
            "index": self.train.index,
            "dtypes": self.train.dtypes.to_dict(),
        }
        test_features = {
            "columns": self.test.columns,
            "index": self.test.index,
            "dtypes": self.test.dtypes.to_dict(),
        }

        train_imputed = pd.DataFrame(
            model.fit_transform(self.train),
            columns=self.train.columns,
            index=self.train.index,
        ).astype(self.train.dtypes.to_dict())
        test_imputed = pd.DataFrame(
            model.transform(self.test), columns=self.test.columns, index=self.test.index
        ).astype(self.test.dtypes.to_dict())
        return train_imputed, test_imputed
