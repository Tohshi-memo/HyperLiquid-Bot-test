# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T00:07:31.384476+00:00`
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

- `market_context_high->unknown_1h` score `364.0607` n `50` status `ready` deltaP `10.4251` edge `30.2738` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.1043` n `50` status `ready` deltaP `10.5183` edge `24.2719` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.0774` n `70` status `ready` deltaP `37.9564` edge `1.1221` maxDD `-1.4956`
- `market_context_high->crypto_alt_24h` score `10.727` n `50` status `ready` deltaP `20.5278` edge `0.9274` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.4058` n `70` status `ready` deltaP `33.7351` edge `0.6074` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.0258` n `50` status `ready` deltaP `31.8264` edge `0.6816` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.7527` n `50` status `ready` deltaP `18.9146` edge `0.5903` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `7.0569` n `109` status `ready` deltaP `27.8376` edge `0.5369` maxDD `-6.4195`
- `market_context_high->crypto_alt_4h` score `6.1993` n `50` status `ready` deltaP `17.1037` edge `0.5315` maxDD `-7.6465`
- `market_context_high->crypto_alt_1h` score `3.2673` n `50` status `ready` deltaP `14.9521` edge `0.2389` maxDD `-3.6376`
- `news_risk_high->crypto_major_24h` score `3.0373` n `70` status `ready` deltaP `8.3978` edge `0.5491` maxDD `-10.2547`
- `news_risk_high->equity_4h` score `3.0349` n `109` status `ready` deltaP `25.5566` edge `0.1438` maxDD `-2.9013`
- `market_context_high->crypto_major_1h` score `3.0229` n `50` status `ready` deltaP `13.5509` edge `0.2066` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8153` n `50` status `ready` deltaP `31.4695` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->crypto_major_4h` score `2.632` n `109` status `ready` deltaP `19.7219` edge `0.3749` maxDD `-7.849`
- `market_context_high->fx_1h` score `1.4603` n `50` status `ready` deltaP `20.491` edge `0.0115` maxDD `-0.113`
- `news_risk_high->index_24h` score `1.4356` n `70` status `ready` deltaP `17.9811` edge `0.0448` maxDD `-0.2696`
- `news_risk_high->metal_24h` score `1.4051` n `70` status `ready` deltaP `14.6528` edge `0.2084` maxDD `-2.0759`
- `news_risk_high->crypto_alt_1h` score `1.2902` n `109` status `ready` deltaP `5.8328` edge `0.1247` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.2858` n `50` status `ready` deltaP `6.0208` edge `0.3109` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
