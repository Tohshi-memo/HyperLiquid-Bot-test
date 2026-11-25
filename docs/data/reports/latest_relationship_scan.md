# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T19:07:28.445619+00:00`
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

- `market_context_high->unknown_1h` score `32174.4458` n `45` status `ready` deltaP `1.8662` edge `2681.2008` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21841.7854` n `45` status `ready` deltaP `1.958` edge `1820.1496` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `939.4908` n `31` status `ready` deltaP `2.0813` edge `78.2946` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `588.8379` n `31` status `ready` deltaP `3.1766` edge `49.0543` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `300.8567` n `31` status `ready` deltaP `5.7292` edge `25.0332` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.4367` n `31` status `ready` deltaP `52.0833` edge `3.5225` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.6027` n `31` status `ready` deltaP `54.5139` edge `3.1868` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.5409` n `31` status `ready` deltaP `54.8611` edge `2.846` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.0086` n `31` status `ready` deltaP `41.2355` edge `0.7533` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.4583` n `31` status `ready` deltaP `26.6079` edge `0.8645` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `11.1765` n `31` status `ready` deltaP `37.8344` edge `0.7272` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4636` n `31` status `ready` deltaP `53.125` edge `0.2678` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.1116` n `31` status `ready` deltaP `17.8452` edge `0.9345` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.4711` n `31` status `ready` deltaP `47.0934` edge `0.1548` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6775` n `31` status `ready` deltaP `19.9874` edge `0.1919` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4014` n `31` status `ready` deltaP `36.31` edge `0.0674` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6327` n `31` status `ready` deltaP `31.244` edge `0.0196` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5163` n `31` status `ready` deltaP `10.6094` edge `0.298` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4068` n `45` status `ready` deltaP `29.6307` edge `0.0315` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2947` n `31` status `ready` deltaP `12.8549` edge `0.2442` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
