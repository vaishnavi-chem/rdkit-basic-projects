from rdkit import Chem
smiles_list=["CCO", "CC(=O)O", "CC(=O)OC"]
patterns={
    "OH (alcohol)":
Chem.MolFromSmarts("[OX2H][CX4]"),
    "COOH (acid)":
Chem.MolFromSmarts("C(=O)[OX2H]"),
    "C=O (carbonyl)":
Chem.MolFromSmarts("C(=O)")    
}
for smi in smiles_list:
    mol=Chem.MolFromSmiles(smi)
    print("\nSMILES:", smi)
    for name, pattern in patterns.items():
        matches=mol.GetSubstructMatches(pattern)
        count=len(matches)
        print(f"{name}:",count)
