# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T15:46:44.211526+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4278`

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

- `market_context_high->unknown_1h` score `32303.0522` n `45` status `ready` deltaP `1.7165` edge `2691.919` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22127.0909` n `45` status `ready` deltaP `2.5678` edge `1843.921` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1068.0972` n `31` status `ready` deltaP `1.9316` edge `89.0128` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `874.1434` n `31` status `ready` deltaP `3.7864` edge `72.8257` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `37.1323` n `31` status `ready` deltaP `49.4792` edge `2.7645` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.9007` n `31` status `ready` deltaP `40.7986` edge `2.6364` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.2795` n `31` status `ready` deltaP `47.0486` edge `2.3763` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.087` n `31` status `ready` deltaP `41.2355` edge `0.6765` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9886` n `31` status `ready` deltaP `24.3214` edge `0.8406` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.2354` n `31` status `ready` deltaP `32.6515` edge `0.6` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.7584` n `31` status `ready` deltaP `15.2537` edge `0.9065` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.457` n `31` status `ready` deltaP `54.2115` edge `0.1895` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.1581` n `31` status `ready` deltaP `38.5417` edge `0.1729` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4377` n `31` status `ready` deltaP `18.6401` edge `0.1809` maxDD `-0.1621`
- `market_context_high->fx_4h` score `2.9413` n `45` status `ready` deltaP `35.5759` edge `0.0364` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8976` n `31` status `ready` deltaP `31.7369` edge `0.0559` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.6013` n `31` status `ready` deltaP `11.6573` edge `0.3019` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5356` n `31` status `ready` deltaP `30.1961` edge `0.0185` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2746` n `31` status `ready` deltaP `11.3579` edge `0.2516` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6303` n `31` status `ready` deltaP `30.7803` edge `0.0317` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
