import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Faraja - Public Project Tracker",
  description: "Track government projects for accountability"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
