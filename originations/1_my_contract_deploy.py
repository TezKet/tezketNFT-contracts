from chinstrap.originations import getContract

def deploy(chinstrapState, network, accounts):
    contract = getContract("my_contract_compiled")
    initial_storage = contract.storage.encode(
        0
    )
    return initial_storage, contract


# {"counter": 0, "owner": accounts[0].key.public_key_hash()}
# {"int": 0}