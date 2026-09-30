# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T12:52:30.983942+00:00`
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

- `market_context_high->unknown_1h` score `403.5982` n `51` status `ready` deltaP `7.9194` edge `33.5853` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `320.0973` n `45` status `ready` deltaP `8.2317` edge `26.6199` maxDD `0.0`
- `news_risk_high->unknown_24h` score `25.8244` n `135` status `ready` deltaP `1.9097` edge `2.1393` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.0113` n `135` status `ready` deltaP `26.6435` edge `1.1776` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `6.8169` n `135` status `ready` deltaP `25.2546` edge `0.6346` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.2834` n `135` status `ready` deltaP `23.8195` edge `0.6802` maxDD `-15.8971`
- `market_context_high->crypto_major_4h` score `5.3452` n `45` status `ready` deltaP `15.2066` edge `0.4144` maxDD `-3.294`
- `market_context_high->fx_4h` score `3.395` n `45` status `ready` deltaP `37.9912` edge `0.0427` maxDD `-0.0449`
- `news_risk_high->index_24h` score `3.3736` n `135` status `ready` deltaP `31.4468` edge `0.1193` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.9161` n `135` status `ready` deltaP `23.1018` edge `0.2164` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.5257` n `135` status `ready` deltaP `27.4943` edge `0.1873` maxDD `-9.143`
- `market_context_high->crypto_major_1h` score `2.2962` n `51` status `ready` deltaP `14.8409` edge `0.1534` maxDD `-3.546`
- `market_context_high->crypto_alt_1h` score `2.0046` n `51` status `ready` deltaP `12.6101` edge `0.1493` maxDD `-3.6387`
- `market_context_high->fx_1h` score `1.4789` n `51` status `ready` deltaP `20.7086` edge `0.0116` maxDD `-0.113`
- `market_context_high->crypto_alt_4h` score `1.4382` n `45` status `ready` deltaP `11.0265` edge `0.2402` maxDD `-7.6792`
- `news_risk_high->equity_1h` score `0.8648` n `135` status `ready` deltaP `9.4012` edge `0.0717` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.7996` n `135` status `ready` deltaP `7.9042` edge `0.105` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4634` n `135` status `ready` deltaP `8.5185` edge `0.0106` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.4247` n `135` status `ready` deltaP `8.0635` edge `0.2476` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `-0.0088` n `51` status `ready` deltaP `9.1229` edge `-0.0073` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
