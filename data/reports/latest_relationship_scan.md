# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T16:52:23.830414+00:00`
- Price records: `672`
- Market context records: `8005`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11806`

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

- `market_context_high->equity_24h` score `15.8663` n `91` status `ready` deltaP `26.1714` edge `1.2819` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.7398` n `91` status `ready` deltaP `35.9375` edge `0.4054` maxDD `0.0`
- `market_context_high->equity_4h` score `6.1513` n `104` status `ready` deltaP `24.613` edge `0.4378` maxDD `-5.1426`
- `market_context_high->metal_4h` score `2.5905` n `104` status `ready` deltaP `24.1675` edge `0.117` maxDD `-0.979`
- `market_context_high->index_4h` score `2.3792` n `104` status `ready` deltaP `24.9531` edge `0.0679` maxDD `-0.8791`
- `market_context_high->index_24h` score `2.1088` n `91` status `ready` deltaP `13.0438` edge `0.1558` maxDD `-1.3621`
- `market_context_high->commodity_24h` score `2.0557` n `91` status `ready` deltaP `20.5605` edge `0.1875` maxDD `-6.5945`
- `market_context_high->equity_1h` score `1.5828` n `104` status `ready` deltaP `13.3291` edge `0.1248` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2184` n `91` status `ready` deltaP `26.1294` edge `0.0361` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.8486` n `104` status `ready` deltaP `14.0143` edge `0.0203` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6793` n `104` status `ready` deltaP `9.8918` edge `0.0285` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.6112` n `104` status `ready` deltaP `9.6505` edge `0.1584` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.5511` n `104` status `ready` deltaP `6.1562` edge `0.1166` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `0.5085` n `104` status `ready` deltaP `10.3409` edge `0.0373` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0777` n `104` status `ready` deltaP `0.4491` edge `0.0303` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2488` n `104` status `ready` deltaP `0.5585` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.3522` n `104` status `ready` deltaP `6.1679` edge `0.0043` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5475` n `104` status `ready` deltaP `-0.5355` edge `-0.0043` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2277` n `104` status `ready` deltaP `-0.3166` edge `-0.0051` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.943` n `104` status `ready` deltaP `6.9035` edge `-0.1656` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
