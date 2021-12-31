from scripts.helpful_scripts import get_account
from brownie import Lottery

def deploy_lottery(index=None, id=None):
    account = get_account()
    lottery = Lottery.deploy()

def main():
    deploy_lottery()