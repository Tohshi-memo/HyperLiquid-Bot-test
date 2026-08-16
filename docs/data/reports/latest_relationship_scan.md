# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T23:07:26.090397+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `110.929` n `81` status `ready` deltaP `-29.7261` edge `14.6882` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `5.8099` n `81` status `ready` deltaP `38.2716` edge `0.2431` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.0784` n `111` status `ready` deltaP `12.5508` edge `0.0533` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.1861` n `115` status `ready` deltaP `1.9383` edge `0.0127` maxDD `-0.624`
- `market_context_high->metal_4h` score `-0.2859` n `111` status `ready` deltaP `14.3801` edge `0.0082` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.3862` n `115` status `ready` deltaP `0.4061` edge `0.0016` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.4729` n `111` status `ready` deltaP `2.9184` edge `0.0016` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5075` n `115` status `ready` deltaP `1.5465` edge `-0.0038` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.602` n `115` status `ready` deltaP `-3.5433` edge `-0.0014` maxDD `-0.5064`
- `market_context_high->crypto_major_4h` score `-0.6424` n `111` status `ready` deltaP `3.0008` edge `0.0013` maxDD `-3.9599`
- `market_context_high->index_24h` score `-0.7989` n `81` status `ready` deltaP `6.8479` edge `-0.0469` maxDD `-0.8927`
- `market_context_high->index_4h` score `-1.1417` n `111` status `ready` deltaP `-9.0419` edge `-0.0052` maxDD `-0.8045`
- `market_context_high->crypto_major_24h` score `-1.3277` n `81` status `ready` deltaP `-3.6266` edge `0.1292` maxDD `-16.019`
- `market_context_high->crypto_alt_1h` score `-1.9328` n `115` status `ready` deltaP `-4.9323` edge `-0.0224` maxDD `-4.796`
- `market_context_high->crypto_major_1h` score `-1.9847` n `115` status `ready` deltaP `-5.6522` edge `-0.0282` maxDD `-3.9605`
- `market_context_high->fx_24h` score `-2.2463` n `81` status `ready` deltaP `-17.9012` edge `-0.0079` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.3549` n `81` status `ready` deltaP `-14.1783` edge `0.0438` maxDD `-7.0954`
- `market_context_high->equity_1h` score `-2.4212` n `115` status `ready` deltaP `-9.5378` edge `-0.0429` maxDD `-4.289`
- `market_context_high->crypto_alt_4h` score `-5.4039` n `111` status `ready` deltaP `-6.8955` edge `-0.0362` maxDD `-16.786`
- `market_context_high->equity_24h` score `-5.5589` n `81` status `ready` deltaP `1.1381` edge `-0.3284` maxDD `-25.0155`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
