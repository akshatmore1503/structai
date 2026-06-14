import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50:  "#eef2ff",
          100: "#e0e7ff",
          300: "#a5b4fc",
          400: "#818cf8",
          500: "#6366f1",
          600: "#4f46e5",
          700: "#4338ca",
          900: "#312e81",
        },
        navy: {
          950: "#04050F",
          900: "#06071A",
          800: "#0C0E24",
          700: "#12143A",
        },
      },
      fontFamily: {
        display: ["Space Grotesk", "system-ui", "sans-serif"],
        sans:    ["Inter",         "system-ui", "sans-serif"],
        mono:    ["JetBrains Mono","Fira Code",  "monospace"],
      },
      animation: {
        "fade-up":  "fadeUp  0.5s cubic-bezier(.16,1,.3,1) both",
        "fade-in":  "fadeIn  0.3s ease both",
        "slide-in": "slideRight 0.35s cubic-bezier(.16,1,.3,1) both",
        "gradient": "gradientShift 6s ease infinite",
      },
      keyframes: {
        fadeUp:        { "0%": { opacity:"0", transform:"translateY(14px)" }, "100%": { opacity:"1", transform:"translateY(0)" } },
        fadeIn:        { "0%": { opacity:"0" }, "100%": { opacity:"1" } },
        slideRight:    { "0%": { transform:"translateX(20px)", opacity:"0" }, "100%": { transform:"translateX(0)", opacity:"1" } },
        gradientShift: { "0%,100%": { backgroundPosition:"0% 50%" }, "50%": { backgroundPosition:"100% 50%" } },
      },
    },
  },
  plugins: [],
};

export default config;
