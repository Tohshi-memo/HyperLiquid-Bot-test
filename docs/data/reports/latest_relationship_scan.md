# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T10:37:26.708405+00:00`
- Price records: `672`
- Market context records: `7660`
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

- `market_context_high->index_1h` score `0.0328` n `146` status `ready` deltaP `6.2117` edge `0.0107` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1807` n `146` status `ready` deltaP `8.0059` edge `0.0195` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2599` n `146` status `ready` deltaP `1.9051` edge `0.0172` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3352` n `145` status `ready` deltaP `9.4545` edge `0.0178` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4217` n `146` status `ready` deltaP `1.0777` edge `-0.0042` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5642` n `146` status `ready` deltaP `4.7761` edge `0.0472` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6388` n `146` status `ready` deltaP `1.0889` edge `0.0154` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7032` n `146` status `ready` deltaP `1.6066` edge `0.0052` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.741` n `146` status `ready` deltaP `7.5342` edge `0.0249` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7422` n `146` status `ready` deltaP `-1.4727` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-1.0204` n `145` status `ready` deltaP `8.0128` edge `0.0199` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.1175` n `146` status `ready` deltaP `1.8251` edge `0.0435` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.2168` n `146` status `ready` deltaP `8.9792` edge `0.0519` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.5158` n `146` status `ready` deltaP `-1.134` edge `-0.0564` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7045` n `146` status `ready` deltaP `-2.7376` edge `0.0454` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.8094` n `146` status `ready` deltaP `0.0733` edge `0.1819` maxDD `-20.4824`
- `market_context_high->equity_24h` score `-2.1305` n `145` status `ready` deltaP `13.1443` edge `0.1298` maxDD `-34.5784`
- `market_context_high->metal_24h` score `-2.2707` n `146` status `ready` deltaP `-3.2772` edge `0.0564` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.7669` n `146` status `ready` deltaP `-8.4936` edge `-0.0055` maxDD `-2.1425`
- `market_context_high->index_24h` score `-3.5298` n `145` status `ready` deltaP `-20.5623` edge `-0.0307` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
