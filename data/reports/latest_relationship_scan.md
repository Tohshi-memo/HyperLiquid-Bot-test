# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T10:37:37.360933+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `news_risk_high->unknown_24h` score `438.9988` n `135` status `ready` deltaP `1.9097` edge `36.5705` maxDD `0.0`
- `market_context_high->unknown_1h` score `432.14` n `48` status `ready` deltaP `7.7969` edge `35.9646` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `366.3681` n `36` status `ready` deltaP `8.2317` edge `30.4758` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.8425` n `135` status `ready` deltaP `27.1643` edge `1.2434` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.227` n `135` status `ready` deltaP `25.7755` edge `0.6653` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.8985` n `135` status `ready` deltaP `23.9931` edge `0.7303` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.4885` n `135` status `ready` deltaP `31.9676` edge `0.1254` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.0811` n `135` status `ready` deltaP `24.1435` edge `0.2232` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.9425` n `36` status `ready` deltaP `33.6551` edge `0.0339` maxDD `-0.0449`
- `market_context_high->crypto_major_4h` score `2.7663` n `36` status `ready` deltaP `7.6897` edge `0.2496` maxDD `-3.294`
- `news_risk_high->equity_4h` score `2.6427` n `135` status `ready` deltaP `27.9516` edge `0.194` maxDD `-9.143`
- `market_context_high->crypto_alt_1h` score `2.4398` n `48` status `ready` deltaP `15.02` edge `0.1695` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.2298` n `48` status `ready` deltaP `13.4107` edge `0.1574` maxDD `-3.546`
- `market_context_high->fx_1h` score `1.3194` n `48` status `ready` deltaP `18.7749` edge `0.0112` maxDD `-0.113`
- `news_risk_high->crypto_alt_4h` score `1.3061` n `135` status `ready` deltaP `9.4354` edge `0.3119` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.9123` n `135` status `ready` deltaP `8.3533` edge `0.1114` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.8936` n `135` status `ready` deltaP `9.4012` edge `0.0741` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.4814` n `135` status `ready` deltaP `8.6682` edge `0.0111` maxDD `-0.302`
- `market_context_high->crypto_alt_4h` score `0.0373` n `36` status `ready` deltaP `4.065` edge `0.107` maxDD `-7.6792`
- `market_context_high->equity_1h` score `0.0285` n `48` status `ready` deltaP `3.5679` edge `0.0474` maxDD `-2.4027`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
