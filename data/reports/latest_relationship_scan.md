# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T10:22:27.920575+00:00`
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

- `news_risk_high->unknown_24h` score `482.6416` n `135` status `ready` deltaP `1.9097` edge `40.2074` maxDD `0.0`
- `market_context_high->unknown_1h` score `446.9252` n `47` status `ready` deltaP `7.7525` edge `37.197` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `376.3161` n `35` status `ready` deltaP `8.2317` edge `31.3048` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.9812` n `135` status `ready` deltaP `27.3379` edge `1.2538` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.2948` n `135` status `ready` deltaP `25.9491` edge `0.6698` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.9885` n `135` status `ready` deltaP `23.9931` edge `0.7378` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.5132` n `135` status `ready` deltaP `32.1412` edge `0.1263` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.1082` n `135` status `ready` deltaP `24.3171` edge `0.2243` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.8646` n `35` status `ready` deltaP `32.8615` edge `0.0327` maxDD `-0.0449`
- `news_risk_high->equity_4h` score `2.6777` n `135` status `ready` deltaP `28.1041` edge `0.1959` maxDD `-9.143`
- `market_context_high->crypto_alt_1h` score `2.4478` n `47` status `ready` deltaP `14.4604` edge `0.1739` maxDD `-3.6387`
- `market_context_high->crypto_major_4h` score `2.4009` n `35` status `ready` deltaP `6.5723` edge `0.2266` maxDD `-3.294`
- `market_context_high->crypto_major_1h` score `2.1576` n `47` status `ready` deltaP `12.7182` edge `0.156` maxDD `-3.546`
- `news_risk_high->crypto_alt_4h` score `1.4047` n `135` status `ready` deltaP `9.5878` edge `0.3191` maxDD `-15.9436`
- `market_context_high->fx_1h` score `1.2508` n `47` status `ready` deltaP `18.0214` edge `0.0105` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `0.9435` n `135` status `ready` deltaP `8.503` edge `0.113` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.902` n `135` status `ready` deltaP `9.4012` edge `0.0748` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.4826` n `135` status `ready` deltaP `8.6682` edge `0.0112` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.2268` n `47` status `ready` deltaP `4.7203` edge `0.0508` maxDD `-2.4027`
- `market_context_high->metal_1h` score `-0.1406` n `47` status `ready` deltaP `1.9302` edge `0.01` maxDD `-0.6053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
