# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T11:37:31.126525+00:00`
- Price records: `672`
- Market context records: `7664`
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

- `market_context_high->index_1h` score `0.0164` n `146` status `ready` deltaP `5.9114` edge `0.0106` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.2025` n `146` status `ready` deltaP `7.7065` edge `0.0187` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2513` n `146` status `ready` deltaP `2.0548` edge `0.0173` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3292` n `145` status `ready` deltaP `9.4545` edge `0.0183` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4475` n `146` status `ready` deltaP `0.6273` edge `-0.0045` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5743` n `146` status `ready` deltaP `4.6259` edge `0.0469` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6489` n `146` status `ready` deltaP `0.9392` edge `0.0151` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7032` n `146` status `ready` deltaP `1.6066` edge `0.0052` maxDD `-2.2943`
- `market_context_high->fx_1h` score `-0.7434` n `146` status `ready` deltaP `-1.4727` edge `-0.0022` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.7696` n `146` status `ready` deltaP `7.0755` edge `0.0243` maxDD `-3.2774`
- `market_context_high->commodity_24h` score `-1.0816` n `145` status `ready` deltaP `8.0128` edge `0.0148` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.0821` n `146` status `ready` deltaP `2.1299` edge `0.046` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.2176` n `146` status `ready` deltaP `8.9792` edge `0.0518` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.5325` n `146` status `ready` deltaP `-1.4334` edge `-0.0558` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7099` n `146` status `ready` deltaP `-2.7376` edge `0.0447` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.9013` n `146` status `ready` deltaP `-0.5383` edge `0.1742` maxDD `-20.4824`
- `market_context_high->metal_24h` score `-2.2871` n `146` status `ready` deltaP `-3.2772` edge `0.0543` maxDD `-7.3868`
- `market_context_high->equity_24h` score `-2.4428` n `145` status `ready` deltaP `12.4475` edge `0.0944` maxDD `-34.5784`
- `market_context_high->fx_4h` score `-2.7131` n `146` status `ready` deltaP `-7.882` edge `-0.0051` maxDD `-2.1425`
- `market_context_high->index_24h` score `-3.609` n `145` status `ready` deltaP `-21.2592` edge `-0.0362` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
