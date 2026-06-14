"use client";
import { useEffect, useState } from "react";
import { getTopics } from "@/lib/api";
import { TopicCard } from "@/components/learn/TopicCard";
import { Spinner } from "@/components/ui/Spinner";
import type { Topic } from "@/types";

const FILTERS = ["all", "beginner", "intermediate", "advanced"] as const;

const FILTER_COLORS: Record<string, { active: string; bg: string }> = {
  all:          { active: "#4F46E5", bg: "#EEF2FF" },
  beginner:     { active: "#059669", bg: "#ECFDF5" },
  intermediate: { active: "#D97706", bg: "#FFFBEB" },
  advanced:     { active: "#DC2626", bg: "#FEF2F2" },
};

export default function LearnPage() {
  const [topics, setTopics] = useState<Topic[]>([]);
  const [filter, setFilter] = useState<typeof FILTERS[number]>("all");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getTopics().then(setTopics).finally(() => setLoading(false));
  }, []);

  const visible = filter === "all" ? topics : topics.filter((t) => t.difficulty === filter);

  return (
    <div className="max-w-5xl animate-fade-up">

      {/* ── HEADER ─────────────────────────────────────────── */}
      <div className="mb-10">
        <p className="section-label mb-3">( Learn Mode )</p>
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
          System Design Concepts.
        </h1>
        <p className="mt-2" style={{ fontSize: 15, color: "#6B7280" }}>
          Study a topic then test your understanding with an AI-generated quiz.
        </p>
      </div>

      {/* ── FILTERS ─────────────────────────────────────────── */}
      <div className="flex gap-2 mb-8">
        {FILTERS.map((f) => {
          const active = filter === f;
          const c = FILTER_COLORS[f];
          return (
            <button
              key={f}
              onClick={() => setFilter(f)}
              className="px-4 py-1.5 rounded-full text-[12px] font-semibold transition-all duration-150"
              style={active
                ? { background: c.bg, color: c.active, border: `1.5px solid ${c.active}` }
                : { background: "#fff", color: "#6B7280", border: "1px solid #E5E7EB" }
              }
            >
              {f.charAt(0).toUpperCase() + f.slice(1)}
            </button>
          );
        })}
      </div>

      {loading ? (
        <div className="flex justify-center py-14">
          <Spinner className="w-5 h-5" />
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {visible.map((topic, i) => (
            <div key={topic.id} className="animate-fade-up" style={{ animationDelay: `${i * 0.04}s` }}>
              <TopicCard topic={topic} />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
