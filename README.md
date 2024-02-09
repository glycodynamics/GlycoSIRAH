# GlycoSIRAH
### This repository will have a collection of programs/scripts to run coarse grain MD simulation of Glycan or glycoproteins in AMBER

#### 1. Creating glycosidic linkages between monosaccharides in tleap
#### Overview:
find_linkages.py is a Python script designed to streamline the process of converting bond commands for the tleap tool, a component of the Amber Molecular Dynamics software suite. Specifically tailored for creating coarse-grain models of glycans derived from the Glycam format output on the Glycam web server, this script parses PDB files generated from the Glycam web server to extract link information marked by the "LINK" keyword. It then transforms this information into bond commands compatible with the SIRAH coarse-grain force field.

#### Features:
1. Create glycosylated protein or glycan in Glycam web server
2. Parses PDB files obtained from the Glycam web server ('Glycam web server'), focusing on lines marked with the "LINK" keyword.
3. Converts link information into tleap-compatible bond commands, facilitating the creation of coarse-grain glycan models using SIRAH.
4. Offers flexibility in specifying prefixes for glycoprotein and protein residues in the generated bond statements.
#### Usage:
Run the find_linkages.py script, providing the path to the PDB file as the first argument.

```
python3 find_linkages.py structure_AMBER.pdb string_prefix
```
```
Example output:
[sushil@idose 01.PREP]$ python3 find_linkages.py structure_AMBER.pdb mol
bond protein.149.BND protein.871.GNac
bond protein.871.GO4 protein.872.GNAc
bond protein.872.GO4 protein.873.GO2
bond protein.873.GO6 protein.874.GO2
bond protein.873.GO3 protein.881.GO2
bond protein.881.GO4 protein.885.GNAc
bond protein.881.GO4 protein.882.GNAc
bond protein.885.GO4 protein.886.GO2
bond protein.886.GO3 protein.887.GO2
bond protein.882.GO4 protein.883.GO2
bond protein.883.GO3 protein.884.GO2
bond protein.874.GO4 protein.875.GNAc
bond protein.874.GO4 protein.878.GNAc
bond protein.878.GO4 protein.879.GO2
bond protein.879.GO3 protein.880.GO2
bond protein.875.GO4 protein.876.GO2
bond protein.876.GO3 protein.877.GO2
```
Optionally, specify additional arguments for customizing prefixes:
The script will process the PDB file, extract link information, convert it into SIRAH-compatible bond commands, and print them to the console.
Copy and paste the generated bond commands into a tleap input file for further use in creating coarse-grain models with the SIRAH force field.

#### Dependencies:
Python 3.x

#### Contributing:
Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

Author:
**Sushil Mishra
**
