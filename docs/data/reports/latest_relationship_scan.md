# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T11:07:34.888203+00:00`
- Price records: `672`
- Market context records: `7662`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14697`

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

- `market_context_high->index_1h` score `0.0156` n `146` status `ready` deltaP `5.9114` edge `0.0105` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1916` n `146` status `ready` deltaP `7.8562` edge `0.0191` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2412` n `146` status `ready` deltaP `2.2045` edge `0.0176` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3328` n `145` status `ready` deltaP `9.4545` edge `0.018` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4303` n `146` status `ready` deltaP `0.9276` edge `-0.0043` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5775` n `146` status `ready` deltaP `4.6259` edge `0.0465` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6489` n `146` status `ready` deltaP `0.9392` edge `0.0151` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7032` n `146` status `ready` deltaP `1.6066` edge `0.0052` maxDD `-2.2943`
- `market_context_high->fx_1h` score `-0.7434` n `146` status `ready` deltaP `-1.4727` edge `-0.0022` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.7601` n `146` status `ready` deltaP `7.2284` edge `0.0245` maxDD `-3.2774`
- `market_context_high->commodity_24h` score `-1.0504` n `145` status `ready` deltaP `8.0128` edge `0.0174` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.0884` n `146` status `ready` deltaP `2.1299` edge `0.0452` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.2152` n `146` status `ready` deltaP `8.9792` edge `0.0521` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.5433` n `146` status `ready` deltaP `-1.4334` edge `-0.0567` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7068` n `146` status `ready` deltaP `-2.7376` edge `0.0451` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.8581` n `146` status `ready` deltaP `-0.2325` edge `0.1777` maxDD `-20.4824`
- `market_context_high->metal_24h` score `-2.2801` n `146` status `ready` deltaP `-3.2772` edge `0.0552` maxDD `-7.3868`
- `market_context_high->equity_24h` score `-2.2944` n `145` status `ready` deltaP `12.7959` edge `0.1111` maxDD `-34.5784`
- `market_context_high->fx_4h` score `-2.7412` n `146` status `ready` deltaP `-8.1878` edge `-0.0054` maxDD `-2.1425`
- `market_context_high->index_24h` score `-3.5713` n `145` status `ready` deltaP `-20.9107` edge `-0.0337` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
