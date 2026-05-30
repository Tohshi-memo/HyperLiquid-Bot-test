# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T19:07:20.098292+00:00`
- Price records: `672`
- Market context records: `2379`
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

- `news_risk_high->crypto_alt_24h` score `21.8624` n `43` status `ready` deltaP `50.2099` edge `1.546` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.0164` n `43` status `ready` deltaP `48.8897` edge `1.2194` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2443` n `43` status `ready` deltaP `29.7925` edge `1.1032` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8694` n `43` status `ready` deltaP `19.7674` edge `0.9154` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2649` n `43` status `ready` deltaP `28.1613` edge `0.5236` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `6.7996` n `131` status `ready` deltaP `17.9389` edge `0.8363` maxDD `-25.1408`
- `market_context_high->crypto_major_4h` score `5.5407` n `147` status `ready` deltaP `24.0336` edge `0.4825` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `5.4315` n `131` status `ready` deltaP `23.6522` edge `0.3361` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3514` n `43` status `ready` deltaP `13.4448` edge `0.3982` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.4124` n `147` status `ready` deltaP `19.0943` edge `0.5083` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `4.1593` n `147` status `ready` deltaP `18.5664` edge `0.2838` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7061` n `43` status `ready` deltaP `32.0051` edge `0.3289` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4976` n `43` status `ready` deltaP `37.0559` edge `0.0629` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9979` n `43` status `ready` deltaP `25.6026` edge `0.0142` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.6557` n `154` status `ready` deltaP `13.8891` edge `0.1648` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.4837` n `131` status `ready` deltaP `11.4742` edge `0.0989` maxDD `-1.4737`
- `market_context_high->index_4h` score `1.3145` n `147` status `ready` deltaP `15.7541` edge `0.0871` maxDD `-2.2732`
- `news_risk_high->unknown_4h` score `1.2358` n `43` status `ready` deltaP `14.0102` edge `0.0819` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `1.2237` n `154` status `ready` deltaP `9.6917` edge `0.1561` maxDD `-6.1656`
- `news_risk_high->unknown_1h` score `0.9527` n `43` status `ready` deltaP `19.3984` edge `-0.003` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
