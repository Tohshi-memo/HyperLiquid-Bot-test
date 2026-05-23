# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T13:37:12.947869+00:00`
- Price records: `672`
- Market context records: `1634`
- Flow alert records: `6615`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `10.1064` n `181` status `ready` deltaP `27.1647` edge `0.9037` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.3306` n `181` status `ready` deltaP `19.268` edge `0.2869` maxDD `-5.3574`
- `market_context_high->crypto_alt_4h` score `1.5333` n `185` status `ready` deltaP `17.3393` edge `0.3474` maxDD `-16.3135`
- `market_context_high->equity_4h` score `1.4195` n `185` status `ready` deltaP `11.5866` edge `0.1505` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.8088` n `181` status `ready` deltaP `17.7514` edge `0.4389` maxDD `-33.1875`
- `market_context_high->crypto_major_4h` score `0.7101` n `185` status `ready` deltaP `13.0989` edge `0.2746` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.1867` n `196` status `ready` deltaP `1.775` edge `0.0666` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.3548` n `181` status `ready` deltaP `7.1909` edge `0.0274` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.4311` n `181` status `ready` deltaP `23.3193` edge `0.6672` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.5332` n `196` status `ready` deltaP `0.9777` edge `0.0299` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6471` n `196` status `ready` deltaP `0.5622` edge `0.0055` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8025` n `196` status `ready` deltaP `-0.0825` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.8604` n `196` status `ready` deltaP `-1.3198` edge `0.0316` maxDD `-5.9819`
- `market_context_high->index_4h` score `-0.8689` n `185` status `ready` deltaP `-0.0009` edge `0.0365` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.8945` n `196` status `ready` deltaP `1.7139` edge `0.002` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.4071` n `196` status `ready` deltaP `2.0133` edge `0.0029` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.5137` n `185` status `ready` deltaP `7.3266` edge `0.0942` maxDD `-12.5349`
- `market_context_high->crypto_alt_24h` score `-1.5239` n `181` status `ready` deltaP `23.6123` edge `0.8965` maxDD `-88.8062`
- `market_context_high->fx_4h` score `-1.9767` n `185` status `ready` deltaP `-8.7646` edge `-0.0134` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.8549` n `185` status `ready` deltaP `8.0818` edge `-0.148` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
