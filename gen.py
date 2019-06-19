import commands,sys

N = 10
network = 'bitcoinhot'


if len(sys.argv) > 1:
    N = int(sys.argv[1])

    if len(sys.argv) > 2:
        network = sys.argv[2]



#print(len(sys.argv))


genAddrCmdStr = "./bitcoin-tool --network {} --input-type private-key --input-format raw --input {}  --output-type address --output-format base58check --public-key-compression compressed"
genWifCmdStr = "./bitcoin-tool --network {} --input-type private-key --input-format raw --input {}  --output-type private-key-wif --output-format base58check --public-key-compression compressed"


for i in range(N):
    rand= commands.getstatusoutput("openssl rand -hex 16")[1]
    address = commands.getstatusoutput(genAddrCmdStr.format(network, rand))[1]
    wif = commands.getstatusoutput(genWifCmdStr.format(network, rand))[1]

    print("%s, %s" %(address,wif))
