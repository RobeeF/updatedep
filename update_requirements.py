import os
import re

# Origin and destination branches of the PR
origin_branch = os.getenv('ORIGIN_BRANCH')
target_branch = os.getenv('TARGET_BRANCH')

# Path to the requirements.txt file
requirements_file = "requirements.txt"

# Check that the dependencies to update are in the right organization 
orgname = 'blaorg'
pattern = re.compile('git\+ssh://git@github.com/' + orgname)

# Update utility function
def update_dependency(dependency_line) -> str:
    ''' Update the dependency line to match the target branch
    Args:
        dependency_line (str): dependency line to update
    Returns:
        str: updated dependency line
    '''
    return re.sub('@' + origin_branch, '@' + target_branch, dependency_line)

# Read the requirements.txt file
with open(requirements_file, 'r') as f:
    lines = f.readlines()

# Replace the branch of our internal dependencies
with open(requirements_file, 'w') as f:
    for line in lines:
        # Only if the dependency is ours
        match = pattern.search(line)
        if match:
            # Update the branch
            new_line = update_dependency(line)
            f.write(new_line)
        else:
            # Leave the dependency line as it is
            f.write(line)

# Test