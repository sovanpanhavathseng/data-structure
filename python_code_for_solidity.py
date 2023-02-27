from web3 import Web3
from solcx import compile_source
from web3.contract import ConciseContract

# Connect to the local Ethereum node
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Solidity source code
contract_source_code = """
pragma solidity ^0.4.0;

contract SimpleStorage {
    uint storedData;

    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
"""

# Compile the contract source code
compiled_sol = compile_source(contract_source_code)

# Get the contract interface and bytecode
contract_interface = compiled_sol['<stdin>:SimpleStorage']
bytecode = contract_interface['bin']
abi = contract_interface['abi']

# Create a new contract instance
SimpleStorage = web3.eth.contract(abi=abi, bytecode=bytecode)

# Deploy the contract
tx_hash = SimpleStorage.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Create a concise contract interface for interacting with the deployed contract
simple_storage = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi,
    ContractFactoryClass=ConciseContract
)

# Call the contract functions
simple_storage.set(42, transact={'from': web3.eth.accounts[0]})
stored_data = simple_storage.get()
print(stored_data)
