# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T10:52:30.522640+00:00`
- Price records: `672`
- Market context records: `7661`
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

- `market_context_high->index_1h` score `0.0242` n `146` status `ready` deltaP `6.0616` edge `0.0106` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1815` n `146` status `ready` deltaP `8.0059` edge `0.0194` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2505` n `146` status `ready` deltaP `2.0548` edge `0.0174` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.334` n `145` status `ready` deltaP `9.4545` edge `0.0179` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4209` n `146` status `ready` deltaP `1.0777` edge `-0.0041` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5751` n `146` status `ready` deltaP `4.6259` edge `0.0468` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6481` n `146` status `ready` deltaP `0.9392` edge `0.0152` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.702` n `146` status `ready` deltaP `1.6066` edge `0.0053` maxDD `-2.2943`
- `market_context_high->fx_1h` score `-0.7422` n `146` status `ready` deltaP `-1.4727` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.7513` n `146` status `ready` deltaP `7.3813` edge `0.0246` maxDD `-3.2774`
- `market_context_high->commodity_24h` score `-1.0348` n `145` status `ready` deltaP `8.0128` edge `0.0187` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.1033` n `146` status `ready` deltaP `1.9775` edge `0.0443` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.216` n `146` status `ready` deltaP `8.9792` edge `0.052` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.529` n `146` status `ready` deltaP `-1.2837` edge `-0.0565` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7052` n `146` status `ready` deltaP `-2.7376` edge `0.0453` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.8369` n `146` status `ready` deltaP `-0.0796` edge `0.1794` maxDD `-20.4824`
- `market_context_high->equity_24h` score `-2.2167` n `145` status `ready` deltaP `12.9701` edge `0.1199` maxDD `-34.5784`
- `market_context_high->metal_24h` score `-2.2762` n `146` status `ready` deltaP `-3.2772` edge `0.0557` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.7546` n `146` status `ready` deltaP `-8.3407` edge `-0.0055` maxDD `-2.1425`
- `market_context_high->index_24h` score `-3.5514` n `145` status `ready` deltaP `-20.7365` edge `-0.0323` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
