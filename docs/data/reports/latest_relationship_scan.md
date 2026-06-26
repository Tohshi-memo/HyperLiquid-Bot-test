# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T15:52:29.240973+00:00`
- Price records: `672`
- Market context records: `4842`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7616`

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

- `market_context_high->unknown_1h` score `13.3942` n `110` status `ready` deltaP `9.7115` edge `1.0932` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.6036` n `98` status `ready` deltaP `24.1382` edge `0.8108` maxDD `-3.0471`
- `market_context_high->unknown_24h` score `4.5562` n `93` status `ready` deltaP `22.0654` edge `0.271` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `3.0266` n `98` status `ready` deltaP `15.3061` edge `0.2854` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `1.8725` n `98` status `ready` deltaP `11.5761` edge `0.2853` maxDD `-7.1265`
- `market_context_high->metal_4h` score `0.2732` n `98` status `ready` deltaP `10.5898` edge `0.0653` maxDD `-4.7365`
- `market_context_high->index_4h` score `0.207` n `98` status `ready` deltaP `6.8255` edge `0.0277` maxDD `-0.7334`
- `market_context_high->equity_1h` score `0.1183` n `110` status `ready` deltaP `3.4758` edge `0.0536` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.0854` n `98` status `ready` deltaP `7.6002` edge `0.0104` maxDD `-0.788`
- `market_context_high->crypto_alt_1h` score `-0.1185` n `110` status `ready` deltaP `5.8928` edge `0.0546` maxDD `-6.0592`
- `market_context_high->equity_4h` score `-0.1338` n `98` status `ready` deltaP `8.8197` edge `0.0622` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `-0.2046` n `98` status `ready` deltaP `11.1871` edge `0.0164` maxDD `-4.377`
- `market_context_high->commodity_1h` score `-0.3043` n `110` status `ready` deltaP `1.9134` edge `0.0142` maxDD `-1.278`
- `market_context_high->crypto_major_1h` score `-0.3615` n `110` status `ready` deltaP `3.8922` edge `0.0667` maxDD `-8.4525`
- `market_context_high->index_1h` score `-0.6001` n `110` status `ready` deltaP `-1.6576` edge `0.0096` maxDD `-0.7054`
- `market_context_high->metal_1h` score `-0.7816` n `110` status `ready` deltaP `0.4055` edge `-0.0023` maxDD `-4.7154`
- `market_context_high->fx_1h` score `-1.2966` n `110` status `ready` deltaP `-6.2575` edge `-0.0043` maxDD `-0.6295`
- `market_context_high->fx_24h` score `-1.8518` n `93` status `ready` deltaP `-6.3732` edge `-0.0108` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-3.3332` n `93` status `ready` deltaP `11.9624` edge `0.0038` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.6813` n `93` status `ready` deltaP `-8.1765` edge `-0.1446` maxDD `-24.085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
