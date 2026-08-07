# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T08:22:33.254709+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11739`

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

- `market_context_high->commodity_4h` score `0.949` n `120` status `ready` deltaP `11.6565` edge `0.086` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.5706` n `109` status `ready` deltaP `21.3184` edge `0.0516` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.4722` n `109` status `ready` deltaP `1.3632` edge `0.1471` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4356` n `120` status `ready` deltaP `7.5` edge `0.0279` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0974` n `120` status `ready` deltaP `7.5` edge `-0.0025` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1729` n `120` status `ready` deltaP `8.6585` edge `0.0061` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6619` n `120` status `ready` deltaP `-3.7225` edge `-0.0106` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8183` n `120` status `ready` deltaP `-3.2934` edge `-0.0119` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.018` n `120` status `ready` deltaP `-2.8243` edge `-0.0126` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.1212` n `109` status `ready` deltaP `-0.8792` edge `0.0816` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.3147` n `120` status `ready` deltaP `3.6477` edge `-0.0364` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.5054` n `120` status `ready` deltaP `-5.8435` edge `-0.0286` maxDD `-4.7021`
- `market_context_high->metal_4h` score `-1.7435` n `120` status `ready` deltaP `-2.1037` edge `-0.0078` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-2.0543` n `120` status `ready` deltaP `1.1992` edge `-0.0402` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6418` n `120` status `ready` deltaP `-6.4521` edge `-0.0398` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.956` n `109` status `ready` deltaP `-11.1546` edge `-0.111` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8604` n `120` status `ready` deltaP `0.6504` edge `-0.2268` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2908` n `109` status `ready` deltaP `9.8099` edge `0.0046` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.3434` n `120` status `ready` deltaP `-6.189` edge `-0.1495` maxDD `-27.3622`
- `market_context_high->unknown_1h` score `-8.4096` n `120` status `ready` deltaP `1.7715` edge `-0.6679` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
