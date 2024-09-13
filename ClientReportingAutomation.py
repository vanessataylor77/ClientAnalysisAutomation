import pandas as pd

# Sample client data
client_data = {
    'Client_ID': [1, 2, 3],
    'Investment_Amount': [100000, 250000, 150000],
    'Income': [5000, 12500, 7500],
    'AUM': [105000, 260000, 157500]
}

df_clients = pd.DataFrame(client_data)

def generate_client_report(df):
    """
    Generate and export a client investment report.
    """
    report = df.copy()

    # Calculate yield
    report['Yield'] = (report['Income'] / report['Investment_Amount']) * 100

    # Export to CSV
    report.to_csv('client_report.csv', index=False)
    print("Client Report Generated:\n", report)

# Run the client reporting function
generate_client_report(df_clients)
