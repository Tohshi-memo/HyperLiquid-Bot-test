# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T08:07:29.803466+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `11.7671` n `92` status `ready` deltaP `4.4686` edge `0.9551` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.0848` n `109` status `ready` deltaP `-1.1929` edge `0.4479` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.179` n `109` status `ready` deltaP `13.7517` edge `0.0912` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8875` n `92` status `ready` deltaP `2.7626` edge `0.2122` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5387` n `92` status `ready` deltaP `20.8862` edge `0.0504` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4359` n `109` status `ready` deltaP `7.9094` edge `0.0252` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0255` n `109` status `ready` deltaP `5.3837` edge `-0.003` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1984` n `109` status `ready` deltaP `8.0947` edge `0.0066` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5409` n `109` status `ready` deltaP `-1.8596` edge `-0.0075` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7525` n `109` status `ready` deltaP `-3.5063` edge `-0.0197` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7626` n `109` status `ready` deltaP `3.0894` edge `0.0051` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.234` n `92` status `ready` deltaP `-2.9287` edge `0.0808` maxDD `-7.8922`
- `market_context_high->crypto_alt_24h` score `-1.3275` n `92` status `ready` deltaP `0.2868` edge `-0.0278` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5277` n `109` status `ready` deltaP `-5.2876` edge `-0.021` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8354` n `109` status `ready` deltaP `1.1194` edge `-0.0892` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0862` n `109` status `ready` deltaP `-12.363` edge `-0.0596` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1609` n `109` status `ready` deltaP `1.2321` edge `-0.0493` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-2.2156` n `109` status `ready` deltaP `1.1344` edge `-0.1475` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3247` n `109` status `ready` deltaP `-11.5984` edge `-0.0624` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3923` n `92` status `ready` deltaP `7.4124` edge `-0.0368` maxDD `-51.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
