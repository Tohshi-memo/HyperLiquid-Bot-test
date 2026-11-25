# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T19:22:29.191930+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32174.4854` n `45` status `ready` deltaP `1.8662` edge `2681.2041` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21838.6666` n `45` status `ready` deltaP `1.958` edge `1819.8897` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `939.5304` n `31` status `ready` deltaP `2.0813` edge `78.2979` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `585.7191` n `31` status `ready` deltaP `3.1766` edge `48.7944` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `300.9383` n `31` status `ready` deltaP `5.7292` edge `25.04` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.4247` n `31` status `ready` deltaP `52.0833` edge `3.5215` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.5739` n `31` status `ready` deltaP `54.5139` edge `3.1844` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.473` n `31` status `ready` deltaP `54.6875` edge `2.8415` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.0002` n `31` status `ready` deltaP `41.2355` edge `0.7526` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.3537` n `31` status `ready` deltaP `26.4555` edge `0.8568` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `11.0829` n `31` status `ready` deltaP `37.8344` edge `0.7194` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4648` n `31` status `ready` deltaP `53.125` edge `0.2679` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.0413` n `31` status `ready` deltaP `17.6927` edge `0.9265` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.4573` n `31` status `ready` deltaP `46.9198` edge `0.1548` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6307` n `31` status `ready` deltaP `19.8377` edge `0.189` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.393` n `31` status `ready` deltaP `36.31` edge `0.0667` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6171` n `31` status `ready` deltaP `31.0943` edge `0.0193` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.482` n `31` status `ready` deltaP `10.4597` edge `0.2946` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4056` n `45` status `ready` deltaP `29.6307` edge `0.0314` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2651` n `31` status `ready` deltaP `12.7052` edge `0.2414` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
