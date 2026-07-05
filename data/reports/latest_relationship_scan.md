# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T08:37:28.082995+00:00`
- Price records: `672`
- Market context records: `5754`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8664`

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

- `market_context_high->equity_24h` score `0.8152` n `222` status `ready` deltaP `14.9259` edge `0.5129` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.175` n `285` status `ready` deltaP `7.6728` edge `0.1273` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2116` n `291` status `ready` deltaP `2.9652` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4425` n `291` status `ready` deltaP `1.7234` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6014` n `291` status `ready` deltaP `3.401` edge `0.0279` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6405` n `291` status `ready` deltaP `0.1379` edge `0.0038` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7251` n `291` status `ready` deltaP `3.7579` edge `0.038` maxDD `-5.5448`
- `market_context_high->commodity_1h` score `-0.7699` n `291` status `ready` deltaP `-1.8288` edge `-0.0058` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.7924` n `291` status `ready` deltaP `2.6046` edge `0.037` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-0.9537` n `222` status `ready` deltaP `13.8701` edge `0.0436` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1536` n `285` status `ready` deltaP `1.4752` edge `0.011` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2199` n `285` status `ready` deltaP `3.3189` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.5964` n `285` status `ready` deltaP `-6.9314` edge `-0.0491` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.6211` n `285` status `ready` deltaP `8.5216` edge `0.1553` maxDD `-25.1094`
- `market_context_high->index_24h` score `-2.9949` n `222` status `ready` deltaP `0.3003` edge `0.0285` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7297` n `285` status `ready` deltaP `-2.3636` edge `-0.0275` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.774` n `285` status `ready` deltaP `6.7067` edge `0.1098` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.2248` n `222` status `ready` deltaP `8.0894` edge `0.0397` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.8584` n `222` status `ready` deltaP `-10.2149` edge `-0.2509` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.8834` n `222` status `ready` deltaP `-13.4103` edge `-0.0869` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
