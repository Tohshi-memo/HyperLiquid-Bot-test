# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T20:37:33.370871+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8948`

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

- `market_context_high->unknown_24h` score `1380.7672` n `40` status `ready` deltaP `-22.3958` edge `115.2496` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `51.8098` n `91` status `ready` deltaP `-3.8947` edge `4.4015` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.7912` n `40` status `ready` deltaP `27.6736` edge `0.591` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4` n `40` status `ready` deltaP `52.4306` edge `0.1838` maxDD `0.0`
- `market_context_high->unknown_1h` score `5.9563` n `103` status `ready` deltaP `-3.1684` edge `0.5511` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.1201` n `40` status `ready` deltaP `35.3819` edge `0.0371` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.4104` n `40` status `ready` deltaP `-21.1111` edge `0.5731` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.8661` n `91` status `ready` deltaP `13.8954` edge `0.0079` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.5284` n `91` status `ready` deltaP `12.2504` edge `0.0157` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.3514` n `103` status `ready` deltaP `7.1958` edge `0.1005` maxDD `-4.9401`
- `market_context_high->commodity_1h` score `0.2715` n `103` status `ready` deltaP `6.674` edge `0.0065` maxDD `-0.6025`
- `market_context_high->crypto_major_4h` score `0.236` n `91` status `ready` deltaP `2.1626` edge `0.2264` maxDD `-11.1784`
- `market_context_high->metal_4h` score `0.1405` n `91` status `ready` deltaP `9.2519` edge `0.0223` maxDD `-1.1153`
- `market_context_high->crypto_alt_4h` score `0.0553` n `91` status `ready` deltaP `-0.0854` edge `0.2635` maxDD `-13.8008`
- `market_context_high->fx_1h` score `0.0197` n `103` status `ready` deltaP `3.6844` edge `0.0013` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.1148` n `103` status `ready` deltaP `6.8281` edge `0.0038` maxDD `-0.7107`
- `market_context_high->crypto_major_1h` score `-0.257` n `103` status `ready` deltaP `0.0363` edge `0.0557` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.4446` n `91` status `ready` deltaP `0.9499` edge `0.0067` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7016` n `103` status `ready` deltaP `-3.5521` edge `-0.0012` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.9216` n `103` status `ready` deltaP `-5.1305` edge `0.003` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
