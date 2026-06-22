"use client";
import { X, Lightbulb, GitFork, AlertTriangle, BookOpen, Sparkles } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { Spinner } from "@/components/ui/Spinner";
import type { ArchNode, ComponentExplanation } from "@/types";

interface Props {
  node: ArchNode | null;
  explanation: ComponentExplanation | null;
  loading: boolean;
  onClose: () => void;
}

export function ExplainerPanel({ node, explanation, loading, onClose }: Props) {
  return (
    <AnimatePresence>
      {node && (
        <motion.div
          key={node.id}
          initial={{ x: "100%", opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          exit={{ x: "100%", opacity: 0 }}
          transition={{ type: "spring", stiffness: 320, damping: 32 }}
          className="absolute right-0 top-0 h-full w-[360px] flex flex-col z-20 overflow-hidden"
          style={{
            background: "#0E0E16",
            borderLeft: "1px solid rgba(255,255,255,0.07)",
            boxShadow: "-16px 0 40px rgba(0,0,0,0.4)",
          }}
        >
          {/* Header */}
          <div
            className="flex items-start justify-between px-5 py-4 flex-shrink-0"
            style={{ borderBottom: "1px solid rgba(255,255,255,0.06)" }}
          >
            <div className="flex-1 min-w-0 mr-3">
              <h3 className="text-[14px] font-semibold text-white leading-tight truncate">
                {node.label}
              </h3>
              <p className="text-[11px] mt-0.5 truncate" style={{ color: "#4E4E60" }}>
                {node.tech}
              </p>
            </div>
            <button
              onClick={onClose}
              className="p-1.5 rounded-[7px] transition-all duration-150 flex-shrink-0"
              style={{ color: "#4E4E60" }}
              onMouseEnter={(e) => {
                (e.currentTarget as HTMLElement).style.background = "rgba(255,255,255,0.07)";
                (e.currentTarget as HTMLElement).style.color = "#EEEEF0";
              }}
              onMouseLeave={(e) => {
                (e.currentTarget as HTMLElement).style.background = "transparent";
                (e.currentTarget as HTMLElement).style.color = "#4E4E60";
              }}
            >
              <X size={14} />
            </button>
          </div>

          {/* Body */}
          <div className="flex-1 overflow-y-auto px-5 py-5 space-y-5">
            {loading ? (
              <div className="flex flex-col items-center justify-center h-48 gap-3">
                <div className="relative">
                  <Spinner className="w-6 h-6" />
                  <div
                    className="absolute inset-0 rounded-full"
                    style={{ boxShadow: "0 0 16px rgba(99,102,241,0.4)" }}
                  />
                </div>
                <p className="text-[12px]" style={{ color: "#4E4E60" }}>
                  Generating explanation…
                </p>
              </div>
            ) : explanation ? (
              <>
                <Section icon={<Lightbulb size={12} />} title="What it is" color="#818cf8">
                  <p className="text-[13px] leading-relaxed" style={{ color: "#AEAEBF" }}>
                    {explanation.what}
                  </p>
                </Section>

                <Section icon={<GitFork size={12} />} title="Why it was chosen" color="#34d399">
                  <p className="text-[13px] leading-relaxed" style={{ color: "#AEAEBF" }}>
                    {explanation.why}
                  </p>
                </Section>

                <Section icon={<AlertTriangle size={12} />} title="Trade-offs" color="#fbbf24">
                  <p className="text-[13px] leading-relaxed" style={{ color: "#AEAEBF" }}>
                    {explanation.trade_offs}
                  </p>
                </Section>

                {explanation.alternatives?.length > 0 && (
                  <Section icon={<Sparkles size={12} />} title="Alternatives" color="#c084fc">
                    <div className="flex flex-wrap gap-1.5">
                      {explanation.alternatives.map((alt) => (
                        <span
                          key={alt}
                          className="px-2.5 py-1 rounded-full text-[11px] font-medium"
                          style={{
                            background: "rgba(192,132,252,0.1)",
                            border: "1px solid rgba(192,132,252,0.2)",
                            color: "#c084fc",
                          }}
                        >
                          {alt}
                        </span>
                      ))}
                    </div>
                  </Section>
                )}

                {explanation.learn_more && (
                  <Section icon={<BookOpen size={12} />} title="Dig deeper" color="#38bdf8">
                    <p className="text-[13px] leading-relaxed" style={{ color: "#AEAEBF" }}>
                      {explanation.learn_more}
                    </p>
                  </Section>
                )}
              </>
            ) : (
              <div className="flex flex-col items-center justify-center h-48 text-center">
                <div
                  className="w-10 h-10 rounded-[10px] flex items-center justify-center mb-3"
                  style={{ background: "rgba(99,102,241,0.1)", border: "1px solid rgba(99,102,241,0.2)" }}
                >
                  <Lightbulb size={17} style={{ color: "#6366f1" }} />
                </div>
                <p className="text-[13px] font-medium text-white mb-1">Click a node</p>
                <p className="text-[12px]" style={{ color: "#4E4E60" }}>
                  Select any component to see its explanation
                </p>
              </div>
            )}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

function Section({
  icon, title, color, children,
}: {
  icon: React.ReactNode;
  title: string;
  color: string;
  children: React.ReactNode;
}) {
  return (
    <div>
      <div className="flex items-center gap-1.5 mb-2.5">
        <span style={{ color }}>{icon}</span>
        <span
          className="text-[10px] font-semibold uppercase tracking-widest"
          style={{ color }}
        >
          {title}
        </span>
      </div>
      {children}
    </div>
  );
}
