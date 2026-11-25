# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T18:52:29.668292+00:00`
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

- `market_context_high->unknown_1h` score `32177.9834` n `45` status `ready` deltaP `1.8662` edge `2681.4956` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21845.2066` n `45` status `ready` deltaP `1.958` edge `1820.4347` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `943.0284` n `31` status `ready` deltaP `2.0813` edge `78.5894` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `592.2591` n `31` status `ready` deltaP `3.1766` edge `49.3394` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `305.0399` n `31` status `ready` deltaP `5.7292` edge `25.3818` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.4499` n `31` status `ready` deltaP `52.0833` edge `3.5236` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.6051` n `31` status `ready` deltaP `54.5139` edge `3.187` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.5884` n `31` status `ready` deltaP `55.0347` edge `2.8488` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.0182` n `31` status `ready` deltaP `41.2355` edge `0.7541` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.5353` n `31` status `ready` deltaP `26.7604` edge `0.8699` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `11.2437` n `31` status `ready` deltaP `37.8344` edge `0.7328` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4636` n `31` status `ready` deltaP `53.125` edge `0.2678` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.1624` n `31` status `ready` deltaP `17.9976` edge `0.94` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.4862` n `31` status `ready` deltaP `47.267` edge `0.1549` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7099` n `31` status `ready` deltaP `19.9874` edge `0.1946` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4074` n `31` status `ready` deltaP `36.31` edge `0.0679` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6351` n `31` status `ready` deltaP `31.244` edge `0.0198` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5311` n `31` status `ready` deltaP `10.7591` edge `0.2989` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.408` n `45` status `ready` deltaP `29.6307` edge `0.0316` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3095` n `31` status `ready` deltaP `13.0046` edge `0.2451` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
