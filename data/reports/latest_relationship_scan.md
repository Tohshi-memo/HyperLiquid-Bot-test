# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T16:52:13.472254+00:00`
- Price records: `672`
- Market context records: `1031`
- Flow alert records: `4877`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8635`

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

- `market_context_high->crypto_major_24h` score `14.216` n `183` status `ready` deltaP `32.8982` edge `1.0242` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5029` n `183` status `ready` deltaP `11.3019` edge `0.4233` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.3515` n `183` status `ready` deltaP `11.5505` edge `0.2853` maxDD `-3.641`
- `market_context_high->index_24h` score `2.4832` n `183` status `ready` deltaP `10.8461` edge `0.2199` maxDD `-2.155`
- `market_context_high->metal_24h` score `0.7961` n `183` status `ready` deltaP `-5.9824` edge `0.406` maxDD `-16.9823`
- `market_context_high->fx_1h` score `-0.0765` n `183` status `ready` deltaP `5.2739` edge `0.0006` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4688` n `183` status `ready` deltaP `4.1294` edge `0.0114` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6435` n `183` status `ready` deltaP `0.0049` edge `0.022` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6855` n `183` status `ready` deltaP `1.0291` edge `0.0168` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.9972` n `183` status `ready` deltaP `2.0909` edge `0.0026` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.1422` n `183` status `ready` deltaP `5.7753` edge `-0.0097` maxDD `-7.9187`
- `market_context_high->metal_1h` score `-1.3794` n `183` status `ready` deltaP `1.9355` edge `-0.0364` maxDD `-7.6016`
- `market_context_high->crypto_alt_1h` score `-1.4227` n `183` status `ready` deltaP `-0.0556` edge `-0.0096` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.4229` n `183` status `ready` deltaP `-0.5307` edge `0.0326` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.6291` n `183` status `ready` deltaP `1.4769` edge `0.0696` maxDD `-10.5498`
- `market_context_high->crypto_alt_4h` score `-3.0273` n `183` status `ready` deltaP `0.5456` edge `0.0219` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.1605` n `183` status `ready` deltaP `3.3356` edge `-0.0198` maxDD `-19.2774`
- `market_context_high->crypto_major_4h` score `-3.2497` n `183` status `ready` deltaP `7.1238` edge `0.0523` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.5852` n `183` status `ready` deltaP `-5.0413` edge `0.0516` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9812` n `183` status `ready` deltaP `-1.5277` edge `-0.1569` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
