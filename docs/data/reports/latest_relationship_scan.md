# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T18:52:23.599106+00:00`
- Price records: `672`
- Market context records: `2378`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `news_risk_high->crypto_alt_24h` score `21.8876` n `43` status `ready` deltaP `50.2099` edge `1.5481` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.9857` n `43` status `ready` deltaP `48.7161` edge `1.218` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2383` n `43` status `ready` deltaP `29.7925` edge `1.1027` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8826` n `43` status `ready` deltaP `19.7674` edge `0.9165` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2517` n `43` status `ready` deltaP `28.1613` edge `0.5225` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `6.9654` n `132` status `ready` deltaP `18.1818` edge `0.8485` maxDD `-25.1408`
- `market_context_high->crypto_major_4h` score `5.5911` n `147` status `ready` deltaP `24.0336` edge `0.4867` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `5.4502` n `132` status `ready` deltaP `23.7216` edge `0.3372` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3418` n `43` status `ready` deltaP `13.4448` edge `0.3974` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.4904` n `147` status `ready` deltaP `19.0943` edge `0.5148` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `4.2985` n `147` status `ready` deltaP `18.5664` edge `0.2954` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7217` n `43` status `ready` deltaP `32.0051` edge `0.3309` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4952` n `43` status `ready` deltaP `37.0559` edge `0.0627` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9857` n `43` status `ready` deltaP `25.4502` edge `0.0142` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.6632` n `155` status `ready` deltaP `14.1028` edge `0.164` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.512` n `132` status `ready` deltaP `11.6477` edge `0.1001` maxDD `-1.4737`
- `market_context_high->index_4h` score `1.4036` n `147` status `ready` deltaP `16.282` edge `0.091` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.251` n `155` status `ready` deltaP `9.943` edge `0.1567` maxDD `-6.1656`
- `news_risk_high->unknown_4h` score `1.195` n `43` status `ready` deltaP `14.0102` edge `0.0785` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `0.9838` n `43` status `ready` deltaP `19.5481` edge `-0.0014` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
