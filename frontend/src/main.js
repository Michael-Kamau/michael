import { createApp } from "vue";

import HelloWorld from "./components/HelloWorld";
import Navbar from "./components/Navigation/Navbar";
import ContactForm from "./components/Myapp/Contact/ContactForm"

const app = createApp({});

app.component("hello-world", HelloWorld);
app.component("navbar", Navbar);
app.component("contact-form", ContactForm);







app.mount("#app");
