# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T05:07:33.591203+00:00`
- Price records: `672`
- Market context records: `4692`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9760`

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

- `market_context_high->unknown_1h` score `78.2814` n `136` status `ready` deltaP `12.4208` edge `6.4824` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2168` n `135` status `ready` deltaP `10.9169` edge `0.483` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.1653` n `135` status `ready` deltaP `11.6667` edge `0.195` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.5324` n `136` status `ready` deltaP `1.6995` edge `0.0239` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7804` n `135` status `ready` deltaP `3.7692` edge `-0.0129` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8463` n `136` status `ready` deltaP `-2.655` edge `0.0079` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9449` n `135` status `ready` deltaP `-1.6351` edge `-0.002` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.0743` n `136` status `ready` deltaP `-4.3589` edge `-0.005` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.247` n `135` status `ready` deltaP `5.3986` edge `0.0149` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.2568` n `135` status `ready` deltaP `1.3946` edge `0.0065` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7734` n `136` status `ready` deltaP `-5.1999` edge `-0.0127` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8359` n `136` status `ready` deltaP `-4.0463` edge `-0.0798` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7491` n `135` status `ready` deltaP `-12.6968` edge `-0.0151` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-4.7881` n `135` status `ready` deltaP `14.3287` edge `0.0559` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.4555` n `136` status `ready` deltaP `-2.0694` edge `-0.1121` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.5844` n `136` status `ready` deltaP `-4.8477` edge `-0.1411` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3915` n `135` status `ready` deltaP `-10.6366` edge `-0.0909` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.636` n `135` status `ready` deltaP `-3.1595` edge `-0.2204` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.155` n `135` status `ready` deltaP `-0.7012` edge `-0.2837` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.6298` n `135` status `ready` deltaP `-3.5953` edge `-0.377` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
