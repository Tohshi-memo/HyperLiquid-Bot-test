# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T14:37:35.289773+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2650`

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

- `market_context_high->unknown_1h` score `10462.5868` n `123` status `ready` deltaP `1.7916` edge `871.8901` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `6872.0405` n `116` status `ready` deltaP `1.0302` edge `572.6916` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `4.7692` n `107` status `ready` deltaP `27.4257` edge `1.1416` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.5671` n `107` status `ready` deltaP `14.3156` edge `0.9472` maxDD `-66.63`
- `market_context_high->crypto_major_4h` score `0.7865` n `116` status `ready` deltaP `3.3642` edge `0.325` maxDD `-16.2179`
- `market_context_high->metal_4h` score `0.2578` n `116` status `ready` deltaP `16.2058` edge `0.054` maxDD `-6.9113`
- `market_context_high->metal_1h` score `-0.1395` n `123` status `ready` deltaP `4.6188` edge `0.0178` maxDD `-2.6517`
- `market_context_high->crypto_alt_4h` score `-0.1572` n `116` status `ready` deltaP `4.4313` edge `0.2341` maxDD `-18.0373`
- `market_context_high->index_1h` score `-0.2701` n `123` status `ready` deltaP `3.3567` edge `0.0042` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.9947` n `123` status `ready` deltaP `3.4212` edge `0.0509` maxDD `-7.8611`
- `market_context_high->fx_1h` score `-1.2564` n `123` status `ready` deltaP `-7.1479` edge `-0.0011` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.3215` n `123` status `ready` deltaP `6.2448` edge `0.0344` maxDD `-11.559`
- `market_context_high->crypto_alt_1h` score `-1.7679` n `123` status `ready` deltaP `-2.2699` edge `0.0274` maxDD `-8.4343`
- `market_context_high->index_4h` score `-1.8828` n `116` status `ready` deltaP `-1.9134` edge `-0.0089` maxDD `-4.8198`
- `market_context_high->commodity_1h` score `-1.9364` n `123` status `ready` deltaP `-5.158` edge `-0.0138` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.1116` n `116` status `ready` deltaP `-10.3238` edge `-0.0003` maxDD `-1.794`
- `market_context_high->metal_24h` score `-5.9302` n `107` status `ready` deltaP `13.2139` edge `0.0907` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.6372` n `107` status `ready` deltaP `-17.5785` edge `-0.0086` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.0548` n `116` status `ready` deltaP `-21.8882` edge `-0.0727` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.4536` n `116` status `ready` deltaP `-5.2513` edge `-0.0804` maxDD `-50.1249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
