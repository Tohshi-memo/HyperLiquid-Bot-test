# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T15:07:18.190886+00:00`
- Price records: `672`
- Market context records: `2361`
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

- `news_risk_high->crypto_alt_24h` score `21.5641` n `43` status `ready` deltaP `50.0363` edge `1.5223` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.4721` n `43` status `ready` deltaP `46.2855` edge `1.1914` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.8507` n `43` status `ready` deltaP `29.7925` edge `1.0704` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.4074` n `43` status `ready` deltaP `19.7674` edge `0.8769` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.0165` n `140` status `ready` deltaP `20.0` edge `1.0073` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.8177` n `43` status `ready` deltaP `27.6405` edge `0.4898` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.4289` n `140` status `ready` deltaP `24.4346` edge `0.414` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `6.082` n `153` status `ready` deltaP `24.8606` edge `0.5221` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `5.622` n `153` status `ready` deltaP `20.8492` edge `0.5974` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `5.2813` n `153` status `ready` deltaP `21.8516` edge `0.3554` maxDD `-1.8773`
- `news_risk_high->index_24h` score `5.0992` n `43` status `ready` deltaP `13.0976` edge `0.3795` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.8274` n `43` status `ready` deltaP `32.4624` edge `0.3414` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4018` n `43` status `ready` deltaP `36.1879` edge `0.0607` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9479` n `43` status `ready` deltaP `24.9929` edge `0.0141` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.9409` n `140` status `ready` deltaP `12.5992` edge `0.1295` maxDD `-1.4737`
- `market_context_high->crypto_major_1h` score `1.8534` n `157` status `ready` deltaP `15.0092` edge `0.1738` maxDD `-4.2199`
- `market_context_high->index_4h` score `1.8091` n `153` status `ready` deltaP `19.4604` edge `0.1036` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.7572` n `157` status `ready` deltaP `12.2354` edge `0.1836` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.5452` n `140` status `ready` deltaP `19.9752` edge `0.1483` maxDD `-6.8828`
- `market_context_high->equity_4h` score `0.9158` n `153` status `ready` deltaP `10.5541` edge `0.1464` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
