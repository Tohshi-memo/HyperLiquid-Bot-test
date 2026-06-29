# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T05:52:29.987329+00:00`
- Price records: `672`
- Market context records: `5116`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5608`

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

- `market_context_high->unknown_24h` score `23.4664` n `71` status `ready` deltaP `28.663` edge `1.7987` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.1754` n `126` status `ready` deltaP `6.0498` edge `0.7051` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.3896` n `114` status `ready` deltaP `19.7582` edge `0.5863` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.3579` n `114` status `ready` deltaP `15.5568` edge `0.5027` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.4761` n `114` status `ready` deltaP `13.2301` edge `0.4585` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.776` n `126` status `ready` deltaP `6.5583` edge `0.1171` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.3947` n `126` status `ready` deltaP `7.5468` edge `0.0596` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.3468` n `126` status `ready` deltaP `7.4708` edge `0.1192` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.1199` n `114` status `ready` deltaP `6.2153` edge `0.1378` maxDD `-7.4425`
- `market_context_high->metal_1h` score `0.0995` n `126` status `ready` deltaP `6.7223` edge `0.0194` maxDD `-1.4501`
- `market_context_high->index_1h` score `-0.0275` n `126` status `ready` deltaP `5.0613` edge `0.0131` maxDD `-1.0296`
- `market_context_high->commodity_24h` score `-0.3639` n `71` status `ready` deltaP `13.2629` edge `0.0745` maxDD `-10.7656`
- `market_context_high->index_4h` score `-0.5256` n `114` status `ready` deltaP `3.0086` edge `0.0243` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-0.5647` n `114` status `ready` deltaP `1.9389` edge `0.0557` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6363` n `126` status `ready` deltaP `-2.4713` edge `-0.001` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.8887` n `126` status `ready` deltaP `0.7033` edge `-0.002` maxDD `-2.1398`
- `market_context_high->fx_4h` score `-1.0235` n `114` status `ready` deltaP `-3.8137` edge `0.0015` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.3435` n `71` status `ready` deltaP `-1.071` edge `-0.0074` maxDD `-1.4601`
- `market_context_high->commodity_4h` score `-2.388` n `114` status `ready` deltaP `0.0696` edge `-0.0284` maxDD `-7.352`
- `market_context_high->metal_24h` score `-3.0925` n `71` status `ready` deltaP `-3.35` edge `0.0527` maxDD `-26.1474`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
