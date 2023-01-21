import React from 'react';
import { embedDashboard } from "@superset-ui/embedded-sdk";

embedDashboard({
  id: "af911979-b3cb-45be-8088-25b991160c18", // given by the Superset embedding UI
  supersetDomain: "http://localhost:8088",
  mountPoint: document.getElementById("my-superset-container"), // any html element that can contain an iframe
  fetchGuestToken: () => "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoiYWRtaW4ifSwicmVzb3VyY2VzIjpbeyJ0eXBlIjoiZGFzaGJvYXJkIiwiaWQiOiIxIn1dLCJybHNfcnVsZXMiOltdLCJpYXQiOjE2NzQxNDA0NTYuMjA5MTU0NCwiZXhwIjoxNjc0MTQwNzU2LjIwOTE1NDQsImF1ZCI6Imh0dHA6Ly8wLjAuMC4wOjgwODAvIiwidHlwZSI6Imd1ZXN0In0.7NFb5IsleerT1PX_mDYzWVXtLSRL06uiM7gwjZNDCXE",
  dashboardUiConfig: { // dashboard UI config: hideTitle, hideTab, hideChartControls, filters.visible, filters.expanded (optional)
      hideTitle: true,
      filters: {
          expanded: true,
      }
  },
  debug: true,
});

export const App = () => {
  return (
    <h1>Embedded Dashboard</h1>
  )
}
