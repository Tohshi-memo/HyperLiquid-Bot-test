# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T19:22:23.246258+00:00`
- Price records: `672`
- Market context records: `2487`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.3491` n `124` status `ready` deltaP `19.8869` edge `0.346` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.2574` n `137` status `ready` deltaP `21.7175` edge `0.4779` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9549` n `137` status `ready` deltaP `18.5809` edge `0.3867` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.9572` n `124` status `ready` deltaP `11.2175` edge `0.5654` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.3518` n `137` status `ready` deltaP `8.9806` edge `0.1563` maxDD `-3.6149`
- `market_context_high->crypto_alt_1h` score `0.5006` n `149` status `ready` deltaP `6.7426` edge `0.1155` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.4645` n `149` status `ready` deltaP `7.264` edge `0.1097` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.0592` n `124` status `ready` deltaP `4.3514` edge `0.074` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0775` n `124` status `ready` deltaP `1.2768` edge `0.6773` maxDD `-43.6595`
- `market_context_high->equity_24h` score `-0.1569` n `124` status `ready` deltaP `18.4084` edge `0.0169` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.211` n `137` status `ready` deltaP `5.6091` edge `0.0197` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3189` n `149` status `ready` deltaP `1.2288` edge `0.0044` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.4943` n `149` status `ready` deltaP `1.7502` edge `0.0191` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.4989` n `149` status `ready` deltaP `3.3869` edge `0.0013` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5685` n `149` status `ready` deltaP `-0.3556` edge `0.0044` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.5909` n `137` status `ready` deltaP `0.2126` edge `0.0088` maxDD `-0.8774`
- `market_context_high->metal_1h` score `-0.7261` n `149` status `ready` deltaP `1.3111` edge `0.0067` maxDD `-3.0759`
- `market_context_high->equity_1h` score `-0.8807` n `149` status `ready` deltaP `-0.3807` edge `0.013` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9034` n `124` status `ready` deltaP `2.8506` edge `0.0037` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9547` n `137` status `ready` deltaP `3.238` edge `0.0376` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
