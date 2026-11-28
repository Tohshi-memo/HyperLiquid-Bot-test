# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T03:07:29.755533+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3248`

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

- `news_risk_high->unknown_1h` score `3312.7057` n `31` status `ready` deltaP `1.6322` edge `276.0655` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3175.4265` n `31` status `ready` deltaP `3.634` edge `264.6003` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `18.0384` n `31` status `ready` deltaP `28.7695` edge `1.3114` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.4576` n `31` status `ready` deltaP `26.6898` edge `0.8602` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.3009` n `31` status `ready` deltaP `23.9168` edge `0.7823` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.0513` n `31` status `ready` deltaP `18.6811` edge `0.5501` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `4.9682` n `31` status `ready` deltaP `27.9259` edge `0.2759` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.721` n `31` status `ready` deltaP `38.6762` edge `0.1484` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.3511` n `31` status `ready` deltaP `13.1196` edge `0.6121` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.3452` n `31` status `ready` deltaP `12.1877` edge `0.225` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.1726` n `31` status `ready` deltaP `26.753` edge `0.0112` maxDD `-0.0136`
- `news_risk_high->index_4h` score `2.1631` n `31` status `ready` deltaP `27.0112` edge `0.0262` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.162` n `31` status `ready` deltaP `24.6101` edge `0.0161` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.0836` n `31` status `ready` deltaP `13.9994` edge `0.099` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.7081` n `31` status `ready` deltaP `4.7711` edge `0.2333` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.562` n `31` status `ready` deltaP `7.9148` edge `0.1832` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.071` n `31` status `ready` deltaP `23.5947` edge `0.0079` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3523` n `31` status `ready` deltaP `8.8267` edge `0.0261` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2008` n `31` status `ready` deltaP `9.461` edge `0.0184` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3843` n `31` status `ready` deltaP `-2.6608` edge `0.0119` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
