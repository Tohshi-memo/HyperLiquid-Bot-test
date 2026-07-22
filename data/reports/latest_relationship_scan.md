# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T12:52:28.797567+00:00`
- Price records: `672`
- Market context records: `7566`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `market_context_high->commodity_4h` score `0.0709` n `172` status `ready` deltaP `8.2676` edge `0.0268` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.0838` n `172` status `ready` deltaP `6.0794` edge `0.0083` maxDD `-1.7657`
- `market_context_high->fx_1h` score `-0.2385` n `172` status `ready` deltaP `2.8145` edge `0.0006` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-0.2816` n `153` status `ready` deltaP `12.4024` edge `0.0522` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.3279` n `172` status `ready` deltaP `4.1238` edge `0.0024` maxDD `-1.5775`
- `market_context_high->unknown_1h` score `-0.3989` n `172` status `ready` deltaP `2.6424` edge `0.0115` maxDD `-1.3217`
- `market_context_high->unknown_4h` score `-0.4739` n `172` status `ready` deltaP `11.3869` edge `0.0992` maxDD `-6.2031`
- `market_context_high->crypto_major_1h` score `-0.6214` n `172` status `ready` deltaP `5.2326` edge `0.0265` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.6386` n `172` status `ready` deltaP `0.3168` edge `0.0199` maxDD `-5.9775`
- `market_context_high->index_4h` score `-0.6973` n `172` status `ready` deltaP `10.3104` edge `0.0273` maxDD `-4.5012`
- `market_context_high->metal_1h` score `-0.7201` n `172` status `ready` deltaP `0.6684` edge `0.0136` maxDD `-1.4971`
- `market_context_high->fx_24h` score `-0.7857` n `153` status `ready` deltaP `9.4281` edge `0.0157` maxDD `-3.8554`
- `market_context_high->fx_4h` score `-1.2623` n `172` status `ready` deltaP `0.4854` edge `0.0034` maxDD `-2.1439`
- `market_context_high->equity_1h` score `-1.4178` n `172` status `ready` deltaP `4.4853` edge `0.0294` maxDD `-14.6193`
- `market_context_high->metal_4h` score `-1.5192` n `172` status `ready` deltaP `0.7232` edge `0.0486` maxDD `-4.8549`
- `market_context_high->unknown_24h` score `-1.6469` n `154` status `ready` deltaP `4.9874` edge `0.0305` maxDD `-9.9917`
- `market_context_high->crypto_alt_4h` score `-1.8579` n `172` status `ready` deltaP `0.3616` edge `0.0337` maxDD `-15.2776`
- `market_context_high->crypto_major_4h` score `-2.4549` n `172` status `ready` deltaP `4.8604` edge `0.0423` maxDD `-23.4879`
- `market_context_high->equity_4h` score `-3.2057` n `172` status `ready` deltaP `2.354` edge `0.1568` maxDD `-33.6787`
- `market_context_high->index_24h` score `-4.3418` n `153` status `ready` deltaP `-19.7604` edge `-0.013` maxDD `-18.2857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
