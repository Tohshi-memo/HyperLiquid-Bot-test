# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T05:07:27.270759+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6738`

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

- `market_context_high->unknown_1h` score `324.6064` n `50` status `ready` deltaP `6.8323` edge `27.0099` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.8688` n `50` status `ready` deltaP `6.8598` edge `23.36` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.1377` n `132` status `ready` deltaP `29.214` edge `1.421` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9751` n `50` status `ready` deltaP `18.9146` edge `0.5255` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4578` n `132` status `ready` deltaP `23.6743` edge `0.6957` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.32` n `132` status `ready` deltaP `24.3687` edge `0.5991` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.9011` n `50` status `ready` deltaP `14.2073` edge `0.3597` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9866` n `50` status `ready` deltaP `15.1976` edge `0.1926` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8267` n `50` status `ready` deltaP `31.9268` edge `0.0362` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.7448` n `132` status `ready` deltaP `24.5196` edge `0.175` maxDD `-6.1115`
- `news_risk_high->index_24h` score `2.6835` n `132` status `ready` deltaP `25.5208` edge `0.1013` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6483` n `50` status `ready` deltaP `13.006` edge `0.2003` maxDD `-3.6387`
- `news_risk_high->metal_24h` score `1.9188` n `132` status `ready` deltaP `22.6957` edge `0.2221` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4052` n `50` status `ready` deltaP `19.8922` edge `0.0109` maxDD `-0.113`
- `news_risk_high->crypto_alt_4h` score `1.0` n `132` status `ready` deltaP `9.3588` edge `0.2602` maxDD `-13.8071`
- `news_risk_high->equity_1h` score `0.575` n `132` status `ready` deltaP `6.4054` edge `0.0631` maxDD `-1.2977`
- `news_risk_high->crypto_alt_1h` score `0.5188` n `132` status `ready` deltaP `6.8545` edge `0.0886` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3175` n `132` status `ready` deltaP `6.9951` edge `0.0086` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0939` n `50` status `ready` deltaP `9.9461` edge `-0.0019` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.1847` n `50` status `ready` deltaP `-1.4431` edge `0.051` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
