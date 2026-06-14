import { NextRequest, NextResponse } from "next/server";
import { getToken } from "next-auth/jwt";
import { jwtVerify } from "jose";

function secret() {
  return new TextEncoder().encode(process.env.NEXTAUTH_SECRET!);
}

export async function middleware(req: NextRequest) {
  const token = await getToken({
    req,
    secret: process.env.NEXTAUTH_SECRET!,
    decode: async ({ token: raw }) => {
      if (!raw) return null;
      try {
        const { payload } = await jwtVerify(raw, secret());
        return payload as Record<string, unknown>;
      } catch {
        return null;
      }
    },
  });

  if (!token) {
    return NextResponse.redirect(new URL("/login", req.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/builder/:path*", "/learn/:path*", "/analytics/:path*", "/admin/:path*"],
};
