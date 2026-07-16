# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T06:37:29.715434+00:00`
- Price records: `672`
- Market context records: `6893`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11702`

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

- `market_context_high->unknown_24h` score `0.4678` n `185` status `ready` deltaP `-5.1684` edge `0.4818` maxDD `-13.3224`
- `market_context_high->fx_1h` score `-0.2222` n `224` status `ready` deltaP `2.6866` edge `0.0021` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5863` n `224` status `ready` deltaP `-0.4491` edge `-0.0037` maxDD `-2.1443`
- `market_context_high->crypto_alt_1h` score `-0.5925` n `224` status `ready` deltaP `1.9114` edge `0.0143` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6785` n `224` status `ready` deltaP `3.3977` edge `0.0112` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8133` n `224` status `ready` deltaP `-1.4783` edge `-0.0033` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8643` n `224` status `ready` deltaP `13.2405` edge `0.0073` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8993` n `224` status `ready` deltaP `-4.5926` edge `-0.0079` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3177` n `224` status `ready` deltaP `-1.8838` edge `-0.0074` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7093` n `224` status `ready` deltaP `-3.7104` edge `-0.0276` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8456` n `224` status `ready` deltaP `1.3366` edge `-0.0275` maxDD `-13.1084`
- `market_context_high->commodity_24h` score `-1.9324` n `185` status `ready` deltaP `1.1981` edge `0.0178` maxDD `-5.2791`
- `market_context_high->index_4h` score `-2.0277` n `224` status `ready` deltaP `3.3319` edge `-0.0242` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.3345` n `224` status `ready` deltaP `1.0997` edge `-0.0083` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.0201` n `224` status `ready` deltaP `0.5335` edge `-0.0324` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-3.0491` n `224` status `ready` deltaP `-1.1542` edge `-0.0505` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.1371` n `224` status `ready` deltaP `-9.1899` edge `0.0364` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2614` n `185` status `ready` deltaP `-6.7029` edge `-0.0068` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.4211` n `224` status `ready` deltaP `0.7295` edge `-0.1618` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.5681` n `185` status `ready` deltaP `-14.8813` edge `-0.1407` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
