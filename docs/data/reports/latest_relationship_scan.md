# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T04:22:31.842016+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7164`

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

- `news_risk_high->unknown_24h` score `945.2344` n `132` status `ready` deltaP `1.9097` edge `78.7568` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.6152` n `132` status `ready` deltaP `30.082` edge `1.455` maxDD `-1.0093`
- `news_risk_high->crypto_major_24h` score `8.7829` n `132` status `ready` deltaP `25.0632` edge `0.8802` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `8.7479` n `132` status `ready` deltaP `29.577` edge `0.7667` maxDD `-9.4579`
- `news_risk_high->index_24h` score `4.0665` n `132` status `ready` deltaP `35.9375` edge `0.1471` maxDD `-0.4916`
- `news_risk_high->equity_4h` score `3.0114` n `135` status `ready` deltaP `30.0858` edge `0.2105` maxDD `-9.143`
- `news_risk_high->metal_24h` score `2.4103` n `132` status `ready` deltaP `27.5411` edge `0.2528` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `2.0726` n `135` status `ready` deltaP `12.0269` edge `0.3585` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1653` n `135` status `ready` deltaP `9.7006` edge `0.1235` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9583` n `135` status `ready` deltaP `9.8503` edge `0.0765` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5209` n `135` status `ready` deltaP `9.1173` edge `0.0114` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0201` n `135` status `ready` deltaP `8.1685` edge `0.0292` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4208` n `135` status `ready` deltaP `3.0882` edge `0.0726` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4539` n `135` status `ready` deltaP `1.4571` edge `0.0154` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2412` n `135` status `ready` deltaP `-7.2369` edge `0.0299` maxDD `-2.9297`
- `news_risk_high->fx_4h` score `-1.4171` n `135` status `ready` deltaP `7.0754` edge `-0.0075` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.4609` n `135` status `ready` deltaP `-3.226` edge `0.1057` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-1.8374` n `135` status `ready` deltaP `-8.8179` edge `-0.0093` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.9296` n `135` status `ready` deltaP `-10.2528` edge `-0.0044` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.242` n `135` status `ready` deltaP `-8.8449` edge `0.0134` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
