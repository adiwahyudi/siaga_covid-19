module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",    
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {        
        'bg-covid': "url('/img/background.jpg')",          
      }
    },
  },
  plugins: [],
}
