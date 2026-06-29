# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T05:22:28.536433+00:00`
- Price records: `672`
- Market context records: `5114`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10328`

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

- `market_context_high->unknown_24h` score `22.3257` n `73` status `ready` deltaP `28.6244` edge `1.7039` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `7.7878` n `126` status `ready` deltaP `6.0498` edge `0.6728` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.6544` n `114` status `ready` deltaP `21.2077` edge `0.5987` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.3243` n `114` status `ready` deltaP `15.5568` edge `0.4999` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.4871` n `114` status `ready` deltaP `13.2301` edge `0.4599` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.7329` n `126` status `ready` deltaP `5.9144` edge `0.1178` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.3916` n `126` status `ready` deltaP `7.5468` edge `0.0592` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.3` n `126` status `ready` deltaP `6.8268` edge `0.1175` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.1681` n `126` status `ready` deltaP `7.3662` edge `0.0221` maxDD `-1.3057`
- `market_context_high->equity_4h` score `0.1433` n `114` status `ready` deltaP `6.2153` edge `0.1408` maxDD `-7.4425`
- `market_context_high->index_1h` score `-0.0392` n `126` status `ready` deltaP `5.0613` edge `0.0116` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.506` n `114` status `ready` deltaP `2.6636` edge `0.0584` maxDD `-4.6157`
- `market_context_high->index_4h` score `-0.5287` n `114` status `ready` deltaP `3.0086` edge `0.0239` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.6339` n `126` status `ready` deltaP `-2.4713` edge `-0.0007` maxDD `-0.7944`
- `market_context_high->commodity_24h` score `-0.7031` n `73` status `ready` deltaP `11.758` edge `0.0622` maxDD `-11.7913`
- `market_context_high->commodity_1h` score `-0.7991` n `126` status `ready` deltaP `1.3473` edge `0.0002` maxDD `-2.062`
- `market_context_high->fx_4h` score `-0.9843` n `114` status `ready` deltaP `-3.0889` edge `0.0017` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.4297` n `73` status `ready` deltaP `-2.0358` edge `-0.0079` maxDD `-1.4804`
- `market_context_high->commodity_4h` score `-2.224` n `114` status `ready` deltaP `1.5191` edge `-0.0245` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-3.6005` n `73` status `ready` deltaP `-4.2761` edge `0.0311` maxDD `-28.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
