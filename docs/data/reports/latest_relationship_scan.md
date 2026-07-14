# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T22:26:42.495947+00:00`
- Price records: `672`
- Market context records: `6754`
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

- `market_context_high->unknown_24h` score `1.1011` n `176` status `ready` deltaP `0.8838` edge `0.5105` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `-0.0263` n `176` status `ready` deltaP `7.5021` edge `0.0326` maxDD `-4.2122`
- `market_context_high->commodity_24h` score `-0.1018` n `176` status `ready` deltaP `7.9704` edge `0.1252` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.11` n `176` status `ready` deltaP `5.6478` edge `0.0296` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3726` n `176` status `ready` deltaP `0.034` edge `0.0005` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5812` n `176` status `ready` deltaP `-0.5682` edge `0.0007` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6094` n `176` status `ready` deltaP `-0.1531` edge `-0.0088` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7059` n `176` status `ready` deltaP `-5.1409` edge `-0.0037` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.1136` n `176` status `ready` deltaP `3.5554` edge `-0.0138` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.2104` n `176` status `ready` deltaP `6.7489` edge `-0.0122` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2264` n `176` status `ready` deltaP `7.3864` edge `-0.0001` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4337` n `176` status `ready` deltaP `-1.7738` edge `-0.023` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7597` n `176` status `ready` deltaP `-7.1754` edge `-0.0087` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.4475` n `176` status `ready` deltaP `4.4207` edge `-0.0118` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.544` n `176` status `ready` deltaP `3.5892` edge `-0.0099` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6549` n `176` status `ready` deltaP `-6.3193` edge `-0.0122` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.6341` n `176` status `ready` deltaP `-15.8675` edge `0.0395` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.127` n `176` status `ready` deltaP `3.617` edge `-0.1263` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2463` n `176` status `ready` deltaP `-7.3548` edge `-0.0012` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.3186` n `176` status `ready` deltaP `-12.5947` edge `-0.134` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
