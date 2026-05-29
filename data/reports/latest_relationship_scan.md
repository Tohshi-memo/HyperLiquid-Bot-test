# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T15:37:21.959578+00:00`
- Price records: `672`
- Market context records: `2257`
- Flow alert records: `8391`
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

- `news_risk_high->crypto_alt_24h` score `23.0059` n `43` status `ready` deltaP `53.5085` edge `1.6193` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.9201` n `43` status `ready` deltaP `43.1605` edge `1.0829` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2748` n `43` status `ready` deltaP `34.1327` edge `1.0768` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `12.6414` n `43` status `ready` deltaP `24.1077` edge `0.9508` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `9.7318` n `115` status `ready` deltaP `30.3668` edge `0.6497` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `9.2953` n `43` status `ready` deltaP `34.4113` edge `0.5678` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.2197` n `140` status `ready` deltaP `27.3258` edge `0.7707` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.9102` n `140` status `ready` deltaP `32.953` edge `0.6205` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `6.4953` n `115` status `ready` deltaP `17.8186` edge `1.1032` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.4397` n `140` status `ready` deltaP `21.4765` edge `0.3711` maxDD `-1.8773`
- `news_risk_high->index_24h` score `3.7812` n `43` status `ready` deltaP `12.4031` edge `0.2743` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7601` n `43` status `ready` deltaP `32.1575` edge `0.3348` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6531` n `43` status `ready` deltaP `37.2295` edge `0.0747` maxDD `-0.1442`
- `market_context_high->index_4h` score `3.4945` n `140` status `ready` deltaP `28.1969` edge `0.1541` maxDD `-1.4028`
- `market_context_high->index_24h` score `3.3916` n `115` status `ready` deltaP `14.2029` edge `0.2397` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.0114` n `43` status `ready` deltaP `2.0309` edge `0.3191` maxDD `-3.202`
- `market_context_high->equity_24h` score `2.9136` n `115` status `ready` deltaP `21.6757` edge `0.251` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `2.2736` n `152` status `ready` deltaP `14.2058` edge `0.2135` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.2714` n `140` status `ready` deltaP `19.1289` edge `0.2022` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0649` n `43` status `ready` deltaP `26.3648` edge `0.0147` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
