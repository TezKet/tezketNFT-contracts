# Tezket NFT contracts

```
bash <(curl -s https://smartpy.io/cli/install.sh) --prefix `pwd`/scripts/smartpy-cli
./scripts/smartpy-cli/SmartPy.sh --version

./scripts/smartpy-cli/SmartPy.sh compile ./contracts/my_contract.py ./compilation
./scripts/smartpy-cli/SmartPy.sh test ./contracts/my_contract.py ./compilation

./scripts/SmartPy.sh originate-contract 
    --code ./compilation/my_contract/<...>_contract.tz \
    --storage ./scripts/compilation/my_contract/<...>_storage.tz \
    --rpc https://granadanet.smartpy.io \
    --private-key <edsk...>
    
```