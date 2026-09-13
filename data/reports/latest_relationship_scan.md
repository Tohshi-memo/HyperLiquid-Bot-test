# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T02:07:27.352111+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12553`

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

- `market_context_high->unknown_24h` score `16593.2438` n `59` status `ready` deltaP `12.0616` edge `1382.6951` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `379.588` n `82` status `ready` deltaP `-5.5499` edge `31.7115` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.0924` n `82` status `ready` deltaP `32.5796` edge `1.3393` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0241` n `82` status `ready` deltaP `39.3251` edge `1.3869` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.4885` n `59` status `ready` deltaP `46.7014` edge `0.5627` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `10.1939` n `59` status `ready` deltaP `22.5342` edge `0.782` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.2314` n `82` status `ready` deltaP `16.2136` edge `0.5892` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.1288` n `82` status `ready` deltaP `42.4796` edge `0.2452` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.9751` n `82` status `ready` deltaP `27.871` edge `0.2742` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2517` n `59` status `ready` deltaP `42.3611` edge `0.0719` maxDD `0.0`
- `market_context_high->index_24h` score `4.0075` n `59` status `ready` deltaP `43.0791` edge `0.086` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.3428` n `59` status `ready` deltaP `8.6688` edge `0.1059` maxDD `-2.9132`
- `risk_on_high->crypto_alt_4h` score `0.1949` n `53` status `ready` deltaP `7.8233` edge `0.1403` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.1949` n `53` status `ready` deltaP `7.8233` edge `0.1403` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.1666` n `82` status `ready` deltaP `8.3841` edge `0.0283` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.1386` n `56` status `ready` deltaP `7.4529` edge `0.0011` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1386` n `56` status `ready` deltaP `7.4529` edge `0.0011` maxDD `-0.3081`
- `risk_on_high->fx_1h` score `-0.2233` n `56` status `ready` deltaP `-0.8768` edge `0.0028` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `-0.2233` n `56` status `ready` deltaP `-0.8768` edge `0.0028` maxDD `-0.0464`
- `risk_on_high->index_1h` score `-0.2433` n `56` status `ready` deltaP `3.1223` edge `0.0003` maxDD `-0.1844`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
