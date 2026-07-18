with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We will find the indices of the comment lines
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '2. SHOPPING CART LOGIC' in line:
        # Go back to find the starting comment line /* ======
        j = i
        while j >= 0:
            if '/*' in lines[j]:
                start_idx = j
                break
            j -= 1
    if '3. SHOP FILTER & SORT LOGIC' in line:
        j = i
        while j >= 0:
            if '/*' in lines[j]:
                end_idx = j
                break
            j -= 1

if start_idx != -1 and end_idx != -1:
    new_lines = lines[:start_idx] + lines[end_idx:]
    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Successfully removed lines from {start_idx} to {end_idx}")
else:
    print("Could not find start or end index", start_idx, end_idx)
