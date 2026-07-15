# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T07:22:28.005858+00:00`
- Price records: `672`
- Market context records: `6794`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8582` n `176` status `ready` deltaP `-1.3731` edge `0.4944` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1541` n `176` status `ready` deltaP `8.6648` edge `0.1419` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2887` n `185` status `ready` deltaP `6.3489` edge `0.0196` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.402` n `185` status `ready` deltaP `-0.4863` edge `0.0002` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4489` n `185` status `ready` deltaP `3.3468` edge `0.0167` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.6587` n `185` status `ready` deltaP `-1.8587` edge `-0.0005` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.705` n `185` status `ready` deltaP `-1.8255` edge `-0.0099` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.721` n `185` status `ready` deltaP `-5.4426` edge `-0.0033` maxDD `-1.2285`
- `market_context_high->equity_1h` score `-1.287` n `185` status `ready` deltaP `2.2326` edge `-0.0177` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.355` n `179` status `ready` deltaP `5.2587` edge `-0.0024` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.4219` n `179` status `ready` deltaP `3.8305` edge `-0.0196` maxDD `-5.7256`
- `market_context_high->commodity_4h` score `-1.4836` n `179` status `ready` deltaP `-2.9738` edge `-0.0214` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5479` n `185` status `ready` deltaP `-5.1432` edge `-0.0046` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.615` n `179` status `ready` deltaP `-4.9982` edge `-0.0065` maxDD `-5.3013`
- `market_context_high->crypto_major_4h` score `-2.9965` n `179` status `ready` deltaP `1.6478` edge `-0.0637` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-3.0286` n `179` status `ready` deltaP `0.7341` edge `-0.053` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.2856` n `179` status `ready` deltaP `-13.5816` edge `0.0533` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.4357` n `179` status `ready` deltaP `1.1905` edge `-0.1497` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.4845` n `176` status `ready` deltaP `-9.6117` edge `-0.006` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-9.2465` n `176` status `ready` deltaP `-18.8447` edge `-0.2113` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
