# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T13:37:17.038253+00:00`
- Price records: `672`
- Market context records: `870`
- Flow alert records: `2443`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `22.2695` n `31` status `ready` deltaP `32.6389` edge `1.6382` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.2695` n `31` status `ready` deltaP `32.6389` edge `1.6382` maxDD `0.0`
- `risk_on_high->equity_24h` score `13.7434` n `31` status `ready` deltaP `25.3472` edge `0.9763` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.7434` n `31` status `ready` deltaP `25.3472` edge `0.9763` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `13.6678` n `31` status `ready` deltaP `7.8125` edge `1.0869` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.6678` n `31` status `ready` deltaP `7.8125` edge `1.0869` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.1366` n `165` status `ready` deltaP `28.3965` edge `0.9388` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5705` n `165` status `ready` deltaP `7.2064` edge `0.5043` maxDD `-0.0508`
- `risk_on_high->index_24h` score `4.4969` n `31` status `ready` deltaP `27.9514` edge `0.1884` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.4969` n `31` status `ready` deltaP `27.9514` edge `0.1884` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4456` n `32` status `ready` deltaP `8.003` edge `0.2703` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4456` n `32` status `ready` deltaP `8.003` edge `0.2703` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `2.9809` n `32` status `ready` deltaP `22.3323` edge `0.12` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.9809` n `32` status `ready` deltaP `22.3323` edge `0.12` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.8234` n `32` status `ready` deltaP `20.4268` edge `0.1363` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8234` n `32` status `ready` deltaP `20.4268` edge `0.1363` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.5777` n `32` status `ready` deltaP `14.253` edge `0.1286` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5777` n `32` status `ready` deltaP `14.253` edge `0.1286` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.7289` n `31` status `ready` deltaP `-7.2972` edge `0.338` maxDD `-1.7492`
- `risk_on_and_context->commodity_24h` score `1.7289` n `31` status `ready` deltaP `-7.2972` edge `0.338` maxDD `-1.7492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
