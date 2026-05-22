# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T02:37:19.089139+00:00`
- Price records: `672`
- Market context records: `1485`
- Flow alert records: `6184`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8810`

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

- `market_context_high->crypto_alt_24h` score `12.2484` n `172` status `ready` deltaP `28.985` edge `1.0291` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.2062` n `172` status `ready` deltaP `16.4204` edge `0.9786` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.1824` n `172` status `ready` deltaP `27.3538` edge `0.8627` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.1126` n `172` status `ready` deltaP `20.3327` edge `0.3158` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9333` n `172` status `ready` deltaP `13.6144` edge `0.4697` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5585` n `209` status `ready` deltaP `7.3011` edge `0.1642` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.6383` n `172` status `ready` deltaP `16.1701` edge `0.0503` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.12` n `209` status `ready` deltaP `12.1287` edge `0.2611` maxDD `-19.5565`
- `market_context_high->equity_1h` score `0.0312` n `209` status `ready` deltaP `3.3628` edge `0.0402` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1065` n `209` status `ready` deltaP `3.5742` edge `0.0138` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5408` n `209` status `ready` deltaP `-0.4505` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5462` n `209` status `ready` deltaP `1.4018` edge `0.0475` maxDD `-4.1892`
- `market_context_high->index_4h` score `-0.6463` n `209` status `ready` deltaP `-0.2188` edge `0.0565` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-0.7094` n `209` status `ready` deltaP `6.8656` edge `0.166` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.7607` n `209` status `ready` deltaP `5.4379` edge `-0.0002` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.0113` n `209` status `ready` deltaP `-4.1348` edge `-0.0092` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.1392` n `209` status `ready` deltaP `-0.5093` edge `0.0006` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.6174` n `209` status `ready` deltaP `-1.3194` edge `0.0097` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.6535` n `209` status `ready` deltaP `8.6993` edge `0.0734` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.1158` n `209` status `ready` deltaP `-12.5904` edge `-0.0721` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
