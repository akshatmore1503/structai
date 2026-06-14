"use client";
import { signIn } from "next-auth/react";
import { Cpu, ArrowRight } from "lucide-react";

export default function LoginPage() {
  return (
    <div
      className="min-h-screen flex items-center justify-center px-6"
      style={{ background: "#F8F9FB" }}
    >
      <div className="w-full max-w-[380px] animate-fade-up">

        {/* Card */}
        <div
          className="rounded-2xl p-8 bg-white"
          style={{ border: "1px solid #E8E9F0", boxShadow: "0 8px 32px rgba(0,0,0,0.06)" }}
        >
          {/* Logo */}
          <div className="flex flex-col items-center mb-8">
            <div
              className="w-12 h-12 rounded-2xl flex items-center justify-center mb-4"
              style={{ background: "#4F46E5", boxShadow: "0 4px 16px rgba(79,70,229,0.3)" }}
            >
              <Cpu size={22} className="text-white" />
            </div>
            <h1
              style={{
                fontSize: 20,
                fontWeight: 700,
                color: "#0A0E2E",
                letterSpacing: "-0.02em",
                fontFamily: "'Space Grotesk', system-ui",
              }}
            >
              Welcome to StructAI
            </h1>
            <p className="mt-1.5 text-center" style={{ fontSize: 13, color: "#9CA3AF" }}>
              Sign in to start designing systems with AI
            </p>
          </div>

          {/* Divider */}
          <div className="mb-6 h-px w-full" style={{ background: "#F3F4F6" }} />

          {/* Sign in button */}
          <button
            onClick={() => signIn("google", { callbackUrl: "/dashboard" })}
            className="w-full flex items-center justify-center gap-3 py-2.5 px-4 rounded-xl text-[14px] font-medium transition-all duration-200"
            style={{
              background: "#fff",
              border: "1px solid #E5E7EB",
              color: "#374151",
              boxShadow: "0 1px 3px rgba(0,0,0,0.04)",
            }}
            onMouseEnter={(e) => {
              const el = e.currentTarget as HTMLElement;
              el.style.background = "#F9FAFB";
              el.style.borderColor = "#D1D5DB";
            }}
            onMouseLeave={(e) => {
              const el = e.currentTarget as HTMLElement;
              el.style.background = "#fff";
              el.style.borderColor = "#E5E7EB";
            }}
          >
            <svg className="w-4 h-4 flex-shrink-0" viewBox="0 0 24 24">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
              <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
            </svg>
            Continue with Google
            <ArrowRight size={14} className="ml-auto" style={{ color: "#9CA3AF" }} />
          </button>

          <p className="text-center mt-5" style={{ fontSize: 11, color: "#D1D5DB" }}>
            By signing in you agree to our terms of service
          </p>
        </div>
      </div>
    </div>
  );
}
