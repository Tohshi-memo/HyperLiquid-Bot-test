# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T07:52:23.993037+00:00`
- Price records: `672`
- Market context records: `2542`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_major_24h` score `5.5155` n `116` status `ready` deltaP `13.2663` edge `0.6362` maxDD `-16.2014`
- `market_context_high->crypto_alt_4h` score `5.2769` n `153` status `ready` deltaP `23.6161` edge `0.5502` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.253` n `116` status `ready` deltaP `19.3307` edge `0.3417` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.6795` n `153` status `ready` deltaP `16.8191` edge `0.3755` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.8739` n `153` status `ready` deltaP `10.5651` edge `0.1907` maxDD `-3.7312`
- `market_context_high->equity_24h` score `1.4558` n `116` status `ready` deltaP `20.546` edge `0.0514` maxDD `-3.0311`
- `market_context_high->crypto_alt_1h` score `1.1309` n `153` status `ready` deltaP `9.6415` edge `0.1487` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6798` n `153` status `ready` deltaP `8.1846` edge `0.1215` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.517` n `116` status `ready` deltaP `5.2143` edge `0.1064` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.1462` n `116` status `ready` deltaP `-0.1556` edge `0.685` maxDD `-41.2179`
- `market_context_high->unknown_1h` score `-0.1381` n `153` status `ready` deltaP `3.405` edge `0.0348` maxDD `-2.8543`
- `market_context_high->index_4h` score `-0.1673` n `153` status `ready` deltaP `5.8206` edge `0.0314` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.3043` n `153` status `ready` deltaP `2.631` edge `0.0065` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.3305` n `153` status `ready` deltaP `1.0352` edge `0.0042` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.3826` n `153` status `ready` deltaP `1.8786` edge `0.0132` maxDD `-2.9823`
- `market_context_high->commodity_1h` score `-0.3838` n `153` status `ready` deltaP `3.814` edge `0.0132` maxDD `-4.3601`
- `market_context_high->equity_1h` score `-0.7659` n `153` status `ready` deltaP `0.3053` edge `0.018` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8192` n `153` status `ready` deltaP `3.7014` edge `0.0458` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.858` n `116` status `ready` deltaP `2.4365` edge `0.0032` maxDD `-2.3556`
- `market_context_high->fx_4h` score `-0.8882` n `153` status `ready` deltaP `-0.0219` edge `0.0121` maxDD `-0.8774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
