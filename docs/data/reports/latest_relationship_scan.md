# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T15:37:32.722458+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6784`

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

- `market_context_high->unknown_24h` score `1569.1141` n `136` status `ready` deltaP `-0.2553` edge `130.8074` maxDD `-1.3618`
- `market_context_high->unknown_4h` score `62.4479` n `136` status `ready` deltaP `7.048` edge `5.1703` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.93` n `136` status `ready` deltaP `24.8162` edge `0.0137` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `0.2324` n `136` status `ready` deltaP `12.8318` edge `0.0557` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.1973` n `136` status `ready` deltaP `9.8978` edge `0.0089` maxDD `-0.6342`
- `market_context_high->metal_4h` score `0.0179` n `136` status `ready` deltaP `12.8407` edge `0.0117` maxDD `-2.2674`
- `market_context_high->fx_1h` score `-0.0545` n `136` status `ready` deltaP `4.3986` edge `-0.0005` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2488` n `136` status `ready` deltaP `2.2191` edge `0.0159` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.3221` n `136` status `ready` deltaP `2.8426` edge `-0.0004` maxDD `-0.4545`
- `market_context_high->equity_1h` score `-0.4145` n `136` status `ready` deltaP `1.0083` edge `0.0305` maxDD `-2.5621`
- `market_context_high->index_1h` score `-0.7413` n `136` status `ready` deltaP `-4.1784` edge `-0.003` maxDD `-1.1344`
- `market_context_high->crypto_major_1h` score `-0.7801` n `136` status `ready` deltaP `4.3854` edge `0.0227` maxDD `-6.0219`
- `market_context_high->fx_24h` score `-0.8523` n `136` status `ready` deltaP `7.0874` edge `0.0148` maxDD `-0.9792`
- `market_context_high->crypto_alt_1h` score `-1.3825` n `136` status `ready` deltaP `1.2372` edge `0.0133` maxDD `-9.2367`
- `market_context_high->equity_4h` score `-1.7579` n `136` status `ready` deltaP `-2.6453` edge `-0.0284` maxDD `-7.6803`
- `market_context_high->metal_24h` score `-1.806` n `136` status `ready` deltaP `3.2782` edge `0.0113` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4907` n `136` status `ready` deltaP `-7.1915` edge `-0.0247` maxDD `-3.7932`
- `market_context_high->crypto_major_4h` score `-2.7275` n `136` status `ready` deltaP `4.2234` edge `-0.0374` maxDD `-19.9013`
- `market_context_high->equity_24h` score `-3.7202` n `136` status `ready` deltaP `7.1691` edge `-0.0821` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.7269` n `136` status `ready` deltaP `-0.8987` edge `-0.041` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
