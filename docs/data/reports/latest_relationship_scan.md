# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T16:22:32.372133+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4862`

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

- `market_context_high->unknown_1h` score `359.1105` n `50` status `ready` deltaP `11.1737` edge `29.8563` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.8682` n `50` status `ready` deltaP `11.128` edge `24.3315` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.3984` n `73` status `ready` deltaP `39.795` edge `1.0388` maxDD `-1.005`
- `news_risk_high->equity_24h` score `9.2256` n `73` status `ready` deltaP `33.4475` edge `0.5943` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.0819` n `50` status `ready` deltaP `32.3472` edge `0.6828` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0731` n `50` status `ready` deltaP `16.5347` edge `0.8162` maxDD `-11.6271`
- `market_context_high->crypto_major_4h` score `6.8379` n `50` status `ready` deltaP `16.7805` edge `0.5283` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7956` n `50` status `ready` deltaP `14.5122` edge `0.4318` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.6166` n `116` status `ready` deltaP `20.3743` edge `0.3833` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `2.9483` n `50` status `ready` deltaP `13.9042` edge `0.2193` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9437` n `50` status `ready` deltaP `13.7006` edge `0.199` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8481` n `50` status `ready` deltaP `31.7744` edge `0.039` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4135` n `116` status `ready` deltaP `22.0984` edge `0.1234` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.8232` n `50` status `ready` deltaP `9.6667` edge `0.3555` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.568` n `73` status `ready` deltaP `6.5116` edge `0.473` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4603` n `50` status `ready` deltaP `20.491` edge `0.0115` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3047` n `73` status `ready` deltaP `12.8354` edge `0.2091` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `1.0141` n `116` status `ready` deltaP `13.4357` edge `0.2714` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.8009` n `116` status `ready` deltaP `4.8008` edge `0.0908` maxDD `-2.4854`
- `market_context_high->index_24h` score `0.7656` n `50` status `ready` deltaP `14.2708` edge `0.0601` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
