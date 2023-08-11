import streamlit as st
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd
import matplotlib.pyplot as plt
import io

# Function to calculate GC fraction for a sequence
def calculate_gc_fraction(sequence):
    return gc_fraction(sequence)

st.title("GC Fraction")
st.subheader("This displays the GC fraction of each sequence in the FASTA file")

# Upload FASTA file
uploaded_file = st.file_uploader("Upload a FASTA file", type=["fasta"])

if uploaded_file is not None:
    # Read the uploaded FASTA file
    fasta_data = uploaded_file.read()
    fasta_io = io.StringIO(fasta_data.decode("utf-8"))
    records = list(SeqIO.parse(fasta_io, "fasta"))

    # Calculate GC fraction
    gc_fractions = [calculate_gc_fraction(record.seq) for record in records]

    # Create a DataFrame for displaying GC fractions
    data = {'Sequence ID': [record.id for record in records],
            'GC Fraction': gc_fractions}
    df = pd.DataFrame(data)

    # Display GC fractions as a table
    st.write("GC Fractions:")
    st.dataframe(df)

    # Display GC fractions as a bar chart
    plt.bar(df['Sequence ID'], df['GC Fraction'])
    plt.xlabel('Sequence ID')
    plt.ylabel('GC Fraction')
    plt.xticks(rotation=45, ha="right")
    st.pyplot(plt)
