# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T01:22:29.244876+00:00`
- Price records: `672`
- Market context records: `6342`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.2711` n `32` status `ready` deltaP `43.0556` edge `1.0003` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1028` n `32` status `ready` deltaP `50.6944` edge `0.1706` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3622` n `32` status `ready` deltaP `16.6667` edge `0.5261` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.1911` n `32` status `ready` deltaP `43.6738` edge `0.0627` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.5459` n `32` status `ready` deltaP `31.25` edge `0.1077` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3763` n `32` status `ready` deltaP `28.5928` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5131` n `32` status `ready` deltaP `14.7268` edge `0.1425` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9548` n `32` status `ready` deltaP `11.9199` edge `0.0891` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.551` n `196` status `ready` deltaP `12.5809` edge `0.0417` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2173` n `207` status `ready` deltaP `-7.182` edge `0.1668` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.0677` n `196` status `ready` deltaP `6.4118` edge `0.0222` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.3972` n `207` status `ready` deltaP `3.7114` edge `0.0021` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5465` n `207` status `ready` deltaP `-0.3233` edge `0.0004` maxDD `-2.1314`
- `market_context_high->metal_24h` score `-0.5831` n `136` status `ready` deltaP `15.3288` edge `0.0799` maxDD `-11.8809`
- `market_context_high->commodity_24h` score `-0.654` n `136` status `ready` deltaP `-3.8603` edge `0.1283` maxDD `-6.2457`
- `market_context_high->equity_4h` score `-0.6959` n `196` status `ready` deltaP `5.3198` edge `0.0452` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.7045` n `207` status `ready` deltaP `-0.5135` edge `-0.0019` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7117` n `32` status `ready` deltaP `0.3472` edge `-0.0064` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.7551` n `32` status `ready` deltaP `-3.2934` edge `-0.0251` maxDD `-1.6464`
- `news_risk_high->unknown_1h` score `-0.8619` n `32` status `ready` deltaP `5.3331` edge `-0.0729` maxDD `-0.7581`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
