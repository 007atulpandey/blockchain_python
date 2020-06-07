#BlockChaining 

#imports
import json
import hashlib
from collections import OrderedDict
from hash_util import hash_string_256, hash_block
#globals
MiningReward = 10
first ={
    'previous_hash':'first',
    'index':'0',
    'transactions':[],
    'proof':2608
}
blockchain = [first]
transaction = []
sender = 'AtulPandey'
participants ={'AtulPandey'}


'''
# functions :

addelement
getlast
get_user
printchain
printParticipants
getBalance
verify_transaction
verify
hash_block
mine_block
get_sendAmount
get_recievedAmount
proof_of_work
valid_proof

'''



def addelement(recipient , amount):
    # newTx= {
    #     'sender':sender,
    #     'recipient':recipient,
    #     'amount':amount
    # }
    # use ordered dict
    newTx =OrderedDict([('sender',sender),('recipient',recipient),('amount',amount)])

    if verify_transaction(newTx):
        participants.add(sender)
        participants.add(recipient)
        transaction.append(newTx)
        print('-'*20)
        print('successfully transaction done')
    else:
        print('Not enough Balance')

def getlast():
    return blockchain[-1]

def get_user():
    tx_recipient =input('Recipient name')
    tx_amount = float(input('Amount to send'))
    return tx_recipient , tx_amount

def printchain():
    for i in blockchain:
        print(i)

def printParticipants():
    print('*'*20)
    for tx in participants:
        print(tx, " :")

        print("sendAmount : ",get_sendAmount(tx))
        print("recieveAmount : ",get_recievedAmount(tx))
        print('TotalBalance : {:6.2f} '.format(getBalance(tx)))
    else:
        print('*'*20)

def getBalance(user):
    return get_recievedAmount(user)-get_sendAmount(user)

def verify_transaction(transaction):

    if getBalance(transaction['sender']) >= transaction['amount']:
        return True
    return False



def verify():
    hash = hash_block(blockchain[0])
    for i in range(1,len(blockchain)):
        if(hash!=blockchain[i]['previous_hash']):
            return False
        if not valid_proof(blockchain[i]['transactions'][:-1],blockchain[i]['previous_hash'],blockchain[i]['proof']):
            print('Proof of work invalid')
            return False

        hash = hash_block(blockchain[i])
    return True

# def hash_block(block):
#     hash = hashlib.sha256(json.dumps(block,sort_keys=True).encode())
#     return hash.hexdigest()


def mine_block():
    last_block= blockchain[-1]
    hash = hash_block(last_block)
    # createNew = {
    #     'sender':'mining',
    #     'recipient':sender,
    #     'amount':MiningReward
    # }
    proof = proof_of_work()
    createNew = OrderedDict([('sender','mining'),('recipient',sender),('amount',MiningReward)])
    transaction.append(createNew)
    block= {
        'previous_hash':hash,
        'index':len(blockchain),
        'transactions':transaction,
        'proof':proof
    }
    blockchain.append(block)

def get_sendAmount(participant):
    tx_send = [ [ tx['amount'] for tx in block['transactions'] if tx['sender']==participant] for block in blockchain ] 
    amount=0
    for a in tx_send:

        if(len(a)>0):
            amount+=sum(a)
    return amount
def get_recievedAmount(participant):
    tx_send = [ [ tx['amount'] for tx in block['transactions'] if tx['recipient']==participant] for block in blockchain ] 
    amount=0
    for a in tx_send:
        
        if(len(a)>0):
            amount+=a[0]
    return amount


def valid_proof(transactions,last_hash,proof):
    guess = str(transactions)+str(last_hash)+str(proof)

    guess_hash= hash_string_256(guess.encode())
    return guess_hash[0:2]=='00'


def proof_of_work():
    last_block= blockchain[-1] 
    last_hash = hash_block(last_block)
    proof=0
    while not valid_proof(transaction,last_hash,proof):
        proof+=1
    return proof

# main function 

loop =True
while(loop):
    print("1 : add element\n2: print chain\n3:Output Participants\nm: Mine transactions \nq: exit")
    a= input()
    if a=='1':
        recipient,amount = get_user()
        addelement(recipient,amount)
    elif a=='2':
        printchain()
    elif a=='3':
        printParticipants()
    elif a=='h':
        blockchain[0]={
            'previous_hash':'hacking',
            'index':'0',
            'transactions':[{
                'sender':'ABCD',
                'recipient':'Atul',
                'amount':11.23
            }]

        }
    elif a=='m':
        mine_block()
        transaction=[]
    else :
        loop =False
    if not verify():
        print("blockchain hacked !!!!")
        loop=False
    
else:
    print("Usser left")