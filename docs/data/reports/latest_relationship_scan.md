# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T08:37:37.543320+00:00`
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

- `market_context_high->unknown_24h` score `11.7359` n `92` status `ready` deltaP `4.4686` edge `0.9525` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1152` n `109` status `ready` deltaP `-0.8881` edge `0.4484` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1354` n `109` status `ready` deltaP `13.4468` edge `0.0896` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8906` n `92` status `ready` deltaP `2.7626` edge `0.2126` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5242` n `92` status `ready` deltaP `20.7126` edge `0.0497` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4203` n `109` status `ready` deltaP `7.7597` edge `0.0249` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0123` n `109` status `ready` deltaP `5.5334` edge `-0.0029` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2173` n `109` status `ready` deltaP `7.7898` edge `0.0062` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.53` n `109` status `ready` deltaP `-1.7099` edge `-0.0071` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7338` n `109` status `ready` deltaP `-3.2069` edge `-0.0193` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7485` n `109` status `ready` deltaP `3.2418` edge `0.0059` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.1723` n `92` status `ready` deltaP `-2.5815` edge `0.0864` maxDD `-7.8922`
- `market_context_high->crypto_alt_24h` score `-1.3236` n `92` status `ready` deltaP `0.2868` edge `-0.0273` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4905` n `109` status `ready` deltaP `-4.9882` edge `-0.0199` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8027` n `109` status `ready` deltaP `1.4188` edge `-0.087` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.061` n `109` status `ready` deltaP `-12.0581` edge `-0.0584` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1549` n `109` status `ready` deltaP `1.2321` edge `-0.0488` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-2.1868` n `109` status `ready` deltaP `1.4338` edge `-0.1471` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.2803` n `109` status `ready` deltaP `-11.299` edge `-0.0607` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3985` n `92` status `ready` deltaP `7.4124` edge `-0.0376` maxDD `-51.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
