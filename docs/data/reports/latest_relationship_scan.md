# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T04:22:29.211296+00:00`
- Price records: `672`
- Market context records: `6781`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11716`

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

- `market_context_high->unknown_24h` score `0.9321` n `176` status `ready` deltaP `-0.8523` edge `0.5004` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0357` n `176` status `ready` deltaP `8.144` edge `0.1355` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0334` n `179` status `ready` deltaP `7.71` edge `0.0303` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1486` n `179` status `ready` deltaP `5.4352` edge `0.0278` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3798` n `179` status `ready` deltaP `-0.1188` edge `0.0006` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5955` n `179` status `ready` deltaP `-0.9183` edge `0.0012` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6446` n `179` status `ready` deltaP `-0.7393` edge `-0.0094` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7435` n `179` status `ready` deltaP `-5.7455` edge `-0.0045` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.1315` n `179` status `ready` deltaP `3.2407` edge `-0.0132` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.2736` n `176` status `ready` deltaP `5.8342` edge `-0.0142` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2818` n `176` status `ready` deltaP `6.4718` edge `-0.0011` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5382` n `176` status `ready` deltaP `-3.6031` edge `-0.0242` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5697` n `179` status `ready` deltaP `-5.5958` edge `-0.0034` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.6353` n `176` status `ready` deltaP `-6.1669` edge `-0.0107` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.8163` n `176` status `ready` deltaP `2.7439` edge `-0.0479` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.9547` n `176` status `ready` deltaP `1.1502` edge `-0.0463` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.3249` n `176` status `ready` deltaP `-14.3432` edge `0.0551` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2447` n `176` status `ready` deltaP `2.7023` edge `-0.1353` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.3935` n `176` status `ready` deltaP `-8.7437` edge `-0.0042` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.9619` n `176` status `ready` deltaP `-16.7614` edge `-0.1887` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
