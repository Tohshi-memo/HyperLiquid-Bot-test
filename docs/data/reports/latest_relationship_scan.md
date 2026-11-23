# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T10:52:32.982945+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4482`

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

- `market_context_high->unknown_1h` score `21526.3519` n `65` status `ready` deltaP `0.6494` edge `1793.8745` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `14395.3544` n `65` status `ready` deltaP `4.8499` edge `1199.5944` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1297.8323` n `31` status `ready` deltaP `3.4286` edge `108.1474` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1131.0286` n `31` status `ready` deltaP `4.701` edge `94.2267` maxDD `-0.119`
- `news_risk_high->equity_24h` score `45.9155` n `31` status `ready` deltaP `51.3889` edge `3.4837` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.0461` n `31` status `ready` deltaP `48.6111` edge `2.7631` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.602` n `31` status `ready` deltaP `48.7847` edge `2.3916` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.5946` n `31` status `ready` deltaP `51.9994` edge `0.8137` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.5356` n `31` status `ready` deltaP `33.7186` edge `0.7014` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.1504` n `31` status `ready` deltaP `22.0348` edge `0.786` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.2228` n `31` status `ready` deltaP `49.3056` edge `0.2732` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.4308` n `31` status `ready` deltaP `54.5587` edge `0.185` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.1992` n `31` status `ready` deltaP `11.5952` edge `0.8592` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.6368` n `31` status `ready` deltaP `18.191` edge `0.2005` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.3386` n `31` status `ready` deltaP `35.0905` edge `0.0703` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6232` n `31` status `ready` deltaP `30.7949` edge `0.0218` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3644` n `31` status `ready` deltaP `9.1124` edge `0.2885` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9497` n `31` status `ready` deltaP `7.6154` edge `0.2349` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5103` n `31` status `ready` deltaP `28.8342` edge `0.0293` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4365` n `31` status `ready` deltaP `19.9793` edge `0.1067` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
