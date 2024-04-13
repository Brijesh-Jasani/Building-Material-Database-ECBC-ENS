import streamlit as st
import pandas as pd

st.set_page_config(

    layout="wide",  # or "centered"
    #initial_sidebar_state="expanded",  # or "collapsed"
)
# Load the Excel file
@st.cache_data
def load_data():
    df = pd.read_excel('U_Value_tool_BJ.xlsx')
    return df

# Load the data
df = load_data()

#Title and description
st.title('Building Material Thermal Properties Explorer: ECBC 2017 & ENS 2018 Database')
st.write("""
Welcome to the Building's Material Thermal Properties Explorer. This tool provides a comprehensive database of materials available in the Energy Conservation Building Code (ECBC) 2017 and Eco Niwas Samhita 2018 (ENS) documents. It is designed to assist engineers and architects in quickly finding material properties such as Density (kg/m³), Conductivity (k, W/(m·K)), Resistance (R, (m²·K)/W), and Specific Heat (kJ/(kg·K)).

By leveraging this tool, you can streamline your material selection process, optimize your designs, and make more informed decisions. Simply select the desired material from the dropdown menu to view its properties. Enjoy exploring!
""")

# Get the list of columns
c1 = df["Source"].unique()

#columns = df.columns.tolist()

# Create a multiselect widget for the columns
selected_columns_1 = st.multiselect('Select Data Source Type', c1, default = c1)
new_df = df[df['Source'].isin(selected_columns_1)]

c2 = new_df["Material type"].unique()
selected_columns_2 = st.multiselect('Select Material Type', c2, default = c2[-2])
new_df = new_df[new_df['Material type'].isin(selected_columns_2)]

st.write('Number of Results Based on Filters: ', new_df.shape[0])
st.write(new_df)

# Display the dataframe
#st.write(df)

st.markdown("""
## References

This tool uses data from the following sources:

- **ECBC 2017**: Energy Conservation Building Code 2017. For more details, please refer to the ECBC 2017 document. (https://beeindia.gov.in/sites/default/files/BEE_ECBC%202017.pdf)

- **ENS**: Eco Niwas Samhita 2018. For more details, please refer to the ENS document. (https://beeindia.gov.in/en/eco-niwas-samhita-ens)

I thanks the authors and organizations behind these resources for their valuable work.
""")
