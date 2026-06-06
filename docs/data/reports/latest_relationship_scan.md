# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T19:07:26.187566+00:00`
- Price records: `672`
- Market context records: `3103`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6921`

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

- `market_context_high->crypto_alt_24h` score `16.4456` n `83` status `ready` deltaP `13.596` edge `2.5488` maxDD `-33.816`
- `market_context_high->commodity_24h` score `15.1323` n `83` status `ready` deltaP `45.233` edge `1.0023` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.8323` n `83` status `ready` deltaP `23.2681` edge `1.1297` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.6027` n `83` status `ready` deltaP `32.3167` edge `0.9173` maxDD `-15.6019`
- `market_context_high->equity_24h` score `7.4521` n `83` status `ready` deltaP `18.453` edge `1.3691` maxDD `-36.9377`
- `market_context_high->commodity_4h` score `3.0665` n `118` status `ready` deltaP `18.4115` edge `0.1786` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.105` n `121` status `ready` deltaP `1.0962` edge `0.0262` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.2743` n `118` status `ready` deltaP `5.7488` edge `0.0616` maxDD `-7.4891`
- `market_context_high->index_1h` score `-0.4494` n `121` status `ready` deltaP `4.8387` edge `0.0164` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.6557` n `83` status `ready` deltaP `3.2128` edge `-0.0033` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.699` n `121` status `ready` deltaP `-7.4021` edge `-0.003` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7786` n `121` status `ready` deltaP `3.3355` edge `0.0909` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.2969` n `121` status `ready` deltaP `-2.5932` edge `-0.0004` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3369` n `118` status `ready` deltaP `-12.4251` edge `-0.0042` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4154` n `118` status `ready` deltaP `9.8466` edge `0.0438` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.1687` n `121` status `ready` deltaP `-0.6656` edge `0.05` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.4024` n `121` status `ready` deltaP `-7.2648` edge `-0.0124` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.6909` n `121` status `ready` deltaP `3.5099` edge `-0.0632` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.9147` n `118` status `ready` deltaP `12.3295` edge `0.2204` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.1591` n `118` status `ready` deltaP `5.1519` edge `-0.037` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
