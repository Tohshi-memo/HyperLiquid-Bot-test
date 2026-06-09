# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T14:52:49.413104+00:00`
- Price records: `672`
- Market context records: `3393`
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

- `risk_on_high->crypto_major_24h` score `55.4786` n `32` status `ready` deltaP `58.3333` edge `4.2386` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.4786` n `32` status `ready` deltaP `58.3333` edge `4.2386` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.8694` n `32` status `ready` deltaP `55.2083` edge `4.1362` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.8694` n `32` status `ready` deltaP `55.2083` edge `4.1362` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.3617` n `32` status `ready` deltaP `56.0764` edge `3.4063` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.3617` n `32` status `ready` deltaP `56.0764` edge `3.4063` maxDD `0.0`
- `risk_on_high->index_24h` score `23.2012` n `32` status `ready` deltaP `51.2153` edge `1.592` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.2012` n `32` status `ready` deltaP `51.2153` edge `1.592` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.0689` n `157` status `ready` deltaP `17.569` edge `2.4371` maxDD `-56.8787`
- `market_context_high->crypto_major_24h` score `18.3967` n `157` status `ready` deltaP `23.2417` edge `2.2835` maxDD `-65.4311`
- `market_context_high->equity_24h` score `18.0461` n `157` status `ready` deltaP `31.8726` edge `2.065` maxDD `-49.8914`
- `risk_on_high->crypto_major_4h` score `15.1246` n `32` status `ready` deltaP `28.2012` edge `1.1846` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.1246` n `32` status `ready` deltaP `28.2012` edge `1.1846` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.6914` n `32` status `ready` deltaP `28.9931` edge `0.9738` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.6914` n `32` status `ready` deltaP `28.9931` edge `0.9738` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.6218` n `157` status `ready` deltaP `34.6548` edge `0.9929` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `6.8332` n `32` status `ready` deltaP `8.003` edge `0.7005` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.8332` n `32` status `ready` deltaP `8.003` edge `0.7005` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7048` n `32` status `ready` deltaP `15.1677` edge `0.4873` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7048` n `32` status `ready` deltaP `15.1677` edge `0.4873` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
