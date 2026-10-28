# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T15:22:28.574582+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8510`

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

- `market_context_high->unknown_24h` score `1465.1014` n `137` status `ready` deltaP `-3.4913` edge `122.2078` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.1244` n `149` status `ready` deltaP `4.385` edge `1.8297` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.5029` n `137` status `ready` deltaP `25.1901` edge `0.0261` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1745` n `149` status `ready` deltaP `7.269` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0199` n `149` status `ready` deltaP `8.2962` edge `0.0062` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0621` n `149` status `ready` deltaP `8.7761` edge `0.0082` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2557` n `149` status `ready` deltaP `7.8779` edge `0.043` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3738` n `149` status `ready` deltaP `7.3539` edge `0.0417` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4856` n `137` status `ready` deltaP `11.4406` edge `0.0187` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.7027` n `149` status `ready` deltaP `-0.9394` edge `0.0061` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.711` n `149` status `ready` deltaP `-3.0252` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7419` n `149` status `ready` deltaP `9.0563` edge `-0.0014` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.368` n `149` status `ready` deltaP `1.3885` edge `0.0066` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5198` n `149` status `ready` deltaP `3.1949` edge `0.0202` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-2.6848` n `137` status `ready` deltaP `3.3088` edge `0.0326` maxDD `-8.2716`
- `market_context_high->equity_24h` score `-2.9058` n `137` status `ready` deltaP `6.492` edge `0.011` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.9726` n `149` status `ready` deltaP `-8.5693` edge `-0.0284` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2055` n `137` status `ready` deltaP `1.2685` edge `0.0663` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.3936` n `149` status `ready` deltaP `4.119` edge `-0.0306` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3022` n `149` status `ready` deltaP `-2.7152` edge `-0.1383` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
