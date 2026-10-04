# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T11:21:16.544141+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4964`

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

- `market_context_high->unknown_4h` score `153.1526` n `75` status `ready` deltaP `8.996` edge `12.7171` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `125.3065` n `87` status `ready` deltaP `1.3749` edge `10.4745` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `11.9592` n `46` status `ready` deltaP `29.2195` edge `0.9291` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `11.3771` n `46` status `ready` deltaP `35.6582` edge `0.7756` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.8451` n `65` status `ready` deltaP `38.8016` edge `0.6654` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `9.9699` n `59` status `ready` deltaP `26.0328` edge `0.6673` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.3083` n `65` status `ready` deltaP `23.75` edge `0.5851` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.3107` n `75` status `ready` deltaP `25.1606` edge `0.4285` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.463` n `59` status `ready` deltaP `29.6875` edge `0.174` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.9263` n `65` status `ready` deltaP `26.9793` edge `0.2086` maxDD `-2.9013`
- `market_context_high->crypto_alt_4h` score `3.8953` n `75` status `ready` deltaP `13.0833` edge `0.3663` maxDD `-7.6465`
- `news_risk_high->index_4h` score `3.1538` n `65` status `ready` deltaP `34.3528` edge `0.06` maxDD `-0.4296`
- `market_context_high->equity_24h` score `2.9958` n `46` status `ready` deltaP `6.7255` edge `0.3045` maxDD `-6.3081`
- `news_risk_high->crypto_major_1h` score `2.9676` n `65` status `ready` deltaP `12.7107` edge `0.1981` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.5749` n `87` status `ready` deltaP `17.8213` edge `0.1408` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5012` n `65` status `ready` deltaP `21.2125` edge `0.1086` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1213` n `65` status `ready` deltaP `26.0663` edge `0.018` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6062` n `65` status `ready` deltaP `5.1681` edge `0.1513` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3591` n `46` status `ready` deltaP `25.536` edge `0.1058` maxDD `-1.8102`
- `market_context_high->crypto_alt_1h` score `0.9945` n `87` status `ready` deltaP `6.4767` edge `0.131` maxDD `-3.6376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
