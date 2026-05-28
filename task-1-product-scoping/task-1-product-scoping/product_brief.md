Product Brief: Marketing Performance Intelligence Tool
Version: 1.0  
Author: Bharavi S  
Date:28 May 2026  
Status:Scoping — V1 Definition

---

1. Problem Statement

Marketing teams supporting multiple client brands are repeatedly asked one question:

> **"How is our marketing performing across channels right now, and where should we focus?"**

Today, answering this question means someone manually logs into several tools, exports data, and stitches together a response. The result:

- The answer looks **different every time**, depending on who pulls it
- It takes **longer than it should**
- If the person who usually does it is unavailable, **the question goes unanswered**
- There is **no single source of truth** — knowledge is locked in one person's head

This is not a reporting problem. It is a **data access and consistency problem**.

--- 

2. Goal

Build an internal tool that makes answering this question:
- **Faster** — available on demand, not dependent on someone's availability
- **Consistent** — the same question always returns the same structured answer
- **Accessible** — usable by anyone on the team, not just the analyst who knows where everything lives

**Hard constraint:** The team will not change their existing tools or workflows. This tool must fit around what they already use.

---

3. Users

Primary User — Internal Analyst / Team Member
- Needs to answer performance questions quickly, for themselves or for a client
- Currently spends 30–90 minutes pulling data manually before they can answer
- Wants: one place to look, always up to date, no manual work

Secondary User — Team Lead / Account Manager
- Needs to check on any client at any time without asking the analyst
- Wants: a quick overview they can trust without digging into raw data

Future User (V2) — Client
- Currently receives manually prepared reports on a delay
- Wants: self-serve access to their own brand's performance
- **Explicitly out of scope for V1**

---

4. The Tool: Overview

Name (working): Marketing Pulse

**What it is:**  
A two-layer internal tool combining:
1. **An automated performance dashboard** (V1) — always-on, always-updated view of marketing performance across channels
2. **AI-Assisted Insights Layer** (V2) — lets users ask questions in plain English and get instant answers backed by real data

---

5. V1 Scope — The Dashboard

What V1 does

Data Connections
- Connects to tools the team already uses (e.g. Google Ads, Meta Ads, HubSpot, LinkedIn Ads)
- Pulls performance data automatically on a daily schedule
- No manual exports, no copy-pasting, no human in the loop

The Dashboard View
- One unified view per client brand
- Key metrics shown per channel:
  - **Spend** (daily / weekly / monthly)
  - **Impressions**
  - **Clicks**
  - **Conversions**
  - **Cost per result** (CPL, CPA, ROAS depending on channel)
- Week-on-week and month-on-month comparisons
- Simple visual indicators: 🟢 up, 🔴 down, ⚪ flat

Alerts
- Automated flag when a key metric moves significantly (e.g. ROAS drops >20% week-on-week)
- Delivered via the team's existing communication tool (email or Slack — whichever they already use)
- No new tool required to receive alerts

What V1 does NOT include (and why)

| Excluded from V1 | Reason |
|---|---|
| AI / chat interface | Trust in data must be established before intelligence is layered on top. If the data is wrong, AI answers are wrong. |
| Recommendations engine | Requires clean baseline data and time to validate. Premature recommendations erode trust. |
| Custom date range filtering | Adds UI complexity. Default windows (7d, 30d, 90d) cover 90% of use cases. |
| Cross-channel attribution modelling | Technically complex. Needs clean data history first. |
| Client-facing portal / login | Focus on internal users first. Client access adds auth complexity and support burden. |
| Campaign-level drill-down | Channel-level is sufficient for V1. Drill-down is a V2 feature. |

V1 Success Metric
> Any team member can open the tool and answer *"how is [client brand] performing?"* in under 60 seconds — without asking anyone, at any time.

---

6. V2 Scope — The AI Layer

Built on top of a stable, trusted V1 data foundation.

### What V2 adds

#### AI Chat Interface
- User types a plain English question:
  - *"How is Nike's Meta campaign performing this week?"*
  - *"Which channel had the best ROAS last month?"*
  - *"Why did conversions drop on Google Ads?"*
- AI queries the underlying data and responds with numbers + context
- Every answer shows the source data behind it — no black box

Auto-Generated Weekly Summaries
- Every Monday, the tool generates a performance summary per client brand
- Replaces the manual weekly report someone currently writes
- Can be sent directly to clients or used in internal review

Recommendations Layer
- AI surfaces insights based on trends:
  - *"Meta CPL is 40% higher than last month — consider reviewing creative"*
  - *"Google Ads is outperforming ROAS target — opportunity to scale"*
- Framed as suggestions, not decisions — human remains in the loop

