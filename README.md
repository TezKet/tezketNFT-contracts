# Tezket NFT contracts

## Setup Env (Test on M1 Chip).

```
brew tap cuber/homebrew-libsecp256k1
brew install libsodium libsecp256k1 gmp

```

## Install the Swiss-Army-Knife for Tezos.

```
cd scripts

nvm use v19.6.0

conda create -n py310-tezos-blockchain python=3.10
conda activate py310-tezos-blockchain

git clone https://github.com/ant4g0nist/chinstrap
cd chinstrap

export CFLAGS="-I`brew --prefix gmp`/include -I`brew --prefix libsecp256k1`/include"
export LDFLAGS="-L`brew --prefix gmp`/lib -L`brew --prefix libsecp256k1`/lib"
pip install . -U 

```

## Run Workflow.

```
$> chinstrap -h

      _     _           _
  ___| |__ (_)_ __  ___| |_ _ __ __ _ _ __
 / __| '_ \| | '_ \/ __| __| '__/ _` | '_ \
| (__| | | | | | | \__ \ |_| | | (_| | |_) |
 \___|_| |_|_|_| |_|___/\__|_|  \__,_| .__/
                                     |_|

Docs 📖   : https://chinstrap.io/
Tele 💬   : https://t.me/chinstrap_io

🐧 Chinstrap - a cute framework for developing Tezos Smart Contracts!

---

$> chinstrap install
🎉 Ligo installed
🎉 SmartPy installed

---

$> chinstrap init
$> chinstrap compile

$> chinstrap sandbox -i
$> chinstrap sandbox -p Jakarta -o 12345 -c 5

$> chinstrap originate -n development
Using development network
Loaded wallet tz1U7FSJhS8QggXhzuxQ3kRVxtZuivwrL4ho     . Balance: ꜩ 20000.022856

✔ my_contract.py compilation successful!
✔ my_contract_compiled's origination transaction at: op9HEUeiRp75cJFcsT6srs1YbhC1SQQm7EhE1Wmi2HqQBqBrPaz
✔ Baking successful!
✔ my_contract_compiled address: KT1HK5rgA2JMEAwoopwz2YLcjUL5yzys4kfW
✔ Total Cost of originations:  ꜩ 0.076685

```

## Or try to compile with SmartPy 

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

## TODO list!
```
[x] Build and Test contract on Dev.
[x] Switch to "chinstrap" Workflow.
   [x] Deploy to Local node (Flextesa)
```