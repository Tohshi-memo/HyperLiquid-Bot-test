# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T18:48:35.204562+00:00`
- Price records: `672`
- Market context records: `6843`
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

- `market_context_high->unknown_24h` score `1.0098` n `176` status `ready` deltaP `-1.5467` edge `0.515` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `-0.1275` n `176` status `ready` deltaP `8.144` edge `0.1219` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.243` n `219` status `ready` deltaP `2.3467` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_major_1h` score `-0.5326` n `219` status `ready` deltaP `4.4206` edge `0.0163` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.554` n `219` status `ready` deltaP `2.1375` edge `0.016` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6779` n `219` status `ready` deltaP `-2.1819` edge `-0.0039` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.9006` n `219` status `ready` deltaP `-2.9605` edge `-0.0046` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-1.0115` n `219` status `ready` deltaP `-6.3442` edge `-0.0106` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0305` n `209` status `ready` deltaP `10.3593` edge `0.0052` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5294` n `209` status `ready` deltaP `-4.5287` edge `-0.0169` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7218` n `219` status `ready` deltaP `-3.9114` edge `-0.0273` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-2.0096` n `219` status `ready` deltaP `-0.4826` edge `-0.0364` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.2134` n `209` status `ready` deltaP `1.0817` edge `-0.033` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.6791` n `209` status `ready` deltaP `-2.9488` edge `-0.0255` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9618` n `209` status `ready` deltaP `-0.0744` edge `-0.0465` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.154` n `209` status `ready` deltaP `-0.3325` edge `-0.0438` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.3152` n `209` status `ready` deltaP `-9.9311` edge `0.0265` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4756` n `176` status `ready` deltaP `-9.7853` edge `-0.0041` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.9456` n `209` status `ready` deltaP `-1.7213` edge `-0.2174` maxDD `-56.1828`
- `market_context_high->metal_24h` score `-9.2036` n `176` status `ready` deltaP `-18.8447` edge `-0.2058` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
