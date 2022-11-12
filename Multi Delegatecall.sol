// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract TestMultiCall {
    function func1() external  view returns (uint, uint) {
        return (1, block.timestamp);
    }

    
    function func2() external  view returns (uint, uint) {
        return (2, block.timestamp);
    }

    function getDate1() external pure returns (bytes memory) {
        // abi.encodeWithSignature("func1()")
        return abi.encodeWithSelector(this, func1.selector);
    }

    function getDate2() external pure returns (bytes memory) {
        // abi.encodeWithSignature("func2()")
        return abi.encodeWithSelector(this, func2.selector);
    }
}

contract MultiCall {
    function MultiCall(address[] calldata targets, bytes[] calldata data)
        external
        view
        returns (bytes[] memory)
    {
        require(tragets.length == data.length, "tragets length != data lengyh");
        bytes[] memory results = new bytes[](data.length);

        for (uint i; i < targets.length; i++) {
            (bool success, bytes memory result) = targets[i].staticcall(data[i]);
            require(success, "call failed");
            results[i] = result;
        }

        return results;
    }
}
