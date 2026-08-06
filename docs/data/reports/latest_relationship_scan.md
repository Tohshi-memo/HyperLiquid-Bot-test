# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T06:37:27.635658+00:00`
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

- `market_context_high->unknown_24h` score `11.8703` n `92` status `ready` deltaP `4.4686` edge `0.9637` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1152` n `109` status `ready` deltaP `-0.8881` edge `0.4484` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2892` n `109` status `ready` deltaP `14.5139` edge `0.0953` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8508` n `92` status `ready` deltaP `2.7626` edge `0.2075` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.6093` n `92` status `ready` deltaP `21.9279` edge `0.0525` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.497` n `109` status `ready` deltaP `8.5082` edge `0.0263` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0231` n `109` status `ready` deltaP `5.3837` edge `-0.0028` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.143` n `109` status `ready` deltaP `9.0093` edge `0.0076` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5744` n `109` status `ready` deltaP `-2.3087` edge `-0.0088` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7611` n `109` status `ready` deltaP `-3.656` edge `-0.0198` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8476` n `109` status `ready` deltaP `2.1748` edge `0.0003` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2833` n `92` status `ready` deltaP `0.8077` edge `-0.0256` maxDD `-4.5445`
- `market_context_high->index_24h` score `-1.4247` n `92` status `ready` deltaP `-3.9704` edge `0.0633` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.5049` n `109` status `ready` deltaP `-5.1379` edge `-0.0201` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8533` n `109` status `ready` deltaP `0.9697` edge `-0.0905` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.0873` n `109` status `ready` deltaP `1.5369` edge `-0.0452` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.154` n `109` status `ready` deltaP `-13.2776` edge `-0.0622` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-2.3417` n `109` status `ready` deltaP `1.7332` edge `-0.162` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3678` n `109` status `ready` deltaP `-11.8978` edge `-0.064` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3521` n `92` status `ready` deltaP `7.586` edge `-0.0328` maxDD `-51.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
