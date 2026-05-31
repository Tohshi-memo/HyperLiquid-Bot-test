# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T19:52:17.767573+00:00`
- Price records: `672`
- Market context records: `2489`
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

- `market_context_high->unknown_24h` score `5.4223` n `124` status `ready` deltaP `19.8869` edge `0.3521` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.0499` n `139` status `ready` deltaP `20.6988` edge `0.4674` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.7214` n `139` status `ready` deltaP `17.5831` edge `0.3739` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.0158` n `124` status `ready` deltaP `11.5647` edge `0.5706` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.2523` n `139` status `ready` deltaP `8.7494` edge `0.151` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.4689` n `151` status `ready` deltaP `6.6314` edge `0.1136` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.3636` n `151` status `ready` deltaP `6.4817` edge `0.1065` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.0748` n `124` status `ready` deltaP `4.3514` edge `0.0753` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.0389` n `124` status `ready` deltaP `1.6241` edge `0.6899` maxDD `-43.6595`
- `market_context_high->equity_24h` score `-0.1545` n `124` status `ready` deltaP `18.4084` edge `0.0171` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1756` n `139` status `ready` deltaP `5.8399` edge `0.0227` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3553` n `151` status `ready` deltaP `0.5443` edge `0.0043` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.4938` n `151` status `ready` deltaP `3.4699` edge `0.0014` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5016` n `151` status `ready` deltaP `0.2399` edge `0.006` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.54` n `151` status `ready` deltaP `1.7191` edge `0.0155` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.5832` n `139` status `ready` deltaP `0.3597` edge `0.0088` maxDD `-0.8774`
- `market_context_high->metal_1h` score `-0.7691` n `151` status `ready` deltaP `0.803` edge `0.0065` maxDD `-3.0759`
- `market_context_high->equity_1h` score `-0.8414` n `151` status `ready` deltaP `0.126` edge `0.0129` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9042` n `124` status `ready` deltaP `2.8506` edge `0.0036` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-1.0273` n `139` status `ready` deltaP `2.5553` edge `0.0361` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
