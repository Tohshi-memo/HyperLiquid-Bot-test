# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T01:37:25.803961+00:00`
- Price records: `672`
- Market context records: `6872`
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

- `market_context_high->unknown_24h` score `1.1321` n `176` status `ready` deltaP `-2.84` edge `0.5393` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2401` n `224` status `ready` deltaP `2.3872` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5781` n `224` status `ready` deltaP `1.9114` edge `0.0155` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6058` n `224` status `ready` deltaP `-0.7485` edge `-0.0042` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6161` n `224` status `ready` deltaP `3.5474` edge `0.0154` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8219` n `224` status `ready` deltaP `-1.7777` edge `-0.0024` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9196` n `224` status `ready` deltaP `-5.0417` edge `-0.0075` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9889` n `224` status `ready` deltaP `11.0242` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_24h` score `-1.0821` n `176` status `ready` deltaP `4.4322` edge `0.0671` maxDD `-5.2791`
- `market_context_high->commodity_4h` score `-1.3506` n `224` status `ready` deltaP `-2.4102` edge `-0.0081` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6649` n `224` status `ready` deltaP `-3.411` edge `-0.0259` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8541` n `224` status `ready` deltaP `1.0372` edge `-0.0266` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9959` n `224` status `ready` deltaP `3.7182` edge `-0.0227` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4123` n `224` status `ready` deltaP `0.0972` edge `-0.0116` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0817` n `224` status `ready` deltaP `-1.3753` edge `-0.0532` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1165` n `224` status `ready` deltaP `-0.2997` edge `-0.0392` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1877` n `224` status `ready` deltaP `-9.5823` edge `0.0348` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.557` n `176` status `ready` deltaP `-9.7083` edge `-0.0114` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3998` n `224` status `ready` deltaP `0.9588` edge `-0.1606` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.896` n `176` status `ready` deltaP `-18.24` edge `-0.1704` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
