# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T22:52:31.800283+00:00`
- Price records: `672`
- Market context records: `6756`
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

- `market_context_high->unknown_24h` score `1.0628` n `176` status `ready` deltaP `0.5366` edge `0.5079` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `-0.031` n `176` status `ready` deltaP `7.5021` edge `0.032` maxDD `-4.2122`
- `market_context_high->commodity_24h` score `-0.0922` n `176` status `ready` deltaP `7.9704` edge `0.126` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.1304` n `176` status `ready` deltaP `5.4981` edge `0.0289` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3882` n `176` status `ready` deltaP `-0.2654` edge `0.0005` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5812` n `176` status `ready` deltaP `-0.5682` edge `0.0007` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6071` n `176` status `ready` deltaP `-0.1531` edge `-0.0085` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6981` n `176` status `ready` deltaP `-4.9912` edge `-0.0037` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.1004` n `176` status `ready` deltaP `3.7051` edge `-0.0137` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.2191` n `176` status `ready` deltaP `6.5964` edge `-0.0123` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2343` n `176` status `ready` deltaP `7.234` edge `-0.0001` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4282` n `176` status `ready` deltaP `-1.7738` edge `-0.0223` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7933` n `176` status `ready` deltaP `-7.1754` edge `-0.0115` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.4797` n `176` status `ready` deltaP `4.1159` edge `-0.0139` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.584` n `176` status `ready` deltaP `3.2843` edge `-0.013` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6683` n `176` status `ready` deltaP `-6.4718` edge `-0.0129` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.6123` n `176` status `ready` deltaP `-15.7151` edge `0.0403` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.1522` n `176` status `ready` deltaP `3.3121` edge `-0.1275` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2614` n `176` status `ready` deltaP `-7.5284` edge `-0.0013` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.3717` n `176` status `ready` deltaP `-12.942` edge `-0.1385` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
