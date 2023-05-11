# chik-blockchain

[![Chik Network logo](https://www.chia.net/wp-content/uploads/2022/09/chia-logo.svg "Chik logo")](https://www.chiknetwork.org/)

| Current Release/main | Development Branch/dev |
|         :---:          |          :---:         |
| [![Ubuntu Core Tests](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-test-ubuntu-core.yml/badge.svg)](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-test-ubuntu-core.yml) [![MacOS Core Tests](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-test-macos-core.yml/badge.svg)](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-test-macos-core.yml) [![Windows Installer on Windows 10 and Python 3.7](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-windows-installer.yml/badge.svg)](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-windows-installer.yml)  |  [![Ubuntu Core Tests](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-test-ubuntu-core.yml/badge.svg?branch=dev)](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-test-ubuntu-core.yml) [![MacOS Core Tests](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-test-macos-core.yml/badge.svg?branch=dev)](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-test-macos-core.yml) [![Windows Installer on Windows 10 and Python 3.7](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-windows-installer.yml/badge.svg?branch=dev)](https://github.com/Chik-Network/chik-blockchain/actions/workflows/build-windows-installer.yml) |


***********************************************
# PROJECT DESCRIPTION
Chik is an eco-friendly decentralization blockchain based on the Proof of Space and Time (PoST) consensus pioneered by Chia™. It maintains network robustness, in line with Satoshi Nakamoto's principles.

Chik uses the powerful and secure Chialisp language for Smart Contracts, and supports digital money, global payments and applications. HDDcoin is not affiliated with Chia Network, Inc., but uses their open-sourced software as its foundation.

Farming Chik does not consume significant amounts of electricity, and utilizes hard drive space, instead of specialized computing hardware that most Proof of Work (PoW) consensus blockchains have come to demand. Moreover, since electrical energy costs for running hard drives is very minimal, due to this low cost of entry, Chik will remain more decentralized and fair, and thus more secure than any Proof of Stake cryptocurrency.

Chik core values include green cryptocurrency, long term value, building for the future, strength in community, and maintaining a huge team to ensure long term development.

The goal of Chik is to reshape the global financial system through the power of the blockchain technology, powered by thousands of nodes maintained by the community, and with transparency and a commitment to the environment — thereby taking control from any central entity, person or organization, and giving that control back to the community.

**BLOCKCHAIN SPECIFICATION:**
- Launch date: July 8th 2023
- Cryptocurrency coin: XCK
- Lowest coin denomination: Bytes
- Conversion: 1 XCK = 1,000,000,000,000 Bytes
- Blocks per 24 hours target: 4,608
- Farmed rewards per block: 2 XCK
- Halving period for block rewards: 3 years

**BLOCKCHAIN RESOURCES:**
- Website: https://chiknetwork.org
- Online Store: https://store.chiknetwork.org
- Explorer: https://explorer.chiknetwork.org
- Graphs: https://graphs.chiknetwork.org
- White Paper: https://chiknetwork.org/white-paper
- Roadmap: https://chiknetwork.org/roadmap
- Calculator: https://chiaforkscalculator.com/chiknetwork
- Chik DB: https://download.chiknetwork.org/blockchain_v1_mainnet.sqlite

**COMMUNITIES AND SOCIAL CHANNELS:**
- Discord: https://discord.gg/
- Twitter: https://twitter.com/chik
- Facebook: https://www.facebook.com/ChikNetwork
- Reddit: https://www.reddit.com/r/ChikNetwork
- YouTube: https://www.youtube.com/channel/
- Telegram: https://t.me/ChikNetwork


***********************************************
# CO-FARMING WITH COMPATIBLE PLOTS?
Please note that if you wish to co-farm with compatible plots made using the Client of another blockchain (like Chia™), or any other plotting tool like MadMax, because public keys are encoded in the plots, in order to utilize these plots for HDDcoin, you'll need to set the same mnemonic phrase (24 words) that you used for creating the plots. Learn more on our FAQ page -- https://chiknetwork.org/faq.
 
***********************************************
# INSTALL INSTRUCTIONS:

You can install Chik by building from source, or by using the latest binaries for your operating system.

(A.) To **install from available binaries**, download executables from:  https://github.com/Chik-Network/chik-blockchain/releases


(B.) To **build from source**, do the following:

```
# Update / Upgrade OS:

   sudo apt-get update
   sudo apt-get upgrade -y

# Install Git:

   sudo apt install git -y

# Checkout the correct source:

   git clone https://github.com/Chik-Network/chik-blockchain.git

  
# Install the Blockchain:

   cd chik-blockchain
   sh install.sh
   . ./activate
   chik init

# Install and run the GUI:

   sh install-gui.sh
   cd chik-blockchain-gui
   npm run electron &
```

If the client does not find any connections automatically, you can add any of the following:

- introducer.chiknetwork.org / Port: 28555
- dns-introducer.chiknetwork.org / Port: 28555

***********************************************
# UPDATE/UPGRADE INSTRUCTIONS:

You can update Chik from a previous version by downloading and installing the latest executable for your operating system, available from the **Releases page**, or by building from source:

```
# Checkout the source and update

  cd chik-blockchain
  . ./activate
  chik stop -d all
  deactivate
  git fetch
  git checkout main
  git reset --hard FETCH_HEAD --recurse-submodules
  sh install.sh
  . ./activate
  chik init

# Update the GUI

  chmod +x ./install-gui.sh
  ./install-gui.sh
```
