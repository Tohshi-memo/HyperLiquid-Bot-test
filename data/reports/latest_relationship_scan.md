# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T01:22:24.414949+00:00`
- Price records: `672`
- Market context records: `6871`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11786`

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

- `market_context_high->unknown_24h` score `1.1443` n `176` status `ready` deltaP `-2.6666` edge `0.5397` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2324` n `224` status `ready` deltaP `2.5369` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5961` n `224` status `ready` deltaP `1.7617` edge `0.015` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.605` n `224` status `ready` deltaP `-0.7485` edge `-0.0041` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6197` n `224` status `ready` deltaP `3.5474` edge `0.0151` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8312` n `224` status `ready` deltaP `-1.9274` edge `-0.0026` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9305` n `224` status `ready` deltaP `-5.1914` edge `-0.0079` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9976` n `224` status `ready` deltaP `10.872` edge `0.006` maxDD `-2.1765`
- `market_context_high->commodity_24h` score `-1.0569` n `176` status `ready` deltaP `4.4322` edge `0.0692` maxDD `-5.2791`
- `market_context_high->commodity_4h` score `-1.349` n `224` status `ready` deltaP `-2.4102` edge `-0.0079` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6793` n `224` status `ready` deltaP `-3.5607` edge `-0.0261` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8666` n `224` status `ready` deltaP `0.8875` edge `-0.0272` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0062` n `224` status `ready` deltaP `3.566` edge `-0.023` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4226` n `224` status `ready` deltaP `-0.0551` edge `-0.0119` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0997` n `224` status `ready` deltaP `-1.5275` edge `-0.0545` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1353` n `224` status `ready` deltaP `-0.4519` edge `-0.0406` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1889` n `224` status `ready` deltaP `-9.5823` edge `0.0347` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.5534` n `176` status `ready` deltaP `-9.7083` edge `-0.0111` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.4249` n `224` status `ready` deltaP `0.8066` edge `-0.1628` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.9152` n `176` status `ready` deltaP `-18.4133` edge `-0.1717` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
