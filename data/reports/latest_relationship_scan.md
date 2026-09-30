# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T04:37:39.791033+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7190`

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

- `news_risk_high->unknown_24h` score `890.0392` n `132` status `ready` deltaP `1.9097` edge `74.1572` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.4681` n `132` status `ready` deltaP `29.9084` edge `1.4439` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.6656` n `132` status `ready` deltaP `29.4034` edge `0.761` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `8.655` n `132` status `ready` deltaP `24.8895` edge `0.8707` maxDD `-15.8971`
- `news_risk_high->index_24h` score `4.0406` n `132` status `ready` deltaP `35.7639` edge `0.1461` maxDD `-0.4916`
- `news_risk_high->equity_4h` score `3.0102` n `135` status `ready` deltaP `30.0858` edge `0.2104` maxDD `-9.143`
- `news_risk_high->metal_24h` score `2.3887` n `132` status `ready` deltaP `27.3675` edge `0.2512` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `2.0472` n `135` status `ready` deltaP `11.8744` edge `0.3574` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1593` n `135` status `ready` deltaP `9.7006` edge `0.123` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9415` n `135` status `ready` deltaP `9.7006` edge `0.0761` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5077` n `135` status `ready` deltaP `8.9676` edge `0.0113` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0201` n `135` status `ready` deltaP `8.1685` edge `0.0292` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4448` n `135` status `ready` deltaP `2.9385` edge `0.0716` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4551` n `135` status `ready` deltaP `1.4571` edge `0.0153` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2444` n `135` status `ready` deltaP `-7.2369` edge `0.0295` maxDD `-2.9297`
- `news_risk_high->fx_4h` score `-1.4068` n `135` status `ready` deltaP `7.2279` edge `-0.0072` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.486` n `135` status `ready` deltaP `-3.3785` edge `0.1035` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-1.8289` n `135` status `ready` deltaP `-8.6682` edge `-0.0092` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.9296` n `135` status `ready` deltaP `-10.2528` edge `-0.0044` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2388` n `135` status `ready` deltaP `-8.8449` edge `0.0138` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
