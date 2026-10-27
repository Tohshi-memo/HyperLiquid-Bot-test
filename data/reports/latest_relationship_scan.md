# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T04:22:25.945520+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9688`

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

- `market_context_high->unknown_4h` score `83.1838` n `150` status `ready` deltaP `1.7012` edge `6.9542` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `12.4635` n `150` status `ready` deltaP `1.1477` edge `1.0799` maxDD `-1.5807`
- `market_context_high->fx_4h` score `0.341` n `150` status `ready` deltaP `11.8293` edge `0.0094` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.3126` n `150` status `ready` deltaP `8.8303` edge `0.003` maxDD `-0.1986`
- `market_context_high->index_24h` score `0.2017` n `122` status `ready` deltaP `18.3254` edge `0.0166` maxDD `-3.6998`
- `market_context_high->metal_24h` score `0.1236` n `122` status `ready` deltaP `21.0898` edge `0.1278` maxDD `-6.204`
- `market_context_high->metal_1h` score `-0.0544` n `150` status `ready` deltaP `9.2395` edge `0.0078` maxDD `-1.4429`
- `market_context_high->commodity_1h` score `-0.127` n `150` status `ready` deltaP `3.3872` edge `0.0169` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.1402` n `122` status `ready` deltaP `17.0938` edge `0.0253` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3067` n `150` status `ready` deltaP `7.1606` edge `0.0496` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6074` n `150` status `ready` deltaP `-0.3533` edge `-0.0018` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8206` n `150` status `ready` deltaP `4.6946` edge `0.0156` maxDD `-8.8351`
- `market_context_high->metal_4h` score `-0.8331` n `150` status `ready` deltaP `8.7845` edge `-0.0002` maxDD `-4.8806`
- `market_context_high->equity_1h` score `-1.7717` n `150` status `ready` deltaP `1.5249` edge `-0.0097` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9626` n `150` status `ready` deltaP `-0.2974` edge `-0.0052` maxDD `-12.8878`
- `market_context_high->index_4h` score `-3.4844` n `150` status `ready` deltaP `-6.8943` edge `-0.0269` maxDD `-6.734`
- `market_context_high->crypto_major_24h` score `-4.0015` n `122` status `ready` deltaP `0.7657` edge `-0.0324` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.4537` n `150` status `ready` deltaP `-0.2662` edge `-0.0849` maxDD `-31.412`
- `market_context_high->equity_24h` score `-4.7587` n `122` status `ready` deltaP `-3.4264` edge `-0.1341` maxDD `-28.2517`
- `market_context_high->equity_4h` score `-6.8733` n `150` status `ready` deltaP `-0.9695` edge `-0.1684` maxDD `-44.8401`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
