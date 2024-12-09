with open('input.txt', 'r') as file:
    disk_map = [int(c) for c in file.read().strip()]

# parse

blocks_1, blocks_2 = [], []
last_id = 0
is_file = True
for size in disk_map:
    blocks_1.extend([str(last_id) if is_file else "."] * size)
    blocks_2.append({"id": last_id if is_file else None, "size": size})
    last_id += is_file
    is_file = not is_file

# part 1

last_index = len(blocks_1) - 1
while (first_free := blocks_1.index(".")) <= last_index:
    if (block_id := blocks_1[last_index]) != ".":
        blocks_1[first_free], blocks_1[last_index] = block_id, "."
    last_index -= 1

# part 2

last_index = len(blocks_2) - 1
while last_index > 0:
    if (last_block := blocks_2[last_index])["id"] is not None:
        for i, free_block in enumerate(blocks_2):
            if i >= last_index:
                break
            if free_block["id"] is None and free_block["size"] >= last_block["size"]:
                # replace free space with last file
                blocks_2[last_index] = {"id": None, "size": last_block["size"]}
                blocks_2[i] = last_block
                # add remaining free space back in
                if free_block["size"] > last_block["size"]:
                    blocks_2.insert(i + 1, {"id": None, "size": free_block["size"] - last_block["size"]})
                    # merge free blocks
                    if blocks_2[i + 2]["id"] is None:
                        blocks_2[i + 1]["size"] += blocks_2.pop(i + 2)["size"]
                    else:
                        last_index += 1
                break
    last_index -= 1

blocks_2_strings = []
for block in blocks_2:
        blocks_2_strings.extend([str(block["id"]) if block["id"] is not None else "."] * block["size"])

# result

def checksum(blocks_str):
    checksum = 0
    for i, block in enumerate(blocks_str):
        if block == ".":
            continue
        checksum += int(block) * i
    return checksum

print(f"Checksum Part 1: {checksum(blocks_1)}")
print(f"Checksum Part 2: {checksum(blocks_2_strings)}")
