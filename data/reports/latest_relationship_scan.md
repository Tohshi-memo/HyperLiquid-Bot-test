# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T19:52:30.975982+00:00`
- Price records: `672`
- Market context records: `6741`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11724`

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

- `market_context_high->unknown_24h` score `1.2736` n `176` status `ready` deltaP `2.4463` edge `0.5222` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0555` n `176` status `ready` deltaP `8.1009` edge `0.0391` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0543` n `176` status `ready` deltaP `6.3963` edge `0.0383` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.193` n `176` status `ready` deltaP `7.9704` edge `0.1176` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3719` n `176` status `ready` deltaP `0.034` edge `0.0006` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5765` n `176` status `ready` deltaP `-0.5682` edge `0.0013` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6211` n `176` status `ready` deltaP `-0.1531` edge `-0.0103` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6646` n `176` status `ready` deltaP `-4.6918` edge `-0.0014` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.0116` n `176` status `ready` deltaP `4.0045` edge `-0.0083` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.1813` n `176` status `ready` deltaP `7.0538` edge `-0.0105` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2177` n `176` status `ready` deltaP `7.5388` edge `0.0` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4665` n `176` status `ready` deltaP `-1.7738` edge `-0.0272` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7609` n `176` status `ready` deltaP `-7.1754` edge `-0.0088` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.2283` n `176` status `ready` deltaP `5.3354` edge `0.0102` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.3721` n `176` status `ready` deltaP `3.8941` edge `0.0101` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.5987` n `176` status `ready` deltaP `-6.1669` edge `-0.006` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.8431` n `176` status `ready` deltaP `-16.9346` edge `0.0292` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-3.9377` n `176` status `ready` deltaP `5.1414` edge `-0.1122` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.3496` n `176` status `ready` deltaP `-8.5701` edge `-0.0017` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.974` n `176` status `ready` deltaP `-10.8586` edge `-0.1014` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
