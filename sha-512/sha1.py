import binascii

def bintohex(pt):
    """Convert binary string to hexadecimal."""
    ans = ""
    btoh = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    for i in range(0, len(pt), 4):
        wd = pt[i:i+4]
        ans += btoh[wd]
    return ans

def hextobin(x):
    """Convert hexadecimal to binary string."""
    htob = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    return ''.join(htob[char] for char in x.upper())

def right_rotate(x, k, bits=64):
    """Perform right rotation on 64-bit integer."""
    return ((x >> k) | (x << (bits - k))) & ((1 << bits) - 1)

def sigma0(x):
    """SHA-512 sigma 0 function."""
    return right_rotate(x, 1) ^ right_rotate(x, 8) ^ (x >> 7)

def sigma1(x):
    """SHA-512 sigma 1 function."""
    return right_rotate(x, 19) ^ right_rotate(x, 61) ^ (x >> 6)

def Ch(x, y, z):
    """Choose function."""
    return (x & y) ^ (~x & z)

def Maj(x, y, z):
    """Majority function."""
    return (x & y) ^ (x & z) ^ (y & z)

def big_sigma0(x):
    """Big sigma 0 function."""
    return right_rotate(x, 28) ^ right_rotate(x, 34) ^ right_rotate(x, 39)

def big_sigma1(x):
    """Big sigma 1 function."""
    return right_rotate(x, 14) ^ right_rotate(x, 18) ^ right_rotate(x, 41)

# Complete Constants for SHA-512
K = [
    0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
    0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
    0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
    0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
    0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
    0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
    0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
    0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
    0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
    0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
    0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
    0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
    0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
    0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
    0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
    0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
    0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
    0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
    0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
    0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817
]

def preprocess_message(message):
    """Preprocess the input message for SHA-512."""
    # Convert message to binary
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    
    # Append 1 bit
    binary_message += '1'
    
    # Pad with zeros
    k = (896 - (len(binary_message) % 1024)) % 1024
    binary_message += '0' * k
    
    # Append length of  original message (in bits) as 128-bit big-endian integer
    length_bits = len(message) * 8
    binary_length = format(length_bits, '0128b')
    binary_message += binary_length
    
    return binary_message

def sha512(message):
    """Implement SHA-512 hash algorithm."""
    # Initial hash values
    H = [
        0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
        0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b, 0x5be0cd19137e2179
    ]
    
    # Preprocess the message
    preprocessed_message = preprocess_message(message)
    print(preprocessed_message)
    # Process message in 1024-bit chunks
    for chunk_start in range(0, len(preprocessed_message), 1024):
        chunk = preprocessed_message[chunk_start:chunk_start+1024]
        print(chunk==preprocessed_message)
        # Prepare message schedule
        W = [0] * 80
        for t in range(16):
            W[t] = int(chunk[t*64:(t+1)*64], 2)
        print(W)
        for t in range(16, 80):
            W[t] = (sigma1(W[t-2]) + W[t-7] + sigma0(W[t-15]) + W[t-16]) & ((1 << 64) - 1)
        
        # Initialize working variables
        a, b, c, d, e, f, g, h = H
        
        # Main loop
        for t in range(80):
            T1 = (h + big_sigma1(e) + Ch(e, f, g) + K[t] + W[t]) & ((1 << 64) - 1)
            T2 = (big_sigma0(a) + Maj(a, b, c)) & ((1 << 64) - 1)
            
            h = g
            g = f
            f = e
            e = (d + T1) & ((1 << 64) - 1)
            d = c
            c = b
            b = a
            a = (T1 + T2) & ((1 << 64) - 1)

        # Update hash values
        H[0] = (H[0] + a) & ((1 << 64) - 1)
        H[1] = (H[1] + b) & ((1 << 64) - 1)
        H[2] = (H[2] + c) & ((1 << 64) - 1)
        H[3] = (H[3] + d) & ((1 << 64) - 1)
        H[4] = (H[4] + e) & ((1 << 64) - 1)
        H[5] = (H[5] + f) & ((1 << 64) - 1)
        H[6] = (H[6] + g) & ((1 << 64) - 1)
        H[7] = (H[7] + h) & ((1 << 64) - 1)
    
    # Convert final hash to hexadecimal
    print(H)
    return ''.join(f'{x:016x}' for x in H)

# Example usage
message = "abc"
print(f"SHA-512 hash of '{message}': {sha512(message)}")