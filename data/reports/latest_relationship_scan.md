# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T15:22:30.039318+00:00`
- Price records: `672`
- Market context records: `2573`
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

- `market_context_high->crypto_alt_4h` score `6.0947` n `146` status `ready` deltaP `26.2634` edge `0.6007` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.0401` n `116` status `ready` deltaP `13.2663` edge `0.62` maxDD `-16.7415`
- `market_context_high->unknown_24h` score `4.6342` n `116` status `ready` deltaP `19.4863` edge `0.2891` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.2308` n `146` status `ready` deltaP `17.9648` edge `0.4138` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.5547` n `146` status `ready` deltaP `12.0294` edge `0.1681` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.5255` n `116` status `ready` deltaP `20.546` edge `0.0567` maxDD `-2.324`
- `market_context_high->unknown_4h` score `1.3164` n `146` status `ready` deltaP `9.9712` edge `0.1482` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `1.0134` n `146` status `ready` deltaP `10.3601` edge `0.1348` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6422` n `116` status `ready` deltaP `6.0584` edge `0.1112` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.429` n `116` status `ready` deltaP `0.5448` edge `0.6892` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2476` n `146` status `ready` deltaP `8.5178` edge `0.048` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1239` n `146` status `ready` deltaP `3.9414` edge `0.0128` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4224` n `146` status `ready` deltaP `1.6508` edge `0.0201` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4243` n `146` status `ready` deltaP `5.502` edge `0.0158` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5718` n `146` status `ready` deltaP `0.2133` edge `0.0044` maxDD `-0.278`
- `market_context_high->fx_24h` score `-0.5957` n `116` status `ready` deltaP `1.5685` edge `0.0042` maxDD `-1.6157`
- `market_context_high->metal_1h` score `-0.6596` n `146` status `ready` deltaP `0.8121` edge `0.0144` maxDD `-2.9823`
- `market_context_high->metal_4h` score `-0.6898` n `146` status `ready` deltaP `4.0448` edge `0.0543` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.8` n `146` status `ready` deltaP `-0.527` edge `0.0207` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8244` n `146` status `ready` deltaP `0.5367` edge `0.0135` maxDD `-0.8621`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
