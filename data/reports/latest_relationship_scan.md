# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T20:07:20.452173+00:00`
- Price records: `672`
- Market context records: `2491`
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

- `market_context_high->unknown_24h` score `5.4535` n `124` status `ready` deltaP `19.8869` edge `0.3547` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.0094` n `140` status `ready` deltaP `20.7622` edge `0.4636` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.6116` n `140` status `ready` deltaP `17.0949` edge `0.368` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.0404` n `124` status `ready` deltaP `11.7383` edge `0.5726` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.2464` n `140` status `ready` deltaP `8.9155` edge `0.1494` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.4957` n `152` status `ready` deltaP `6.7562` edge `0.115` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.3747` n `152` status `ready` deltaP `6.6065` edge `0.1066` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.0924` n `124` status `ready` deltaP `1.7977` edge `0.6956` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.082` n `124` status `ready` deltaP `4.3514` edge `0.0759` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1533` n `124` status `ready` deltaP `18.4084` edge `0.0172` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1668` n `140` status `ready` deltaP `5.9494` edge `0.0231` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3463` n `152` status `ready` deltaP `0.717` edge `0.0043` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.5141` n `152` status `ready` deltaP `3.258` edge `0.0002` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5201` n `152` status `ready` deltaP `0.0237` edge `0.0059` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.5365` n `152` status `ready` deltaP `1.8831` edge `0.0147` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.5648` n `140` status `ready` deltaP `0.7143` edge `0.0088` maxDD `-0.8774`
- `market_context_high->metal_1h` score `-0.7854` n `152` status `ready` deltaP `0.6303` edge `0.0063` maxDD `-3.0759`
- `market_context_high->equity_1h` score `-0.8239` n `152` status `ready` deltaP `0.3743` edge `0.0127` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9042` n `124` status `ready` deltaP `2.8506` edge `0.0036` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-1.0649` n `140` status `ready` deltaP `2.2213` edge `0.0352` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
