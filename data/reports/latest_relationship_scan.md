# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T20:07:35.267438+00:00`
- Price records: `672`
- Market context records: `6850`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `1.0761` n `176` status `ready` deltaP `-1.5467` edge `0.5235` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2523` n `223` status `ready` deltaP `2.169` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.3494` n `176` status `ready` deltaP `7.2759` edge `0.1092` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.5893` n `223` status `ready` deltaP `1.8622` edge `0.0149` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6178` n `223` status `ready` deltaP `3.8056` edge `0.0133` maxDD `-4.2122`
- `market_context_high->commodity_1h` score `-0.6751` n `223` status `ready` deltaP `-2.0213` edge `-0.0046` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.8904` n `223` status `ready` deltaP `-2.9148` edge `-0.0036` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.969` n `223` status `ready` deltaP `-5.7517` edge `-0.0091` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0092` n `214` status `ready` deltaP `10.648` edge `0.006` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4879` n `214` status `ready` deltaP `-4.1059` edge `-0.0144` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6645` n `223` status `ready` deltaP `-3.0612` edge `-0.0282` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-2.0002` n `223` status `ready` deltaP `-0.527` edge `-0.0349` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.1234` n `214` status `ready` deltaP `2.1214` edge `-0.0284` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.5441` n `214` status `ready` deltaP `-1.5514` edge `-0.0175` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0522` n `214` status `ready` deltaP `-0.6425` edge `-0.0543` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.2041` n `214` status `ready` deltaP `-0.8449` edge `-0.0468` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2049` n `214` status `ready` deltaP `-9.333` edge `0.0317` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4924` n `176` status `ready` deltaP `-9.7853` edge `-0.0055` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.7944` n `214` status `ready` deltaP `-0.8847` edge `-0.1989` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.1201` n `176` status `ready` deltaP `-18.8447` edge `-0.1951` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
