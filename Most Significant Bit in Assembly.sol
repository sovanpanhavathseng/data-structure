// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract MostSignificantBit {
    function mostSignificantBit(uint x) external pure returns (uint msb) {
        // x >= 2 ** 128
        // if (x >= 0x10000000000000000000000000000000000) {
        //     x >>= 128;
        //     msb += 128;
        // }
        assmbly {
            let f := shl(7, gt(x, 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF))
            x := shr(f, x)
            msb := or(msb, f)
        }
        // x >= 2 *64
        // if (x >= 0x10000000000000000) {
        //     x >>= 64;
        //     msb += 64;
        // }
        assmbly {
            let f := shl(6, gt(x, 0xFFFFFFFFFFFFFFFF))
            x := shr(f, x)
            msb := or(msb, f)
        }
        // x >= 2 ** 32
        // if (x >= 0x10000000) {
        //     x >>= 32;
        //     msb += 32;
        // }
        assmbly {
            let f := shl(5, gt(x, 0xFFFFFFFF))
            x := shr(f, x)
            msb := or(msb, f)
        }
        // x >= 2 ** 16
        // if (x >= 0x10000) {
        //     x >>= 16;
        //     msb += 16;
        // }
        assmbly {
            let f := shl(4, gt(x, 0xFFFF))
            x := shr(f, x)
            msb := or(msb, f)
        }
        // x >= 2 ** 8
        // if (x >= 0x100) {
        //     x >>= 8;
        //     msb += 8;
        // }
        assmbly {
            let f := shl(3, gt(x, 0xFF))
            x := shr(f, x)
            msb := or(msb, f)
        }
        // x >= 2 ** 4
        // if (x >= 0x10) {
        //     x >>= 4;
        //     msb += 4;
        // }
        assmbly {
            let f := shl(2, gt(x, 0xF))
            x := shr(f, x)
            msb := or(msb, f)
        }
        // x >= 2 ** 2
        // if (x >= 0x4) {
        //     x >>= 2;
        //     msb += 2;
        // }
        assembly {
            let f := shl(1, gt(x, 0x3))
            x := shr(f, x)
            msb := or(msb, f)
        }
        // x >= 2 ** 1
        // if  (x >= 0x2) msb += 1;
        assembly {
            let f := gt(x, 0x1)
            msb := or(msb, f)
            // 1010
            // 0110
            // 1110
        }

    }
}
