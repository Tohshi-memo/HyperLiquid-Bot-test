# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T19:52:29.007952+00:00`
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

- `market_context_high->unknown_1h` score `32172.8474` n `45` status `ready` deltaP `1.8662` edge `2681.0676` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21841.1638` n `45` status `ready` deltaP `1.958` edge `1820.0978` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `937.8924` n `31` status `ready` deltaP `2.0813` edge `78.1614` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `588.2163` n `31` status `ready` deltaP `3.1766` edge `49.0025` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `300.6551` n `31` status `ready` deltaP `5.7292` edge `25.0164` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.4079` n `31` status `ready` deltaP `52.0833` edge `3.5201` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.5307` n `31` status `ready` deltaP `54.5139` edge `3.1808` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.3667` n `31` status `ready` deltaP `54.5139` edge `2.8338` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.9846` n `31` status `ready` deltaP `41.2355` edge `0.7513` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.2397` n `31` status `ready` deltaP `26.4555` edge `0.8473` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.9461` n `31` status `ready` deltaP `37.8344` edge `0.708` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4811` n `31` status `ready` deltaP `53.2986` edge `0.2681` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.9703` n `31` status `ready` deltaP `17.6927` edge `0.9174` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.4549` n `31` status `ready` deltaP `46.9198` edge `0.1546` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6115` n `31` status `ready` deltaP `19.8377` edge `0.1874` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.381` n `31` status `ready` deltaP `36.31` edge `0.0657` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6291` n `31` status `ready` deltaP `31.244` edge `0.0193` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4376` n `31` status `ready` deltaP `10.1603` edge `0.2909` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.402` n `45` status `ready` deltaP `29.6307` edge `0.0311` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2316` n `31` status `ready` deltaP `12.5555` edge `0.2381` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
