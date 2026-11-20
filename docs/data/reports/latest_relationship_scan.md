# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T15:22:35.625856+00:00`
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

- `market_context_high->unknown_1h` score `10271.2194` n `125` status `ready` deltaP `1.9737` edge `855.9416` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `6691.4928` n `119` status `ready` deltaP `1.2041` edge `557.6448` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `4.7802` n `107` status `ready` deltaP `27.4257` edge `1.143` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.5839` n `107` status `ready` deltaP `14.3156` edge `0.9486` maxDD `-66.63`
- `market_context_high->metal_4h` score `-0.0044` n `119` status `ready` deltaP `14.9019` edge `0.049` maxDD `-7.5797`
- `market_context_high->metal_1h` score `-0.144` n `125` status `ready` deltaP `4.788` edge `0.0161` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2925` n `125` status `ready` deltaP `3.0898` edge `0.0031` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-0.5362` n `119` status `ready` deltaP `2.2341` edge `0.2702` maxDD `-21.9735`
- `market_context_high->crypto_alt_4h` score `-1.2754` n `119` status `ready` deltaP `3.3012` edge `0.1874` maxDD `-24.1675`
- `market_context_high->fx_1h` score `-1.2945` n `125` status `ready` deltaP `-7.6096` edge `-0.0012` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.5487` n `125` status `ready` deltaP `5.9389` edge `0.0175` maxDD `-11.559`
- `market_context_high->crypto_major_1h` score `-1.8028` n `125` status `ready` deltaP `2.6407` edge `0.0242` maxDD `-10.6962`
- `market_context_high->index_4h` score `-1.9205` n `119` status `ready` deltaP `-2.2686` edge `-0.0093` maxDD `-4.8491`
- `market_context_high->commodity_1h` score `-2.0148` n `125` status `ready` deltaP `-5.8084` edge `-0.016` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.0388` n `119` status `ready` deltaP `-8.9991` edge `0.0002` maxDD `-1.794`
- `market_context_high->crypto_alt_1h` score `-2.4547` n `125` status `ready` deltaP `-2.9593` edge `0.0062` maxDD `-10.9492`
- `market_context_high->metal_24h` score `-5.875` n `107` status `ready` deltaP `13.2139` edge `0.0953` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.6583` n `107` status `ready` deltaP `-17.7521` edge `-0.0092` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9662` n `119` status `ready` deltaP `-20.9904` edge `-0.0713` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.8745` n `119` status `ready` deltaP `-5.411` edge `-0.0944` maxDD `-51.7257`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
