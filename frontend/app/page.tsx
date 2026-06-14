"use client";
import { signIn, useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { Cpu, ArrowRight } from "lucide-react";

const FEATURES = [
  { num: "01", title: "Instant Architecture",   desc: "Paste a problem. Get a full system design in seconds — nodes, edges, and tech stack included." },
  { num: "02", title: "Interactive Diagrams",   desc: "Click any component to understand why it was chosen and what the trade-offs are." },
  { num: "03", title: "Learn & Quiz Mode",       desc: "AI-generated quizzes on caching, databases, CAP theorem, message queues, and more." },
  { num: "04", title: "Export Reports",          desc: "Download polished PDF or Markdown reports ready for interviews and presentations." },
];

const TECH = ["GPT-4o", "FAISS", "LangGraph", "FastAPI", "Next.js 14", "MongoDB"];

export default function LandingPage() {
  const { data: session } = useSession();
  const router = useRouter();
  useEffect(() => { if (session) router.push("/dashboard"); }, [session, router]);

  return (
    <main
      style={{
        minHeight: "100vh",
        background: "linear-gradient(160deg, #EEF2FF 0%, #EDE8FF 40%, #F3EEFF 70%, #EDF2FF 100%)",
        color: "#0A0E2E",
        overflowX: "hidden",
      }}
    >
      {/* ── NAV ─────────────────────────────────────────────── */}
      <header
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          maxWidth: 1280,
          margin: "0 auto",
          padding: "24px 48px",
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <div
            style={{
              width: 34, height: 34, borderRadius: 10,
              background: "linear-gradient(135deg,#7c3aed,#5b21b6)",
              display: "flex", alignItems: "center", justifyContent: "center",
              boxShadow: "0 4px 16px rgba(124,58,237,0.4)",
            }}
          >
            <Cpu size={15} color="#fff" />
          </div>
          <span
            style={{
              fontSize: 17, fontWeight: 700,
              fontFamily: "'Space Grotesk', system-ui",
              color: "#0A0E2E",
              letterSpacing: "-0.02em",
            }}
          >
            StructAI
          </span>
        </div>

        <button
          onClick={() => signIn("google", { callbackUrl: "/dashboard" })}
          style={{
            fontSize: 13, fontWeight: 600, padding: "9px 22px",
            borderRadius: 10, cursor: "pointer",
            background: "#0A0E2E", color: "#fff", border: "none",
            letterSpacing: "-0.01em",
            transition: "opacity .15s",
          }}
          onMouseEnter={(e) => ((e.currentTarget as HTMLButtonElement).style.opacity = "0.85")}
          onMouseLeave={(e) => ((e.currentTarget as HTMLButtonElement).style.opacity = "1")}
        >
          Sign in →
        </button>
      </header>

      {/* ── HERO ────────────────────────────────────────────── */}
      <section
        style={{
          maxWidth: 1280,
          margin: "0 auto",
          padding: "56px 48px 72px",
          position: "relative",
        }}
      >
        {/* Badge */}
        <div
          style={{
            display: "inline-flex", alignItems: "center", gap: 8,
            padding: "6px 16px", borderRadius: 99, marginBottom: 52,
            background: "rgba(124,58,237,0.08)",
            border: "1px solid rgba(124,58,237,0.2)",
            color: "#7c3aed", fontSize: 11, fontWeight: 700,
            letterSpacing: "0.1em", textTransform: "uppercase",
          }}
        >
          ✦ &nbsp;GPT-4o · FAISS · LangGraph
        </div>

        {/* Giant heading */}
        <h1
          style={{
            fontFamily: "'Space Grotesk', system-ui",
            fontWeight: 900,
            lineHeight: 0.92,
            letterSpacing: "-0.04em",
            margin: 0,
            marginBottom: 48,
            userSelect: "none",
          }}
        >
          {/* Line 1 — filled */}
          <span
            style={{
              display: "block",
              fontSize: "clamp(68px, 10.5vw, 148px)",
              color: "#0A0E2E",
            }}
          >
            DESIGN
          </span>

          {/* Line 2 — outlined stroke */}
          <span
            style={{
              display: "block",
              fontSize: "clamp(68px, 10.5vw, 148px)",
              color: "transparent",
              WebkitTextStroke: "2.5px #7c3aed",
            }}
          >
            SYSTEMS
          </span>

          {/* Line 3 — smaller filled tagline */}
          <span
            style={{
              display: "block",
              fontSize: "clamp(28px, 4.2vw, 58px)",
              color: "#3A3F7A",
              marginTop: "0.18em",
              fontWeight: 700,
              letterSpacing: "-0.03em",
            }}
          >
            like a senior architect.
          </span>
        </h1>

        {/* Sub-row: description + CTA */}
        <div
          style={{
            display: "flex",
            alignItems: "flex-start",
            gap: 64,
            flexWrap: "wrap",
            marginBottom: 100,
          }}
        >
          <p
            style={{
              fontSize: 17,
              lineHeight: 1.7,
              maxWidth: 420,
              color: "#4A4F80",
              margin: 0,
              fontWeight: 400,
            }}
          >
            StructAI turns your problem statement into a complete, interactive
            system architecture — with explanations, trade-offs, and learning
            built in.
          </p>

          <div style={{ display: "flex", flexDirection: "column", gap: 12, flexShrink: 0 }}>
            <button
              onClick={() => signIn("google", { callbackUrl: "/dashboard" })}
              style={{
                display: "flex", alignItems: "center", gap: 10,
                padding: "15px 28px",
                background: "#0A0E2E", color: "#fff",
                fontSize: 15, fontWeight: 700, borderRadius: 14,
                border: "none", cursor: "pointer",
                boxShadow: "0 12px 40px rgba(10,14,46,0.2)",
                letterSpacing: "-0.02em",
                transition: "transform .15s, box-shadow .15s",
              }}
              onMouseEnter={(e) => {
                const el = e.currentTarget as HTMLButtonElement;
                el.style.transform = "translateY(-2px)";
                el.style.boxShadow = "0 16px 48px rgba(10,14,46,0.28)";
              }}
              onMouseLeave={(e) => {
                const el = e.currentTarget as HTMLButtonElement;
                el.style.transform = "translateY(0)";
                el.style.boxShadow = "0 12px 40px rgba(10,14,46,0.2)";
              }}
            >
              {/* Google icon */}
              <svg width="17" height="17" viewBox="0 0 24 24" style={{ flexShrink: 0 }}>
                <path fill="#fff" opacity=".9" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
                <path fill="#fff" opacity=".9" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
                <path fill="#fff" opacity=".9" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" />
                <path fill="#fff" opacity=".9" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
              </svg>
              Continue with Google
              <ArrowRight size={15} />
            </button>
            <p style={{ textAlign: "center", fontSize: 11, color: "#9090B4", margin: 0 }}>
              Free · No credit card
            </p>
          </div>
        </div>

        {/* Horizontal rule */}
        <div
          style={{
            width: "100%", height: 1,
            background: "linear-gradient(90deg, transparent, rgba(124,58,237,0.2), transparent)",
            marginBottom: 64,
          }}
        />

        {/* Feature grid */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
            gap: 40,
          }}
        >
          {FEATURES.map(({ num, title, desc }) => (
            <div key={num}>
              <div
                style={{
                  fontSize: 10, fontWeight: 800, letterSpacing: "0.12em",
                  color: "#a78bfa", marginBottom: 14, textTransform: "uppercase",
                }}
              >
                {num}
              </div>
              <h3
                style={{
                  fontSize: 15, fontWeight: 700, color: "#0A0E2E",
                  marginBottom: 8, letterSpacing: "-0.02em",
                  fontFamily: "'Space Grotesk', system-ui",
                }}
              >
                {title}
              </h3>
              <p style={{ fontSize: 13, lineHeight: 1.65, color: "#636399" }}>
                {desc}
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* ── FOOTER ──────────────────────────────────────────── */}
      <footer
        style={{
          borderTop: "1px solid rgba(124,58,237,0.12)",
          padding: "24px 48px",
          maxWidth: 1280,
          margin: "0 auto",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          flexWrap: "wrap",
          gap: 12,
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <div
            style={{
              width: 22, height: 22, borderRadius: 7,
              background: "linear-gradient(135deg,#7c3aed,#5b21b6)",
              display: "flex", alignItems: "center", justifyContent: "center",
            }}
          >
            <Cpu size={10} color="#fff" />
          </div>
          <span style={{ fontSize: 13, fontWeight: 600, color: "#0A0E2E", letterSpacing: "-0.01em" }}>
            StructAI
          </span>
        </div>

        <div style={{ display: "flex", gap: 20, flexWrap: "wrap" }}>
          {TECH.map((t) => (
            <span key={t} style={{ fontSize: 11, color: "#8888B4", fontWeight: 500 }}>{t}</span>
          ))}
        </div>
      </footer>
    </main>
  );
}
