# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T15:52:20.505819+00:00`
- Price records: `672`
- Market context records: `2472`
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

- `market_context_high->unknown_24h` score `5.6064` n `117` status `ready` deltaP `22.1287` edge `0.3525` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9787` n `136` status `ready` deltaP `20.5882` edge `0.4622` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8443` n `136` status `ready` deltaP `18.0236` edge `0.3812` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2997` n `117` status `ready` deltaP `12.3131` edge `0.602` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.6387` n `136` status `ready` deltaP `10.4556` edge `0.1689` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.807` n `136` status `ready` deltaP `8.6342` edge `0.1291` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.6326` n `136` status `ready` deltaP `6.8774` edge `0.1256` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.0405` n `117` status `ready` deltaP `1.7896` edge `0.689` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0401` n `117` status `ready` deltaP `3.3921` edge `0.0788` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.1386` n `136` status `ready` deltaP `6.4024` edge `0.0237` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.2982` n `117` status `ready` deltaP `17.5882` edge `0.0106` maxDD `-6.8828`
- `market_context_high->fx_1h` score `-0.3414` n `136` status `ready` deltaP `0.7353` edge `0.0048` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.416` n `136` status `ready` deltaP `0.9114` edge `0.0082` maxDD `-3.0759`
- `market_context_high->index_1h` score `-0.4753` n `136` status `ready` deltaP `-1.9857` edge `0.0017` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.5658` n `136` status `ready` deltaP `1.0215` edge `0.018` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.603` n `136` status `ready` deltaP `2.1795` edge `-0.004` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.6785` n `136` status `ready` deltaP `-1.3988` edge `0.0083` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.7699` n `136` status `ready` deltaP `0.3743` edge `0.0172` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8126` n `117` status `ready` deltaP `4.4471` edge `0.0047` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9576` n `136` status `ready` deltaP `2.977` edge `0.0391` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
