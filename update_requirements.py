import re

# Le nom de la branche cible (par exemple, "staging")
target_branch = "staging"

# Chemin vers votre fichier requirements.txt
requirements_file = "requirements.txt"

# Pattern pour rechercher les lignes de dépendances de votre organisation
pattern = re.compile(r'^(myorganization/\w+)')

# Fonction pour mettre à jour la ligne de dépendance
def update_dependency(match):
    return f'{match.group(1)} @ git+ssh://git@github.com/blaorg/{match.group(1)}.git@{target_branch}'

# Ouvrir le fichier requirements.txt en mode lecture
with open(requirements_file, 'r') as f:
    lines = f.readlines()

# Ouvrir le fichier requirements.txt en mode écriture
with open(requirements_file, 'w') as f:
    for line in lines:
        # Rechercher des correspondances avec le pattern
        match = pattern.match(line)
        if match:
            # Mettre à jour la ligne de dépendance
            new_line = update_dependency(match) + '\n'
            f.write(new_line)
        else:
            # Écrire la ligne telle quelle
            f.write(line)
