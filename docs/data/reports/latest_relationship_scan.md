# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T15:52:29.192866+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7312`

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

- `market_context_high->unknown_24h` score `1381.4953` n `40` status `ready` deltaP `-19.4444` edge `115.2906` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `53.6287` n `75` status `ready` deltaP `-7.4228` edge `4.5766` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `12.5123` n `84` status `ready` deltaP `-4.6478` edge `1.1073` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.8821` n `40` status `ready` deltaP `28.1944` edge `0.5951` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4285` n `40` status `ready` deltaP `52.9514` edge `0.1827` maxDD `0.0`
- `market_context_high->fx_24h` score `3.4308` n `40` status `ready` deltaP `38.6806` edge `0.041` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.6681` n `40` status `ready` deltaP `-20.5903` edge `0.5911` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.9094` n `75` status `ready` deltaP `14.3028` edge `0.0088` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.6424` n `75` status `ready` deltaP `13.6159` edge `0.0161` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.1708` n `84` status `ready` deltaP `5.1825` edge `0.0831` maxDD `-4.9401`
- `market_context_high->commodity_1h` score `0.0013` n `84` status `ready` deltaP `3.4004` edge `0.0058` maxDD `-0.6025`
- `market_context_high->fx_1h` score `-0.0156` n `84` status `ready` deltaP `3.2435` edge `0.0013` maxDD `-0.271`
- `market_context_high->metal_4h` score `-0.2994` n `75` status `ready` deltaP `2.1138` edge `0.0198` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.3669` n `84` status `ready` deltaP `3.8566` edge `0.0026` maxDD `-0.7107`
- `market_context_high->crypto_major_1h` score `-0.3981` n `84` status `ready` deltaP `-0.0071` edge `0.0379` maxDD `-3.7778`
- `market_context_high->index_1h` score `-0.772` n `84` status `ready` deltaP `-4.6193` edge `-0.0031` maxDD `-0.5392`
- `market_context_high->index_4h` score `-0.9354` n `75` status `ready` deltaP `-7.6768` edge `0.0013` maxDD `-0.9364`
- `market_context_high->crypto_major_4h` score `-1.1902` n `75` status `ready` deltaP `-5.313` edge `0.0934` maxDD `-11.1784`
- `market_context_high->equity_1h` score `-1.1914` n `84` status `ready` deltaP `-8.8181` edge `-0.007` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-1.6808` n `75` status `ready` deltaP `-8.2113` edge `0.0951` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
