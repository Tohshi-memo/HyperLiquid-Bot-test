# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T02:52:28.723391+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12541`

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

- `market_context_high->unknown_24h` score `16599.587` n `59` status `ready` deltaP `12.0616` edge `1383.2237` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `380.0775` n `82` status `ready` deltaP `-5.2505` edge `31.7503` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.0636` n `82` status `ready` deltaP `32.5796` edge `1.3369` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0313` n `82` status `ready` deltaP `39.3251` edge `1.3875` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.5854` n `59` status `ready` deltaP `47.2222` edge `0.5673` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `10.1651` n `59` status `ready` deltaP `22.5342` edge `0.7796` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.3282` n `82` status `ready` deltaP `16.7344` edge `0.5938` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.1741` n `82` status `ready` deltaP `43.0005` edge `0.2455` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.9262` n `82` status `ready` deltaP `27.3501` edge `0.2736` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2378` n `59` status `ready` deltaP `42.1875` edge `0.0719` maxDD `0.0`
- `market_context_high->index_24h` score `4.0527` n `59` status `ready` deltaP `43.6` edge `0.0863` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.311` n `59` status `ready` deltaP `8.1479` edge `0.1053` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.1919` n `82` status `ready` deltaP `8.8414` edge `0.0285` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.158` n `53` status `ready` deltaP `7.5184` edge `0.1376` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.158` n `53` status `ready` deltaP `7.5184` edge `0.1376` maxDD `-6.7304`
- `risk_on_high->metal_1h` score `0.0094` n `59` status `ready` deltaP `4.9376` edge `0.0013` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.0094` n `59` status `ready` deltaP `4.9376` edge `0.0013` maxDD `-0.3081`
- `risk_on_high->fx_1h` score `-0.0879` n `59` status `ready` deltaP `1.6974` edge `0.003` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `-0.0879` n `59` status `ready` deltaP `1.6974` edge `0.003` maxDD `-0.0464`
- `market_context_high->fx_1h` score `-0.2361` n `117` status `ready` deltaP `2.1175` edge `-0.0022` maxDD `-0.5274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
