
pragma solidity ^0.7.0;

contract Lottery {

    address payable[] public players;

    function enter() public payable {
        // min $50
        players.push(msg.sender);
    }
    function getEntranceFee() public view returns (uint256) {
        // ?
    }
    function startLottery() public {}
    function endLottery() public {}

}