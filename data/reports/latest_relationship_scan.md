# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T13:07:25.560009+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `7.7865` n `99` status `ready` deltaP `3.851` edge `0.6275` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.437` n `99` status `ready` deltaP `4.798` edge `0.2046` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.037` n `109` status `ready` deltaP `12.5322` edge `0.0875` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4788` n `99` status `ready` deltaP `20.4546` edge `0.0456` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2752` n `113` status `ready` deltaP `6.351` edge `0.0222` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0799` n `113` status `ready` deltaP `6.7604` edge `-0.0034` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3338` n `109` status `ready` deltaP `6.5703` edge `-0.0006` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5829` n `113` status `ready` deltaP `-2.578` edge `-0.0081` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7013` n `109` status `ready` deltaP `3.6991` edge `0.0089` maxDD `-3.211`
- `market_context_high->index_1h` score `-1.1205` n `113` status `ready` deltaP `-3.3265` edge `-0.0178` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2299` n `99` status `ready` deltaP `-3.9141` edge `0.0879` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.3473` n `113` status `ready` deltaP `-3.8723` edge `-0.0154` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.6694` n `113` status `ready` deltaP `2.3926` edge `-0.0735` maxDD `-10.5179`
- `market_context_high->crypto_alt_24h` score `-1.7018` n `99` status `ready` deltaP `-3.8668` edge `-0.0481` maxDD `-4.5445`
- `market_context_high->index_4h` score `-1.8264` n `109` status `ready` deltaP `-9.4666` edge `-0.0456` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8754` n `109` status `ready` deltaP `3.0613` edge `-0.0377` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.0142` n `113` status `ready` deltaP `-9.292` edge `-0.0519` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.6002` n `99` status `ready` deltaP `7.3548` edge `-0.0187` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.7066` n `109` status `ready` deltaP `-1.3565` edge `-0.3219` maxDD `-34.9766`
- `market_context_high->crypto_major_24h` score `-7.6835` n `99` status `ready` deltaP `-7.9704` edge `-0.2588` maxDD `-40.8499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
