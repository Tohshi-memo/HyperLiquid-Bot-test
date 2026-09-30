# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T09:07:29.691956+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `news_risk_high->unknown_24h` score `720.6892` n `135` status `ready` deltaP `1.9097` edge `60.0447` maxDD `0.0`
- `market_context_high->unknown_1h` score `528.535` n `42` status `ready` deltaP `7.4992` edge `43.9995` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `470.1357` n `30` status `ready` deltaP `8.2317` edge `39.1231` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.6279` n `135` status `ready` deltaP `28.206` edge `1.3019` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.6715` n `135` status `ready` deltaP `26.8171` edge `0.6954` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.3665` n `135` status `ready` deltaP `23.9931` edge `0.7693` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.6414` n `135` status `ready` deltaP `33.0093` edge `0.1312` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.252` n `135` status `ready` deltaP `25.1852` edge `0.2305` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.8143` n `135` status `ready` deltaP `28.8663` edge `0.2022` maxDD `-9.143`
- `market_context_high->fx_4h` score `2.4284` n `30` status `ready` deltaP `28.0996` edge `0.0281` maxDD `-0.0449`
- `market_context_high->crypto_alt_1h` score `1.8847` n `42` status `ready` deltaP `11.1563` edge `0.149` maxDD `-3.6387`
- `news_risk_high->crypto_alt_4h` score `1.6853` n `135` status `ready` deltaP `10.35` edge `0.3374` maxDD `-15.9436`
- `market_context_high->crypto_major_4h` score `1.4287` n `30` status `ready` deltaP `-0.2845` edge `0.1913` maxDD `-3.294`
- `market_context_high->crypto_major_1h` score `1.3117` n `42` status `ready` deltaP `8.3547` edge `0.1146` maxDD `-3.546`
- `news_risk_high->crypto_alt_1h` score `1.0706` n `135` status `ready` deltaP `9.2515` edge `0.1186` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.8936` n `135` status `ready` deltaP `9.2515` edge `0.0751` maxDD `-1.6514`
- `market_context_high->fx_1h` score `0.8823` n `42` status `ready` deltaP `13.8651` edge `0.0075` maxDD `-0.113`
- `market_context_high->equity_1h` score `0.7382` n `42` status `ready` deltaP `11.1563` edge `0.0628` maxDD `-2.4027`
- `news_risk_high->index_1h` score `0.4814` n `135` status `ready` deltaP `8.6682` edge `0.0111` maxDD `-0.302`
- `market_context_high->metal_1h` score `0.2694` n `42` status `ready` deltaP `5.5247` edge `0.0198` maxDD `-0.4338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
