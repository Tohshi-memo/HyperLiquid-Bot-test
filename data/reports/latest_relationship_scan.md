# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T14:22:25.283309+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14802`

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

- `market_context_high->unknown_1h` score `0.7956` n `149` status `ready` deltaP `6.5577` edge `0.0453` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5237` n `144` status `ready` deltaP `18.4282` edge `-0.0353` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.081` n `144` status `ready` deltaP `7.6558` edge `0.0096` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0523` n `149` status `ready` deltaP `6.2985` edge `0.0044` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0795` n `149` status `ready` deltaP `3.1648` edge `0.0046` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2265` n `144` status `ready` deltaP `7.4187` edge `-0.0169` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3393` n `149` status `ready` deltaP `4.7241` edge `0.032` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3398` n `149` status `ready` deltaP `0.4803` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.4768` n `144` status `ready` deltaP `4.624` edge `0.0116` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8415` n `144` status `ready` deltaP `-3.4722` edge `0.0003` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1243` n `149` status `ready` deltaP `-8.3219` edge `-0.0029` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.6034` n `130` status `ready` deltaP `2.3504` edge `0.0117` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.7249` n `144` status `ready` deltaP `-1.4228` edge `0.069` maxDD `-16.1188`
- `market_context_high->crypto_alt_4h` score `-2.2159` n `144` status `ready` deltaP `4.2683` edge `-0.0663` maxDD `-7.0785`
- `market_context_high->commodity_24h` score `-2.2248` n `130` status `ready` deltaP `-6.1164` edge `0.0387` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.498` n `149` status `ready` deltaP `-2.5338` edge `-0.0418` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.586` n `149` status `ready` deltaP `-5.358` edge `-0.1154` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.5481` n `130` status `ready` deltaP `-9.3803` edge `-0.0405` maxDD `-21.0713`
- `market_context_high->crypto_major_4h` score `-5.476` n `144` status `ready` deltaP `-0.4404` edge `-0.3204` maxDD `-5.6395`
- `market_context_high->metal_24h` score `-5.5513` n `130` status `ready` deltaP `-25.7719` edge `-0.2091` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
