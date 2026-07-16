# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T14:37:44.219135+00:00`
- Price records: `672`
- Market context records: `6927`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->fx_1h` score `-0.1752` n `225` status `ready` deltaP `3.5017` edge `0.0027` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3886` n `225` status `ready` deltaP `3.1557` edge `0.023` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.4823` n `208` status `ready` deltaP `-5.7442` edge `0.3781` maxDD `-14.4643`
- `market_context_high->crypto_major_1h` score `-0.4883` n `225` status `ready` deltaP `4.3347` edge `0.0208` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6477` n `225` status `ready` deltaP `-0.9707` edge `-0.0081` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.706` n `225` status `ready` deltaP `0.1051` edge `-0.0001` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7564` n `225` status `ready` deltaP `-2.833` edge `-0.0013` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.7893` n `224` status `ready` deltaP `14.3075` edge `0.0098` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.5074` n `225` status `ready` deltaP `-1.9674` edge `-0.0224` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.5807` n `224` status `ready` deltaP `-3.8655` edge `-0.0279` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.5926` n `225` status `ready` deltaP `3.8011` edge `-0.0115` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.6971` n `224` status `ready` deltaP `7.9051` edge `-0.0123` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-1.9474` n `224` status `ready` deltaP `5.0631` edge `0.0149` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7303` n `224` status `ready` deltaP `1.9055` edge `-0.0044` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7618` n `224` status `ready` deltaP `0.0653` edge `-0.0218` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9549` n `224` status `ready` deltaP `-7.5131` edge `0.0404` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.0662` n `208` status `ready` deltaP `-2.7596` edge `-0.0503` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.0538` n `208` status `ready` deltaP `-4.1228` edge `-0.0067` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.6553` n `224` status `ready` deltaP `5.3027` edge `-0.0941` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.5873` n `208` status `ready` deltaP `-12.2509` edge `-0.115` maxDD `-32.0075`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
