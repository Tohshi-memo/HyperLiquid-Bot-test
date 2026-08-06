# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T06:22:30.344699+00:00`
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

- `market_context_high->unknown_24h` score `11.8871` n `92` status `ready` deltaP `4.4686` edge `0.9651` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1164` n `109` status `ready` deltaP `-0.8881` edge `0.4485` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.3086` n `109` status `ready` deltaP `14.6664` edge `0.0959` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8415` n `92` status `ready` deltaP `2.7626` edge `0.2063` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.6206` n `92` status `ready` deltaP `22.1015` edge `0.0528` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.515` n `109` status `ready` deltaP `8.6579` edge `0.0268` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0087` n `109` status `ready` deltaP `5.5334` edge `-0.0026` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1343` n `109` status `ready` deltaP `9.1618` edge `0.0077` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5837` n `109` status `ready` deltaP `-2.4584` edge `-0.009` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7611` n `109` status `ready` deltaP `-3.656` edge `-0.0198` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8642` n `109` status `ready` deltaP `2.0223` edge `-0.0008` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2848` n `92` status `ready` deltaP `0.8077` edge `-0.0258` maxDD `-4.5445`
- `market_context_high->index_24h` score `-1.4579` n `92` status `ready` deltaP `-4.144` edge `0.0602` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.5049` n `109` status `ready` deltaP `-5.1379` edge `-0.0201` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8518` n `109` status `ready` deltaP `0.9697` edge `-0.0903` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.0813` n `109` status `ready` deltaP `1.5369` edge `-0.0447` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1643` n `109` status `ready` deltaP `-13.43` edge `-0.0625` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-2.3777` n `109` status `ready` deltaP `1.7332` edge `-0.165` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3858` n `109` status `ready` deltaP `-12.0475` edge `-0.0645` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3344` n `92` status `ready` deltaP `7.7596` edge `-0.0317` maxDD `-51.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
