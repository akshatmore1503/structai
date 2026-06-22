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
        steel: {
          50:  "#f8f9fa",
          100: "#e9ecef",
          200: "#dee2e6",
          300: "#ced4da",
          400: "#adb5bd",
          500: "#6c757d",
          600: "#495057",
          700: "#343a40",
          800: "#212529",
        },
      },
      fontFamily: {
        display: ["Ubuntu", "system-ui", "sans-serif"],
        sans:    ["Ubuntu", "system-ui", "sans-serif"],
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
