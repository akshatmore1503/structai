"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { ArrowRight, HelpCircle, ChevronRight, Wand2 } from "lucide-react";
import { generateDesign, submitClarifications } from "@/lib/api";
import { Spinner } from "@/components/ui/Spinner";

const EXAMPLES = [
  "URL shortener like bit.ly",
  "Real-time collab editor like Google Docs",
  "Food delivery like DoorDash",
  "Video streaming like Netflix",
  "Ride-sharing like Uber",
  "Chat app like Discord",
];

export default function BuilderPage() {
  const router = useRouter();
  const [problem, setProblem] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [designId, setDesignId] = useState<string | null>(null);
  const [questions, setQuestions] = useState<string[]>([]);
  const [answers, setAnswers] = useState<Record<string, string>>({});

  async function handleGenerate() {
    if (!problem.trim()) return;
    setLoading(true);
    setError("");
    try {
      const res = await generateDesign(problem.trim());
      if (res.status === "complete") {
        router.push(`/builder/${res.design_id}`);
      } else {
        setDesignId(res.design_id);
        setQuestions(res.clarifying_questions ?? []);
        setAnswers(Object.fromEntries((res.clarifying_questions ?? []).map((_, i) => [String(i), ""])));
      }
    } catch {
      setError("Generation failed. Please check your connection and try again.");
    } finally {
      setLoading(false);
    }
  }

  async function handleClarify() {
    if (!designId) return;
    setLoading(true);
    setError("");
    try {
      const clarifications = Object.fromEntries(
        questions.map((q, i) => [q, answers[String(i)] || "No preference"])
      );
      const res = await submitClarifications(designId, clarifications);
      router.push(`/builder/${res.design_id}`);
    } catch {
      setError("Failed. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  /* ── Clarification step ── */
  if (questions.length > 0) {
    return (
      <div className="p-10 max-w-xl animate-fade-up">
        <div className="flex items-center gap-3 mb-8">
          <div
            className="w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0"
            style={{ background: "#FFFBEB" }}
          >
            <HelpCircle size={18} style={{ color: "#D97706" }} />
          </div>
          <div>
            <h2 style={{ fontSize: 16, fontWeight: 700, color: "#0A0E2E" }}>
              A few quick questions
            </h2>
            <p style={{ fontSize: 12, color: "#9CA3AF" }}>Help us tailor the architecture to your needs</p>
          </div>
        </div>

        <div className="space-y-5 mb-7">
          {questions.map((q, i) => (
            <div key={i}>
              <label
                className="block mb-2"
                style={{ fontSize: 13, fontWeight: 600, color: "#374151" }}
              >
                {q}
              </label>
              <textarea
                rows={2}
                className="input resize-none"
                placeholder="Your answer (or skip for defaults)"
                value={answers[String(i)]}
                onChange={(e) => setAnswers((prev) => ({ ...prev, [String(i)]: e.target.value }))}
              />
            </div>
          ))}
        </div>

        {error && (
          <p className="mb-4" style={{ fontSize: 13, color: "#DC2626" }}>{error}</p>
        )}

        <div className="flex gap-3">
          <button onClick={handleClarify} disabled={loading} className="btn-primary">
            {loading ? <Spinner className="w-4 h-4" /> : <ChevronRight size={15} />}
            Generate Architecture
          </button>
          <button onClick={() => { setQuestions([]); setDesignId(null); }} className="btn-ghost">
            Start over
          </button>
        </div>
      </div>
    );
  }

  /* ── Main compose view ── */
  return (
    <div className="p-10">
      <div className="max-w-2xl mx-auto animate-fade-up">

        {/* ── HEADER ─────────────────────────────────────────── */}
        <div className="mb-8">
          <p className="section-label mb-3">( Design Builder )</p>
          <h1
            style={{
              fontFamily: "'Space Grotesk', system-ui",
              fontSize: 42,
              fontWeight: 900,
              letterSpacing: "-0.03em",
              lineHeight: 1.05,
              color: "#0A0E2E",
              marginBottom: 12,
            }}
          >
            Describe your system.
          </h1>
          <p style={{ fontSize: 15, color: "#6B7280", lineHeight: 1.65 }}>
            One sentence is enough. StructAI will ask clarifying questions if needed,
            then generate a production-grade architecture with interactive diagrams.
          </p>
        </div>

        {/* ── COMPOSE AREA ─────────────────────────────────── */}
        <div
          className="rounded-2xl overflow-hidden mb-5 bg-white"
          style={{ border: "1px solid #E8E9F0", boxShadow: "0 2px 12px rgba(0,0,0,0.04)" }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: 12, padding: "14px 18px", borderBottom: "1px solid #F3F4F6" }}>
            <div
              className="w-7 h-7 rounded-full flex items-center justify-center flex-shrink-0"
              style={{ background: "#4F46E5" }}
            >
              <Wand2 size={13} color="#fff" />
            </div>
            <span style={{ fontSize: 12, fontWeight: 600, color: "#374151" }}>AI Architecture Generator</span>
          </div>

          <textarea
            rows={8}
            placeholder="Design a scalable image hosting service that handles 5M uploads per day with global CDN distribution…"
            value={problem}
            onChange={(e) => setProblem(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) handleGenerate();
            }}
            style={{
              width: "100%",
              padding: "18px 20px",
              fontSize: 15,
              lineHeight: 1.6,
              color: "#0A0E2E",
              background: "#fff",
              border: "none",
              outline: "none",
              resize: "none",
              fontFamily: "'Inter', system-ui",
              caretColor: "#4F46E5",
            }}
          />

          <div
            className="flex items-center justify-between px-4 py-3"
            style={{ borderTop: "1px solid #F3F4F6" }}
          >
            <p style={{ fontSize: 11, color: "#D1D5DB", fontWeight: 500 }}>
              ⌘ + Enter to generate
            </p>
            <button
              onClick={handleGenerate}
              disabled={!problem.trim() || loading}
              className="btn-primary text-[13px] py-2 px-5"
            >
              {loading ? (
                <>
                  <Spinner className="w-3.5 h-3.5" />
                  Generating…
                </>
              ) : (
                <>
                  Generate
                  <ArrowRight size={13} />
                </>
              )}
            </button>
          </div>
        </div>

        {error && (
          <div
            className="flex items-center gap-2.5 px-4 py-3 rounded-xl mb-5"
            style={{ background: "#FEF2F2", border: "1px solid #FECACA", color: "#DC2626", fontSize: 13 }}
          >
            {error}
          </div>
        )}

        {/* ── EXAMPLES ─────────────────────────────────────── */}
        <div>
          <p className="section-label mb-3">Try an example</p>
          <div className="flex flex-wrap gap-2">
            {EXAMPLES.map((ex) => (
              <button
                key={ex}
                onClick={() => setProblem(`Design a ${ex.toLowerCase()}`)}
                className="text-[12px] font-medium px-3.5 py-1.5 rounded-full transition-all duration-150 bg-white"
                style={{ color: "#6B7280", border: "1px solid #E5E7EB" }}
                onMouseEnter={(e) => {
                  const el = e.currentTarget as HTMLElement;
                  el.style.color = "#4F46E5";
                  el.style.background = "#EEF2FF";
                  el.style.borderColor = "#A5B4FC";
                }}
                onMouseLeave={(e) => {
                  const el = e.currentTarget as HTMLElement;
                  el.style.color = "#6B7280";
                  el.style.background = "#fff";
                  el.style.borderColor = "#E5E7EB";
                }}
              >
                {ex}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
