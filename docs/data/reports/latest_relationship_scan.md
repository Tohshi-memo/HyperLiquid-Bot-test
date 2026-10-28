# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T15:37:31.652221+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8518`

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

- `market_context_high->unknown_24h` score `1439.8088` n `138` status `ready` deltaP `-3.359` edge `120.0992` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.1124` n `149` status `ready` deltaP `4.385` edge `1.8287` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.51` n `138` status `ready` deltaP `25.1434` edge `0.027` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1745` n `149` status `ready` deltaP `7.269` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0053` n `149` status `ready` deltaP `8.1437` edge `0.006` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0715` n `149` status `ready` deltaP `8.6264` edge `0.008` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2658` n `149` status `ready` deltaP `7.7282` edge `0.0427` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3738` n `149` status `ready` deltaP `7.3539` edge `0.0417` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4573` n `138` status `ready` deltaP `11.8056` edge `0.0199` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.7015` n `149` status `ready` deltaP `-0.9394` edge `0.0062` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7196` n `149` status `ready` deltaP `-3.1749` edge `-0.0028` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7427` n `149` status `ready` deltaP `9.0563` edge `-0.0015` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3719` n `149` status `ready` deltaP `1.3885` edge `0.0061` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5346` n `149` status `ready` deltaP `3.0452` edge `0.0193` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-2.748` n `138` status `ready` deltaP `2.9967` edge `0.0314` maxDD `-8.43`
- `market_context_high->equity_24h` score `-2.847` n `138` status `ready` deltaP `6.567` edge `0.0154` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.9738` n `149` status `ready` deltaP `-8.5693` edge `-0.0285` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.173` n `138` status `ready` deltaP `1.6229` edge `0.0681` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.3795` n `149` status `ready` deltaP `4.119` edge `-0.0288` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.296` n `149` status `ready` deltaP `-2.7152` edge `-0.1375` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
