"use client";
import { useEffect, useState } from "react";
import { motion } from "framer-motion";

interface Node {
  id: string;
  label: string;
  description: string;
  x: number;
  y: number;
}

interface Edge {
  from: string;
  to: string;
}

const NODES: Node[] = [
  { id: "client", label: "Client", description: "Web/Mobile", x: 250, y: 40 },
  { id: "gateway", label: "API Gateway", description: "Load Balancer", x: 250, y: 140 },
  { id: "auth", label: "Auth Service", description: "JWT & OAuth", x: 80, y: 240 },
  { id: "user", label: "User Service", description: "Profile & Data", x: 250, y: 240 },
  { id: "ai", label: "AI Engine", description: "LLM Processing", x: 420, y: 240 },
  { id: "db", label: "PostgreSQL", description: "Relational DB", x: 80, y: 360 },
  { id: "cache", label: "Redis", description: "Cache Layer", x: 250, y: 360 },
  { id: "vector", label: "Vector DB", description: "Embeddings", x: 420, y: 360 },
];

const EDGES: Edge[] = [
  { from: "client", to: "gateway" },
  { from: "gateway", to: "auth" },
  { from: "gateway", to: "user" },
  { from: "gateway", to: "ai" },
  { from: "auth", to: "db" },
  { from: "user", to: "db" },
  { from: "user", to: "cache" },
  { from: "ai", to: "vector" },
  { from: "ai", to: "cache" },
];

const nodeRadius = 22;

