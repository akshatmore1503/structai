import Link from "next/link";
import { Clock } from "lucide-react";
import type { Topic } from "@/types";

const DIFF = {
  beginner:     { label: "Beginner",     color: "#059669", bg: "#ECFDF5", border: "#A7F3D0" },
  intermediate: { label: "Intermediate", color: "#D97706", bg: "#FFFBEB", border: "#FDE68A" },
  advanced:     { label: "Advanced",     color: "#DC2626", bg: "#FEF2F2", border: "#FECACA" },
};

export function TopicCard({ topic }: { topic: Topic }) {
  const d = DIFF[topic.difficulty];
  return (
    <Link
      href={`/learn/${topic.id}`}
      className="group block rounded-2xl p-5 h-full bg-white transition-all duration-200 hover:-translate-y-0.5"
      style={{ border: "1px solid #E8E9F0" }}
      onMouseEnter={(e) => {
        const el = e.currentTarget as HTMLElement;
        el.style.borderColor = "#D1D5DB";
        el.style.boxShadow = "0 8px 24px rgba(0,0,0,0.07)";
      }}
      onMouseLeave={(e) => {
        const el = e.currentTarget as HTMLElement;
        el.style.borderColor = "#E8E9F0";
        el.style.boxShadow = "none";
      }}
    >
      <div className="flex items-start justify-between mb-4">
        <span className="text-[24px] leading-none">{topic.icon}</span>
        <span
          className="badge text-[10px] font-bold uppercase tracking-wide"
          style={{ background: d.bg, color: d.color, border: `1px solid ${d.border}` }}
        >
          {d.label}
        </span>
      </div>

      <h3
        className="leading-snug mb-2"
        style={{
          fontSize: 14,
          fontWeight: 700,
          color: "#0A0E2E",
          letterSpacing: "-0.01em",
          fontFamily: "'Space Grotesk', system-ui",
        }}
      >
        {topic.title}
      </h3>
      <p style={{ fontSize: 12, lineHeight: 1.6, color: "#9CA3AF" }}>
        {topic.description}
      </p>

      <div className="flex items-center gap-1.5 mt-5" style={{ fontSize: 11, color: "#D1D5DB" }}>
        <Clock size={11} />
        <span>{topic.estimated_minutes} min read</span>
      </div>
    </Link>
  );
}
