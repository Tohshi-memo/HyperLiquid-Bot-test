# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T14:37:29.821286+00:00`
- Price records: `672`
- Market context records: `3392`
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

- `risk_on_high->crypto_major_24h` score `55.4666` n `32` status `ready` deltaP `58.3333` edge `4.2376` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.4666` n `32` status `ready` deltaP `58.3333` edge `4.2376` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.7739` n `32` status `ready` deltaP `55.0347` edge `4.1294` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.7739` n `32` status `ready` deltaP `55.0347` edge `4.1294` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.3413` n `32` status `ready` deltaP `56.0764` edge `3.4046` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.3413` n `32` status `ready` deltaP `56.0764` edge `3.4046` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1597` n `32` status `ready` deltaP `51.0417` edge `1.5897` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1597` n `32` status `ready` deltaP `51.0417` edge `1.5897` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.2714` n `156` status `ready` deltaP `17.7751` edge `2.4526` maxDD `-56.8787`
- `market_context_high->crypto_major_24h` score `18.744` n `156` status `ready` deltaP `23.6378` edge `2.3098` maxDD `-65.4311`
- `market_context_high->equity_24h` score `18.2914` n `156` status `ready` deltaP `32.3585` edge `2.0822` maxDD `-49.8914`
- `risk_on_high->crypto_major_4h` score `15.1198` n `32` status `ready` deltaP `28.2012` edge `1.1842` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.1198` n `32` status `ready` deltaP `28.2012` edge `1.1842` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.7094` n `32` status `ready` deltaP `28.9931` edge `0.9753` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.7094` n `32` status `ready` deltaP `28.9931` edge `0.9753` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.7431` n `156` status `ready` deltaP `35.0161` edge `1.0006` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `6.8356` n `32` status `ready` deltaP `8.003` edge `0.7007` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.8356` n `32` status `ready` deltaP `8.003` edge `0.7007` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6782` n `32` status `ready` deltaP `15.1677` edge `0.4839` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6782` n `32` status `ready` deltaP `15.1677` edge `0.4839` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
