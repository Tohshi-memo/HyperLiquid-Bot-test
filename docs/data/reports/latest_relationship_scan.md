# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T15:22:23.988705+00:00`
- Price records: `672`
- Market context records: `2362`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `news_risk_high->crypto_alt_24h` score `21.6085` n `43` status `ready` deltaP `50.0363` edge `1.526` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.5244` n `43` status `ready` deltaP `46.4591` edge `1.1946` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.8807` n `43` status `ready` deltaP `29.7925` edge `1.0729` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.459` n `43` status `ready` deltaP `19.7674` edge `0.8812` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `8.8545` n `140` status `ready` deltaP `20.0` edge `0.9938` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.8453` n `43` status `ready` deltaP `27.6405` edge `0.4921` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.3401` n `140` status `ready` deltaP `24.4346` edge `0.4066` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `6.003` n `152` status `ready` deltaP `24.7273` edge `0.5164` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `5.4993` n `152` status `ready` deltaP `20.6514` edge `0.5885` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `5.2338` n `152` status `ready` deltaP `21.6624` edge `0.3527` maxDD `-1.8773`
- `news_risk_high->index_24h` score `5.1184` n `43` status `ready` deltaP `13.0976` edge `0.3811` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.8078` n `43` status `ready` deltaP `32.3099` edge `0.3399` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.403` n `43` status `ready` deltaP `36.1879` edge `0.0608` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9479` n `43` status `ready` deltaP `24.9929` edge `0.0141` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.8833` n `140` status `ready` deltaP `12.5992` edge `0.1247` maxDD `-1.4737`
- `market_context_high->crypto_major_1h` score `1.8426` n `157` status `ready` deltaP `15.0092` edge `0.1729` maxDD `-4.2199`
- `market_context_high->index_4h` score `1.7907` n `152` status `ready` deltaP `19.3357` edge `0.1029` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.6618` n `157` status `ready` deltaP `11.7482` edge `0.1789` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.4504` n `140` status `ready` deltaP `19.9752` edge `0.1404` maxDD `-6.8828`
- `news_risk_high->unknown_4h` score `0.8786` n `43` status `ready` deltaP `13.4005` edge `0.0562` maxDD `-2.7857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
