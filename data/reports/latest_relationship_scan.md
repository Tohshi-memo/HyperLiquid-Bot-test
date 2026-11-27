# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T06:07:25.868707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3564`

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

- `news_risk_high->unknown_1h` score `3222.3624` n `31` status `ready` deltaP `1.7819` edge `268.5359` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3183.901` n `31` status `ready` deltaP `3.7864` edge `265.3055` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `22.5416` n `31` status `ready` deltaP `31.9444` edge `1.6655` maxDD `0.0`
- `news_risk_high->equity_24h` score `20.2151` n `31` status `ready` deltaP `31.4236` edge `1.4751` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.1105` n `31` status `ready` deltaP `31.0764` edge `1.2187` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.127` n `31` status `ready` deltaP `23.1018` edge `0.6936` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.1234` n `31` status `ready` deltaP `32.6515` edge `0.424` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.8519` n `31` status `ready` deltaP `16.0159` edge `0.7852` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.6639` n `31` status `ready` deltaP `19.3605` edge `0.3704` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6943` n `31` status `ready` deltaP `39.1073` edge `0.1433` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.5953` n `31` status `ready` deltaP `32.9861` edge `0.0797` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6904` n `31` status `ready` deltaP `31.1271` edge `0.0427` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.6233` n `31` status `ready` deltaP `16.2449` edge `0.129` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3715` n `31` status `ready` deltaP `28.6991` edge `0.0148` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0823` n `31` status `ready` deltaP `6.8669` edge `0.2673` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.859` n `31` status `ready` deltaP `9.7112` edge `0.2093` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1761` n `31` status `ready` deltaP `25.3911` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4537` n `31` status `ready` deltaP `12.5098` edge `0.0305` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.0445` n `31` status `ready` deltaP `6.2352` edge `-0.0075` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6539` n `31` status `ready` deltaP `-4.9063` edge `0.0044` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