Cross-Channel View + Attribution
- Combined performance view across all channels
- Basic attribution modelling — which channel is driving conversions?
- Budget allocation view — spend vs. performance by channel

Custom Filters
- Filter by date range, channel, campaign, client brand
- Side-by-side period comparisons

Client-Facing Portal
- Clients get read-only access to their brand's data
- Can ask the AI questions without going through the internal team
- Reduces back-and-forth between clients and account managers

V2 Success Metric
> A client asks *"how did our campaigns do last month?"* — the team shares a link and the client finds the answer themselves in under 2 minutes, with no analyst involvement.

---

7. Feature Comparison: V1 vs V2

| Feature | V1 | V2 |
|---|---|---|
| Automated data pull from existing tools | ✅ | ✅ |
| Unified dashboard per client brand | ✅ | ✅ |
| Key metrics by channel | ✅ | ✅ |
| Week-on-week / month-on-month comparison | ✅ | ✅ |
| Automated alerts | ✅ | ✅ |
| AI chat interface | ❌ | ✅ |
| Auto-generated weekly summaries | ❌ | ✅ |
| Recommendations layer | ❌ | ✅ |
| Cross-channel attribution | ❌ | ✅ |
| Campaign-level drill-down | ❌ | ✅ |
| Custom date range filtering | ❌ | ✅ |
| Client-facing portal | ❌ | ✅ |

---

8. Data Architecture

### Where the data comes from
- Marketing platforms via their native APIs (Google Ads API, Meta Marketing API, HubSpot API, etc.)
- Data pulled on a scheduled basis (daily, overnight)
- Raw data stored in a centralised data warehouse (e.g. BigQuery)

How it flows

```
[Marketing Platforms] 
        ↓  (API pull — scheduled daily)
[Data Pipeline / ETL]
        ↓  (clean, transform, standardise)
[Central Data Warehouse — BigQuery]
        ↓  (query layer)
[Dashboard — V1]    [AI Chat Layer — V2]
        ↓                    ↓
[Internal Team]        [Internal Team + Clients]
```

Data reliability considerations
- All data pulls are logged — if a source fails, it is flagged immediately
- Stale data is clearly marked in the UI (e.g. "Last updated: 2 days ago ⚠️")
- No data is shown without a clear timestamp — users always know how fresh it is

---

9. What Would Make Users Trust This Tool

This is the most important question in V1. A dashboard no one trusts is worse than no dashboard at all.

Trust is built by:
1. **Showing the source** — every number shows where it came from and when it was last updated
2. **Being honest about gaps** — if a data source failed or data is missing, say so clearly rather than showing zeros
3. **Matching existing numbers** — in the first weeks, users will cross-check against the tools they already use. The numbers must match.
4. **Starting narrow** — better to show 5 metrics that are always correct than 20 that are sometimes wrong

---

10. Open Questions (To Revisit)

| Question | Why it matters |
|---|---|
| Which marketing platforms does the team actually use? | Determines which API integrations to build first |
| How is data currently organised — by client brand, by campaign? | Determines the data model and dashboard structure |
| Who maintains the tool after it's built? | Affects build decisions — simpler is more maintainable |
| What does a "significant" metric change mean to this team? | Needed to calibrate alerts correctly |
| Is there a preference for dashboard tool (Looker, custom, etc.)? | Affects build vs. buy decision |

---

11. What I Would Revisit With More Time

- **User interviews** — I have assumed the primary user is the internal analyst. A 30-minute conversation with two or three team members would either confirm this or reveal a different primary use case entirely.
- **Existing tool audit** — Before scoping data connections, I would want to see exactly which platforms the team uses and whether those platforms have accessible APIs.
- **V1 build vs. buy decision** — For the dashboard layer, tools like Looker Studio or Metabase connected to BigQuery might get to V1 faster than a custom build. Worth evaluating.
- **Alert thresholds** — The right thresholds for automated alerts need input from the team. Wrong thresholds mean either alert fatigue or missed signals.

---

12. Decisions Made and Why

| Decision | Reasoning |
|---|---|
| No AI in V1 | AI answers are only as good as the data underneath. Establishing data trust first prevents the AI layer from inheriting data quality problems. |
| No client access in V1 | Internal users are the people who will test, validate, and give feedback. Adding clients too early introduces support complexity before the product is stable. |
| Daily refresh (not real-time) | Most marketing performance questions are day-level questions, not minute-level. Real-time adds significant infrastructure complexity for minimal user benefit in V1. |
| Alerts via existing channels | The team will not change their tools. Pushing alerts into email or Slack (whichever they already use) means zero behaviour change required to receive them. |
| Channel-level metrics, not campaign-level | Channel-level answers the primary question. Campaign-level is a drill-down that adds complexity without unlocking the core use case. |

---
