# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T22:30:44.037242+00:00`
- Price records: `672`
- Market context records: `2502`
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

- `market_context_high->unknown_24h` score `5.4607` n `124` status `ready` deltaP `19.8869` edge `0.3553` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.3548` n `150` status `ready` deltaP `21.3902` edge `0.4882` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.6949` n `150` status `ready` deltaP `17.6565` edge `0.3712` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1547` n `124` status `ready` deltaP `12.78` edge `0.5803` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.6792` n `150` status `ready` deltaP `10.8008` edge `0.1729` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.5367` n `157` status `ready` deltaP `6.7289` edge `0.1186` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.4886` n `124` status `ready` deltaP `3.0129` edge `0.7383` maxDD `-43.6595`
- `market_context_high->crypto_major_1h` score `0.4061` n `157` status `ready` deltaP `7.0283` edge `0.1064` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.1432` n `124` status `ready` deltaP `4.3514` edge `0.081` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1317` n `124` status `ready` deltaP `18.4084` edge `0.019` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1363` n `150` status `ready` deltaP `6.8537` edge `0.0271` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.2836` n `157` status `ready` deltaP `1.8918` edge `0.0045` maxDD `-0.278`
- `market_context_high->index_1h` score `-0.5404` n `157` status `ready` deltaP `-0.2746` edge `0.0062` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.577` n `157` status `ready` deltaP `1.8565` edge `0.0115` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.5962` n `157` status `ready` deltaP `-0.5826` edge `0.0034` maxDD `-3.0759`
- `market_context_high->commodity_1h` score `-0.6513` n `157` status `ready` deltaP `3.5795` edge `0.0097` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.6565` n `150` status `ready` deltaP `1.5265` edge `0.0444` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.6731` n `150` status `ready` deltaP `-1.2947` edge `0.0083` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.9026` n `124` status `ready` deltaP `2.8506` edge `0.0038` maxDD `-2.7484`
- `market_context_high->equity_1h` score `-0.9406` n `157` status `ready` deltaP `-0.8295` edge `0.011` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
