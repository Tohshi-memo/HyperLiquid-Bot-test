# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T13:52:33.623062+00:00`
- Price records: `672`
- Market context records: `3796`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13048`

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

- `risk_on_high->crypto_major_24h` score `30.7177` n `32` status `ready` deltaP `32.2917` edge `2.3488` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.7177` n `32` status `ready` deltaP `32.2917` edge `2.3488` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.2088` n `32` status `ready` deltaP `40.625` edge `1.8299` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.2088` n `32` status `ready` deltaP `40.625` edge `1.8299` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.1147` n `32` status `ready` deltaP `31.9444` edge `1.7284` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.1147` n `32` status `ready` deltaP `31.9444` edge `1.7284` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4676` n `32` status `ready` deltaP `31.25` edge `0.7473` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4676` n `32` status `ready` deltaP `31.25` edge `0.7473` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.7412` n `32` status `ready` deltaP `15.8537` edge `0.8183` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.7412` n `32` status `ready` deltaP `15.8537` edge `0.8183` maxDD `-5.9781`
- `market_context_high->equity_24h` score `7.2213` n `154` status `ready` deltaP `20.4951` edge `0.7399` maxDD `-13.6477`
- `market_context_high->crypto_major_24h` score `5.4588` n `154` status `ready` deltaP `7.4946` edge `0.8513` maxDD `-31.0425`
- `market_context_high->index_24h` score `5.3686` n `154` status `ready` deltaP `26.7045` edge `0.3833` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.4391` n `154` status `ready` deltaP `26.6549` edge `0.3354` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.3299` n `178` status `ready` deltaP `12.2722` edge `0.3024` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.5127` n `32` status `ready` deltaP `8.3079` edge `0.252` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5127` n `32` status `ready` deltaP `8.3079` edge `0.252` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.3689` n `32` status `ready` deltaP `14.2361` edge `0.0453` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3689` n `32` status `ready` deltaP `14.2361` edge `0.0453` maxDD `-0.7574`
- `risk_on_high->commodity_4h` score `1.2581` n `32` status `ready` deltaP `15.625` edge `0.0874` maxDD `-3.6044`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
