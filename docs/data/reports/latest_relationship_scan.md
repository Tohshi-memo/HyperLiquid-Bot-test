# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T20:52:31.892649+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3780`

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

- `market_context_high->unknown_1h` score `32159.4038` n `45` status `ready` deltaP `1.4171` edge `2679.9503` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21830.8762` n `45` status `ready` deltaP `1.958` edge `1819.2405` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `924.4489` n `31` status `ready` deltaP `1.6322` edge `77.0441` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `577.9287` n `31` status `ready` deltaP `3.1766` edge `48.1452` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `300.0527` n `31` status `ready` deltaP `5.7292` edge `24.9662` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.3311` n `31` status `ready` deltaP `52.0833` edge `3.5137` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.4136` n `31` status `ready` deltaP `54.3403` edge `3.1722` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.0964` n `31` status `ready` deltaP `53.8194` edge `2.8159` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.8739` n `31` status `ready` deltaP `40.541` edge `0.7467` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.0249` n `31` status `ready` deltaP `26.4555` edge `0.8294` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.6425` n `31` status `ready` deltaP `37.8344` edge `0.6827` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4799` n `31` status `ready` deltaP `53.2986` edge `0.268` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.8299` n `31` status `ready` deltaP `17.6927` edge `0.8994` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3945` n `31` status `ready` deltaP `46.2254` edge `0.1542` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6703` n `31` status `ready` deltaP `20.1371` edge `0.1903` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3534` n `31` status `ready` deltaP `36.31` edge `0.0634` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6686` n `31` status `ready` deltaP `31.6931` edge `0.0196` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4454` n `31` status `ready` deltaP `10.1603` edge `0.2919` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3461` n `45` status `ready` deltaP `29.021` edge `0.0305` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2635` n `31` status `ready` deltaP `12.8549` edge `0.2402` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
