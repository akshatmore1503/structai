import type { NextAuthOptions } from "next-auth";
import GoogleProvider from "next-auth/providers/google";
import { SignJWT, jwtVerify } from "jose";

function secret() {
  return new TextEncoder().encode(process.env.NEXTAUTH_SECRET!);
}

export const authOptions: NextAuthOptions = {
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),
  ],
  session: { strategy: "jwt" },
  jwt: {
    encode: async ({ token }) => {
      const { exp, iat, jti, ...rest } = token as Record<string, unknown>;
      return new SignJWT(rest)
        .setProtectedHeader({ alg: "HS256" })
        .setExpirationTime("30d")
        .sign(secret());
    },
    decode: async ({ token }) => {
      if (!token) return null;
      try {
        const { payload } = await jwtVerify(token, secret());
        return payload as Record<string, unknown>;
      } catch {
        return null;
      }
    },
  },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.email = user.email;
        token.name = user.name;
        token.picture = user.image;
      }
      return token;
    },
    async session({ session, token }) {
      if (session.user) {
        session.user.email = token.email as string;
        session.user.name = token.name as string;
        session.user.image = token.picture as string;
      }
      // Re-encode the token as a plain HS256 JWT string for FastAPI
      const { exp, iat, jti, ...rest } = token as Record<string, unknown>;
      const accessToken = await new SignJWT(rest)
        .setProtectedHeader({ alg: "HS256" })
        .setExpirationTime("30d")
        .sign(secret());
      (session as unknown as Record<string, unknown>).accessToken = accessToken;
      return session;
    },
  },
  pages: {
    signIn: "/login",
    error: "/login",
  },
};
