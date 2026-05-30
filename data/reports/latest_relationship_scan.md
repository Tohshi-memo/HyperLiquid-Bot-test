# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T15:37:18.186659+00:00`
- Price records: `672`
- Market context records: `2363`
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

- `news_risk_high->crypto_alt_24h` score `21.6733` n `43` status `ready` deltaP `50.0363` edge `1.5314` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.5695` n `43` status `ready` deltaP `46.6327` edge `1.1972` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9155` n `43` status `ready` deltaP `29.7925` edge `1.0758` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.5274` n `43` status `ready` deltaP `19.7674` edge `0.8869` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `8.6397` n `140` status `ready` deltaP `20.0` edge `0.9759` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.8753` n `43` status `ready` deltaP `27.6405` edge `0.4946` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.2465` n `140` status `ready` deltaP `24.4346` edge `0.3988` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.9358` n `152` status `ready` deltaP `24.7273` edge `0.5108` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `5.3565` n `152` status `ready` deltaP `20.6514` edge `0.5766` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `5.181` n `152` status `ready` deltaP `21.6624` edge `0.3483` maxDD `-1.8773`
- `news_risk_high->index_24h` score `5.1376` n `43` status `ready` deltaP `13.0976` edge `0.3827` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7866` n `43` status `ready` deltaP `32.1575` edge `0.3382` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4042` n `43` status `ready` deltaP `36.1879` edge `0.0609` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9479` n `43` status `ready` deltaP `24.9929` edge `0.0141` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.8257` n `140` status `ready` deltaP `12.5992` edge `0.1199` maxDD `-1.4737`
- `market_context_high->crypto_major_1h` score `1.8126` n `157` status `ready` deltaP `15.0092` edge `0.1704` maxDD `-4.2199`
- `market_context_high->index_4h` score `1.7823` n `152` status `ready` deltaP `19.3357` edge `0.1022` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.5592` n `157` status `ready` deltaP `11.2609` edge `0.1736` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.3424` n `140` status `ready` deltaP `19.9752` edge `0.1314` maxDD `-6.8828`
- `news_risk_high->unknown_4h` score `0.8942` n `43` status `ready` deltaP `13.4005` edge `0.0575` maxDD `-2.7857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
