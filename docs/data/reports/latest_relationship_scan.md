# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T06:52:21.711363+00:00`
- Price records: `672`
- Market context records: `2221`
- Flow alert records: `8285`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `26.4524` n `31` status `ready` deltaP `57.7845` edge `1.878` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.5822` n `31` status `ready` deltaP `48.3367` edge `0.9369` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `13.0007` n `132` status `ready` deltaP `37.7587` edge `0.9253` maxDD `-5.1574`
- `news_risk_high->equity_24h` score `11.922` n `31` status `ready` deltaP `39.3089` edge `0.7629` maxDD `-2.1831`
- `market_context_high->crypto_major_4h` score `11.7607` n `132` status `ready` deltaP `42.1286` edge `0.7522` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `10.1246` n `31` status `ready` deltaP `38.6873` edge `0.6084` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.2941` n `31` status `ready` deltaP `18.4812` edge `0.87` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.5069` n `132` status `ready` deltaP `21.5263` edge `0.3833` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.9229` n `43` status `ready` deltaP `32.9197` edge `0.3506` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3798` n `132` status `ready` deltaP `23.4156` edge `0.235` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2233` n `134` status `ready` deltaP `17.6133` edge `0.1989` maxDD `-1.817`
- `market_context_high->index_4h` score `3.2222` n `132` status `ready` deltaP `26.6214` edge `0.1594` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.0501` n `134` status `ready` deltaP `16.7173` edge `0.2291` maxDD `-4.9097`
- `news_risk_high->fx_24h` score `2.75` n `31` status `ready` deltaP `29.301` edge `0.0523` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.206` n `43` status `ready` deltaP `27.8892` edge `0.0163` maxDD `-0.1382`
- `market_context_high->unknown_24h` score `2.0733` n `132` status `ready` deltaP `24.6844` edge `0.4897` maxDD `-32.8525`
- `news_risk_high->commodity_24h` score `2.0387` n `31` status `ready` deltaP `-4.5923` edge `0.2822` maxDD `-3.202`
- `market_context_high->index_24h` score `1.8728` n `132` status `ready` deltaP `9.6906` edge `0.2143` maxDD `-4.1604`
- `news_risk_high->unknown_1h` score `1.4539` n `43` status `ready` deltaP `21.3445` edge `0.0258` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3433` n `43` status `ready` deltaP `14.62` edge `0.0868` maxDD `-2.7857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
