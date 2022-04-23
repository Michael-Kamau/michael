import { createApp } from "vue";

import HelloWorld from "./components/HelloWorld";
import Navbar from "./components/Navbar";

const app = createApp({});

app.component("hello-world", HelloWorld);
app.component("navbar", Navbar);







app.mount("#app");
