# Task 3 - Protocol State Fuzzing

## Introduction
In this part of the assignment we will look at a more serious task: protocol state fuzzing of TLS. Protocol state fuzzing uses active state machine learning to learn how a protocol behaves. This will result in a state machine representing the implementation of said protocol, which allows us to inspect it for errors and/or implementation flaws. 

First, we will use [TLSAttacker](https://github.com/tls-attacker/TLS-Attacker) to send TLS messages to openSSL, using an adapter class we already provided for you in the Task3 Folder. 
Before you can begin, you need to do the following:

- Set up TLSAttacker according to the guide on their github page
- Download and compile [OpenSSL 1.1.1k](https://github.com/openssl/openssl/releases/tag/OpenSSL_1_1_1k)

The instructions for compiling OpenSSL are included in the source. On x86_64 linux it is:
```
./Configure linux-x86_64
make -j$(nproc)
```
after which the openssl binary will be found at `apps/openssl`

After doing this you should have a folder with the following contents:
```
├── openssl-OpenSSL_1_1_1k
└── TLS-Attacker
```

To start an OpenSSL server, first `cd TLS-Attacker/resources` and run the `keygen.sh` script if you haven't already.
Then you can start your desired version of OpenSSL by running:
```
 ../../openssl-OpenSSL_1_1_1k/apps/openssl s_server -key rsa1024key.pem -cert rsa1024cert.pem
```

Once that is up and running, you are ready to start learning state machines!

Please use the code provided in the Task3 folder to learn a state machine of openssl, and please read about how the TLS protocol works 
- [here](https://tls.ulfheim.net/)
- [or here](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)

Try to see if the protocol state machine you learned matches with what you expect from the TLS protocol.

Learning the state machine can take a while, so go get some coffee and read up on the next part in the meantime.

## Finding a vulnerability

Now it is up to you to find a vulnerability in an implementation of the TLS protocol. Search for known vulnerabilities online, and download and compile a vulnerable implementation of your choice (it doesn't have to be openssl).

Depending on what you are trying to do, you may have to extend the mapper in `TLSAttackerMapper.py` to be able to send a message to trigger your chosen vulnerability. Be sure to check out the TLSAttacker repository for inspiration

Learn a state machine of a vulnerable TLS implementation of your choice and use the state machine to point out where the flaw is and how it works.

(Optional) also learn a state machine of the newest version of your chosen TLS implementation and check if the flaw has been fixed!