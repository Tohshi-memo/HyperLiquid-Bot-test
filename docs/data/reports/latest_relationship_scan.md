# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T12:07:32.514923+00:00`
- Price records: `672`
- Market context records: `7563`
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

- `market_context_high->commodity_4h` score `-0.0415` n `175` status `ready` deltaP `7.4172` edge `0.0231` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.1132` n `175` status `ready` deltaP `5.6036` edge `0.0077` maxDD `-1.7657`
- `market_context_high->fx_1h` score `-0.2161` n `175` status `ready` deltaP `3.2304` edge `0.0007` maxDD `-0.6615`
- `market_context_high->unknown_1h` score `-0.377` n `175` status `ready` deltaP `3.0205` edge `0.0108` maxDD `-1.3217`
- `market_context_high->unknown_4h` score `-0.3831` n `175` status `ready` deltaP `12.1742` edge `0.1056` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.4181` n `175` status `ready` deltaP `3.1471` edge `0.0014` maxDD `-1.5775`
- `market_context_high->commodity_24h` score `-0.4998` n `153` status `ready` deltaP `10.9642` edge `0.0436` maxDD `-7.0012`
- `market_context_high->crypto_alt_1h` score `-0.6067` n `175` status `ready` deltaP `0.7348` edge `0.0212` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6314` n `175` status `ready` deltaP `5.1292` edge `0.0259` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-0.6658` n `153` status `ready` deltaP `10.8663` edge `0.0161` maxDD `-3.8554`
- `market_context_high->index_4h` score `-0.8875` n `175` status `ready` deltaP `9.3237` edge `0.0224` maxDD `-5.5335`
- `market_context_high->metal_1h` score `-1.0217` n `175` status `ready` deltaP `1.5654` edge `0.0148` maxDD `-1.4971`
- `market_context_high->fx_4h` score `-1.2273` n `175` status `ready` deltaP `0.9934` edge `0.0045` maxDD `-2.1439`
- `market_context_high->equity_1h` score `-1.4597` n `175` status `ready` deltaP `4.0395` edge `0.027` maxDD `-14.6193`
- `market_context_high->metal_4h` score `-1.4678` n `175` status `ready` deltaP `1.6202` edge `0.0492` maxDD `-4.8549`
- `market_context_high->unknown_24h` score `-1.7354` n `154` status `ready` deltaP `4.0359` edge `0.0255` maxDD `-9.9917`
- `market_context_high->crypto_alt_4h` score `-1.7515` n `175` status `ready` deltaP `1.2387` edge `0.0415` maxDD `-15.2776`
- `market_context_high->crypto_major_4h` score `-2.346` n `175` status `ready` deltaP `5.2003` edge `0.054` maxDD `-23.4879`
- `market_context_high->equity_4h` score `-3.9415` n `175` status `ready` deltaP `1.5168` edge `0.1324` maxDD `-38.8271`
- `market_context_high->index_24h` score `-4.575` n `153` status `ready` deltaP `-19.7604` edge `-0.0191` maxDD `-19.8557`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
