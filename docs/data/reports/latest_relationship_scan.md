# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T06:52:29.454436+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5004`

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

- `market_context_high->unknown_4h` score `257.3662` n `57` status `ready` deltaP `7.3118` edge `21.4128` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `199.703` n `69` status `ready` deltaP `1.3755` edge `16.6742` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.4544` n `46` status `ready` deltaP `32.2546` edge `1.1168` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `13.179` n `46` status `ready` deltaP `38.6971` edge `0.9055` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `11.2817` n `59` status `ready` deltaP `29.0955` edge `0.7562` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.1072` n `65` status `ready` deltaP `40.1736` edge `0.6781` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5686` n `65` status `ready` deltaP `24.6646` edge `0.6007` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.1768` n `57` status `ready` deltaP `19.7957` edge `0.4531` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.814` n `59` status `ready` deltaP `32.7556` edge `0.1828` maxDD `0.0`
- `market_context_high->equity_24h` score `4.3076` n `46` status `ready` deltaP `9.7882` edge `0.3934` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9373` n `65` status `ready` deltaP `27.1318` edge `0.2085` maxDD `-2.9013`
- `market_context_high->crypto_alt_4h` score `3.3159` n `57` status `ready` deltaP `18.3488` edge `0.4317` maxDD `-7.6465`
- `news_risk_high->index_4h` score `3.1696` n `65` status `ready` deltaP `34.5052` edge `0.0603` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9843` n `65` status `ready` deltaP `13.1598` edge `0.1965` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.6105` n `69` status `ready` deltaP `16.5712` edge `0.1521` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5646` n `65` status `ready` deltaP `21.9747` edge `0.1088` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1333` n `65` status `ready` deltaP `26.216` edge `0.018` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.0767` n `69` status `ready` deltaP `11.6246` edge `0.1702` maxDD `-3.6376`
- `market_context_high->fx_4h` score `1.8999` n `57` status `ready` deltaP `23.5238` edge `0.0333` maxDD `-0.2105`
- `news_risk_high->crypto_alt_1h` score `1.5451` n `65` status `ready` deltaP `4.8687` edge `0.1482` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
