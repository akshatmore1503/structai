"use client";
import { useEffect, useState, useCallback } from "react";
import { useParams, useRouter } from "next/navigation";
import { ArrowLeft, Download, FileText, ChevronRight } from "lucide-react";
import { getDesign, explainComponent, downloadPdf, downloadMarkdown } from "@/lib/api";
import { ArchitectureCanvas } from "@/components/diagram/ArchitectureCanvas";
import { ExplainerPanel } from "@/components/diagram/ExplainerPanel";
import { Spinner } from "@/components/ui/Spinner";
import type { Design, ArchNode, ComponentExplanation } from "@/types";

export default function DesignViewPage() {
  const { designId } = useParams<{ designId: string }>();
  const router = useRouter();

  const [design, setDesign] = useState<Design | null>(null);
  const [loading, setLoading] = useState(true);
  const [selectedNode, setSelectedNode] = useState<ArchNode | null>(null);
  const [explanation, setExplanation] = useState<ComponentExplanation | null>(null);
  const [explainLoading, setExplainLoading] = useState(false);
  const [exportLoading, setExportLoading] = useState<"pdf" | "md" | null>(null);

  useEffect(() => {
    getDesign(designId)
      .then(setDesign)
      .catch(() => router.push("/builder"))
      .finally(() => setLoading(false));
  }, [designId, router]);

  const handleNodeClick = useCallback(
    async (node: ArchNode) => {
      setSelectedNode(node);
      setExplanation(null);
      const cached = design?.explanations?.[node.id];
      if (cached) { setExplanation(cached as ComponentExplanation); return; }
      setExplainLoading(true);
      try {
        const exp = await explainComponent(designId, node.id);
        setExplanation(exp);
        setDesign((prev) =>
          prev ? { ...prev, explanations: { ...prev.explanations, [node.id]: exp } } : prev
        );
      } catch { setExplanation(null); }
      finally { setExplainLoading(false); }
    },
    [design, designId]
  );

  async function handleExport(format: "pdf" | "md") {
    setExportLoading(format);
    try {
      if (format === "pdf") await downloadPdf(designId);
      else await downloadMarkdown(designId);
    } finally { setExportLoading(null); }
  }

  if (loading) {
    return (
      <div className="h-screen flex items-center justify-center" style={{ background: "#07070C" }}>
        <Spinner className="w-6 h-6" />
      </div>
    );
  }

  if (!design?.architecture) {
    return (
      <div className="h-screen flex items-center justify-center" style={{ background: "#07070C" }}>
        <p className="text-[14px]" style={{ color: "#6B6B80" }}>Design not found or still generating.</p>
      </div>
    );
  }

  return (
    <div className="h-screen flex flex-col" style={{ background: "#07070C" }}>
      {/* Toolbar */}
      <div
        className="flex items-center justify-between px-4 py-2.5 flex-shrink-0 z-10"
        style={{
          background: "rgba(14,14,20,0.92)",
          backdropFilter: "blur(16px)",
          borderBottom: "1px solid rgba(255,255,255,0.06)",
        }}
      >
        <div className="flex items-center gap-3 min-w-0">
          <button
            onClick={() => router.push("/builder")}
            className="p-1.5 rounded-[7px] transition-all duration-150 flex-shrink-0"
            style={{ color: "#5A5A70" }}
            onMouseEnter={(e) => {
              (e.currentTarget as HTMLElement).style.background = "rgba(255,255,255,0.07)";
              (e.currentTarget as HTMLElement).style.color = "#EEEEF0";
            }}
            onMouseLeave={(e) => {
              (e.currentTarget as HTMLElement).style.background = "transparent";
              (e.currentTarget as HTMLElement).style.color = "#5A5A70";
            }}
          >
            <ArrowLeft size={15} />
          </button>
          <div
            className="w-px h-4 flex-shrink-0"
            style={{ background: "rgba(255,255,255,0.08)" }}
          />
          <p className="text-[13px] font-medium text-white truncate max-w-lg">
            {design.problem_statement}
          </p>
          <ChevronRight size={13} style={{ color: "#4E4E60" }} className="flex-shrink-0" />
          <span className="text-[12px] flex-shrink-0" style={{ color: "#4E4E60" }}>Architecture</span>
        </div>

        <div className="flex items-center gap-2 flex-shrink-0">
          <button
            onClick={() => handleExport("md")}
            disabled={!!exportLoading}
            className="btn-ghost text-[12px] py-1.5 px-3"
          >
            {exportLoading === "md" ? <Spinner className="w-3 h-3" /> : <FileText size={13} />}
            Markdown
          </button>
          <button
            onClick={() => handleExport("pdf")}
            disabled={!!exportLoading}
            className="btn-primary text-[12px] py-1.5 px-3"
          >
            {exportLoading === "pdf" ? <Spinner className="w-3 h-3" /> : <Download size={13} />}
            Export PDF
          </button>
        </div>
      </div>

      {/* Tech stack bar */}
      <div
        className="flex items-center gap-2 px-4 py-2 flex-shrink-0 overflow-x-auto"
        style={{ background: "rgba(11,11,18,0.8)", borderBottom: "1px solid rgba(255,255,255,0.04)" }}
      >
        <span className="text-[11px] flex-shrink-0 font-medium" style={{ color: "#3E3E52" }}>
          Stack
        </span>
        <div
          className="w-px h-3 flex-shrink-0"
          style={{ background: "rgba(255,255,255,0.06)" }}
        />
        {design.architecture.tech_stack.map((t) => (
          <span
            key={t}
            className="badge flex-shrink-0 text-[10px]"
            style={{
              background: "rgba(99,102,241,0.08)",
              color: "#818cf8",
              border: "1px solid rgba(99,102,241,0.18)",
            }}
          >
            {t}
          </span>
        ))}
      </div>

      {/* Canvas + Panel */}
      <div className="flex-1 relative overflow-hidden">
        <ArchitectureCanvas
          architecture={design.architecture}
          onNodeClick={handleNodeClick}
          selectedNodeId={selectedNode?.id}
        />
        <ExplainerPanel
          node={selectedNode}
          explanation={explanation}
          loading={explainLoading}
          onClose={() => { setSelectedNode(null); setExplanation(null); }}
        />
      </div>
    </div>
  );
}
