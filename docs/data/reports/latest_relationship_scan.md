# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T20:37:25.384586+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3732`

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

- `market_context_high->unknown_1h` score `32159.5574` n `45` status `ready` deltaP `1.5668` edge `2679.9621` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21834.589` n `45` status `ready` deltaP `1.958` edge `1819.5499` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `924.6024` n `31` status `ready` deltaP `1.7819` edge `77.0559` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `581.6415` n `31` status `ready` deltaP `3.1766` edge `48.4546` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `299.9819` n `31` status `ready` deltaP `5.7292` edge `24.9603` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.3419` n `31` status `ready` deltaP `52.0833` edge `3.5146` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.4304` n `31` status `ready` deltaP `54.3403` edge `3.1736` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.1558` n `31` status `ready` deltaP `53.9931` edge `2.8197` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.9022` n `31` status `ready` deltaP `40.7146` edge `0.7479` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.0717` n `31` status `ready` deltaP `26.4555` edge `0.8333` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.7169` n `31` status `ready` deltaP `37.8344` edge `0.6889` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4787` n `31` status `ready` deltaP `53.2986` edge `0.2679` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.8634` n `31` status `ready` deltaP `17.6927` edge `0.9037` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.4096` n `31` status `ready` deltaP `46.399` edge `0.1543` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6715` n `31` status `ready` deltaP `20.1371` edge `0.1904` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3594` n `31` status `ready` deltaP `36.31` edge `0.0639` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6686` n `31` status `ready` deltaP `31.6931` edge `0.0196` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4563` n `31` status `ready` deltaP `10.31` edge `0.2923` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3595` n `45` status `ready` deltaP `29.1734` edge `0.0306` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2635` n `31` status `ready` deltaP `12.8549` edge `0.2402` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
