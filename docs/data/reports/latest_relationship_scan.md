# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T06:07:32.361027+00:00`
- Price records: `672`
- Market context records: `8487`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5860`

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

- `news_risk_high->unknown_24h` score `6270.2597` n `52` status `ready` deltaP `44.0438` edge `522.2701` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0512` n `64` status `ready` deltaP `22.1799` edge `0.4161` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0363` n `64` status `ready` deltaP `16.8064` edge `0.0767` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6774` n `64` status `ready` deltaP `15.8028` edge `0.0821` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.041` n `64` status `ready` deltaP `15.3963` edge `0.17` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `0.9853` n `64` status `ready` deltaP `5.9832` edge `0.164` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.6113` n `64` status `ready` deltaP `10.058` edge `0.064` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.336` n `64` status `ready` deltaP `6.9143` edge `0.0482` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1337` n `64` status `ready` deltaP `6.1845` edge `0.004` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0658` n `64` status `ready` deltaP `12.0808` edge `0.0207` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.0003` n `64` status `ready` deltaP `3.6209` edge `0.0075` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.1776` n `64` status `ready` deltaP `-0.1143` edge `0.0256` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.2713` n `64` status `ready` deltaP `1.9087` edge `0.005` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.5369` n `64` status `ready` deltaP `-2.8069` edge `-0.0308` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5453` n `52` status `ready` deltaP `-27.7244` edge `-0.0451` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.5179` n `64` status `ready` deltaP `-19.5503` edge `-0.1634` maxDD `-13.2872`
- `news_risk_high->metal_24h` score `-9.3668` n `52` status `ready` deltaP `-36.6186` edge `-0.2594` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9546` n `52` status `ready` deltaP `-13.3013` edge `-0.3969` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.8258` n `52` status `ready` deltaP `-36.7521` edge `-0.4402` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.9468` n `52` status `ready` deltaP `-32.0913` edge `-1.7458` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
