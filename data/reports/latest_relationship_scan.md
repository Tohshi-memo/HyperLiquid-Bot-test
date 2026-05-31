# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T16:52:17.595811+00:00`
- Price records: `672`
- Market context records: `2476`
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

- `market_context_high->unknown_24h` score `5.3095` n `120` status `ready` deltaP `20.2778` edge `0.3401` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.1087` n `136` status `ready` deltaP `20.8931` edge `0.471` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8889` n `136` status `ready` deltaP `18.1761` edge `0.3839` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.0685` n `120` status `ready` deltaP `11.632` edge `0.5769` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.6229` n `136` status `ready` deltaP `10.3031` edge `0.1686` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.6031` n `139` status `ready` deltaP `8.0365` edge `0.1161` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.4469` n `139` status `ready` deltaP `6.3273` edge `0.1138` maxDD `-6.1656`
- `market_context_high->index_24h` score `-0.0223` n `120` status `ready` deltaP `3.4375` edge `0.0733` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.18` n `120` status `ready` deltaP `1.1805` edge `0.6648` maxDD `-43.6595`
- `market_context_high->index_4h` score `-0.1874` n `136` status `ready` deltaP `5.7927` edge `0.0215` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.2535` n `120` status `ready` deltaP `17.9514` edge `0.0119` maxDD `-6.8828`
- `market_context_high->fx_1h` score `-0.3711` n `139` status `ready` deltaP `0.21` edge `0.0045` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.4532` n `139` status `ready` deltaP `1.6489` edge `0.0232` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.4536` n `139` status `ready` deltaP `-1.553` edge `0.0016` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.5122` n `139` status `ready` deltaP `0.5676` edge `0.0065` maxDD `-3.0759`
- `market_context_high->commodity_1h` score `-0.5985` n `139` status `ready` deltaP `1.8901` edge `-0.0015` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.654` n `136` status `ready` deltaP `-0.9415` edge `0.0084` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8647` n `139` status `ready` deltaP `-0.4049` edge `0.0145` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8715` n `120` status `ready` deltaP `3.4028` edge `0.0041` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9526` n `136` status `ready` deltaP `3.1295` edge `0.0385` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
