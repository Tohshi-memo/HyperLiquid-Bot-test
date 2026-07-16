# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T11:52:29.321121+00:00`
- Price records: `672`
- Market context records: `6915`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->fx_1h` score `-0.1537` n `224` status `ready` deltaP `3.8842` edge `0.0029` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.1774` n `199` status `ready` deltaP `-5.6408` edge `0.4165` maxDD `-14.4643`
- `market_context_high->crypto_alt_1h` score `-0.3923` n `224` status `ready` deltaP `2.9593` edge `0.024` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4531` n `224` status `ready` deltaP `4.745` edge `0.021` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.5925` n `224` status `ready` deltaP `-0.4491` edge `-0.0045` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.7204` n `224` status `ready` deltaP `15.527` edge `0.0105` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7542` n `224` status `ready` deltaP `-0.5801` edge `-0.0017` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8183` n `224` status `ready` deltaP `-3.5447` edge `-0.0045` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.357` n `224` status `ready` deltaP `-2.1886` edge `-0.0104` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5259` n `224` status `ready` deltaP `-2.3631` edge `-0.0213` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.6835` n `224` status `ready` deltaP `2.9833` edge `-0.0177` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.8272` n `224` status `ready` deltaP `6.2283` edge `-0.0178` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1157` n `224` status `ready` deltaP `3.3863` edge `0.0045` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6699` n `224` status `ready` deltaP `2.3628` edge `0.0003` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.783` n `224` status `ready` deltaP `-0.0871` edge `-0.0235` maxDD `-16.9508`
- `market_context_high->commodity_24h` score `-2.8213` n `199` status `ready` deltaP `-2.5927` edge `-0.031` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `-2.9233` n `224` status `ready` deltaP `-7.2082` edge `0.041` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.0683` n `199` status `ready` deltaP `-4.4094` edge `-0.006` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.964` n `224` status `ready` deltaP `3.6259` edge `-0.1225` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.2185` n `199` status `ready` deltaP `-12.2066` edge `-0.1127` maxDD `-28.433`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
