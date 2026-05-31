# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T15:07:23.673753+00:00`
- Price records: `672`
- Market context records: `2469`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9236`

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

- `market_context_high->unknown_24h` score `5.6136` n `117` status `ready` deltaP `22.1287` edge `0.3531` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9655` n `136` status `ready` deltaP `20.5882` edge `0.4611` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8755` n `136` status `ready` deltaP `18.0236` edge `0.3838` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.3478` n `117` status `ready` deltaP `12.8339` edge `0.6047` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.6133` n `136` status `ready` deltaP `10.3031` edge `0.1678` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.8801` n `136` status `ready` deltaP `9.0833` edge `0.1322` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.7129` n `136` status `ready` deltaP `7.3265` edge `0.1293` maxDD `-6.1656`
- `market_context_high->index_24h` score `-0.016` n `117` status `ready` deltaP `2.8713` edge `0.0776` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0459` n `117` status `ready` deltaP `1.2687` edge `0.6814` maxDD `-43.6595`
- `market_context_high->index_4h` score `-0.1` n `136` status `ready` deltaP `6.8598` edge `0.0256` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.2742` n `117` status `ready` deltaP `17.5882` edge `0.0126` maxDD `-6.8828`
- `market_context_high->fx_1h` score `-0.3578` n `136` status `ready` deltaP `0.4359` edge `0.0047` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.4082` n `136` status `ready` deltaP `0.9114` edge `0.0092` maxDD `-3.0759`
- `market_context_high->index_1h` score `-0.4457` n `136` status `ready` deltaP `-1.5366` edge `0.0025` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.5766` n `136` status `ready` deltaP `1.0215` edge `0.0171` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.6147` n `136` status `ready` deltaP `2.1795` edge `-0.0055` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.6873` n `136` status `ready` deltaP `-1.5513` edge `0.0082` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.7184` n `136` status `ready` deltaP `0.8234` edge `0.0185` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.842` n `117` status `ready` deltaP `3.9262` edge `0.0044` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9396` n `136` status `ready` deltaP `2.977` edge `0.0406` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
