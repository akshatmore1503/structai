"use client";
import { useCallback, useEffect, useMemo } from "react";
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  BackgroundVariant,
  useNodesState,
  useEdgesState,
  MarkerType,
  type Node,
  type Edge,
} from "@xyflow/react";
import dagre from "@dagrejs/dagre";
import "@xyflow/react/dist/style.css";
import { nodeTypes } from "./nodes";
import type { Architecture, ArchNode } from "@/types";

const DAGRE_GRAPH = new dagre.graphlib.Graph();
DAGRE_GRAPH.setDefaultEdgeLabel(() => ({}));

function applyDagreLayout(nodes: Node[], edges: Edge[]) {
  DAGRE_GRAPH.setGraph({ rankdir: "LR", nodesep: 80, ranksep: 120 });

  nodes.forEach((n) => DAGRE_GRAPH.setNode(n.id, { width: 180, height: 80 }));
  edges.forEach((e) => DAGRE_GRAPH.setEdge(e.source, e.target));

  dagre.layout(DAGRE_GRAPH);

  return nodes.map((n) => {
    const pos = DAGRE_GRAPH.node(n.id);
    return { ...n, position: { x: pos.x - 90, y: pos.y - 40 } };
  });
}

interface Props {
  architecture: Architecture;
  onNodeClick: (node: ArchNode) => void;
  selectedNodeId?: string | null;
}

export function ArchitectureCanvas({ architecture, onNodeClick, selectedNodeId }: Props) {
  const [nodes, setNodes, onNodesChange] = useNodesState<Node>([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState<Edge>([]);

  useEffect(() => {
    const rawNodes: Node[] = architecture.nodes.map((n) => ({
      id: n.id,
      type: n.type,
      position: { x: 0, y: 0 },
      data: { ...n, onExplain: onNodeClick, selected: n.id === selectedNodeId },
      selected: n.id === selectedNodeId,
    }));

    const rawEdges: Edge[] = architecture.edges.map((e) => ({
      id: e.id,
      source: e.source,
      target: e.target,
      label: e.label,
      animated: e.animated,
      style: { stroke: "#4b5563", strokeWidth: 1.5 },
      labelStyle: { fill: "#9ca3af", fontSize: 10 },
      labelBgStyle: { fill: "transparent" },
      markerEnd: { type: MarkerType.ArrowClosed, color: "#4b5563" },
    }));

    const layouted = applyDagreLayout(rawNodes, rawEdges);
    setNodes(layouted);
    setEdges(rawEdges);
  }, [architecture, selectedNodeId, onNodeClick]);

  return (
    <div className="w-full h-full">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        nodeTypes={nodeTypes}
        fitView
        fitViewOptions={{ padding: 0.15 }}
        minZoom={0.3}
        maxZoom={2}
        proOptions={{ hideAttribution: true }}
      >
        <Background variant={BackgroundVariant.Dots} gap={24} size={1} color="#1f2937" />
        <Controls />
        <MiniMap
          nodeColor={(n) => {
            const colors: Record<string, string> = {
              client: "#3b82f6", api_gateway: "#a855f7", load_balancer: "#22c55e",
              database: "#f97316", cache: "#ef4444", message_queue: "#eab308",
            };
            return colors[n.type ?? ""] ?? "#6b7280";
          }}
          maskColor="rgba(3,7,18,0.8)"
        />
      </ReactFlow>
    </div>
  );
}
