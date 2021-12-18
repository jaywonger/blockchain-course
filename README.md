# blockchain-course

Summary
1. decentralized - not controlled by a single centralized entity, run by a network of independent users.
2. transparent - anything that happens on a blockchain can see and work with (same rules)
3. speed - quick and efficient
4. immutable - blockchains cannot be changed, tampered with or corrupted
5. remove counterparty risk - smart contracts remove conflict of interest traditional agreements have, secure math based agreements
6. allow for trust minimized agreements - engage in trustless agreements, self executing code
7. hybrid smart contracts combine on and off-chain - paired with an oracle, bring data into a smart contract

DAOs - decentralized autonomous organizations - do all goverence on chain

Hash - A unique fixed length string, meant to identify a piece of data. They are created by placing said data into a "hash function"

----------------------------------------------------------------------------------------------------------------------------------------------------------
ETH uses Keccak256 as their Hash algorithm 

Block 
- a list of transactions mined together
- combines block, nonce, data = hash
- Nonce: a "number used once" to find the "solution" to the blockchain problem (it's also used to define the transaction number fo an account/address)
- to mine a block it needs to make the hash start with 4 zeroes 
- nonce is the solution to the problem

Blockchain 
- multiple blocks
- block, nonce, data, prev, and hash
- genesis block: the first block in a blockchain
- prev hash is used to solve the next block in a blockchain
- basically a decentralized database

Distributed Blockchain 
- multiple blockchain
- each node is running a blockchain has the exact same power as anyone else
- new data introduced to a block creates a fork in the blockchain
- majority rules in a blockchain

Tokens 
- distribution of tokens is based on distributed blockchain
- the more input power the more output amount of tokens
- how to know if correct tokens are sent (private keys!)

Hash Algorithm - A function that computes data into a unique hash 
Mining - the process of finding the "solution" to the blockchain "problem".
In our eaxmple, the "problem" was to find a hash that starts with four zeroes.
Nodes get paid for mining blocks.

Decentralized: having no single point of authority

Public Key: is dereived from your private key. Anyone can "see" it, and use it to verify that a transaction came from you.
Private Key: only know to the key holder, it's used to "sign" transactions
Signing a transaction: A "one way" process. Someone with a private key signs a transaction by their private key being hashed with their transaction data.
                       Anyone can then verify this new transaction hash with your private key.

ETH Converter
https://eth-converter.com/
       
