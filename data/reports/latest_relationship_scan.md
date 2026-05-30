# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T22:37:15.837829+00:00`
- Price records: `672`
- Market context records: `2396`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9201`

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

- `news_risk_high->crypto_alt_24h` score `21.2533` n `43` status `ready` deltaP `48.821` edge `1.5045` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2342` n `43` status `ready` deltaP `49.9313` edge `1.2306` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3571` n `43` status `ready` deltaP `29.7925` edge `1.1126` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.6306` n `43` status `ready` deltaP `19.7674` edge `0.8955` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3549` n `43` status `ready` deltaP `28.1613` edge `0.5311` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4757` n `43` status `ready` deltaP `13.6184` edge `0.4074` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.3066` n `117` status `ready` deltaP `22.5561` edge `0.333` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.7693` n `140` status `ready` deltaP `23.4364` edge `0.4222` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.5911` n `43` status `ready` deltaP `37.924` edge `0.0649` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.4823` n `140` status `ready` deltaP `17.953` edge `0.4384` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.2969` n `43` status `ready` deltaP `30.4807` edge `0.2866` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.1173` n `117` status `ready` deltaP `14.1026` edge `0.6949` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.4065` n `140` status `ready` deltaP `13.3058` edge `0.1728` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0733` n `43` status `ready` deltaP `26.3648` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6827` n `43` status `ready` deltaP `15.3822` edge `0.11` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.3394` n `140` status `ready` deltaP `12.7545` edge `0.146` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.222` n `117` status `ready` deltaP `8.9076` edge `0.0942` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.0594` n `43` status `ready` deltaP `19.6978` edge `0.0039` maxDD `-1.7548`
- `market_context_high->index_4h` score `0.8237` n `140` status `ready` deltaP `13.7588` edge `0.0595` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `0.7886` n `140` status `ready` deltaP `7.8229` edge `0.1323` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
