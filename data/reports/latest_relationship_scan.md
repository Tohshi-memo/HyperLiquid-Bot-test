# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T10:37:28.921502+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2674`

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

- `market_context_high->unknown_1h` score `10021.9529` n `126` status `ready` deltaP `1.0146` edge `835.1758` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6107.7561` n `126` status `ready` deltaP `-0.3145` edge `509.0123` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1657` n `126` status `ready` deltaP `4.5504` edge `0.0149` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2913` n `126` status `ready` deltaP `3.0082` edge `0.0038` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5352` n `126` status `ready` deltaP `11.491` edge `0.0354` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4286` n `126` status `ready` deltaP `-9.2553` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7736` n `126` status `ready` deltaP `6.4371` edge `0.0152` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.8749` n `126` status `ready` deltaP `-6.1169` edge `0.002` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2188` n `126` status `ready` deltaP `-7.4732` edge `-0.0219` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.4615` n `126` status `ready` deltaP `-4.0989` edge `-0.0145` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5387` n `126` status `ready` deltaP `2.5591` edge `0.0032` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.2722` n `126` status `ready` deltaP `-4.194` edge `-0.017` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.5547` n `126` status `ready` deltaP `-1.5656` edge `0.1194` maxDD `-47.4317`
- `market_context_high->crypto_major_24h` score `-5.2703` n `116` status `ready` deltaP `22.1324` edge `0.682` maxDD `-111.0851`
- `market_context_high->fx_24h` score `-6.4208` n `116` status `ready` deltaP `-14.3319` edge `-0.0065` maxDD `-5.9749`
- `market_context_high->metal_24h` score `-6.5616` n `116` status `ready` deltaP `10.5903` edge `0.1151` maxDD `-48.5999`
- `market_context_high->commodity_4h` score `-6.8236` n `126` status `ready` deltaP `-18.0531` edge `-0.079` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.8602` n `126` status `ready` deltaP `-2.6326` edge `0.0438` maxDD `-46.5016`
- `market_context_high->crypto_alt_24h` score `-9.0318` n `116` status `ready` deltaP `10.2551` edge `0.3812` maxDD `-119.2659`
- `market_context_high->index_24h` score `-13.7863` n `116` status `ready` deltaP `-26.772` edge `-0.1207` maxDD `-35.9743`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
