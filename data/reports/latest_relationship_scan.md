# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T14:22:26.435897+00:00`
- Price records: `672`
- Market context records: `3391`
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

- `risk_on_high->crypto_major_24h` score `55.4618` n `32` status `ready` deltaP `58.3333` edge `4.2372` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.4618` n `32` status `ready` deltaP `58.3333` edge `4.2372` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.6892` n `32` status `ready` deltaP `54.8611` edge `4.1235` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.6892` n `32` status `ready` deltaP `54.8611` edge `4.1235` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.3437` n `32` status `ready` deltaP `56.0764` edge `3.4048` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.3437` n `32` status `ready` deltaP `56.0764` edge `3.4048` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1326` n `32` status `ready` deltaP `50.8681` edge `1.5886` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1326` n `32` status `ready` deltaP `50.8681` edge `1.5886` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.4996` n `156` status `ready` deltaP `18.2425` edge `2.4685` maxDD `-56.8787`
- `market_context_high->crypto_major_24h` score `18.3526` n `156` status `ready` deltaP `23.6378` edge `2.3109` maxDD `-68.1281`
- `market_context_high->equity_24h` score `18.1152` n `156` status `ready` deltaP `32.3585` edge `2.0814` maxDD `-50.6684`
- `risk_on_high->crypto_major_4h` score `15.115` n `32` status `ready` deltaP `28.2012` edge `1.1838` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.115` n `32` status `ready` deltaP `28.2012` edge `1.1838` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.7406` n `32` status `ready` deltaP `28.9931` edge `0.9779` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.7406` n `32` status `ready` deltaP `28.9931` edge `0.9779` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.8189` n `156` status `ready` deltaP `35.4835` edge `1.0038` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `6.8368` n `32` status `ready` deltaP `8.003` edge `0.7008` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.8368` n `32` status `ready` deltaP `8.003` edge `0.7008` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6531` n `32` status `ready` deltaP `15.0152` edge `0.4817` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6531` n `32` status `ready` deltaP `15.0152` edge `0.4817` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
