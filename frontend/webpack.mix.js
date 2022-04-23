let mix = require('laravel-mix');
require('mix-tailwindcss');

mix.js('src/main.js', '../src/assets/js')
// mix.js('src/main.js', '../src/assets/js')
.sass('../src/assets/css/tailwind.scss', 'css/style.css')
.tailwind()
.vue()
.setPublicPath('../src/assets')
;