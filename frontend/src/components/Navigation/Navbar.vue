<template>
  <nav class="bg-gray-50 border-gray-200 px-2 sm:px-4 py-4 rounded dark:bg-gray-800">
    <div class="container flex  flex-wrap justify-between items-center mx-auto">
      <a href="/" class="flex items-center ">
          <!-- <img src="/static/images/michael.png" class=" h-8 w-8 sm:h-12 sm:w-12  rounded-full object-cover" alt="Flowbite Logo" /> -->
          <span class="self-center text-lg text-gray-600 font-semibold whitespace-nowrap dark:text-white ml-2">Michael K. Kamau </span>
      </a>
      <button data-collapse-toggle="mobile-menu" type="button" @click="toggleMenu()" class="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="mobile-menu-2" aria-expanded="false">
        <span class="sr-only">Open main menu</span>
        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
        <svg class="hidden w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
      </button>
      <div :class="[menu_expanded ? 'block' : 'hidden']"  class=" w-full md:block md:w-auto" id="mobile-menu">
        <ul class="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium">
          <li>
            <a  href="/" class="block py-2 pr-4 pl-3 md:p-0 dark:text-white ext-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-emerald-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700" :class="{ ' text-white bg-emerald-700 rounded md:bg-transparent md:text-emerald-700' : active_url  ==   '/'}" aria-current="page">Home</a>
          </li>
          <li>
            <a href="/about/" class="block py-2 pr-4 pl-3 md:p-0 dark:text-white ext-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-emerald-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700" :class="{ ' text-white bg-emerald-700 rounded md:bg-transparent md:text-emerald-700' : active_url  ==   '/about/'}">About</a>
          </li>
          <li>
            <a href="/about/applications/"  class="block py-2 pr-4 pl-3 md:p-0 dark:text-white ext-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-emerald-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700" :class="{ ' text-white bg-emerald-700 rounded md:bg-transparent md:text-emerald-700' : active_url  ==   '/about/applications/'}">Applications</a>
          </li>
        
          <li>
            <a href="/about/contacts/" class="block py-2 pr-4 pl-3 md:p-0 dark:text-white ext-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-emerald-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700" :class="{ ' text-white bg-emerald-700 rounded md:bg-transparent md:text-emerald-700' : active_url  ==   '/about/contacts/'}">Contact</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    active_url: String,
  },
  data:function(){
    return{
      menu_expanded : false 
    }
  },
  methods:{
    toggleMenu(){
      this.menu_expanded=!this.menu_expanded
    }
  }
  
  
  }

</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>


</style>
