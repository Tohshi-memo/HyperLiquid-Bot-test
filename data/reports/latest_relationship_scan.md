# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T20:07:36.366041+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `0.9207` n `144` status `ready` deltaP `20.234` edge `0.0226` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9175` n `178` status `ready` deltaP `12.363` edge `0.0655` maxDD `-2.7169`
- `market_context_high->equity_24h` score `0.7804` n `144` status `ready` deltaP `2.7224` edge `0.3936` maxDD `-21.0709`
- `market_context_high->commodity_1h` score `0.653` n `187` status `ready` deltaP `9.0173` edge `0.0286` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.1188` n `187` status `ready` deltaP `4.4606` edge `0.0002` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.152` n `178` status `ready` deltaP `6.0615` edge `0.0069` maxDD `-0.4647`
- `market_context_high->index_24h` score `-0.3791` n `144` status `ready` deltaP `2.5431` edge `0.1046` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5891` n `187` status `ready` deltaP `-3.7529` edge `-0.0028` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.6904` n `144` status `ready` deltaP `2.3854` edge `0.059` maxDD `-2.9283`
- `market_context_high->index_4h` score `-0.8053` n `178` status `ready` deltaP `-2.4133` edge `-0.0089` maxDD `-1.26`
- `market_context_high->equity_1h` score `-0.9944` n `187` status `ready` deltaP `-3.2597` edge `-0.0068` maxDD `-5.5833`
- `market_context_high->metal_1h` score `-1.1848` n `187` status `ready` deltaP `-4.0091` edge `-0.0084` maxDD `-2.0884`
- `market_context_high->crypto_alt_1h` score `-1.7557` n `187` status `ready` deltaP `-9.592` edge `-0.0414` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-1.9686` n `178` status `ready` deltaP `-6.2551` edge `-0.0343` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2733` n `178` status `ready` deltaP `-11.4501` edge `-0.0906` maxDD `-11.2181`
- `market_context_high->crypto_major_24h` score `-3.6061` n `144` status `ready` deltaP `-0.5825` edge `-0.0472` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-3.6458` n `187` status `ready` deltaP `-9.3151` edge `-0.0513` maxDD `-11.9002`
- `market_context_high->crypto_alt_24h` score `-4.8813` n `144` status `ready` deltaP `-12.3628` edge `-0.1477` maxDD `-7.1322`
- `market_context_high->crypto_alt_4h` score `-6.0701` n `178` status `ready` deltaP `-12.0119` edge `-0.1322` maxDD `-16.8181`
- `market_context_high->commodity_24h` score `-8.4059` n `144` status `ready` deltaP `-4.7588` edge `-0.1744` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
