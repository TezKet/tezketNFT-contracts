# Tezket NFT contracts

## Start Sandbox (Local Development)

```
$> chinstrap sandbox -i
$> chinstrap sandbox -p Jakarta -o 12345 -c 5
...

✔ Sandbox is at level: 20 and ready for use!

```

## Complie and Deploy to Local Node

```
$> chinstrap compile
✔ my_contract.py compilation successful!

$> chinstrap originate -n development

Using development network
Loaded wallet tz1U7FSJhS8QggXhzuxQ3kRVxtZuivwrL4ho     . Balance: ꜩ 20000.022856

✔ my_contract.py compilation successful!
✔ my_contract_compiled's origination transaction at: op9HEUeiRp75cJFcsT6srs1YbhC1SQQm7EhE1Wmi2HqQBqBrPaz
✔ Baking successful!
✔ my_contract_compiled address: KT1HK5rgA2JMEAwoopwz2YLcjUL5yzys4kfW
✔ Total Cost of originations:  ꜩ 0.076685

```

### Note -- Setup scripts

```
# Install chinstrap framework.

nvm use v19.6.0

cd scripts

conda create -n py310-tezos-blockchain python=3.10
conda activate py310-tezos-blockchain

git clone https://github.com/ant4g0nist/chinstrap

cd chinstrap

brew tap cuber/homebrew-libsecp256k1
brew install libsodium libsecp256k1 gmp

export CFLAGS="-I`brew --prefix gmp`/include -I`brew --prefix libsecp256k1`/include"
export LDFLAGS="-L`brew --prefix gmp`/lib -L`brew --prefix libsecp256k1`/lib"
pip install . -U 

cd ..

chinstrap install
🎉 Ligo installed
🎉 SmartPy installed

```

### Note -- Or try to compile with SmartPy (Legacy)

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
