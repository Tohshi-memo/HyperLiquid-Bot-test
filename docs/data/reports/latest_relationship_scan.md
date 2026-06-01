# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T13:22:25.218546+00:00`
- Price records: `672`
- Market context records: `2565`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->crypto_alt_4h` score `5.8112` n `147` status `ready` deltaP `25.2396` edge `0.5839` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.2105` n `116` status `ready` deltaP `13.2663` edge `0.6111` maxDD `-15.2264`
- `market_context_high->unknown_24h` score `4.9426` n `116` status `ready` deltaP `19.6659` edge `0.3136` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.957` n `147` status `ready` deltaP `17.2878` edge `0.3955` maxDD `-10.1468`
- `market_context_high->equity_24h` score `1.5723` n `116` status `ready` deltaP `20.546` edge `0.0524` maxDD `-2.0014`
- `market_context_high->unknown_4h` score `1.5476` n `147` status `ready` deltaP `9.8754` edge `0.1681` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.4033` n `147` status `ready` deltaP `11.1563` edge `0.1613` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.8112` n `147` status `ready` deltaP `9.1969` edge `0.1257` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.641` n `116` status `ready` deltaP `6.0584` edge `0.1111` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.2675` n `116` status `ready` deltaP `-0.6705` edge `0.6766` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.1106` n `147` status `ready` deltaP `7.5545` edge `0.043` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1368` n `147` status `ready` deltaP `3.9309` edge `0.0118` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4192` n `147` status `ready` deltaP `5.1153` edge `0.0188` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4415` n `147` status `ready` deltaP `0.9257` edge `0.012` maxDD `-2.9823`
- `market_context_high->unknown_1h` score `-0.4424` n `147` status `ready` deltaP `1.5775` edge `0.0196` maxDD `-2.6922`
- `market_context_high->fx_1h` score `-0.573` n `147` status `ready` deltaP `0.2587` edge `0.004` maxDD `-0.278`
- `market_context_high->fx_24h` score `-0.6397` n `116` status `ready` deltaP `1.5685` edge `0.0044` maxDD `-1.7496`
- `market_context_high->equity_1h` score `-0.7142` n `147` status `ready` deltaP `0.3514` edge `0.022` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8624` n `147` status `ready` deltaP `0.2105` edge `0.0127` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-0.9083` n `147` status `ready` deltaP `3.1888` edge `0.0418` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
