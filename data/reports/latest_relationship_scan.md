# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T17:52:30.177161+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->metal_24h` score `2.865` n `98` status `ready` deltaP `12.3662` edge `0.2139` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.8507` n `98` status `ready` deltaP `24.3858` edge `0.0528` maxDD `-3.1715`
- `market_context_high->commodity_4h` score `0.7264` n `109` status `ready` deltaP `12.5377` edge `0.081` maxDD `-2.7169`
- `market_context_high->equity_24h` score `0.6793` n `98` status `ready` deltaP `-5.1523` edge `0.4343` maxDD `-21.4677`
- `market_context_high->index_24h` score `0.4109` n `98` status `ready` deltaP `6.5625` edge `0.1418` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.3664` n `120` status `ready` deltaP `9.3812` edge `0.0251` maxDD `-1.2534`
- `market_context_high->fx_4h` score `0.119` n `109` status `ready` deltaP `9.3113` edge `0.0065` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.2916` n `120` status `ready` deltaP `4.7655` edge `-0.0053` maxDD `-1.0616`
- `market_context_high->index_4h` score `-0.6968` n `109` status `ready` deltaP `-2.4349` edge `-0.0105` maxDD `-1.3409`
- `market_context_high->index_1h` score `-0.736` n `120` status `ready` deltaP `-1.4571` edge `-0.0099` maxDD `-1.3375`
- `market_context_high->crypto_alt_1h` score `-0.888` n `120` status `ready` deltaP `-5.494` edge `-0.0143` maxDD `-2.3669`
- `market_context_high->metal_4h` score `-0.9961` n `109` status `ready` deltaP `2.1748` edge `0.0022` maxDD `-2.6429`
- `market_context_high->metal_1h` score `-1.0658` n `120` status `ready` deltaP `-4.6407` edge `-0.0083` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-1.0669` n `120` status `ready` deltaP `4.0968` edge `-0.0253` maxDD `-9.1031`
- `market_context_high->crypto_alt_4h` score `-1.3169` n `109` status `ready` deltaP `0.6223` edge `-0.034` maxDD `-5.7857`
- `market_context_high->equity_4h` score `-2.0954` n `109` status `ready` deltaP `4.7606` edge `-0.1045` maxDD `-12.6698`
- `market_context_high->crypto_major_1h` score `-3.0377` n `120` status `ready` deltaP `-7.0509` edge `-0.0606` maxDD `-8.3095`
- `market_context_high->crypto_major_24h` score `-3.4524` n `98` status `ready` deltaP `-0.4088` edge `-0.1863` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.2381` n `98` status `ready` deltaP `-14.5005` edge `-0.1122` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-6.7181` n `109` status `ready` deltaP `-7.6485` edge `-0.19` maxDD `-19.1749`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
