# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T18:52:51.235169+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8651`

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

- `market_context_high->unknown_4h` score `80.3806` n `135` status `ready` deltaP `4.5472` edge `6.6833` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9819` n `135` status `ready` deltaP `27.1875` edge `0.0527` maxDD `-2.17`
- `market_context_high->fx_4h` score `0.4383` n `135` status `ready` deltaP `12.8963` edge `0.0104` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.3944` n `147` status `ready` deltaP `9.8375` edge `0.0031` maxDD `-0.1986`
- `market_context_high->unknown_1h` score `0.1572` n `147` status `ready` deltaP `0.7394` edge `0.0571` maxDD `-1.5807`
- `market_context_high->metal_1h` score `-0.0838` n `147` status `ready` deltaP `8.4637` edge `0.0075` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3088` n `135` status `ready` deltaP `7.1465` edge `0.0485` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3434` n `147` status `ready` deltaP `7.7966` edge `0.0323` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4936` n `135` status `ready` deltaP `10.8681` edge `0.0215` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.4971` n `147` status `ready` deltaP `0.4216` edge `0.01` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6511` n `147` status `ready` deltaP `-1.7822` edge `-0.0033` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8659` n `135` status `ready` deltaP `7.5564` edge `-0.0073` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.0387` n `135` status `ready` deltaP `15.2315` edge `0.0897` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4424` n `147` status `ready` deltaP `1.5927` edge `-0.0043` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.6734` n `135` status `ready` deltaP `8.0671` edge `0.1032` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.6892` n `147` status `ready` deltaP `2.2465` edge `0.0048` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0082` n `135` status `ready` deltaP `-7.9946` edge `-0.0352` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7704` n `135` status `ready` deltaP `0.544` edge `-0.0013` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.9042` n `135` status `ready` deltaP `2.745` edge `-0.0869` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.593` n `135` status `ready` deltaP `-0.8062` edge `-0.1883` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
