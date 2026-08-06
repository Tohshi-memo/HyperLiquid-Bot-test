# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T08:52:29.408076+00:00`
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

- `market_context_high->unknown_24h` score `11.5449` n `93` status `ready` deltaP `4.4803` edge `0.9365` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1152` n `109` status `ready` deltaP `-0.8881` edge `0.4484` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1184` n `109` status `ready` deltaP `13.2944` edge `0.0892` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9102` n `93` status `ready` deltaP `3.125` edge `0.2127` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5378` n `93` status `ready` deltaP `21.0182` edge `0.0494` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4215` n `109` status `ready` deltaP `7.7597` edge `0.025` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0111` n `109` status `ready` deltaP `5.5334` edge `-0.0028` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.226` n `109` status `ready` deltaP `7.6374` edge `0.0061` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5315` n `109` status `ready` deltaP `-1.7099` edge `-0.0073` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7338` n `109` status `ready` deltaP `-3.2069` edge `-0.0193` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7485` n `109` status `ready` deltaP `3.2418` edge `0.0059` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.2266` n `93` status `ready` deltaP `-3.0858` edge `0.0828` maxDD `-7.8922`
- `market_context_high->crypto_alt_24h` score `-1.3015` n `93` status `ready` deltaP `0.4872` edge `-0.0258` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4905` n `109` status `ready` deltaP `-4.9882` edge `-0.0199` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8003` n `109` status `ready` deltaP `1.4188` edge `-0.0867` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0492` n `109` status `ready` deltaP `-11.9057` edge `-0.0579` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1585` n `109` status `ready` deltaP `1.2321` edge `-0.0491` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-2.1988` n `109` status `ready` deltaP `1.2841` edge `-0.1471` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.2791` n `109` status `ready` deltaP `-11.299` edge `-0.0606` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.4873` n `93` status `ready` deltaP `6.9332` edge `-0.0376` maxDD `-51.559`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
