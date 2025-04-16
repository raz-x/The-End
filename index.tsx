// pages/index.tsx

import { useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import Hero from "@/components/Hero";
import About from "@/components/About";
import Projects from "@/components/Projects";
import Skills from "@/components/Skills";
import Contact from "@/components/Contact";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import LoadingScreen from "@/components/LoadingScreen";
import Head from "next/head";

export default function Home() {
  useEffect(() => {
    // Optional: implement GSAP or ScrollTrigger effects here
  }, []);

  return (
    <>
      <Head>
        <title>Mohamed Rashid | Beginner Web Developer</title>
        <meta name="description" content="Personal portfolio of Mohamed Rashid, a beginner web developer." />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta charSet="UTF-8" />
      </Head>

      <main className="scroll-smooth font-sans bg-white text-gray-900">
        <LoadingScreen />
        <Header />
        <AnimatePresence mode="wait">
          <section id="hero">
            <Hero />
          </section>
          <section id="about">
            <About />
          </section>
          <section id="projects">
            <Projects />
          </section>
          <section id="skills">
            <Skills />
          </section>
          <section id="contact">
            <Contact />
          </section>
        </AnimatePresence>
        <Footer />
      </main>
    </>
  );
          }
