# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T15:22:20.857097+00:00`
- Price records: `672`
- Market context records: `2470`
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

- `market_context_high->unknown_24h` score `5.6124` n `117` status `ready` deltaP `22.1287` edge `0.353` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9679` n `136` status `ready` deltaP `20.5882` edge `0.4613` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8647` n `136` status `ready` deltaP `18.0236` edge `0.3829` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.3333` n `117` status `ready` deltaP `12.6603` edge `0.604` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.6291` n `136` status `ready` deltaP `10.4556` edge `0.1681` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.8621` n `136` status `ready` deltaP `8.9336` edge `0.1317` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.6925` n `136` status `ready` deltaP `7.1768` edge `0.1286` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.0039` n `117` status `ready` deltaP `3.0449` edge `0.0781` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0158` n `117` status `ready` deltaP `1.4424` edge `0.6841` maxDD `-43.6595`
- `market_context_high->index_4h` score `-0.1126` n `136` status `ready` deltaP `6.7073` edge `0.025` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.279` n `117` status `ready` deltaP `17.5882` edge `0.0122` maxDD `-6.8828`
- `market_context_high->fx_1h` score `-0.3578` n `136` status `ready` deltaP `0.4359` edge `0.0047` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.4098` n `136` status `ready` deltaP `0.9114` edge `0.009` maxDD `-3.0759`
- `market_context_high->index_1h` score `-0.4551` n `136` status `ready` deltaP `-1.6863` edge `0.0023` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.5754` n `136` status `ready` deltaP `1.0215` edge `0.0172` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.6139` n `136` status `ready` deltaP `2.1795` edge `-0.0054` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.6873` n `136` status `ready` deltaP `-1.5513` edge `0.0082` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.7316` n `136` status `ready` deltaP `0.6737` edge `0.0184` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8322` n `117` status `ready` deltaP `4.0998` edge `0.0045` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9456` n `136` status `ready` deltaP `2.977` edge `0.0401` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
