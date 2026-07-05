# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T20:52:30.401950+00:00`
- Price records: `672`
- Market context records: `5811`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9076`

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

- `market_context_high->equity_4h` score `0.1739` n `290` status `ready` deltaP `5.8011` edge `0.1216` maxDD `-6.9958`
- `market_context_high->equity_24h` score `0.1613` n `248` status `ready` deltaP `15.3954` edge `0.4187` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.1876` n `290` status `ready` deltaP `3.4483` edge `0.0015` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.6304` n `290` status `ready` deltaP `-1.5476` edge `-0.0034` maxDD `-2.7017`
- `market_context_high->index_1h` score `-0.6498` n `290` status `ready` deltaP `0.064` edge `0.0031` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.6732` n `290` status `ready` deltaP `1.847` edge `-0.001` maxDD `-2.0596`
- `market_context_high->equity_1h` score `-0.6962` n `290` status `ready` deltaP `2.4562` edge `0.0263` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.8999` n `290` status `ready` deltaP `3.0766` edge `0.0366` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0623` n `290` status `ready` deltaP `1.593` edge `0.0343` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2437` n `290` status `ready` deltaP `-0.123` edge `0.0101` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.4002` n `248` status `ready` deltaP `10.3607` edge `0.0318` maxDD `-5.4306`
- `market_context_high->fx_4h` score `-1.4133` n `290` status `ready` deltaP `1.4266` edge `0.0042` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2081` n `290` status `ready` deltaP `-4.3735` edge `-0.0441` maxDD `-9.4534`
- `market_context_high->crypto_major_4h` score `-2.6988` n `290` status `ready` deltaP `8.1203` edge `0.1582` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.7812` n `290` status `ready` deltaP `-1.968` edge `-0.0179` maxDD `-8.7266`
- `market_context_high->index_24h` score `-4.3261` n `248` status `ready` deltaP `3.7131` edge `0.0292` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.3711` n `290` status `ready` deltaP `5.819` edge `0.0978` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-5.6024` n `248` status `ready` deltaP `-4.5363` edge `-0.2363` maxDD `-20.1367`
- `market_context_high->commodity_24h` score `-6.0716` n `248` status `ready` deltaP `-13.1496` edge `-0.0665` maxDD `-32.6068`
- `market_context_high->crypto_major_24h` score `-11.4135` n `248` status `ready` deltaP `-2.453` edge `-0.2643` maxDD `-35.6375`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
