import java.util.*;
import java.math.*;

class RSA {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        BigInteger p, q, n, z, d = BigInteger.ZERO, e;
        System.out.println("Enter the number to be encrypted and decrypted");
        BigInteger msg = sc.nextBigInteger();
        BigInteger c;
        BigInteger msgback;
        System.out.println("Enter 1st prime number p");
        p = sc.nextBigInteger();
        System.out.println("Enter 2nd prime number q");
        q = sc.nextBigInteger();

        n = p.multiply(q);
        z = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));
        System.out.println("the value of z = " + z);

        e = BigInteger.valueOf(2);
        while (e.compareTo(z) < 0) {
            if (gcd(e, z).equals(BigInteger.ONE)) {
                break;
            }
            e = e.add(BigInteger.ONE);
        }
        System.out.println("the value of e = " + e);

        for (int i = 0; i <= 9; i++) {
            BigInteger x = BigInteger.ONE.add(BigInteger.valueOf(i).multiply(z));
            if (x.mod(e).equals(BigInteger.ZERO)) {
                d = x.divide(e);
                break;
            }
        }
        System.out.println("the value of d = " + d);

        c = msg.modPow(e, n);
        System.out.println("Encrypted message is : -");
        System.out.println(c);

        msgback = c.modPow(d, n);
        System.out.println("Decrypted message is : -");
        System.out.println(msgback);
    }

    static BigInteger gcd(BigInteger e, BigInteger z) {
        if (e.equals(BigInteger.ZERO))
            return z;
        else
            return gcd(z.mod(e), e);
    }
}
