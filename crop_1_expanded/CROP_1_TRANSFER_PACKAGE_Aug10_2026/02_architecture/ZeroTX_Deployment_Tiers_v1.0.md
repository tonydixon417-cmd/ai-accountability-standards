# ZeroTX Deployment Tiers v1.0
*Reframing local processing as a design decision for scalable corporate compliance*

---

## Executive Summary

The transition to agentic AI has forced organizations into an artificial compromise: accept massive data transmission risks to achieve centralized oversight, or enforce absolute on-device privacy at the cost of corporate visibility. 

This paper reframes the Zero-Transmission Architecture (**ZeroTX**) not as a rigid technological constraint, but as a flexible deployment decision. By decoupling the execution of AI models from the auditing of AI sessions, ZeroTX resolves the conflict between privacy and compliance. This document details three distinct deployment modes designed to meet the operational realities of any size organization—from a five-person boutique firm to a highly regulated global enterprise.

---

## The Core Philosophy: Flexibility by Design

A fundamental tension exists between the agile workflows of small, highly specialized teams and the strict oversight requirements of enterprise operations. As Contrail founder Tony Dixon notes:

> **"A five-man office runs different than a large corp."**

This is not an engineering limitation; it is an organizational truth. Designing an AI accountability standard that forces a multinational financial institution to operate like a local medical clinic—or vice versa—is an architecture flaw. The system must adapt to the operational scaling of the organization.

The physics of AI safety, drift, and session logging remain identical across all scales. The implementation, however, is a deployment choice. 

### The Aviation Parallel: Scaling the Instrument Panel

In aviation, the fundamental principles of flight recording do not change based on the size of the airframe:

*   A **Cessna 172** and a **Boeing 737** both fly in the same atmosphere and obey the same laws of aerodynamics.
*   Both aircraft require flight recorders to establish accountability, trace system failures, and reconstruct decisions.
*   However, the implementation scales to match the complexity of the operation. A Cessna uses a lightweight, integrated engine monitor and GPS logger suitable for owner-operators and flight schools. A Boeing 737 is equipped with a crash-survivable Flight Data Recorder (FDR) and Cockpit Voice Recorder (CVR) that feed directly into a fleet-wide airline safety management system.

The physics are identical. The implementation scales.

ZeroTX applies this exact paradigm to AI accountability. The core engine—the AI Black Box (AIBB) standard—remains consistent, capturing the prompt, the response, and the drift analysis. The path those records take to satisfy compliance is determined by the deployment tier.

---

## The Three ZeroTX Deployment Tiers

```
+---------------------------------------------------------------------------------+
|                                 ZeroTX PURE                                     |
|  [ AI Engine ] <---> [ AIBB Session Log ] (Stored locally on-device)            |
+---------------------------------------------------------------------------------+
                                         |
                                         v
+---------------------------------------------------------------------------------+
|                              ZeroTX FEDERATED                                   |
|  [ AI Engine ] <---> [ AIBB Session Log ] ---> [ SHA-256 Cryptographic Hash ]   |
|                                                       |                         |
|                                                       v                         |
|                                         [ Central Compliance Ledger ]           |
+---------------------------------------------------------------------------------+
                                         |
                                         v
+---------------------------------------------------------------------------------+
|                              ZeroTX ENTERPRISE                                  |
|  [ AI Engine ] <---> [ AIBB Session Log ] ---> [ Encrypted Local Aggregator ]   |
|                                                       | (RBAC Access Only)      |
|                                                       v                         |
|                                         [ Org's Private Infrastructure ]        |
+---------------------------------------------------------------------------------+
```

### 1. ZeroTX Pure (Local Execution)
*Target: Small firms, independent practices, boutique consultancies, and HIPAA-sensitive environments.*

*   **Architecture:** AI session execution, analysis, and AIBB logging occur entirely within the local user's environment (e.g., the browser or local client). Zero data leaves the physical device.
*   **Compliance Posture:** HIPAA-safe by design, not by contract. Because no Protected Health Information (PHI) or corporate IP is ever transmitted to an external server, the HIPAA trigger is never pulled, eliminating the administrative overhead of negotiating Business Associate Agreements (BAAs).
*   **User Experience:** Maximum privacy and zero latency. The individual user maintains absolute custody of their "black box" session files, ready to be manually exported as a clean "Readback" document if an audit or client verification is requested.

### 2. ZeroTX Federated (Cryptographic Auditability)
*Target: Mid-sized firms, regional offices, and external contractor networks.*

*   **Architecture:** AI processing and session logs remain strictly on-device, preserving absolute privacy for the content of the session. However, upon session completion, the ZeroTX client automatically generates a cryptographic signature (such as a SHA-256 hash) of the local AIBB log. This metadata hash—containing no actual prompt text, document content, or response data—is securely transmitted to a centralized, corporate-controlled compliance ledger.
*   **Compliance Posture:** Zero transmission of raw data combined with absolute mathematical proof of record integrity. In the event of a regulatory inquiry, the organization can demand the local log from the operator and verify its authenticity against the central ledger's tamper-proof hash.
*   **Operational Advantage:** Allows compliance officers to verify that every single active AI session was recorded, analyzed, and logged, without violating the client's privacy or centralizing sensitive IP.

### 3. ZeroTX Enterprise (Aggregated Firewalls)
*Target: Highly regulated multinational corporations, financial institutions, and government agencies.*

*   **Architecture:** AI sessions run on-device, but logs are systematically pushed to a department-level or organization-wide secure aggregator residing within the company’s private cloud infrastructure (such as AWS GovCloud, private VPC, or on-premises servers). 
*   **Compliance Posture:** Data is transmitted, but it never crosses the organizational firewall or enters a third-party vendor's environment. Role-Based Access Control (RBAC) governs who can query the centralized AIBB logs, with strictly defined encryption keys managed by the enterprise's IT division.
*   **Operational Advantage:** Provides enterprise compliance departments with real-time dashboards, automated drift reporting, and consolidated audit trails across thousands of operators, while fully respecting the fundamental ZeroTX security boundary: zero external data transmission.

---

## Conclusion: Reframing the Compliance Narrative

The industry has treated on-device processing as a technical limitation that must be "solved" by transitioning back to cloud-centric logging. This is a profound misunderstanding of risk.

The Contrail System proves that on-device processing is a deliberate architecture. By standardizing the format of the AI flight record (AIBB) and offering scalable deployment paths (Pure, Federated, Enterprise), organizations can transition from a state of blind trust to structured accountability.

We do not force the Cessna pilot to install a commercial jetliner’s data suite, nor do we let the 737 captain fly without a flight recorder. We scale the implementation to match the operation. That is not a weakness—that is the product being flexible by design.
