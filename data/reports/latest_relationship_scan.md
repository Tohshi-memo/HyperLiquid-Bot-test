# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T03:22:30.369545+00:00`
- Price records: `672`
- Market context records: `8475`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6267.0965` n `52` status `ready` deltaP `44.0438` edge `522.0065` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.2497` n `61` status `ready` deltaP `22.5909` edge `0.4299` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2032` n `61` status `ready` deltaP `18.3226` edge `0.0805` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7937` n `64` status `ready` deltaP `16.5513` edge `0.0868` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.308` n `61` status `ready` deltaP `16.9458` edge `0.1939` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `1.2869` n `61` status `ready` deltaP `7.1496` edge `0.1867` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `0.6144` n `64` status `ready` deltaP `10.2077` edge `0.0634` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3438` n `64` status `ready` deltaP `7.064` edge `0.0482` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1173` n `64` status `ready` deltaP `5.8851` edge `0.0039` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.05` n `61` status `ready` deltaP `11.6429` edge `0.0223` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0301` n `64` status `ready` deltaP `4.07` edge `0.0084` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `-0.2689` n `64` status `ready` deltaP `1.9087` edge `0.0052` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.4544` n `61` status `ready` deltaP `-1.9218` edge `0.0222` maxDD `-0.7801`
- `news_risk_high->commodity_1h` score `-1.4998` n `64` status `ready` deltaP `-2.3578` edge `-0.0307` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5573` n `52` status `ready` deltaP `-27.7244` edge `-0.0461` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4188` n `61` status `ready` deltaP `-18.5526` edge `-0.1638` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.2696` n `52` status `ready` deltaP `-36.6186` edge `-0.2513` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9246` n `52` status `ready` deltaP `-13.3013` edge `-0.3944` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.3646` n `52` status `ready` deltaP `-34.8424` edge `-0.4145` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.3741` n `52` status `ready` deltaP `-30.1816` edge `-1.7108` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
