# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T19:52:21.938320+00:00`
- Price records: `672`
- Market context records: `2383`
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

- `news_risk_high->crypto_alt_24h` score `21.7808` n `43` status `ready` deltaP `50.2099` edge `1.5392` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1037` n `43` status `ready` deltaP `49.4105` edge `1.2232` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2779` n `43` status `ready` deltaP `29.7925` edge `1.106` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.843` n `43` status `ready` deltaP `19.7674` edge `0.9132` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2949` n `43` status `ready` deltaP `28.1613` edge `0.5261` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `6.2967` n `128` status `ready` deltaP `17.1875` edge `0.7994` maxDD `-25.1408`
- `news_risk_high->index_24h` score `5.379` n `43` status `ready` deltaP `13.4448` edge `0.4005` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.3339` n `128` status `ready` deltaP `23.4375` edge `0.3294` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.1611` n `144` status `ready` deltaP `23.5942` edge `0.4538` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `3.9583` n `144` status `ready` deltaP `18.4282` edge `0.4749` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.6421` n `43` status `ready` deltaP `32.0051` edge `0.3207` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `3.5711` n `144` status `ready` deltaP `18.0387` edge `0.2383` maxDD `-1.8773`
- `news_risk_high->fx_24h` score `3.5453` n `43` status `ready` deltaP `37.5767` edge `0.0634` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.0369` n `43` status `ready` deltaP `26.0599` edge `0.0144` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.6309` n `151` status `ready` deltaP `13.7437` edge `0.1637` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.3999` n `128` status `ready` deltaP `10.9375` edge `0.0955` maxDD `-1.4737`
- `news_risk_high->unknown_4h` score `1.3872` n `43` status `ready` deltaP `14.1627` edge `0.0935` maxDD `-2.7857`
- `market_context_high->index_4h` score `1.2215` n `144` status `ready` deltaP `15.7012` edge `0.0797` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.1617` n `151` status `ready` deltaP `9.217` edge `0.1541` maxDD `-6.1656`
- `news_risk_high->unknown_1h` score `0.9359` n `43` status `ready` deltaP `19.2487` edge `-0.0034` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
