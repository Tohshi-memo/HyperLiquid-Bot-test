# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T08:07:21.636926+00:00`
- Price records: `672`
- Market context records: `2226`
- Flow alert records: `8300`
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

- `news_risk_high->crypto_alt_24h` score `26.4562` n `33` status `ready` deltaP `57.3075` edge `1.8815` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.8644` n `33` status `ready` deltaP `47.6641` edge `0.9649` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.2146` n `33` status `ready` deltaP `38.6364` edge `0.8751` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.8835` n `132` status `ready` deltaP `37.149` edge `0.9196` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.669` n `132` status `ready` deltaP `41.6713` edge `0.7476` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.9593` n `33` status `ready` deltaP `38.2102` edge `0.5978` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.8585` n `33` status `ready` deltaP `20.1547` edge `0.9312` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.391` n `132` status `ready` deltaP `20.9165` edge `0.3777` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.9424` n `43` status `ready` deltaP `32.9197` edge `0.3531` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.2783` n `132` status `ready` deltaP `22.8058` edge `0.2306` maxDD `-5.0894`
- `market_context_high->index_4h` score `3.2004` n `132` status `ready` deltaP `26.4689` edge `0.1586` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.1139` n `139` status `ready` deltaP `17.0562` edge `0.1935` maxDD `-1.817`
- `news_risk_high->fx_24h` score `2.9712` n `33` status `ready` deltaP `31.0606` edge `0.059` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.8829` n `139` status `ready` deltaP `15.767` edge `0.2215` maxDD `-4.9097`
- `news_risk_high->commodity_24h` score `2.4942` n `33` status `ready` deltaP `-1.0733` edge `0.2967` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.2024` n `43` status `ready` deltaP `27.8892` edge `0.016` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.6629` n `132` status `ready` deltaP `8.8226` edge `0.2026` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.6522` n `132` status `ready` deltaP `23.8163` edge `0.4604` maxDD `-32.8525`
- `news_risk_high->index_24h` score `1.591` n `33` status `ready` deltaP `11.0954` edge `0.1005` maxDD `-1.3507`
- `news_risk_high->unknown_1h` score `1.3472` n `43` status `ready` deltaP `20.8954` edge `0.0199` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
