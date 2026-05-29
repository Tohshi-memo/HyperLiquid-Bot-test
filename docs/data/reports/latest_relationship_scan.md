# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T16:37:26.685963+00:00`
- Price records: `672`
- Market context records: `2261`
- Flow alert records: `8404`
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

- `news_risk_high->crypto_alt_24h` score `22.2568` n `43` status `ready` deltaP `52.8141` edge `1.5615` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.7745` n `43` status `ready` deltaP `42.4661` edge `1.0754` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.8856` n `43` status `ready` deltaP `33.4383` edge `1.049` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `12.0111` n `43` status `ready` deltaP `23.4132` edge `0.9029` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `9.3259` n `115` status `ready` deltaP `29.6724` edge `0.6205` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `8.8894` n `43` status `ready` deltaP `33.7169` edge `0.5386` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.39` n `144` status `ready` deltaP `27.4899` edge `0.7838` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `8.0599` n `144` status `ready` deltaP `32.859` edge `0.6336` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `6.0856` n `115` status `ready` deltaP `17.1241` edge `1.0553` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.354` n `144` status `ready` deltaP `21.6802` edge `0.3626` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7554` n `43` status `ready` deltaP `32.1575` edge `0.3342` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7355` n `43` status `ready` deltaP `12.0559` edge `0.2728` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.6423` n `43` status `ready` deltaP `37.2295` edge `0.0738` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3458` n `115` status `ready` deltaP `13.8557` edge `0.2382` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.1653` n `43` status `ready` deltaP `2.7253` edge `0.3273` maxDD `-3.202`
- `market_context_high->index_4h` score `3.095` n `144` status `ready` deltaP `26.4058` edge `0.1475` maxDD `-1.9166`
- `market_context_high->equity_24h` score `2.5245` n `115` status `ready` deltaP `20.9813` edge `0.2232` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `2.3424` n `156` status `ready` deltaP `14.0603` edge `0.2202` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.335` n `144` status `ready` deltaP `19.0549` edge `0.208` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0601` n `43` status `ready` deltaP `26.3648` edge `0.0143` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
