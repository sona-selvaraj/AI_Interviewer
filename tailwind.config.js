/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#5b21b6",
        secondary: "#7c3aed",
        accent: "#6366f1",
        background: "#f3f4f6",
      },
      backgroundImage: {
        "gradient-bg": "linear-gradient(to right, #7c3aed, #5b21b6)",
        "login-bg": "url('/src/assets/login-bg.svg')",
        "signup-bg": "url('/src/assets/signup-bg.svg')",
      },
    },
  },
  plugins: [],
};
