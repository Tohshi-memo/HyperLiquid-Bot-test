# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T16:07:34.657984+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4822`

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

- `market_context_high->unknown_1h` score `359.1933` n `50` status `ready` deltaP `11.1737` edge `29.8632` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.7818` n `50` status `ready` deltaP `11.128` edge `24.3243` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.3865` n `73` status `ready` deltaP `39.795` edge `1.0378` maxDD `-1.005`
- `news_risk_high->equity_24h` score `9.2791` n `73` status `ready` deltaP `33.6211` edge `0.5976` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.1071` n `50` status `ready` deltaP `32.3472` edge `0.6849` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0611` n `50` status `ready` deltaP `16.5347` edge `0.8152` maxDD `-11.6271`
- `market_context_high->crypto_major_4h` score `6.7957` n `50` status `ready` deltaP `16.628` edge `0.5258` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.763` n `50` status `ready` deltaP `14.3598` edge `0.4301` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.584` n `116` status `ready` deltaP `20.2219` edge `0.3816` maxDD `-6.4195`
- `market_context_high->crypto_major_1h` score `2.958` n `50` status `ready` deltaP `13.8503` edge `0.1992` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9531` n `50` status `ready` deltaP `13.9042` edge `0.2197` maxDD `-3.6376`
- `market_context_high->fx_4h` score `2.8481` n `50` status `ready` deltaP `31.7744` edge `0.039` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4365` n `116` status `ready` deltaP `22.2508` edge `0.1243` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.858` n `50` status `ready` deltaP `9.8403` edge `0.3588` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5844` n `73` status `ready` deltaP `6.5116` edge `0.4751` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4484` n `50` status `ready` deltaP `20.3413` edge `0.0115` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3024` n `73` status `ready` deltaP `12.8354` edge `0.2088` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.9866` n `116` status `ready` deltaP `13.2832` edge `0.2689` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.8057` n `116` status `ready` deltaP `4.8008` edge `0.0912` maxDD `-2.4854`
- `market_context_high->index_24h` score `0.7718` n `50` status `ready` deltaP `14.2708` edge `0.0609` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
