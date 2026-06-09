# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T18:07:32.746912+00:00`
- Price records: `672`
- Market context records: `3406`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13074`

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

- `risk_on_high->crypto_major_24h` score `55.715` n `32` status `ready` deltaP `58.3333` edge `4.2583` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.715` n `32` status `ready` deltaP `58.3333` edge `4.2583` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.988` n `32` status `ready` deltaP `56.7708` edge `4.219` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.988` n `32` status `ready` deltaP `56.7708` edge `4.219` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.8069` n `32` status `ready` deltaP `56.0764` edge `3.4434` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.8069` n `32` status `ready` deltaP `56.0764` edge `3.4434` maxDD `0.0`
- `risk_on_high->index_24h` score `23.7299` n `32` status `ready` deltaP `51.3889` edge `1.6349` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.7299` n `32` status `ready` deltaP `51.3889` edge `1.6349` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.4839` n `153` status `ready` deltaP `18.0657` edge `2.4658` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.1825` n `153` status `ready` deltaP `24.857` edge `2.3726` maxDD `-54.8486`
- `market_context_high->equity_24h` score `20.9213` n `153` status `ready` deltaP `33.8542` edge `2.159` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `15.3046` n `32` status `ready` deltaP `28.2012` edge `1.1996` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.3046` n `32` status `ready` deltaP `28.2012` edge `1.1996` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.5894` n `32` status `ready` deltaP `28.9931` edge `0.9653` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.5894` n `32` status `ready` deltaP `28.9931` edge `0.9653` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.7581` n `153` status `ready` deltaP `37.0098` edge `1.0381` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.0304` n `32` status `ready` deltaP `8.3079` edge `0.7149` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.0304` n `32` status `ready` deltaP `8.3079` edge `0.7149` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.675` n `153` status `ready` deltaP `24.2954` edge `0.8914` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.4426` n `32` status `ready` deltaP `16.997` edge `0.5697` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
