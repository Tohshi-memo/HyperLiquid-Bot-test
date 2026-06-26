# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T09:56:43.580498+00:00`
- Price records: `672`
- Market context records: `4816`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `11.7119` n `117` status `ready` deltaP `11.7074` edge `0.9397` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.851` n `117` status `ready` deltaP `18.1038` edge `0.6546` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.1733` n `110` status `ready` deltaP `12.4022` edge `0.1896` maxDD `-4.6272`
- `market_context_high->equity_4h` score `0.2929` n `117` status `ready` deltaP `9.5842` edge `0.1118` maxDD `-6.3852`
- `market_context_high->commodity_1h` score `0.1659` n `117` status `ready` deltaP `6.4781` edge `0.0294` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.1316` n `117` status `ready` deltaP `12.6277` edge `0.0499` maxDD `-4.377`
- `market_context_high->index_4h` score `-0.2537` n `117` status `ready` deltaP `7.5373` edge `0.0138` maxDD `-4.7259`
- `market_context_high->fx_4h` score `-0.3061` n `117` status `ready` deltaP `5.2182` edge `0.0036` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6061` n `117` status `ready` deltaP `2.5859` edge `0.009` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-1.0251` n `117` status `ready` deltaP `-2.5616` edge `-0.0034` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3386` n `117` status `ready` deltaP `-0.7702` edge `-0.006` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1301` n `110` status `ready` deltaP `20.0694` edge `0.104` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3451` n `117` status `ready` deltaP `-1.7696` edge `-0.0713` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-2.7612` n `110` status `ready` deltaP `-12.6957` edge `-0.0192` maxDD `-3.1009`
- `market_context_high->crypto_major_1h` score `-3.0071` n `117` status `ready` deltaP `0.1957` edge `-0.0778` maxDD `-22.0555`
- `market_context_high->crypto_alt_1h` score `-3.021` n `117` status `ready` deltaP `1.9244` edge `-0.0486` maxDD `-14.945`
- `market_context_high->index_24h` score `-4.3211` n `110` status `ready` deltaP `-6.6067` edge `-0.1191` maxDD `-23.2678`
- `market_context_high->crypto_alt_4h` score `-4.4107` n `117` status `ready` deltaP `6.4702` edge `-0.0178` maxDD `-41.9318`
- `market_context_high->crypto_major_4h` score `-8.2317` n `117` status `ready` deltaP `3.5687` edge `-0.1788` maxDD `-66.6939`
- `market_context_high->metal_4h` score `-8.6002` n `117` status `ready` deltaP `4.8428` edge `-0.3132` maxDD `-61.0675`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
