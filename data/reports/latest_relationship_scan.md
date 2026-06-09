# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T16:52:27.102646+00:00`
- Price records: `672`
- Market context records: `3401`
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

- `risk_on_high->crypto_major_24h` score `55.7042` n `32` status `ready` deltaP `58.3333` edge `4.2574` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.7042` n `32` status `ready` deltaP `58.3333` edge `4.2574` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.6967` n `32` status `ready` deltaP `56.25` edge `4.1982` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.6967` n `32` status `ready` deltaP `56.25` edge `4.1982` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.6833` n `32` status `ready` deltaP `56.0764` edge `3.4331` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.6833` n `32` status `ready` deltaP `56.0764` edge `3.4331` maxDD `0.0`
- `risk_on_high->index_24h` score `23.5331` n `32` status `ready` deltaP `51.3889` edge `1.6185` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.5331` n `32` status `ready` deltaP `51.3889` edge `1.6185` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.0418` n `155` status `ready` deltaP `17.4395` edge `2.4357` maxDD `-56.8787`
- `market_context_high->crypto_major_24h` score `19.6623` n `155` status `ready` deltaP `24.0389` edge `2.3212` maxDD `-60.435`
- `market_context_high->equity_24h` score `19.5042` n `155` status `ready` deltaP `32.8506` edge `2.1084` maxDD `-45.1644`
- `risk_on_high->crypto_major_4h` score `15.301` n `32` status `ready` deltaP `28.2012` edge `1.1993` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.301` n `32` status `ready` deltaP `28.2012` edge `1.1993` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.6074` n `32` status `ready` deltaP `28.9931` edge `0.9668` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.6074` n `32` status `ready` deltaP `28.9931` edge `0.9668` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.2117` n `155` status `ready` deltaP `35.905` edge `1.0136` maxDD `-15.4929`
- `risk_on_high->crypto_alt_4h` score `7.022` n `32` status `ready` deltaP `8.3079` edge `0.7142` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.022` n `32` status `ready` deltaP `8.3079` edge `0.7142` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.1612` n `32` status `ready` deltaP `16.2348` edge `0.5387` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.1612` n `32` status `ready` deltaP `16.2348` edge `0.5387` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
