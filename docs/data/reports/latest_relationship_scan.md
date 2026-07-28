# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T05:52:30.636698+00:00`
- Price records: `672`
- Market context records: `8167`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `news_risk_high->unknown_24h` score `8298.9154` n `36` status `ready` deltaP `37.1528` edge `691.3286` maxDD `0.0`
- `market_context_high->equity_24h` score `18.9516` n `63` status `ready` deltaP `44.4197` edge `1.3742` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.4205` n `64` status `ready` deltaP `38.0716` edge `0.5547` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `9.0785` n `43` status `ready` deltaP `34.2562` edge `0.5487` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.1728` n `63` status `ready` deltaP `41.3194` edge `0.4056` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.498` n `43` status `ready` deltaP `20.4907` edge `0.3821` maxDD `-2.1767`
- `market_context_high->index_4h` score `4.0456` n `64` status `ready` deltaP `36.7378` edge `0.0965` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.6719` n `64` status `ready` deltaP `21.7066` edge `0.1816` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.3967` n `47` status `ready` deltaP `25.43` edge `0.1444` maxDD `-1.1366`
- `market_context_high->index_24h` score `2.9467` n `63` status `ready` deltaP `19.1221` edge `0.1851` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.91` n `43` status `ready` deltaP `24.3831` edge `0.099` maxDD `-0.191`
- `market_context_high->index_1h` score `1.9259` n `64` status `ready` deltaP `22.1744` edge `0.0265` maxDD `-0.1069`
- `market_context_high->metal_4h` score `1.8191` n `64` status `ready` deltaP `21.7988` edge `0.0685` maxDD `-0.979`
- `news_risk_high->metal_4h` score `1.7982` n `43` status `ready` deltaP `16.5662` edge `0.0862` maxDD `-0.7433`
- `market_context_high->fx_24h` score `1.6029` n `63` status `ready` deltaP `22.5199` edge `0.0538` maxDD `-0.6283`
- `news_risk_high->crypto_major_1h` score `1.5011` n `47` status `ready` deltaP `8.4628` edge `0.1084` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.2493` n `47` status `ready` deltaP `9.361` edge `0.0851` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.1769` n `43` status `ready` deltaP `12.8651` edge `0.2043` maxDD `-5.8012`
- `market_context_high->commodity_24h` score `1.1557` n `63` status `ready` deltaP `28.6211` edge `0.2459` maxDD `-15.7497`
- `market_context_high->crypto_major_1h` score `0.7881` n `64` status `ready` deltaP `9.3937` edge `0.0441` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
