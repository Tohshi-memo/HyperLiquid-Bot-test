# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T13:37:21.609486+00:00`
- Price records: `672`
- Market context records: `2249`
- Flow alert records: `8367`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9227`

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

- `news_risk_high->crypto_alt_24h` score `24.3374` n `43` status `ready` deltaP `54.8974` edge `1.721` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.3624` n `43` status `ready` deltaP `44.5494` edge `1.1105` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `16.0207` n `43` status `ready` deltaP `35.5216` edge `1.1297` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `13.7653` n `43` status `ready` deltaP `25.4966` edge `1.0352` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `10.5638` n `132` status `ready` deltaP `30.4878` edge `0.8427` maxDD `-9.2505`
- `market_context_high->unknown_24h` score `10.4178` n `115` status `ready` deltaP `31.7557` edge `0.6976` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `9.9813` n `43` status `ready` deltaP `35.8002` edge `0.6157` maxDD `-1.4744`
- `market_context_high->crypto_major_4h` score `9.6823` n `132` status `ready` deltaP `36.0726` edge `0.6726` maxDD `-5.8313`
- `market_context_high->crypto_major_24h` score `7.2258` n `115` status `ready` deltaP `19.2075` edge `1.1876` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.2175` n `132` status `ready` deltaP `19.854` edge `0.3634` maxDD `-1.8773`
- `market_context_high->index_4h` score `4.0552` n `132` status `ready` deltaP `31.0052` edge `0.1686` maxDD `-0.3228`
- `news_risk_high->index_24h` score `3.9961` n `43` status `ready` deltaP `13.6184` edge `0.2841` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.8605` n `43` status `ready` deltaP `32.9197` edge `0.3426` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6675` n `43` status `ready` deltaP `37.2295` edge `0.0759` maxDD `-0.1442`
- `market_context_high->equity_24h` score `3.6595` n `115` status `ready` deltaP `23.0646` edge `0.3039` maxDD `-6.8828`
- `market_context_high->index_24h` score `3.6064` n `115` status `ready` deltaP `15.4182` edge `0.2495` maxDD `-1.4737`
- `market_context_high->equity_4h` score `3.0126` n `132` status `ready` deltaP `20.838` edge `0.2253` maxDD `-4.0537`
- `news_risk_high->commodity_24h` score `2.9826` n `43` status `ready` deltaP `2.0309` edge `0.3167` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.0952` n `43` status `ready` deltaP `26.6697` edge `0.0152` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.9923` n `144` status `ready` deltaP `13.2485` edge `0.1893` maxDD `-5.9276`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
