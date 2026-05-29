# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T16:06:38.968457+00:00`
- Price records: `672`
- Market context records: `2259`
- Flow alert records: `8398`
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

- `news_risk_high->crypto_alt_24h` score `22.6013` n `43` status `ready` deltaP `53.1613` edge `1.5879` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.8395` n `43` status `ready` deltaP `42.8133` edge `1.0785` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0802` n `43` status `ready` deltaP `33.7855` edge `1.0629` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `12.3053` n `43` status `ready` deltaP `23.7605` edge `0.9251` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `9.5217` n `115` status `ready` deltaP `30.0196` edge `0.6345` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `9.0852` n `43` status `ready` deltaP `34.0641` edge `0.5526` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.2915` n `142` status `ready` deltaP `27.4132` edge `0.7761` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.9631` n `142` status `ready` deltaP `32.9096` edge `0.6252` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `6.2768` n `115` status `ready` deltaP `17.4714` edge `1.0775` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.3835` n `142` status `ready` deltaP `21.5841` edge `0.3657` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7538` n `43` status `ready` deltaP `32.1575` edge `0.334` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7427` n `43` status `ready` deltaP `12.0559` edge `0.2734` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.6471` n `43` status `ready` deltaP `37.2295` edge `0.0742` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.353` n `115` status `ready` deltaP `13.8557` edge `0.2388` maxDD `-1.4737`
- `market_context_high->index_4h` score `3.3331` n `142` status `ready` deltaP `27.2845` edge `0.1506` maxDD `-1.7122`
- `news_risk_high->commodity_24h` score `3.0895` n `43` status `ready` deltaP `2.3781` edge `0.3233` maxDD `-3.202`
- `market_context_high->equity_24h` score `2.7191` n `115` status `ready` deltaP `21.3285` edge `0.2371` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `2.4092` n `154` status `ready` deltaP `14.3849` edge `0.2236` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.2975` n `142` status `ready` deltaP `19.0957` edge `0.2046` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0625` n `43` status `ready` deltaP `26.3648` edge `0.0145` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
