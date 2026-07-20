# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T00:22:29.851574+00:00`
- Price records: `672`
- Market context records: `7305`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14793`

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

- `market_context_high->fx_1h` score `-0.1023` n `126` status `ready` deltaP `5.148` edge `0.0015` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6376` n `126` status `ready` deltaP `-1.7589` edge `-0.0128` maxDD `-1.5775`
- `market_context_high->commodity_4h` score `-0.7638` n `119` status `ready` deltaP `1.7128` edge `-0.0125` maxDD `-2.4139`
- `market_context_high->crypto_major_1h` score `-0.7643` n `126` status `ready` deltaP `3.4146` edge `0.0203` maxDD `-7.6171`
- `market_context_high->index_1h` score `-0.7875` n `126` status `ready` deltaP `-4.5688` edge `-0.007` maxDD `-2.0801`
- `market_context_high->fx_24h` score `-0.8033` n `113` status `ready` deltaP `2.5195` edge `0.003` maxDD `-2.1564`
- `market_context_high->fx_4h` score `-1.0135` n `119` status `ready` deltaP `3.0221` edge `0.0099` maxDD `-1.4649`
- `market_context_high->crypto_alt_1h` score `-1.0833` n `126` status `ready` deltaP `-1.1382` edge `0.0212` maxDD `-5.9775`
- `market_context_high->unknown_4h` score `-1.6135` n `119` status `ready` deltaP `4.4425` edge `0.0718` maxDD `-6.2031`
- `market_context_high->unknown_1h` score `-1.7408` n `126` status `ready` deltaP `0.8079` edge `-0.0881` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.7818` n `119` status `ready` deltaP `3.2346` edge `0.0243` maxDD `-15.2776`
- `market_context_high->metal_1h` score `-2.1681` n `126` status `ready` deltaP `-10.0941` edge `-0.003` maxDD `-1.4971`
- `market_context_high->metal_4h` score `-2.3576` n `119` status `ready` deltaP `-8.1549` edge `0.0003` maxDD `-4.8549`
- `market_context_high->crypto_major_4h` score `-2.7371` n `119` status `ready` deltaP `3.9339` edge `0.0123` maxDD `-23.4879`
- `market_context_high->equity_1h` score `-2.7505` n `126` status `ready` deltaP `-8.5371` edge `-0.0601` maxDD `-14.182`
- `market_context_high->unknown_24h` score `-2.9814` n `114` status `ready` deltaP `-7.3465` edge `-0.0333` maxDD `-11.9961`
- `market_context_high->commodity_24h` score `-3.6448` n `113` status `ready` deltaP `-7.2397` edge `-0.1757` maxDD `-2.3815`
- `market_context_high->index_4h` score `-4.3359` n `119` status `ready` deltaP `-13.0201` edge `-0.045` maxDD `-8.0288`
- `market_context_high->crypto_alt_24h` score `-8.5002` n `114` status `ready` deltaP `3.5818` edge `-0.2423` maxDD `-59.7075`
- `market_context_high->metal_24h` score `-10.6523` n `114` status `ready` deltaP `-28.125` edge `-0.1229` maxDD `-19.5169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
