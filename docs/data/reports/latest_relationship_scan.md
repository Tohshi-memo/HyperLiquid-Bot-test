# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T20:22:27.737534+00:00`
- Price records: `672`
- Market context records: `4968`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `17.5545` n `100` status `ready` deltaP `8.4551` edge `1.4566` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.5486` n `92` status `ready` deltaP `29.8847` edge `0.8979` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.4956` n `92` status `ready` deltaP `21.832` edge `0.6015` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1944` n `92` status `ready` deltaP `22.329` edge `0.5859` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.9313` n `89` status `ready` deltaP `27.4695` edge `0.3454` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7611` n `92` status `ready` deltaP `14.1304` edge `0.1907` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5356` n `92` status `ready` deltaP `11.9897` edge `0.1226` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9377` n `92` status `ready` deltaP `11.8969` edge `0.045` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.8459` n `100` status `ready` deltaP `8.1497` edge `0.0735` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7844` n `100` status `ready` deltaP `5.6407` edge `0.1316` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3925` n `100` status `ready` deltaP `7.5988` edge `0.1019` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0466` n `100` status `ready` deltaP `2.9401` edge `0.0345` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.382` n `100` status `ready` deltaP `2.1018` edge `0.0125` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.4029` n `100` status `ready` deltaP `0.994` edge `0.0077` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-1.0795` n `92` status `ready` deltaP `6.1903` edge `-0.0067` maxDD `-4.9624`
- `market_context_high->fx_4h` score `-1.1052` n `92` status `ready` deltaP `-6.2168` edge `-0.0032` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.3422` n `89` status `ready` deltaP `-1.5313` edge `-0.0118` maxDD `-2.5204`
- `market_context_high->fx_1h` score `-1.4963` n `100` status `ready` deltaP `-9.1078` edge `-0.004` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-4.2191` n `89` status `ready` deltaP `18.4632` edge `0.0362` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.0184` n `89` status `ready` deltaP `-9.6423` edge `0.0249` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
