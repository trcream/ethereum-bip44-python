from crypto import HDPrivateKey, HDKey

def generate_mnemonic():
    # Generate a new master key and mnemonic phrase
    master_key, mnemonic = HDPrivateKey.master_key_from_entropy()
    print('Mnemonic Secret: ' + mnemonic)
    return mnemonic

def derive_addresses_from_mnemonic(mnemonic, num_addresses=10):
    # Generate the master key from the mnemonic
    master_key = HDPrivateKey.master_key_from_mnemonic(mnemonic)
    
    # Derive the root keys using the MetaMask derivation path
    root_keys = HDKey.from_path(master_key,"m/44'/60'/0'")
    acct_priv_key = root_keys[-1]
    
    for i in range(num_addresses):
        keys = HDKey.from_path(acct_priv_key,'{change}/{index}'.format(change=0, index=i))
        private_key = keys[-1]
        public_key = private_key.public_key
        print("Index %s:" % i)
        print("  Private key (hex, compressed): " + private_key._key.to_hex())
        print("  Address: " + public_key.address())

if __name__ == "__main__":
    # Generate a new mnemonic
    mnemonic = generate_mnemonic()

    num_addresses = int(input("Enter the number of Ethereum addresses to generate: "))

    # Derive addresses from the generated mnemonic
    derive_addresses_from_mnemonic(mnemonic, num_addresses)
