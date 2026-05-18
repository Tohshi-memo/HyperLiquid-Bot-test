# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T18:52:21.949632+00:00`
- Price records: `672`
- Market context records: `1145`
- Flow alert records: `5197`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `19.3825` n `152` status `ready` deltaP `42.8545` edge `1.4427` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.101` n `152` status `ready` deltaP `19.2069` edge `0.832` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.4564` n `152` status `ready` deltaP `18.686` edge `0.5898` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.932` n `152` status `ready` deltaP `17.2971` edge `0.4348` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.6695` n `152` status `ready` deltaP `-1.6082` edge `0.6499` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4632` n `168` status `ready` deltaP `12.0137` edge `0.1915` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1625` n `168` status `ready` deltaP `9.3568` edge `0.1028` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5936` n `168` status `ready` deltaP `8.3939` edge `0.0252` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.545` n `168` status `ready` deltaP `4.0775` edge `0.056` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.3786` n `168` status `ready` deltaP `10.1336` edge `0.1731` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.1773` n `168` status `ready` deltaP `7.5813` edge `0.0408` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0777` n `168` status `ready` deltaP `7.7167` edge `0.0006` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1441` n `168` status `ready` deltaP `7.3995` edge `-0.0003` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.1483` n `168` status `ready` deltaP `3.3932` edge `0.0493` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.7704` n `168` status `ready` deltaP `7.3679` edge `0.1486` maxDD `-16.7194`
- `market_context_high->fx_4h` score `-0.8487` n `168` status `ready` deltaP `-1.0453` edge `-0.0022` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.865` n `168` status `ready` deltaP `-3.272` edge `-0.0083` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-2.2673` n `168` status `ready` deltaP `7.6147` edge `-0.0443` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-3.2832` n `168` status `ready` deltaP `9.0085` edge `-0.212` maxDD `-6.7322`
- `market_context_high->unknown_24h` score `-3.351` n `152` status `ready` deltaP `3.7829` edge `-0.0315` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
