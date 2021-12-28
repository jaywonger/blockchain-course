// SPDX-License-Identifier: MIT
pragma solidity >=0.6.6 <0.9.0;

import "@chainlink/contracts/src/v0.7/interfaces/AggregatorV3Interface.sol";

contract Lottery {

    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;

    constructor(address _priceFeedAddress) public {
        usdEntryFee = 50 * 10**18;
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

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