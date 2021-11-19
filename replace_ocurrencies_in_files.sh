# Replacing all occurrences of one string in all files in the current directory
find . -type f -exec sed -i 's/foo/bar/g' {} +
