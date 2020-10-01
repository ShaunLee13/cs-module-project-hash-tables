class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.tbl = [None] * capacity
        self.num_items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_items / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.

        This is the pseudocode for fnv-1:
        algorithm fnv-1 is
            hash := FNV_offset_basis do

            for each byte_of_data to be hashed
                hash := hash × FNV_prime
                hash := hash XOR byte_of_data

            return hash 
        """
        # This is our offset basis
        hval = 14695981039346656037
        for byte in key:
            #1099511628211 is our fnv prime
            hval = hval * 1099511628211 
            hval = hval ^ ord(byte)
        
        return hval % self.capacity


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #get index for key
        #search list for key
        # if found overwrite value
        # else insert it into the list

        # if our load factor is greater than limit, resize automatically
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

        # set our index variable and instantiate the item at that index we're working with
        ind = self.hash_index(key)
        new_item = self.tbl[ind]

        #if the item is None, create our entry at that point; increment counter.
        if new_item is None:
            self.tbl[ind] = HashTableEntry(key, value)
            self.num_items += 1
            return
        
        # otherwise, as long as there is a next and as long as the item we're on isn't the key we're inserting,
        # set our item to the next item in the chain
        # if the key we have matches any in the chain we'll break out of the loop
        while new_item.next and new_item.key != key:
            new_item = new_item.next

        # if we've passed the loop because we have a matching key, update with a new value
        if new_item.key == key:
            new_item.value = value
        # otherwise we're at the end of the list and can just append to the end.
        else:
            new_item.next = HashTableEntry(key, value)
            self.num_items += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # set our index variable and instantiate the item at that index we're checking to remove
        # also create a pointer to the previous item in the list
        ind = self.hash_index(key)
        check = self.tbl[ind]
        prev_item = None
        #search list for key. if our item is none, we continue, otherwise we return warning.
        if check is not None:
            #as long as our item has a value, check for next. if true and if the keys dont match
            # we'll shift our current pointer and previous pointers up one position
            while check.next and check.key != key:
                prev_item = check
                check = check.next
            # if the keys match, and if we are at the head, our new head will be the next item.
            #otherwise set the previous items next pointer to our current next pointer. decrement counter.
            if check.key == key:
                if prev_item is None:
                    self.tbl[ind] = check.next
                else:
                    prev_item.next = check.next
                self.num_items -= 1
        #else warning
        else:
            return 'That key is not located in the table.'


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #get index for key
        #search list for key
        #if found, return value
        #else None
        ind = self.hash_index(key)
        check = self.tbl[ind]
        # if there's nothing at that index. return None
        if check is None:
            return None

        while check.next and check.key != key:
            check = check.next
        
        return check.value if check.key == key else None



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        #save an instance of our current table
        curr_tbl = self.tbl
        #create a new table with the updated capacity and set our current capacity to it
        self.tbl = [None] * new_capacity
        self.capacity = new_capacity
        self.num_items = 0

        # for every index on our current table
        for ind in range(len(curr_tbl)):
            # capture the node located at that index
            current = curr_tbl[ind]
            # and as long as the node is not equal to nothing, put the node onto the new table we created, and follow the next pointer to the next node
            while current:
                self.put(current.key, current.value)
                current = current.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
