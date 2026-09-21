# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T04:22:36.321291+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9272`

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

- `news_risk_high->crypto_major_24h` score `24.5717` n `98` status `ready` deltaP `12.7906` edge `2.6482` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.4821` n `98` status `ready` deltaP `13.531` edge `2.0214` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `15.4287` n `55` status `ready` deltaP `0.9479` edge `1.2944` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `4.7062` n `101` status `ready` deltaP `20.7483` edge `0.3748` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.9029` n `101` status `ready` deltaP `20.7483` edge `0.3127` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.775` n `101` status `ready` deltaP `16.5308` edge `0.1676` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1695` n `101` status `ready` deltaP `18.6266` edge `0.1089` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1099` n `98` status `ready` deltaP `22.6013` edge `0.1222` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0524` n `58` status `ready` deltaP `7.8051` edge `0.061` maxDD `-0.36`
- `market_context_high->index_1h` score `0.8538` n `58` status `ready` deltaP `12.2238` edge `0.0152` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6317` n `101` status `ready` deltaP `14.7477` edge `0.0145` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.4442` n `101` status `ready` deltaP `15.5744` edge `0.0386` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.4114` n `55` status `ready` deltaP `15.8453` edge `0.0108` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.3537` n `58` status `ready` deltaP `6.2978` edge `0.0183` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.2947` n `58` status `ready` deltaP `8.1768` edge `0.0057` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1663` n `101` status `ready` deltaP `8.1834` edge `0.0229` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.0224` n `101` status `ready` deltaP `3.4179` edge `0.0159` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1154` n `58` status `ready` deltaP `-1.1924` edge `0.0702` maxDD `-2.7494`
- `news_risk_high->equity_24h` score `-0.2082` n `98` status `ready` deltaP `13.2724` edge `0.0351` maxDD `-4.941`
- `news_risk_high->fx_1h` score `-0.2543` n `101` status `ready` deltaP `2.5434` edge `0.0062` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
