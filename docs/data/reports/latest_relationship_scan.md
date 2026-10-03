# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T08:52:27.870099+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4806`

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

- `market_context_high->unknown_1h` score `366.1246` n `50` status `ready` deltaP `10.8743` edge `30.4428` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.9002` n `50` status `ready` deltaP `12.0427` edge `24.4114` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `12.585` n `50` status `ready` deltaP `26.0833` edge `1.0452` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.5739` n `69` status `ready` deltaP `31.2953` edge `0.721` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `10.009` n `50` status `ready` deltaP `33.7361` edge `0.7508` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.0055` n `74` status `ready` deltaP `38.7319` edge `0.5959` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.7153` n `74` status `ready` deltaP `29.9934` edge `0.5774` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3777` n `50` status `ready` deltaP `17.5427` edge `0.5682` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.1783` n `50` status `ready` deltaP `17.561` edge `0.5267` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.2526` n `69` status `ready` deltaP `32.9786` edge `0.1504` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9768` n `74` status `ready` deltaP `29.7997` edge `0.194` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3201` n `50` status `ready` deltaP `15.2515` edge `0.2413` maxDD `-3.6376`
- `news_risk_high->crypto_major_1h` score `3.1509` n `74` status `ready` deltaP `15.9168` edge `0.192` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9977` n `50` status `ready` deltaP `13.7006` edge `0.2035` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9444` n `50` status `ready` deltaP `32.9939` edge `0.0389` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.4821` n `74` status `ready` deltaP `27.3814` edge `0.0505` maxDD `-0.4296`
- `news_risk_high->metal_4h` score `2.2444` n `74` status `ready` deltaP `19.3969` edge `0.0993` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `2.0517` n `74` status `ready` deltaP `8.711` edge `0.1648` maxDD `-2.4854`
- `news_risk_high->equity_1h` score `1.4278` n `74` status `ready` deltaP `13.6754` edge `0.064` maxDD `-0.8948`
- `market_context_high->fx_1h` score `1.4244` n `50` status `ready` deltaP `20.0419` edge `0.0115` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
