# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T13:07:32.828996+00:00`
- Price records: `672`
- Market context records: `7671`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14690`

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

- `market_context_high->index_1h` score `0.0211` n `146` status `ready` deltaP `5.9114` edge `0.0112` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1729` n `146` status `ready` deltaP `8.0059` edge `0.0205` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2326` n `146` status `ready` deltaP `2.2045` edge `0.0187` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.322` n `145` status `ready` deltaP `9.4545` edge `0.0189` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4334` n `146` status `ready` deltaP `0.7774` edge `-0.0037` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5345` n `146` status `ready` deltaP `4.7761` edge `0.051` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6419` n `146` status `ready` deltaP `1.0889` edge `0.015` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.7443` n `146` status `ready` deltaP `7.3813` edge `0.0255` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7543` n `146` status `ready` deltaP `-1.6229` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->commodity_4h` score `-0.8222` n `146` status `ready` deltaP `0.6892` edge `0.0014` maxDD `-2.2943`
- `market_context_high->crypto_alt_4h` score `-1.0077` n `146` status `ready` deltaP `2.5873` edge `0.0525` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1633` n `146` status `ready` deltaP `9.4366` edge `0.0557` maxDD `-14.4206`
- `market_context_high->commodity_24h` score `-1.1927` n `145` status `ready` deltaP `7.8385` edge `0.0067` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-1.5529` n `146` status `ready` deltaP `-1.7328` edge `-0.0555` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7076` n `146` status `ready` deltaP `-2.7376` edge `0.045` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.9428` n `146` status `ready` deltaP `-0.6912` edge `0.1699` maxDD `-20.4824`
- `market_context_high->metal_24h` score `-2.298` n `146` status `ready` deltaP `-3.2772` edge `0.0529` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.663` n `146` status `ready` deltaP `-7.2703` edge `-0.005` maxDD `-2.1425`
- `market_context_high->equity_24h` score `-2.8303` n `145` status `ready` deltaP `11.9248` edge `0.0482` maxDD `-34.5784`
- `market_context_high->index_24h` score `-3.686` n `145` status `ready` deltaP `-21.7818` edge `-0.0426` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
