import streamlit as st
import pandas as pd

def main():
    st.title("Income and Expense Tracker")

    # Load existing data or create a new dataframe
    df = load_data()

    # Sidebar for user input
    with st.sidebar.form(key='my_form'):
        st.write("## Add Transaction")
        trans_type = st.radio("Transaction Type", ['Income', 'Expense'])
        amount = st.number_input("Amount", value=0.0)
        description = st.text_input("Description")
        submit_button = st.form_submit_button(label='Submit')

    # Add transaction to the dataframe
    if submit_button:
        add_transaction(df, trans_type, amount, description)
        st.success("Transaction added successfully!")

    # Display current balance
    st.write("## Current Balance")
    st.write(f"Balance: ${calculate_balance(df):,.2f}")

    # Display transaction history
    st.write("## Transaction History")
    st.table(df)

def load_data():
    # Try loading data from file, if not, create a new dataframe
    try:
        df = pd.read_csv('transactions.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Date', 'Type', 'Amount', 'Description'])
    return df

def add_transaction(df, trans_type, amount, description):
    # Add a new row to the dataframe
    new_row = {'Date': pd.Timestamp.now(), 'Type': trans_type, 'Amount': amount, 'Description': description}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # Save the updated dataframe to a file
    df.to_csv('transactions.csv', index=False)

def calculate_balance(df):
    # Calculate the balance based on income and expenses
    income = df[df['Type'] == 'Income']['Amount'].sum()
    expenses = df[df['Type'] == 'Expense']['Amount'].sum()
    balance = income - expenses
    return balance

if __name__ == '__main__':
    main()
