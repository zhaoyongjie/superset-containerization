import React from 'react';
import { embedDashboard } from "@superset-ui/embedded-sdk";

embedDashboard({
  id: "<fill in embedded dashboard uuid>", // given by the Superset embedding UI
  supersetDomain: "http://localhost:8088",
  mountPoint: document.getElementById("my-superset-container"), // any html element that can contain an iframe
  fetchGuestToken: () => "<fill in the guest token>",
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
