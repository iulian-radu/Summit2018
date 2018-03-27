import AlgoAccount
import argparse

first_party_traits = [
    {'name': 'Mini cooper enthusiasts', 'description': 'Mini cooper enthusiasts', 'comment': 'Mini cooper enthusiasts',
     'rule': 'property=="Mini cooper enthusiasts"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Mini Cooper Convertible', 'description': 'Mini Cooper Convertible', 'comment': 'Mini Cooper Convertible',
     'rule': 'property=="Mini Cooper Convertible"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Mini Cooper Coupe', 'description': 'Mini Cooper Coupe', 'comment': 'Mini Cooper Coupe',
     'rule': 'property=="Mini Cooper Coupe"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Mini Cooper Hardtop', 'description': 'Mini Cooper Hardtop', 'comment': 'Mini Cooper Hardtop',
     'rule': 'property=="Mini Cooper Hardtop"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Mini Cooper Hardtop 4 Door', 'description': 'Mini Cooper Hardtop 4 Door',
     'comment': 'Mini Cooper Hardtop 4 Door', 'rule': 'property=="Mini Cooper Hardtop 4 Door"',
     'type': 'RULE_BASED_TRAIT'},
    {'name': 'Mini Cooper Clubman', 'description': 'Mini Cooper Clubman', 'comment': 'Mini Cooper Clubman',
     'rule': 'property=="Mini Cooper Clubman"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Mini Cooper Countryman', 'description': 'Mini Cooper Countryman', 'comment': 'Mini Cooper Countryman',
     'rule': 'property=="Mini Cooper Countryman"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Mini Cooper S', 'description': 'Mini Cooper S', 'comment': 'Mini Cooper S',
     'rule': 'property=="Mini Cooper S"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Mini John Cooper Works', 'description': 'Mini John Cooper Works', 'comment': 'Mini John Cooper Works',
     'rule': 'property=="Mini John Cooper Works"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Honda Fit', 'description': 'Honda Fit', 'comment': 'Honda Fit', 'rule': 'property=="Honda Fit"',
     'type': 'RULE_BASED_TRAIT'},
    {'name': 'Volkswagen GTI', 'description': 'Volkswagen GTI', 'comment': 'Volkswagen GTI',
     'rule': 'property=="Volkswagen GTI"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Fiat 500 Abarth', 'description': 'Fiat 500 Abarth', 'comment': 'Fiat 500 Abarth',
     'rule': 'property=="Fiat 500 Abarth"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Kia Soul', 'description': 'Kia Soul', 'comment': 'Kia Soul', 'rule': 'property=="Kia Soul"',
     'type': 'RULE_BASED_TRAIT'},
    {'name': 'Chevrolet Bolt', 'description': 'Chevrolet Bolt', 'comment': 'Chevrolet Bolt',
     'rule': 'property=="Chevrolet Bolt"', 'type': 'RULE_BASED_TRAIT'},
    {'name': 'Mazda Miata', 'description': 'Mazda Miata', 'comment': 'Mazda Miata', 'rule': 'property=="Mazda Miata"',
     'type': 'RULE_BASED_TRAIT'}
]

conversion_traits = [
    {'name': '[PREGENERATED] Conversion trait', 'type': 'RULE_BASED_TRAIT'}
]

algo_traits = [
    {'name': '[PREGENERATED] MC Algo firstparty Accu > 70%', 'description': '',
     'algo_model': '[PREGENERATED] Mini Cooper look-alike - 1st party data', 'accuracy': '0.7'},
    {'name': '[PREGENERATED] MC Algo firstparty Accu > 90%', 'description': '',
     'algo_model': '[PREGENERATED] Mini Cooper look-alike - 1st party data', 'accuracy': '0.9'},
]

segments = [
    {'name': '[PREGENERATED] MC Algo firstparty Accu > 70%', 'description': '', 'test_group': '[PREGENERATED] firstparty Test'}
]

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Provision accounts for the summit algo lab')
    parser.add_argument('pid', help='Partner id. Your company id')
    parser.add_argument('user', help='Partner id. Your company id')
    parser.add_argument('password', help='Partner id. Your company id')
    parser.add_argument('client_id', help='Partner id. Your company id')
    parser.add_argument('client_secret', help='Partner id. Your company id')
    parser.add_argument('destination_id', help='Partner id. Your company id')

    args = parser.parse_args()

    base_url = 'https://api-sandbox.demdex.com'

    algo_account = AlgoAccount.AlgoAccount(base_url)
    algo_account.provision(int(args.pid),
                           args.user,           # Admin user name for the account you're provisioning
                           args.password,       # user password
                           args.client_id,      # Oauth2 client id
                           args.client_secret,
                           'Main Data Source',  # name of the created data source
                           first_party_traits,  # all the first party traits
                           conversion_traits,   # all the conversion traits
                           algo_traits,         # the algorithmic traits to be created
                           segments,
                           args.destination_id
                           )
