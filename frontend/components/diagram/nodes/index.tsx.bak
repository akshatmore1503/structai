"use client";
import { Handle, Position, type NodeProps } from "@xyflow/react";
import { clsx } from "clsx";
import {
  Monitor, Database, Server, Zap, MessageSquare,
  Globe, HardDrive, Lock, Activity, Brain, Shield
} from "lucide-react";
import type { ArchNode } from "@/types";

const Gateway = Shield;
const Scale = ({ size, className }: { size?: number; className?: string }) => (
  <svg width={size ?? 16} height={size ?? 16} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className={className}>
    <line x1="12" y1="2" x2="12" y2="22" />
    <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
  </svg>
);

interface NodeCfg {
  color: string;
  bg: string;
  border: string;
  dot: string;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  Icon: React.ComponentType<any>;
}

const NODE_CONFIG: Record<string, NodeCfg> = {
  client:         { color: "#60a5fa", bg: "rgba(96,165,250,0.1)",  border: "rgba(96,165,250,0.25)",  dot: "#3b82f6", Icon: Monitor       },
  api_gateway:    { color: "#a78bfa", bg: "rgba(167,139,250,0.1)", border: "rgba(167,139,250,0.25)", dot: "#8b5cf6", Icon: Gateway       },
  load_balancer:  { color: "#34d399", bg: "rgba(52,211,153,0.1)",  border: "rgba(52,211,153,0.25)",  dot: "#10b981", Icon: Scale         },
  web_server:     { color: "#2dd4bf", bg: "rgba(45,212,191,0.1)",  border: "rgba(45,212,191,0.25)",  dot: "#14b8a6", Icon: Server        },
  database:       { color: "#fb923c", bg: "rgba(251,146,60,0.1)",  border: "rgba(251,146,60,0.25)",  dot: "#f97316", Icon: Database      },
  nosql_database: { color: "#fbbf24", bg: "rgba(251,191,36,0.1)",  border: "rgba(251,191,36,0.25)",  dot: "#f59e0b", Icon: Database      },
  cache:          { color: "#f87171", bg: "rgba(248,113,113,0.1)", border: "rgba(248,113,113,0.25)", dot: "#ef4444", Icon: Zap           },
  message_queue:  { color: "#facc15", bg: "rgba(250,204,21,0.1)",  border: "rgba(250,204,21,0.25)",  dot: "#eab308", Icon: MessageSquare },
  cdn:            { color: "#38bdf8", bg: "rgba(56,189,248,0.1)",  border: "rgba(56,189,248,0.25)",  dot: "#0ea5e9", Icon: Globe         },
  object_storage: { color: "#94a3b8", bg: "rgba(148,163,184,0.1)", border: "rgba(148,163,184,0.25)", dot: "#64748b", Icon: HardDrive     },
  auth_service:   { color: "#f472b6", bg: "rgba(244,114,182,0.1)", border: "rgba(244,114,182,0.25)", dot: "#ec4899", Icon: Lock          },
  monitoring:     { color: "#818cf8", bg: "rgba(129,140,248,0.1)", border: "rgba(129,140,248,0.25)", dot: "#6366f1", Icon: Activity      },
  ml_service:     { color: "#c084fc", bg: "rgba(192,132,252,0.1)", border: "rgba(192,132,252,0.25)", dot: "#a855f7", Icon: Brain         },
};

const DEFAULT_CFG: NodeCfg = {
  color: "#94a3b8", bg: "rgba(148,163,184,0.1)", border: "rgba(148,163,184,0.25)", dot: "#64748b", Icon: Server,
};

interface ArchNodeData extends ArchNode {
  selected?: boolean;
  onExplain?: (node: ArchNode) => void;
}

export function ArchitectureNode({ data, selected }: NodeProps) {
  const node = data as unknown as ArchNodeData;
  const cfg = NODE_CONFIG[node.type] ?? DEFAULT_CFG;
  const { Icon } = cfg;

  return (
    <div
      onClick={() => node.onExplain?.(node)}
      className="cursor-pointer transition-all duration-200"
      style={{
        background: selected ? cfg.bg : "rgba(18,18,26,0.95)",
        border: `1px solid ${selected ? cfg.border : "rgba(255,255,255,0.10)"}`,
        borderRadius: "12px",
        padding: "10px 14px",
        minWidth: "148px",
        maxWidth: "186px",
        boxShadow: selected
          ? `0 0 0 2px ${cfg.dot}60, 0 8px 24px rgba(0,0,0,0.4)`
          : "0 2px 12px rgba(0,0,0,0.35)",
        transform: selected ? "scale(1.04)" : "scale(1)",
      }}
    >
      <Handle
        type="target"
        position={Position.Left}
        style={{ background: cfg.dot, border: "2px solid rgba(0,0,0,0.6)", width: 8, height: 8 }}
      />
      <Handle
        type="source"
        position={Position.Right}
        style={{ background: cfg.dot, border: "2px solid rgba(0,0,0,0.6)", width: 8, height: 8 }}
      />

      <div className="flex items-start gap-2.5">
        <div
          className="flex-shrink-0 mt-0.5 w-6 h-6 rounded-[6px] flex items-center justify-center"
          style={{ background: cfg.bg, border: `1px solid ${cfg.border}` }}
        >
          <Icon size={12} style={{ color: cfg.color }} />
        </div>
        <div className="min-w-0 flex-1">
          <p className="text-[11px] font-semibold text-white leading-tight truncate">{node.label}</p>
          <p className="text-[10px] mt-0.5 truncate font-medium" style={{ color: cfg.color }}>
            {node.tech}
          </p>
        </div>
      </div>

      <p
        className="text-[10px] mt-2 leading-relaxed line-clamp-2"
        style={{ color: "#4E4E60" }}
      >
        {node.description}
      </p>
    </div>
  );
}

export const nodeTypes = {
  client: ArchitectureNode,
  api_gateway: ArchitectureNode,
  load_balancer: ArchitectureNode,
  web_server: ArchitectureNode,
  database: ArchitectureNode,
  nosql_database: ArchitectureNode,
  cache: ArchitectureNode,
  message_queue: ArchitectureNode,
  cdn: ArchitectureNode,
  object_storage: ArchitectureNode,
  auth_service: ArchitectureNode,
  monitoring: ArchitectureNode,
  ml_service: ArchitectureNode,
};
