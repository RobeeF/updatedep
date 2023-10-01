import re

# Le nom de la branche cible (par exemple, "staging")
origin_branch = "develop"
target_branch = "staging"

# Translate: Path to your requirements.txt file
requirements_file = "requirements.txt"

# Check that the dependencies to update are in the right organization 
orgname = 'blaorg'
pattern = re.compile('git\+ssh://git@github.com/' + orgname)

# Fonction pour mettre à jour la ligne de dépendance
def update_dependency(dependency_line):
    return re.sub('@' + origin_branch, '@' + target_branch, dependency_line)

# Ouvrir le fichier requirements.txt en mode lecture
with open(requirements_file, 'r') as f:
    lines = f.readlines()

# Ouvrir le fichier requirements.txt en mode écriture
with open(requirements_file, 'w') as f:
    for line in lines:
        # Rechercher des correspondances avec le pattern
        match = pattern.search(line)
        if match:
            # Mettre à jour la ligne de dépendance
            new_line = update_dependency(line)
            f.write(new_line)
        else:
            # Écrire la ligne telle quelle
            f.write(line)
