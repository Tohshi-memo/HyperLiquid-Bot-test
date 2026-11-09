# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T07:37:26.101752+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8646`

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

- `market_context_high->equity_24h` score `9.3908` n `32` status `ready` deltaP `16.4931` edge `0.9099` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4449` n `32` status `ready` deltaP `7.8125` edge `0.2104` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.367` n `32` status `ready` deltaP `16.6667` edge `0.1104` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.8001` n `32` status `ready` deltaP `11.8056` edge `-0.0032` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.3925` n `74` status `ready` deltaP `7.8444` edge `0.0531` maxDD `-1.4065`
- `market_context_high->commodity_4h` score `0.185` n `74` status `ready` deltaP `2.0312` edge `0.0557` maxDD `-1.6393`
- `market_context_high->metal_1h` score `0.0298` n `86` status `ready` deltaP `6.1134` edge `0.0175` maxDD `-1.1285`
- `market_context_high->index_4h` score `-0.1539` n `74` status `ready` deltaP `8.0875` edge `0.0192` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `-0.4048` n `86` status `ready` deltaP `1.6224` edge `0.0044` maxDD `-1.7019`
- `market_context_high->index_1h` score `-0.6897` n `86` status `ready` deltaP `-4.1324` edge `0.0114` maxDD `-0.782`
- `market_context_high->equity_1h` score `-0.7846` n `86` status `ready` deltaP `-4.2821` edge `0.0846` maxDD `-6.5309`
- `market_context_high->fx_1h` score `-1.3812` n `86` status `ready` deltaP `-15.3356` edge `-0.0064` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.4247` n `86` status `ready` deltaP `3.2133` edge `-0.0148` maxDD `-10.1421`
- `market_context_high->metal_24h` score `-1.768` n `32` status `ready` deltaP `-1.3889` edge `-0.1621` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.4251` n `74` status `ready` deltaP `-13.8802` edge `-0.0145` maxDD `-2.3101`
- `market_context_high->crypto_major_1h` score `-2.7769` n `86` status `ready` deltaP `-3.2342` edge `-0.0879` maxDD `-14.7245`
- `market_context_high->equity_4h` score `-3.7365` n `74` status `ready` deltaP `5.4466` edge `0.0303` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.4458` n `32` status `ready` deltaP `-4.8611` edge `0.0262` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-7.9663` n `74` status `ready` deltaP `1.9529` edge `-0.21` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.2062` n `32` status `ready` deltaP `-18.75` edge `-0.1843` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
