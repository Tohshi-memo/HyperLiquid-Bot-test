# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T18:22:32.456205+00:00`
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

- `market_context_high->unknown_1h` score `32178.0445` n `45` status `ready` deltaP `2.0159` edge `2681.4997` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21849.8616` n `45` status `ready` deltaP `2.1105` edge `1820.8216` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `943.0896` n `31` status `ready` deltaP `2.231` edge `78.5935` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `596.9141` n `31` status `ready` deltaP `3.3291` edge `49.7263` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `314.5355` n `31` status `ready` deltaP `5.7292` edge `26.1731` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.4367` n `31` status `ready` deltaP `52.0833` edge `3.5225` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.5648` n `31` status `ready` deltaP `54.3403` edge `3.1848` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.6395` n `31` status `ready` deltaP `55.2083` edge `2.8519` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.0314` n `31` status `ready` deltaP `41.2355` edge `0.7552` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.7289` n `31` status `ready` deltaP `27.0653` edge `0.884` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `11.4588` n `31` status `ready` deltaP `38.1393` edge `0.7487` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.46` n `31` status `ready` deltaP `53.125` edge `0.2675` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.2999` n `31` status `ready` deltaP `18.3025` edge `0.9556` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.4862` n `31` status `ready` deltaP `47.267` edge `0.1549` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8202` n `31` status `ready` deltaP `20.2868` edge `0.2018` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.451` n `31` status `ready` deltaP `36.6149` edge `0.0695` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6674` n `31` status `ready` deltaP `31.5434` edge `0.0205` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5779` n `31` status `ready` deltaP `11.0585` edge `0.3029` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4238` n `45` status `ready` deltaP `29.7832` edge `0.0319` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3461` n `31` status `ready` deltaP `13.304` edge `0.2478` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
