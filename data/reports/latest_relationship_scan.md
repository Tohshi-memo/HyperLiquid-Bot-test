# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T18:37:30.768436+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6812`

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

- `market_context_high->unknown_1h` score `337.0226` n `50` status `ready` deltaP `8.3293` edge `28.0346` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `285.2464` n `50` status `ready` deltaP `6.8598` edge `23.7248` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3238` n `108` status `ready` deltaP `35.4745` edge `1.4781` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.17` n `50` status `ready` deltaP `32.8681` edge `0.77` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.4358` n `50` status `ready` deltaP `19.8293` edge `0.5578` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.2686` n `50` status `ready` deltaP `11.3264` edge `0.5345` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.1946` n `50` status `ready` deltaP `16.9512` edge `0.4492` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.9621` n `108` status `ready` deltaP `21.2385` edge `0.5873` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.9492` n `50` status `ready` deltaP `19.2153` edge `0.5644` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.2513` n `121` status `ready` deltaP `26.2258` edge `0.1657` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1672` n `50` status `ready` deltaP `35.4329` edge `0.0412` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0431` n `50` status `ready` deltaP `14.7485` edge `0.2003` maxDD `-2.2692`
- `news_risk_high->equity_24h` score `2.9626` n `108` status `ready` deltaP `21.5857` edge `0.4708` maxDD `-9.4579`
- `market_context_high->crypto_alt_1h` score `2.9182` n `50` status `ready` deltaP `13.4551` edge `0.2198` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4672` n `108` status `ready` deltaP `24.4213` edge `0.0906` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2513` n `108` status `ready` deltaP `26.3889` edge `0.2401` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5897` n `50` status `ready` deltaP `21.988` edge `0.0123` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9019` n `50` status `ready` deltaP `14.7917` edge `0.0741` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.511` n `50` status `ready` deltaP `14.4306` edge `0.0711` maxDD `-1.8102`
- `news_risk_high->equity_1h` score `0.3426` n `121` status `ready` deltaP `6.061` edge `0.0418` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
