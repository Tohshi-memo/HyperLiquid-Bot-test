# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T00:37:36.355575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11765`

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

- `market_context_high->unknown_24h` score `25.515` n `109` status `ready` deltaP `3.7571` edge `2.1055` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.167` n `120` status `ready` deltaP `13.1818` edge `0.094` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9016` n `109` status `ready` deltaP `3.7004` edge `0.1673` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5543` n `109` status `ready` deltaP `21.4854` edge `0.0484` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4488` n `120` status `ready` deltaP `7.5` edge `0.029` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0116` n `120` status `ready` deltaP `5.7036` edge `-0.0045` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3942` n `120` status `ready` deltaP `5.4545` edge `-0.0009` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.535` n `120` status `ready` deltaP `-1.9261` edge `-0.0063` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7895` n `120` status `ready` deltaP `-3.1437` edge `-0.0092` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0432` n `120` status `ready` deltaP `-2.8243` edge `-0.0147` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2598` n `109` status `ready` deltaP `-3.0494` edge `0.0783` maxDD `-7.8922`
- `market_context_high->metal_4h` score `-1.2909` n `120` status `ready` deltaP `1.4394` edge `0.0063` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.3701` n `120` status `ready` deltaP `3.3483` edge `-0.0415` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.6743` n `120` status `ready` deltaP `-7.6515` edge `-0.0382` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8714` n `120` status `ready` deltaP `2.1212` edge `-0.0311` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6153` n `120` status `ready` deltaP `-6.6018` edge `-0.0366` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.0806` n `109` status `ready` deltaP `-6.6471` edge `-0.0681` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.0572` n `120` status `ready` deltaP `0.0757` edge `-0.2482` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3142` n `109` status `ready` deltaP `9.8099` edge `0.0016` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.271` n `120` status `ready` deltaP `-6.3636` edge `-0.1423` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