export default function ArchitectureHero() {
  const [animated, setAnimated] = useState(false);
  const [hoveredNode, setHoveredNode] = useState<string | null>(null);

  useEffect(() => {
    setAnimated(true);
    const interval = setInterval(() => {
      setAnimated(false);
      setTimeout(() => setAnimated(true), 500);
    }, 8000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="relative w-full h-full flex items-center justify-center overflow-hidden bg-gradient-to-br from-gray-50 via-transparent to-transparent rounded-xl">
      <svg
        viewBox="0 0 500 420"
        className="w-full h-full"
        style={{
          filter: "drop-shadow(0 20px 40px rgba(73, 80, 87, 0.15))",
        }}
      >
        <defs>
          {/* Node gradients */}
          <linearGradient id="nodeGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#ced4da" />
            <stop offset="100%" stopColor="#adb5bd" />
          </linearGradient>

          {/* Glow filter */}
          <filter id="nodeGlow">
            <feGaussianBlur stdDeviation="2" result="coloredBlur" />
            <feMerge>
              <feMergeNode in="coloredBlur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>

          {/* Strong glow for active nodes */}
          <filter id="activeNodeGlow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur" />
            <feMerge>
              <feMergeNode in="coloredBlur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>

          {/* Line glow */}
          <filter id="lineGlow">
            <feGaussianBlur stdDeviation="1.5" result="coloredBlur" />
            <feMerge>
              <feMergeNode in="coloredBlur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
        </defs>

        {/* Background grid */}
        <g opacity="0.03">
          {Array.from({ length: 5 }).map((_, i) => (
            <line
              key={`v-${i}`}
              x1={i * 125}
              y1="0"
              x2={i * 125}
              y2="420"
              stroke="#495057"
              strokeWidth="1"
            />
          ))}
          {Array.from({ length: 4 }).map((_, i) => (
            <line
              key={`h-${i}`}
              x1="0"
              y1={i * 140}
              x2="500"
              y2={i * 140}
              stroke="#495057"
              strokeWidth="1"
            />
          ))}
        </g>

        {/* Animated connection lines */}
        {EDGES.map((edge, idx) => {
          const fromNode = NODES.find((n) => n.id === edge.from);
          const toNode = NODES.find((n) => n.id === edge.to);
          if (!fromNode || !toNode) return null;

          return (
            <g key={`edge-${idx}`}>
              {/* Line background glow */}
              <motion.line
                x1={fromNode.x}
                y1={fromNode.y}
                x2={toNode.x}
                y2={toNode.y}
                stroke="#212529"
                strokeWidth="3"
                opacity="0.08"
                initial={{ pathLength: 0 }}
                animate={animated ? { pathLength: 1 } : { pathLength: 0 }}
                transition={{
                  delay: 0.3 + idx * 0.08,
                  duration: 0.8,
                  ease: "easeInOut",
                }}
                style={{ vectorEffect: "non-scaling-stroke" }}
              />
              {/* Main line */}
              <motion.line
                x1={fromNode.x}
                y1={fromNode.y}
                x2={toNode.x}
                y2={toNode.y}
                stroke="#adb5bd"
                strokeWidth="1.5"
                opacity="0.7"
                initial={{ pathLength: 0 }}
                animate={animated ? { pathLength: 1 } : { pathLength: 0 }}
                transition={{
                  delay: 0.3 + idx * 0.08,
                  duration: 0.8,
                  ease: "easeInOut",
                }}
                style={{ vectorEffect: "non-scaling-stroke" }}
              />
            </g>
          );
        })}

        {/* Nodes */}
        {NODES.map((node, idx) => (
          <g key={node.id}>
            {/* Pulsing outer ring */}
            <motion.circle
              cx={node.x}
              cy={node.y}
              r={nodeRadius}
              fill="none"
              stroke="#212529"
              strokeWidth="1"
              opacity="0.2"
              animate={
                hoveredNode === node.id
                  ? { r: nodeRadius + 12, opacity: 0.4, strokeWidth: 1.5 }
                  : animated
                    ? { r: [nodeRadius + 2, nodeRadius + 8, nodeRadius + 2] }
                    : { r: nodeRadius }
              }
              transition={{
                duration: hoveredNode === node.id ? 0.3 : 2.5,
                repeat: hoveredNode === node.id ? 0 : Infinity,
                ease: "easeInOut",
              }}
            />

            {/* Inner background circle */}
            <motion.circle
              cx={node.x}
              cy={node.y}
              r={nodeRadius}
              fill="white"
              opacity="0.95"
              initial={{ scale: 0 }}
              animate={animated ? { scale: 1 } : { scale: 0 }}
              transition={{
                delay: idx * 0.05,
                duration: 0.6,
                ease: "backOut",
              }}
            />

            {/* Node circle with gradient */}
            <motion.circle
              cx={node.x}
              cy={node.y}
              r={nodeRadius - 2}
              fill="url(#nodeGradient)"
              filter={hoveredNode === node.id ? "url(#activeNodeGlow)" : "url(#nodeGlow)"}
              initial={{ scale: 0 }}
              animate={animated ? { scale: 1 } : { scale: 0 }}
              whileHover={{ scale: 1.15 }}
              transition={{
                delay: idx * 0.05,
                duration: 0.6,
                ease: "backOut",
              }}
              onMouseEnter={() => setHoveredNode(node.id)}
              onMouseLeave={() => setHoveredNode(null)}
              style={{ cursor: "pointer" }}
            />

            {/* Main label */}
            <motion.text
              x={node.x}
              y={node.y + 2}
              textAnchor="middle"
              dominantBaseline="middle"
              fontSize="13"
              fontWeight="700"
              fill="#212529"
              fontFamily="'Ubuntu', -apple-system, sans-serif"
              initial={{ opacity: 0 }}
              animate={animated ? { opacity: 1 } : { opacity: 0 }}
              transition={{
                delay: idx * 0.05 + 0.3,
                duration: 0.5,
              }}
              pointerEvents="none"
            >
              {node.label}
            </motion.text>
          </g>
        ))}
      </svg>

      {/* Overlay gradient for blend */}
      <div className="absolute inset-0 pointer-events-none rounded-xl">
        <div className="absolute top-0 right-0 w-48 h-48 bg-gradient-to-bl from-white via-white to-transparent opacity-60" />
        <div className="absolute bottom-0 left-0 w-48 h-48 bg-gradient-to-tr from-white via-white to-transparent opacity-60" />
        <div className="absolute top-1/2 right-0 w-40 h-40 bg-gradient-to-l from-white via-white to-transparent opacity-50" />
      </div>
    </div>
  );
}
