/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,py}"],
  theme: {
    extend: {
      colors: {},
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light", "dark", "cupcake", "lofi"],
  },
}
