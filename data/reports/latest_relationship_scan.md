# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T18:52:25.828274+00:00`
- Price records: `672`
- Market context records: `6844`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11802`

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

- `market_context_high->unknown_24h` score `1.0106` n `176` status `ready` deltaP `-1.5467` edge `0.5151` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `-0.1275` n `176` status `ready` deltaP `8.144` edge `0.1219` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2438` n `219` status `ready` deltaP `2.3467` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5564` n `219` status `ready` deltaP `2.1375` edge `0.0158` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5643` n `219` status `ready` deltaP `4.1137` edge `0.0157` maxDD `-4.2122`
- `market_context_high->index_1h` score `-0.9021` n `219` status `ready` deltaP `-2.9605` edge `-0.0048` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-1.0123` n `219` status `ready` deltaP `-6.3442` edge `-0.0107` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0305` n `209` status `ready` deltaP `10.3593` edge `0.0052` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.0442` n `219` status `ready` deltaP `-2.1819` edge `-0.004` maxDD `-2.1443`
- `market_context_high->commodity_4h` score `-1.5294` n `209` status `ready` deltaP `-4.5287` edge `-0.0169` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7218` n `219` status `ready` deltaP `-3.9114` edge `-0.0273` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-2.0143` n `219` status `ready` deltaP `-0.4826` edge `-0.037` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.2134` n `209` status `ready` deltaP `1.0817` edge `-0.033` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.6784` n `209` status `ready` deltaP `-2.9488` edge `-0.0254` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9665` n `209` status `ready` deltaP `-0.0744` edge `-0.0471` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1564` n `209` status `ready` deltaP `-0.3325` edge `-0.0441` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2867` n `209` status `ready` deltaP `-9.6051` edge `0.0267` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4756` n `176` status `ready` deltaP `-9.7853` edge `-0.0041` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.964` n `209` status `ready` deltaP `-1.7213` edge `-0.218` maxDD `-56.3242`
- `market_context_high->metal_24h` score `-9.2028` n `176` status `ready` deltaP `-18.8447` edge `-0.2057` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
