# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T04:07:27.748482+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7162`

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

- `news_risk_high->unknown_24h` score `1000.528` n `132` status `ready` deltaP `1.9097` edge `83.3646` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.7599` n `132` status `ready` deltaP `30.2556` edge `1.4659` maxDD `-1.0093`
- `news_risk_high->crypto_major_24h` score `8.906` n `132` status `ready` deltaP `25.2368` edge `0.8893` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `8.8278` n `132` status `ready` deltaP `29.7507` edge `0.7722` maxDD `-9.4579`
- `news_risk_high->index_24h` score `4.0923` n `132` status `ready` deltaP `36.1111` edge `0.1481` maxDD `-0.4916`
- `news_risk_high->equity_4h` score `3.0078` n `135` status `ready` deltaP `30.0858` edge `0.2102` maxDD `-9.143`
- `news_risk_high->metal_24h` score `2.4318` n `132` status `ready` deltaP `27.7147` edge `0.2544` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `2.0918` n `135` status `ready` deltaP `12.0269` edge `0.3601` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1713` n `135` status `ready` deltaP `9.7006` edge `0.124` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9739` n `135` status `ready` deltaP `10.0` edge `0.0768` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5341` n `135` status `ready` deltaP `9.267` edge `0.0115` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0201` n `135` status `ready` deltaP `8.1685` edge `0.0292` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.3957` n `135` status `ready` deltaP `3.2379` edge `0.0737` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4539` n `135` status `ready` deltaP `1.4571` edge `0.0154` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2397` n `135` status `ready` deltaP `-7.2369` edge `0.0301` maxDD `-2.9297`
- `news_risk_high->fx_4h` score `-1.4274` n `135` status `ready` deltaP `6.923` edge `-0.0078` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.435` n `135` status `ready` deltaP `-3.0736` edge `0.108` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-1.8468` n `135` status `ready` deltaP `-8.9676` edge `-0.0095` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.9296` n `135` status `ready` deltaP `-10.2528` edge `-0.0044` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2443` n `135` status `ready` deltaP `-8.8449` edge `0.0131` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
