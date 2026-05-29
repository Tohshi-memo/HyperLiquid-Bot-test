# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T20:22:21.145826+00:00`
- Price records: `672`
- Market context records: `2277`
- Flow alert records: `8450`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9287`

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

- `news_risk_high->crypto_alt_24h` score `20.7034` n `43` status `ready` deltaP `50.5571` edge `1.4471` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5715` n `43` status `ready` deltaP `40.9036` edge `1.0689` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.8877` n `43` status `ready` deltaP `30.8341` edge `0.9832` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.5979` n `43` status `ready` deltaP `20.8091` edge `0.8025` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `8.0895` n `158` status `ready` deltaP `25.8336` edge `0.7698` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `8.0808` n `115` status `ready` deltaP `27.0682` edge `0.5341` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `7.8766` n `158` status `ready` deltaP `30.4029` edge `0.6347` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.6443` n `43` status `ready` deltaP `31.1127` edge `0.4522` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.586` n `158` status `ready` deltaP `21.9995` edge `0.3798` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.167` n `115` status `ready` deltaP `14.52` edge `0.9549` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.7948` n `43` status `ready` deltaP `32.6148` edge `0.3362` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7194` n `43` status `ready` deltaP `12.2295` edge `0.2703` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.5907` n `43` status `ready` deltaP `37.2295` edge `0.0695` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `3.4461` n `43` status `ready` deltaP `3.9406` edge `0.3426` maxDD `-3.202`
- `market_context_high->index_24h` score `3.3297` n `115` status `ready` deltaP `14.0293` edge `0.2357` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.5288` n `158` status `ready` deltaP `24.0468` edge `0.133` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `2.3137` n `159` status `ready` deltaP `13.6717` edge `0.2204` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.2516` n `158` status `ready` deltaP `18.5821` edge `0.2042` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0856` n `43` status `ready` deltaP `26.6697` edge `0.0144` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.9863` n `159` status `ready` deltaP `13.8214` edge `0.1928` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
