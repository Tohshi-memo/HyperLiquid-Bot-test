# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T15:52:34.134497+00:00`
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

- `market_context_high->unknown_1h` score `359.2617` n `50` status `ready` deltaP `11.1737` edge `29.8689` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.741` n `50` status `ready` deltaP `11.128` edge `24.3209` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.366` n `73` status `ready` deltaP `39.795` edge `1.0361` maxDD `-1.005`
- `news_risk_high->equity_24h` score `9.335` n `73` status `ready` deltaP `33.7947` edge `0.6011` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.1287` n `50` status `ready` deltaP `32.3472` edge `0.6867` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0407` n `50` status `ready` deltaP `16.5347` edge `0.8135` maxDD `-11.6271`
- `market_context_high->crypto_major_4h` score `6.7595` n `50` status `ready` deltaP `16.4756` edge `0.5238` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7498` n `50` status `ready` deltaP `14.3598` edge `0.429` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.5708` n `116` status `ready` deltaP `20.2219` edge `0.3805` maxDD `-6.4195`
- `market_context_high->crypto_major_1h` score `2.9724` n `50` status `ready` deltaP `14.0` edge `0.1994` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9579` n `50` status `ready` deltaP `13.9042` edge `0.2201` maxDD `-3.6376`
- `market_context_high->fx_4h` score `2.8493` n `50` status `ready` deltaP `31.7744` edge `0.0391` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4643` n `116` status `ready` deltaP `22.4033` edge `0.1256` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.8943` n `50` status `ready` deltaP `10.0139` edge `0.3623` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5985` n `73` status `ready` deltaP `6.5116` edge `0.4769` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2992` n `73` status `ready` deltaP `12.8354` edge `0.2084` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.9631` n `116` status `ready` deltaP `13.1308` edge `0.2669` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.8105` n `116` status `ready` deltaP `4.8008` edge `0.0916` maxDD `-2.4854`
- `market_context_high->index_24h` score `0.7886` n `50` status `ready` deltaP `14.4444` edge `0.0619` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
