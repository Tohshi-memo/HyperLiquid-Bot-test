# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T04:37:17.894749+00:00`
- Price records: `672`
- Market context records: `2423`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `19.7521` n `43` status `ready` deltaP `45.1752` edge `1.4037` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.6048` n `43` status `ready` deltaP `50.7994` edge `1.2557` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0427` n `43` status `ready` deltaP `29.7925` edge `1.0864` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3939` n `43` status `ready` deltaP `18.3785` edge `0.8017` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.7606` n `43` status `ready` deltaP `26.2516` edge `0.4943` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.0035` n `101` status `ready` deltaP `24.9622` edge `0.3667` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.1139` n `43` status `ready` deltaP `10.1462` edge `0.4004` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.735` n `124` status `ready` deltaP `23.0379` edge `0.5089` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.6052` n `124` status `ready` deltaP `21.3858` edge `0.4222` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.5047` n `43` status `ready` deltaP `36.7087` edge `0.0658` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2203` n `43` status `ready` deltaP `29.4136` edge `0.2839` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.666` n `124` status `ready` deltaP `13.6851` edge `0.1919` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `2.6348` n `101` status `ready` deltaP `10.9873` edge `0.6538` maxDD `-25.1408`
- `market_context_high->index_24h` score `2.6145` n `101` status `ready` deltaP `14.2447` edge `0.1486` maxDD `-0.3888`
- `news_risk_high->fx_4h` score `2.1122` n `43` status `ready` deltaP `26.8221` edge `0.0156` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7363` n `43` status `ready` deltaP `15.9919` edge `0.1104` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2132` n `124` status `ready` deltaP `11.2227` edge `0.1457` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1109` n `43` status `ready` deltaP `20.4463` edge `0.0032` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0533` n `124` status `ready` deltaP `8.9869` edge `0.1466` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.631` n `101` status `ready` deltaP `1.3115` edge `0.7679` maxDD `-43.6595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
