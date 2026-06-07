# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T02:22:21.666495+00:00`
- Price records: `672`
- Market context records: `3135`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7126`

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

- `market_context_high->commodity_24h` score `14.3258` n `106` status `ready` deltaP `47.5858` edge `0.9194` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.8149` n `106` status `ready` deltaP `21.1314` edge `0.8925` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.7378` n `106` status `ready` deltaP `10.0727` edge `2.3071` maxDD `-71.142`
- `market_context_high->index_24h` score `6.4493` n `106` status `ready` deltaP `30.703` edge `0.8776` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.313` n `106` status `ready` deltaP `10.8556` edge `1.3222` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.0479` n `138` status `ready` deltaP `20.2191` edge `0.165` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1211` n `146` status `ready` deltaP `3.8328` edge `0.0268` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.4468` n `146` status `ready` deltaP `5.6066` edge `0.1183` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4657` n `106` status `ready` deltaP `5.3328` edge `-0.0016` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.4883` n `146` status `ready` deltaP `3.8512` edge `0.018` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8316` n `146` status `ready` deltaP `3.1888` edge `0.0207` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9788` n `146` status `ready` deltaP `3.076` edge `0.0803` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1586` n `146` status `ready` deltaP `-11.2173` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.2816` n `138` status `ready` deltaP `10.7547` edge `0.0549` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.5178` n `138` status `ready` deltaP `-14.6474` edge `-0.0088` maxDD `-1.3846`
- `market_context_high->metal_1h` score `-2.0312` n `146` status `ready` deltaP `-4.005` edge `-0.0032` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.1029` n `138` status `ready` deltaP `4.4672` edge `0.0172` maxDD `-14.7778`
- `market_context_high->crypto_alt_4h` score `-2.4177` n `138` status `ready` deltaP `18.1823` edge `0.3733` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0698` n `146` status `ready` deltaP `2.2086` edge `-0.0679` maxDD `-14.2111`
- `market_context_high->equity_4h` score `-3.1653` n `138` status `ready` deltaP `11.7842` edge `0.0462` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
