# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T02:07:31.650999+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.897` n `50` status `ready` deltaP `10.5749` edge `30.3425` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.1707` n `50` status `ready` deltaP `10.2134` edge `24.3628` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.308` n `70` status `ready` deltaP `31.6815` edge `1.0477` maxDD `-2.9926`
- `market_context_high->crypto_alt_24h` score `10.92` n `50` status `ready` deltaP `21.3958` edge `0.9377` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.0154` n `70` status `ready` deltaP `33.7351` edge `0.6582` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.8942` n `50` status `ready` deltaP `31.3056` edge `0.6741` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.7975` n `101` status `ready` deltaP `32.1752` edge `0.5697` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4391` n `50` status `ready` deltaP `17.6951` edge `0.5723` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.7943` n `70` status `ready` deltaP `12.1627` edge `0.6034` maxDD `-5.1298`
- `news_risk_high->crypto_major_4h` score `5.9142` n `101` status `ready` deltaP `23.9525` edge `0.4201` maxDD `-3.9549`
- `market_context_high->crypto_alt_4h` score `5.856` n `50` status `ready` deltaP `16.0366` edge `0.51` maxDD `-7.6465`
- `market_context_high->crypto_alt_1h` score `3.2302` n `50` status `ready` deltaP `14.8024` edge `0.2368` maxDD `-3.6376`
- `news_risk_high->equity_4h` score `3.1509` n `101` status `ready` deltaP `25.8512` edge `0.1515` maxDD `-2.9013`
- `market_context_high->crypto_major_1h` score `3.0001` n `50` status `ready` deltaP `13.4012` edge `0.2057` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8043` n `50` status `ready` deltaP `31.3171` edge `0.0384` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.0296` n `70` status `ready` deltaP `20.4911` edge `0.0734` maxDD `-0.2696`
- `news_risk_high->metal_24h` score `1.7534` n `70` status `ready` deltaP `9.6329` edge `0.1993` maxDD `-2.0587`
- `news_risk_high->crypto_alt_1h` score `1.481` n `101` status `ready` deltaP `6.2281` edge `0.1338` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.2312` n `50` status `ready` deltaP `6.0208` edge `0.3039` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
