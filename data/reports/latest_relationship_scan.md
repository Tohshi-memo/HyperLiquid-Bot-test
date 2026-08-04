# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T16:07:31.283786+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9839`

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

- `market_context_high->unknown_24h` score `31.0021` n `53` status `ready` deltaP `22.2451` edge `2.4395` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.1861` n `89` status `ready` deltaP `-0.1319` edge `0.5326` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `4.8434` n `53` status `ready` deltaP `27.139` edge `0.2702` maxDD `-1.4673`
- `market_context_high->commodity_24h` score `2.7453` n `53` status `ready` deltaP `28.2266` edge `0.2852` maxDD `-7.3801`
- `market_context_high->commodity_4h` score `1.1101` n `89` status `ready` deltaP `14.6153` edge `0.0797` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2142` n `89` status `ready` deltaP `15.7441` edge `0.0085` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2028` n `89` status `ready` deltaP `5.3556` edge `0.0228` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1865` n `89` status `ready` deltaP `8.0536` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.5041` n `89` status `ready` deltaP `1.016` edge `-0.018` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5589` n `89` status `ready` deltaP `-1.8317` edge `-0.01` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6547` n `89` status `ready` deltaP `3.8144` edge `0.0141` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.817` n `89` status `ready` deltaP `4.7907` edge `0.0023` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.0775` n `89` status `ready` deltaP `-1.9848` edge `-0.0055` maxDD `-3.0178`
- `market_context_high->fx_24h` score `-1.1717` n `53` status `ready` deltaP `0.1998` edge `0.0216` maxDD `-4.3126`
- `market_context_high->equity_1h` score `-1.7208` n `89` status `ready` deltaP `4.3884` edge `-0.0963` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9055` n `89` status `ready` deltaP `-10.5834` edge `-0.0483` maxDD `-4.7021`
- `market_context_high->metal_24h` score `-2.0317` n `53` status `ready` deltaP `-18.56` edge `-0.0199` maxDD `-2.6802`
- `market_context_high->unknown_1h` score `-3.4206` n `89` status `ready` deltaP `2.661` edge `-0.2581` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4809` n `89` status `ready` deltaP `-12.3966` edge `-0.0701` maxDD `-7.6533`
- `market_context_high->index_24h` score `-4.4027` n `53` status `ready` deltaP `-22.7038` edge `-0.1936` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
