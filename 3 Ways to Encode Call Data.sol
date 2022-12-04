// SPDX-Linense-Identifier: MIT
pragma solidity ^0.8.7;

interface IERC20 {
    function transfer(address, uint) external;
}

contract Token {
    function transter(address, uint) external  {}
}

contract AbiEncode{
    function test(address _contract, bytes calldata data) external {
        (bool ok,) = _contract.call(data);
        require(ok, "call failed");
    }

    function encodeWithSignature(address to, uint amount)
        external
        pure 
        returns (bytes memory)
    {
        return abi.encodeWithSignature("transter(address,uint256)", to, amount);
    }

    function encodeWithSelector(address to, uint amount)
        external
        pure 
        returns (bytes memory)
    {
        return  abi.encodeWithSelector(IERC20.transfer.selector, to, true, amount);
    }

    function ecodeCall(address to,  uint amount) external pure returns (bytes calldata) {
        return abi.encodeCall(IERC20.transfer, (to, amount));
    }
} 
