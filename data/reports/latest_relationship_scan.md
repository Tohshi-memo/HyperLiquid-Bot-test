# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T01:22:28.626805+00:00`
- Price records: `672`
- Market context records: `3537`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13197`

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

- `risk_on_high->crypto_major_24h` score `53.124` n `32` status `ready` deltaP `57.8802` edge `4.0454` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `53.124` n `32` status `ready` deltaP `57.8802` edge `4.0454` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `48.2774` n `32` status `ready` deltaP `57.5336` edge `3.6547` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `48.2774` n `32` status `ready` deltaP `57.5336` edge `3.6547` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.925` n `32` status `ready` deltaP `54.5927` edge `3.3798` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.925` n `32` status `ready` deltaP `54.5927` edge `3.3798` maxDD `0.0`
- `risk_on_high->index_24h` score `25.4572` n `32` status `ready` deltaP `53.8995` edge `1.7621` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.4572` n `32` status `ready` deltaP `53.8995` edge `1.7621` maxDD `0.0`
- `market_context_high->equity_24h` score `19.2811` n `156` status `ready` deltaP `31.5158` edge `2.0379` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6374` n `32` status `ready` deltaP `37.2075` edge `1.3312` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6374` n `32` status `ready` deltaP `37.2075` edge `1.3312` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `17.6899` n `156` status `ready` deltaP `23.1847` edge `2.0927` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `14.8786` n `32` status `ready` deltaP `28.2012` edge `1.1641` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.8786` n `32` status `ready` deltaP `28.2012` edge `1.1641` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.1903` n `156` status `ready` deltaP `17.7099` edge `1.8687` maxDD `-56.6728`
- `market_context_high->index_24h` score `14.0725` n `156` status `ready` deltaP `38.5149` edge `1.1376` maxDD `-15.0661`
- `market_context_high->metal_24h` score `7.6058` n `156` status `ready` deltaP `31.278` edge `1.2206` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `6.737` n `32` status `ready` deltaP `8.7652` edge `0.6874` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.737` n `32` status `ready` deltaP `8.7652` edge `0.6874` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.0622` n `32` status `ready` deltaP `17.3018` edge `0.5189` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
