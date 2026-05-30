# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T15:42:45.149542+00:00`
- Price records: `672`
- Market context records: `2364`
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

- `news_risk_high->crypto_alt_24h` score `21.6781` n `43` status `ready` deltaP `50.0363` edge `1.5318` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.5695` n `43` status `ready` deltaP `46.6327` edge `1.1972` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9167` n `43` status `ready` deltaP `29.7925` edge `1.0759` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.5334` n `43` status `ready` deltaP `19.7674` edge `0.8874` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `8.6229` n `140` status `ready` deltaP `20.0` edge `0.9745` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.8976` n `43` status `ready` deltaP `27.8141` edge `0.4953` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.178` n `140` status `ready` deltaP `23.8939` edge `0.3967` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.9202` n `152` status `ready` deltaP `24.7273` edge `0.5095` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `5.3029` n `152` status `ready` deltaP `20.146` edge `0.5755` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `5.1546` n `152` status `ready` deltaP `21.6624` edge `0.3461` maxDD `-1.8773`
- `news_risk_high->index_24h` score `5.1376` n `43` status `ready` deltaP `13.0976` edge `0.3827` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7874` n `43` status `ready` deltaP `32.1575` edge `0.3383` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4042` n `43` status `ready` deltaP `36.1879` edge `0.0609` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9479` n `43` status `ready` deltaP `24.9929` edge `0.0141` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.8245` n `140` status `ready` deltaP `12.5992` edge `0.1198` maxDD `-1.4737`
- `market_context_high->index_4h` score `1.7811` n `152` status `ready` deltaP `19.3357` edge `0.1021` maxDD `-2.2732`
- `market_context_high->crypto_major_1h` score `1.758` n `157` status `ready` deltaP `14.5219` edge `0.1691` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `1.5472` n `157` status `ready` deltaP `11.2609` edge `0.1726` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.34` n `140` status `ready` deltaP `19.9752` edge `0.1312` maxDD `-6.8828`
- `news_risk_high->unknown_4h` score `0.9026` n `43` status `ready` deltaP `13.4005` edge `0.0582` maxDD `-2.7857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
