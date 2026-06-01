# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T17:22:25.149162+00:00`
- Price records: `672`
- Market context records: `2581`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->unknown_24h` score `6.4192` n `124` status `ready` deltaP `18.834` edge `0.4422` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.2023` n `146` status `ready` deltaP `26.8731` edge `0.6056` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.3956` n `146` status `ready` deltaP `18.2697` edge `0.4255` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.4815` n `146` status `ready` deltaP `11.8797` edge `0.163` maxDD `-6.1656`
- `market_context_high->crypto_major_24h` score `1.3638` n `124` status `ready` deltaP `9.2686` edge `0.5028` maxDD `-27.0753`
- `market_context_high->unknown_4h` score `1.227` n `146` status `ready` deltaP `9.5139` edge `0.1438` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.999` n `146` status `ready` deltaP `10.5098` edge `0.1326` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.7541` n `124` status `ready` deltaP `1.9209` edge `0.7217` maxDD `-39.0265`
- `market_context_high->index_24h` score `0.6979` n `124` status `ready` deltaP `7.5045` edge `0.1062` maxDD `-2.5127`
- `market_context_high->equity_24h` score `0.6798` n `124` status `ready` deltaP `17.8147` edge `0.0049` maxDD `-2.3615`
- `market_context_high->index_4h` score `0.3508` n `146` status `ready` deltaP `9.4325` edge `0.0505` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1635` n `146` status `ready` deltaP `3.642` edge `0.0115` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4212` n `146` status `ready` deltaP `1.8005` edge `0.0192` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4542` n `146` status `ready` deltaP `5.2026` edge `0.0153` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.4832` n `146` status `ready` deltaP `5.1119` edge `0.0644` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.62` n `146` status `ready` deltaP `1.1115` edge `0.0157` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6497` n `146` status `ready` deltaP `-0.6849` edge `0.0039` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.8396` n `146` status `ready` deltaP `-0.527` edge `0.0174` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8634` n `146` status `ready` deltaP `0.0793` edge `0.0133` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-1.0518` n `124` status `ready` deltaP `1.5625` edge `0.0013` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
