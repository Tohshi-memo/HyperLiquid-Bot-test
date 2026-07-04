# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T16:22:29.363104+00:00`
- Price records: `672`
- Market context records: `5680`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8758`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->equity_24h` score `1.8841` n `203` status `ready` deltaP `16.0355` edge `0.558` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8798` n `253` status `ready` deltaP `11.683` edge `0.2182` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.433` n `253` status `ready` deltaP `8.7584` edge `0.1587` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.1843` n `253` status `ready` deltaP `5.7487` edge `0.1409` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2579` n `265` status `ready` deltaP `2.0037` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.419` n `265` status `ready` deltaP `2.8551` edge `0.0422` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.4882` n `265` status `ready` deltaP `0.7999` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5008` n `265` status `ready` deltaP `4.3894` edge `0.0297` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.5939` n `265` status `ready` deltaP `0.8841` edge `0.0048` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6213` n `265` status `ready` deltaP `4.4955` edge `0.0428` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.917` n `265` status `ready` deltaP `0.5598` edge `-0.0036` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-1.051` n `203` status `ready` deltaP `14.2087` edge `0.0475` maxDD `-3.0515`
- `market_context_high->fx_4h` score `-1.1691` n `253` status `ready` deltaP `3.9978` edge `0.0069` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2604` n `253` status `ready` deltaP `-0.3325` edge `0.0078` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.4946` n `203` status `ready` deltaP `6.3398` edge `0.0378` maxDD `-16.9906`
- `market_context_high->metal_4h` score `-2.8848` n `253` status `ready` deltaP `-11.8179` edge `-0.0535` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.779` n `253` status `ready` deltaP `-2.3047` edge `-0.032` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.8203` n `203` status `ready` deltaP `3.9306` edge `0.0178` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3132` n `203` status `ready` deltaP `-12.4401` edge `-0.2483` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.0831` n `203` status `ready` deltaP `-10.22` edge `-0.0779` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
