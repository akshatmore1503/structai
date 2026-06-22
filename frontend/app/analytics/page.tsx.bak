"use client";
import { useEffect, useState } from "react";
import { TrendingUp, ArrowUpRight } from "lucide-react";
import { getMyStats } from "@/lib/api";
import { Spinner } from "@/components/ui/Spinner";
import type { UserStats } from "@/types";
import Link from "next/link";

const STATS = [
  { key: "total_designs"  as const, label: "Designs Created", suffix: ""  },
  { key: "total_quizzes"  as const, label: "Quizzes Taken",   suffix: ""  },
  { key: "avg_quiz_score" as const, label: "Avg Quiz Score",  suffix: "%" },
];

export default function AnalyticsPage() {
  const [stats, setStats] = useState<UserStats | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => { getMyStats().then(setStats).finally(() => setLoading(false)); }, []);

  if (loading) return <div className="flex justify-center py-20"><Spinner className="w-5 h-5" /></div>;
  if (!stats) return null;

  return (
    <div className="max-w-4xl animate-fade-up">

      {/* ── HEADER ─────────────────────────────────────────── */}
      <div className="mb-12">
        <p className="section-label mb-3">( Analytics )</p>
        <h1
          style={{
            fontFamily: "'Space Grotesk', system-ui",
            fontSize: 42,
            fontWeight: 900,
            letterSpacing: "-0.03em",
            lineHeight: 1.05,
            color: "#0A0E2E",
          }}
        >
          Your Progress.
        </h1>
        <p className="mt-2" style={{ fontSize: 15, color: "#6B7280" }}>
          Track your growth across designs and quizzes.
        </p>
      </div>

      {/* ── STATS — Bungee style large numbers ────────────── */}
      <div
        className="rounded-2xl bg-white mb-10"
        style={{ border: "1px solid #E8E9F0" }}
      >
        <div className="grid grid-cols-3 divide-x" style={{ borderColor: "#F3F4F6" }}>
          {STATS.map(({ key, label, suffix }) => (
            <div key={key} className="px-8 py-8">
              <p
                style={{
                  fontFamily: "'Space Grotesk', system-ui",
                  fontSize: 56,
                  fontWeight: 900,
                  letterSpacing: "-0.04em",
                  lineHeight: 1,
                  color: "#0A0E2E",
                  marginBottom: 8,
                }}
              >
                {stats[key]}{suffix}
              </p>
              <p style={{ fontSize: 12, fontWeight: 600, color: "#9CA3AF", letterSpacing: "0.05em", textTransform: "uppercase" }}>
                {label}
              </p>
            </div>
          ))}
        </div>
      </div>

      {/* ── RECENT DESIGNS ──────────────────────────────────── */}
      {stats.recent_designs.length > 0 && (
        <div className="mb-10">
          <div className="flex items-center justify-between mb-5">
            <p className="section-label">( Recent Designs )</p>
            <Link href="/builder" className="flex items-center gap-1 text-[12px] font-semibold" style={{ color: "#4F46E5" }}>
              View all <ArrowUpRight size={12} />
            </Link>
          </div>
          <div className="rounded-2xl overflow-hidden bg-white" style={{ border: "1px solid #E8E9F0" }}>
            {stats.recent_designs.map((d, i) => (
              <div
                key={d.id}
                className="flex items-center px-6 py-4 gap-4"
                style={{ borderTop: i > 0 ? "1px solid #F3F4F6" : "none" }}
              >
                <div
                  className="w-2 h-2 rounded-full flex-shrink-0"
                  style={{ background: "#4F46E5" }}
                />
                <p className="truncate flex-1" style={{ fontSize: 13, color: "#374151", fontWeight: 500 }}>
                  {d.problem_statement}
                </p>
                <p className="flex-shrink-0" style={{ fontSize: 11, color: "#D1D5DB" }}>
                  {new Date(d.created_at).toLocaleDateString("en-US", { month: "short", day: "numeric" })}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* ── QUIZ HISTORY ────────────────────────────────────── */}
      {stats.quiz_history.length > 0 && (
        <div>
          <p className="section-label mb-5">( Quiz History )</p>
          <div className="space-y-2">
            {stats.quiz_history.map((q, i) => {
              const good = q.score >= 70;
              return (
                <div
                  key={i}
                  className="rounded-2xl px-6 py-4 flex items-center gap-5 bg-white"
                  style={{ border: "1px solid #E8E9F0" }}
                >
                  <div
                    className="w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0"
                    style={{ background: good ? "#ECFDF5" : "#FFFBEB" }}
                  >
                    <TrendingUp size={16} style={{ color: good ? "#059669" : "#D97706" }} />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p style={{ fontSize: 13, fontWeight: 600, color: "#0A0E2E" }} className="truncate">
                      {q.topic}
                    </p>
                    <p className="mt-0.5" style={{ fontSize: 11, color: "#D1D5DB" }}>
                      {new Date(q.completed_at).toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" })}
                    </p>
                  </div>
                  <div className="flex items-center gap-4">
                    <div className="w-28 h-1.5 rounded-full overflow-hidden" style={{ background: "#F3F4F6" }}>
                      <div
                        className="h-full rounded-full"
                        style={{
                          width: `${q.score}%`,
                          background: good ? "#059669" : "#D97706",
                        }}
                      />
                    </div>
                    <span
                      style={{
                        fontSize: 15,
                        fontWeight: 900,
                        letterSpacing: "-0.03em",
                        color: good ? "#059669" : "#D97706",
                        fontFamily: "'Space Grotesk', system-ui",
                        minWidth: 44,
                        textAlign: "right",
                      }}
                    >
                      {q.score}%
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
