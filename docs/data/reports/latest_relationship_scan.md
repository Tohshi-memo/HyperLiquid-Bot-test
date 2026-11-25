# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T21:07:27.356295+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3720`

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

- `market_context_high->unknown_1h` score `32159.399` n `45` status `ready` deltaP `1.4171` edge `2679.9499` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21830.785` n `45` status `ready` deltaP `1.958` edge `1819.2329` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `924.4441` n `31` status `ready` deltaP `1.6322` edge `77.0437` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `577.8375` n `31` status `ready` deltaP `3.1766` edge `48.1376` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `299.5967` n `31` status `ready` deltaP `5.7292` edge `24.9282` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.2891` n `31` status `ready` deltaP `52.0833` edge `3.5102` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.3625` n `31` status `ready` deltaP `54.1667` edge `3.1691` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.0177` n `31` status `ready` deltaP `53.6458` edge `2.8105` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.8432` n `31` status `ready` deltaP `40.3674` edge `0.7453` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9901` n `31` status `ready` deltaP `26.4555` edge `0.8265` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.6005` n `31` status `ready` deltaP `37.8344` edge `0.6792` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4775` n `31` status `ready` deltaP `53.2986` edge `0.2678` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.808` n `31` status `ready` deltaP `17.6927` edge `0.8966` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3794` n `31` status `ready` deltaP `46.0518` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6655` n `31` status `ready` deltaP `20.1371` edge `0.1899` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3498` n `31` status `ready` deltaP `36.31` edge `0.0631` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6686` n `31` status `ready` deltaP `31.6931` edge `0.0196` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.429` n `31` status `ready` deltaP `10.0106` edge `0.2908` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3339` n `45` status `ready` deltaP `28.8685` edge `0.0305` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2471` n `31` status `ready` deltaP `12.7052` edge `0.2391` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
