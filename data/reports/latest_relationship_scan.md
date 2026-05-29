# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T20:07:25.658007+00:00`
- Price records: `672`
- Market context records: `2276`
- Flow alert records: `8447`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9287`

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

- `news_risk_high->crypto_alt_24h` score `20.7857` n `43` status `ready` deltaP `50.7307` edge `1.4528` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5926` n `43` status `ready` deltaP `41.0772` edge `1.0695` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.9484` n `43` status `ready` deltaP `31.0077` edge `0.9871` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.6742` n `43` status `ready` deltaP `20.9827` edge `0.8077` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `8.1378` n `115` status `ready` deltaP `27.2418` edge `0.5377` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `8.1255` n `158` status `ready` deltaP `25.8336` edge `0.7728` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.903` n `158` status `ready` deltaP `30.4029` edge `0.6369` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.7013` n `43` status `ready` deltaP `31.2863` edge `0.4558` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5426` n `158` status `ready` deltaP `21.847` edge `0.3772` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.2166` n `115` status `ready` deltaP `14.6936` edge `0.9601` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.7845` n `43` status `ready` deltaP `32.4624` edge `0.3359` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7416` n `43` status `ready` deltaP `12.4031` edge `0.271` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.5955` n `43` status `ready` deltaP `37.2295` edge `0.0699` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `3.4167` n `43` status `ready` deltaP `3.767` edge `0.3413` maxDD `-3.202`
- `market_context_high->index_24h` score `3.352` n `115` status `ready` deltaP `14.2029` edge `0.2364` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.547` n `158` status `ready` deltaP `24.1992` edge `0.1335` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `2.3401` n `159` status `ready` deltaP `13.8214` edge `0.2216` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.2818` n `158` status `ready` deltaP `18.7346` edge `0.2057` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0856` n `43` status `ready` deltaP `26.6697` edge `0.0144` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.9935` n `159` status `ready` deltaP `13.8214` edge `0.1934` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
