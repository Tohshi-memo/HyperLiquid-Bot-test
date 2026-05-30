# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T14:22:19.201351+00:00`
- Price records: `672`
- Market context records: `2358`
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

- `news_risk_high->crypto_alt_24h` score `21.4813` n `43` status `ready` deltaP `50.0363` edge `1.5154` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.3471` n `43` status `ready` deltaP `45.9383` edge `1.1833` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7967` n `43` status `ready` deltaP `29.7925` edge `1.0659` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.3054` n `43` status `ready` deltaP `19.7674` edge `0.8684` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.3321` n `140` status `ready` deltaP `20.0` edge `1.0336` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.7637` n `43` status `ready` deltaP `27.6405` edge `0.4853` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.5945` n `140` status `ready` deltaP `24.4346` edge `0.4278` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `6.2877` n `155` status `ready` deltaP `25.122` edge `0.5375` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `5.9662` n `155` status `ready` deltaP `21.2372` edge `0.6235` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `5.4634` n `155` status `ready` deltaP `22.2227` edge `0.3681` maxDD `-1.8773`
- `news_risk_high->index_24h` score `5.0464` n `43` status `ready` deltaP `13.0976` edge `0.3751` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.8839` n `43` status `ready` deltaP `32.9197` edge `0.3456` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.403` n `43` status `ready` deltaP `36.1879` edge `0.0608` maxDD `-0.1442`
- `market_context_high->index_24h` score `2.1053` n `140` status `ready` deltaP `12.5992` edge `0.1432` maxDD `-1.4737`
- `news_risk_high->fx_4h` score `1.9491` n `43` status `ready` deltaP `24.9929` edge `0.0142` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.8634` n `155` status `ready` deltaP `19.7049` edge `0.1065` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.7885` n `158` status `ready` deltaP `12.4612` edge `0.1847` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.7562` n `158` status `ready` deltaP `14.2443` edge `0.1708` maxDD `-4.2199`
- `market_context_high->equity_24h` score `1.7096` n `140` status `ready` deltaP `19.9752` edge `0.162` maxDD `-6.8828`
- `market_context_high->equity_4h` score `1.0204` n `155` status `ready` deltaP `10.7818` edge `0.1536` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
