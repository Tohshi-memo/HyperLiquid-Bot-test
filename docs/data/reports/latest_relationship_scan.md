# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T18:07:24.650261+00:00`
- Price records: `672`
- Market context records: `2375`
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

- `news_risk_high->crypto_alt_24h` score `21.9164` n `43` status `ready` deltaP `50.2099` edge `1.5505` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.8973` n `43` status `ready` deltaP `48.1952` edge `1.2141` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2035` n `43` status `ready` deltaP `29.7925` edge `1.0998` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8814` n `43` status `ready` deltaP `19.7674` edge `0.9164` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.1857` n `43` status `ready` deltaP `28.1613` edge `0.517` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `7.472` n `135` status `ready` deltaP `18.8889` edge `0.886` maxDD `-25.1408`
- `market_context_high->crypto_major_4h` score `5.6367` n `147` status `ready` deltaP `24.0336` edge `0.4905` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `5.5756` n `135` status `ready` deltaP `23.9236` edge `0.3463` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3142` n `43` status `ready` deltaP `13.4448` edge `0.3951` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.6896` n `147` status `ready` deltaP `19.0943` edge `0.5314` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `4.6206` n `147` status `ready` deltaP `19.6221` edge `0.3152` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7435` n `43` status `ready` deltaP `32.0051` edge `0.3337` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4627` n `43` status `ready` deltaP `36.7087` edge `0.0623` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9845` n `43` status `ready` deltaP `25.4502` edge `0.0141` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.6356` n `155` status `ready` deltaP `14.1028` edge `0.1617` maxDD `-4.2199`
- `market_context_high->index_4h` score `1.6299` n `147` status `ready` deltaP `17.8654` edge `0.0993` maxDD `-2.2732`
- `market_context_high->index_24h` score `1.5872` n `135` status `ready` deltaP `12.1528` edge `0.103` maxDD `-1.4737`
- `market_context_high->crypto_alt_1h` score `1.2606` n `155` status `ready` deltaP `9.943` edge `0.1575` maxDD `-6.1656`
- `news_risk_high->unknown_4h` score `1.1022` n `43` status `ready` deltaP `13.7053` edge `0.0728` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `0.9707` n `43` status `ready` deltaP `19.3984` edge `-0.0015` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
