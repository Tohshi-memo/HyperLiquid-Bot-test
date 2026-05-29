# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T14:52:21.391775+00:00`
- Price records: `672`
- Market context records: `2254`
- Flow alert records: `8382`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9257`

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

- `news_risk_high->crypto_alt_24h` score `23.584` n `43` status `ready` deltaP `54.0294` edge `1.664` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.0674` n `43` status `ready` deltaP `43.6813` edge `1.0917` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.5432` n `43` status `ready` deltaP `34.6536` edge `1.0957` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `13.1355` n `43` status `ready` deltaP `24.6285` edge `0.9885` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `9.9811` n `115` status `ready` deltaP `30.8876` edge `0.667` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `9.5446` n `43` status `ready` deltaP `34.9321` edge `0.5851` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.4371` n `137` status `ready` deltaP `27.7506` edge `0.7793` maxDD `-15.2301`
- `market_context_high->crypto_major_4h` score `7.9503` n `137` status `ready` deltaP `33.0036` edge `0.6235` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `6.8164` n `115` status `ready` deltaP `18.3394` edge `1.1409` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.4954` n `137` status `ready` deltaP `20.9876` edge `0.379` maxDD `-1.8773`
- `market_context_high->index_4h` score `3.8234` n `137` status `ready` deltaP `29.6322` edge `0.1615` maxDD `-0.5679`
- `news_risk_high->index_24h` score `3.821` n `43` status `ready` deltaP `12.7504` edge `0.2753` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7601` n `43` status `ready` deltaP `32.1575` edge `0.3348` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6627` n `43` status `ready` deltaP `37.2295` edge `0.0755` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.4314` n `115` status `ready` deltaP `14.5502` edge `0.2407` maxDD `-1.4737`
- `market_context_high->equity_24h` score `3.1821` n `115` status `ready` deltaP `22.1966` edge `0.2699` maxDD `-6.8828`
- `news_risk_high->commodity_24h` score `2.9164` n `43` status `ready` deltaP `1.6836` edge `0.3135` maxDD `-3.202`
- `market_context_high->equity_4h` score `2.2848` n `137` status `ready` deltaP `19.0115` edge `0.2041` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0685` n `43` status `ready` deltaP `26.3648` edge `0.015` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.9119` n `149` status `ready` deltaP `13.464` edge `0.1883` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
