import pandas as pd
import sys

def read_links_from_glycan(pdb_file):
    """
    Read the PDB file and extract the lines starting with "LINK".

    Args:
    - pdb_file (str): Path to the PDB file.

    Returns:
    - pd.DataFrame: DataFrame containing the relevant data from the PDB file.
    """
    link_lines = []
    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith("LINK"):
                link_lines.append(line.strip().split())

    amber_df = pd.DataFrame(link_lines, columns=["Record", "Atom1", "Residue1", "Res_num1", "Atom2", "Residue2", "Res_num2"])
    return amber_df

def amber_to_sirah(amber_df):
    """
    Convert the given DataFrame from AMBER format to SIRAH format based on specific conditions.

    Args:
    - glycam_df (pd.DataFrame): DataFrame containing the data to be modified.

    Returns:
    - pd.DataFrame: Modified DataFrame.
    """
    sirah_df = amber_df.copy()
    for index, row in sirah_df.iterrows():
        if row['Residue1'] == "ASN" and row['Atom1'] == "ND2":
            sirah_df.at[index, 'Atom1'] = "BND"
            sirah_df.at[index, 'Atom2'] = "GNac"
        elif row['Residue2'] == "ASN" and row['Atom2'] == "ND2":
            sirah_df.at[index, 'Atom2'] = "BND"
            sirah_df.at[index, 'Atom1'] = "GNac"

        elif row['Residue1'] == "4YB" and row['Atom1'] == "C1":
            sirah_df.at[index, 'Atom2'] = "GO4"
            sirah_df.at[index, 'Atom1'] = "GNAc"
        elif row['Residue2'] == "4YB" and row['Atom2'] == "C1":
            sirah_df.at[index, 'Atom1'] = "GO4"
            sirah_df.at[index, 'Atom2'] = "GNAc"


        elif row['Atom2'] == "C1" or "C2":
            sirah_df.at[index, 'Atom2'] = "GO2"
            sirah_df.at[index, 'Atom1'] = "G" + sirah_df.at[index, 'Atom1']
        elif row['Atom1'] == "C1" or "C2":
            sirah_df.at[index, 'Atom1'] = "GO2"
            sirah_df.at[index, 'Atom2'] = "G" + sirah_df.at[index, 'Atom2']



    return sirah_df

def print_sirah_df(sirah_df, protein_str):
    """
    Convert the given DataFrame from AMBER format to SIRAH format based on specific conditions.

    Args:
    - glycam_df (pd.DataFrame): DataFrame containing the data to be modified.

    Returns:
    - pd.DataFrame: Modified DataFrame.
    """
    for index, row in sirah_df.iterrows():
        print(f"bond {protein_str}.{row['Res_num1']}.{row['Atom1']} {protein_str}.{row['Res_num2']}.{row['Atom2']}")

# Example usage:
if __name__ == "__main__":
    pdb_file = sys.argv[1]
    glycoprot_str = sys.argv[2] if len(sys.argv) > 2 else "glycoprot"  # Default value is "glycoprot"
    protein_str = sys.argv[3] if len(sys.argv) > 3 else "protein"  # Default value is "protein"
    
    amber_df = read_links_from_glycan(pdb_file)
    sirah_df = amber_to_sirah(amber_df)
    print_sirah_df(sirah_df, protein_str)
