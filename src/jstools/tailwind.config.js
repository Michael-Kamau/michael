module.exports = {
  mode: 'jit',
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  content: [
    '../**/templates/*.html',
    '../**/templates/**/*.html',
    '../templates/*.html'
],
  theme: {
      extend: {},
  },
  variants: {},
  plugins: [],
}
