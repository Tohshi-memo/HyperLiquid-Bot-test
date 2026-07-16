# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T01:52:33.906243+00:00`
- Price records: `672`
- Market context records: `6873`
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

- `market_context_high->unknown_24h` score `1.1192` n `176` status `ready` deltaP `-3.0133` edge `0.5388` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2487` n `224` status `ready` deltaP `2.2375` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5769` n `224` status `ready` deltaP `1.9114` edge `0.0156` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6143` n `224` status `ready` deltaP `-0.8982` edge `-0.0043` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6173` n `224` status `ready` deltaP `3.5474` edge `0.0153` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8133` n `224` status `ready` deltaP `-1.628` edge `-0.0023` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9087` n `224` status `ready` deltaP `-4.892` edge `-0.0071` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.981` n `224` status `ready` deltaP `11.1764` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_24h` score `-1.1049` n `176` status `ready` deltaP `4.4322` edge `0.0652` maxDD `-5.2791`
- `market_context_high->commodity_4h` score `-1.3506` n `224` status `ready` deltaP `-2.4102` edge `-0.0081` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6625` n `224` status `ready` deltaP `-3.411` edge `-0.0257` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8533` n `224` status `ready` deltaP `1.0372` edge `-0.0265` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9857` n `224` status `ready` deltaP `3.8704` edge `-0.0224` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4013` n `224` status `ready` deltaP `0.2494` edge `-0.0112` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0809` n `224` status `ready` deltaP `-1.3753` edge `-0.0531` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1133` n `224` status `ready` deltaP `-0.2997` edge `-0.0388` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1889` n `224` status `ready` deltaP `-9.5823` edge `0.0347` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.5594` n `176` status `ready` deltaP `-9.7083` edge `-0.0116` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3794` n `224` status `ready` deltaP `1.111` edge `-0.159` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.8777` n `176` status `ready` deltaP `-18.0666` edge `-0.1692` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
