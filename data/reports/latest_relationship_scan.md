# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T15:52:20.474676+00:00`
- Price records: `672`
- Market context records: `1752`
- Flow alert records: `6944`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `market_context_high->metal_24h` score `7.1721` n `163` status `ready` deltaP `27.012` edge `0.6602` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.9345` n `196` status `ready` deltaP `20.514` edge `0.5344` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.3432` n `196` status `ready` deltaP `22.1099` edge `0.4551` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.2325` n `163` status `ready` deltaP `18.9215` edge `0.3494` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `4.0902` n `163` status `ready` deltaP `15.1489` edge `0.7719` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.9983` n `196` status `ready` deltaP `16.1119` edge `0.2519` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `2.8431` n `196` status `ready` deltaP `12.7271` edge `0.3792` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.8376` n `163` status `ready` deltaP `17.1619` edge `0.6119` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.8407` n `196` status `ready` deltaP `11.4081` edge `0.1029` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7993` n `196` status `ready` deltaP `7.5706` edge `0.1185` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.5653` n `163` status `ready` deltaP `19.454` edge `0.776` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.24` n `196` status `ready` deltaP `4.8974` edge `0.0947` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0838` n `196` status `ready` deltaP `5.1204` edge `0.0537` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1796` n `196` status `ready` deltaP `4.0664` edge `0.0211` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.249` n `196` status `ready` deltaP `12.444` edge `0.1543` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.4887` n `196` status `ready` deltaP `6.2447` edge `0.0293` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.634` n `163` status `ready` deltaP `6.8965` edge `0.0061` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6723` n `196` status `ready` deltaP `-3.2659` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->crypto_alt_24h` score `-0.6907` n `163` status `ready` deltaP `20.288` edge `0.9881` maxDD `-88.8062`
- `market_context_high->unknown_1h` score `-1.7278` n `196` status `ready` deltaP `-0.11` edge `0.0037` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
