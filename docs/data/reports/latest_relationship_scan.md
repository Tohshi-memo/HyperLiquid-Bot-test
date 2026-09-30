# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T02:52:25.398751+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7026`

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

- `news_risk_high->unknown_24h` score `1276.9096` n `132` status `ready` deltaP `1.9097` edge `106.3964` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.4929` n `132` status `ready` deltaP `31.1237` edge `1.5212` maxDD `-1.0093`
- `news_risk_high->crypto_major_24h` score `9.4734` n `132` status `ready` deltaP `26.1048` edge `0.9308` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `9.1744` n `132` status `ready` deltaP `30.6187` edge `0.7953` maxDD `-9.4579`
- `news_risk_high->index_24h` score `4.2122` n `132` status `ready` deltaP `36.9791` edge `0.1523` maxDD `-0.4916`
- `news_risk_high->equity_4h` score `2.9266` n `135` status `ready` deltaP `29.476` edge `0.2075` maxDD `-9.143`
- `news_risk_high->metal_24h` score `2.5331` n `132` status `ready` deltaP `28.5827` edge `0.2616` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `2.1002` n `135` status `ready` deltaP `12.0269` edge `0.3608` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0982` n `135` status `ready` deltaP `9.2515` edge `0.1209` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.92` n `135` status `ready` deltaP `9.5509` edge `0.0753` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5089` n `135` status `ready` deltaP `8.9676` edge `0.0114` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0761` n `135` status `ready` deltaP `7.5587` edge `0.0286` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4826` n `135` status `ready` deltaP `1.1577` edge `0.015` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.512` n `135` status `ready` deltaP `2.4894` edge `0.069` maxDD `-7.2607`
- `news_risk_high->metal_4h` score `-1.235` n `135` status `ready` deltaP `-7.2369` edge `0.0307` maxDD `-2.9297`
- `news_risk_high->crypto_major_4h` score `-1.4235` n `135` status `ready` deltaP `-3.226` edge `0.1105` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.4764` n `135` status `ready` deltaP `6.1608` edge `-0.009` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8102` n `135` status `ready` deltaP `-8.3688` edge `-0.0088` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.89` n `135` status `ready` deltaP `-9.8037` edge `-0.0041` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2371` n `135` status `ready` deltaP `-8.6924` edge `0.013` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
