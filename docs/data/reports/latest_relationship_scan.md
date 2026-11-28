# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T19:07:31.361500+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7476`

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

- `news_risk_high->unknown_4h` score `3270.5655` n `31` status `ready` deltaP `3.1766` edge `272.5316` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `2757.3108` n `31` status `ready` deltaP `2.231` edge `229.7786` maxDD `-0.7395`
- `news_risk_high->crypto_major_24h` score `25.4579` n `31` status `ready` deltaP `39.5833` edge `1.8576` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.7431` n `31` status `ready` deltaP `37.6736` edge `1.3941` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.2957` n `31` status `ready` deltaP `29.8611` edge `0.9089` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.5395` n `31` status `ready` deltaP `24.7787` edge `0.7168` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.0342` n `31` status `ready` deltaP `33.871` edge `0.3251` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.9988` n `31` status `ready` deltaP `19.0647` edge `0.7837` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2004` n `31` status `ready` deltaP `43.274` edge `0.1577` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.8854` n `31` status `ready` deltaP `16.9299` edge `0.2384` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.7557` n `31` status `ready` deltaP `33.4137` edge `0.0329` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.5772` n `31` status `ready` deltaP `27.4306` edge `0.0319` maxDD `0.0`
- `news_risk_high->index_1h` score `2.4062` n `31` status `ready` deltaP `29.4476` edge `0.0127` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.3306` n `31` status `ready` deltaP `15.6461` edge `0.1086` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.1391` n `31` status `ready` deltaP `7.6154` edge `0.2696` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9845` n `31` status `ready` deltaP `10.9088` edge `0.2174` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.18` n `31` status `ready` deltaP `25.3911` edge `0.0099` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.5857` n `31` status `ready` deltaP `12.7901` edge `0.0296` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.5852` n `65` status `ready` deltaP `11.8293` edge `0.0095` maxDD `-0.1673`
- `news_risk_high->metal_4h` score `0.482` n `31` status `ready` deltaP `13.7293` edge `0.026` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
