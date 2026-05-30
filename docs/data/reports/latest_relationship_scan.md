# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T12:22:23.021122+00:00`
- Price records: `672`
- Market context records: `2349`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9176`

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

- `news_risk_high->crypto_alt_24h` score `21.2881` n `43` status `ready` deltaP `50.0363` edge `1.4993` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.0286` n `43` status `ready` deltaP `44.8966` edge `1.1637` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.6275` n `43` status `ready` deltaP `29.7925` edge `1.0518` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.0318` n `43` status `ready` deltaP `19.7674` edge `0.8456` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.8488` n `139` status `ready` deltaP `19.7842` edge `1.0781` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.6725` n `43` status `ready` deltaP `27.6405` edge `0.4777` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.8239` n `139` status `ready` deltaP `24.378` edge `0.4473` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.5634` n `155` status `ready` deltaP `22.2227` edge `0.6667` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.5373` n `155` status `ready` deltaP `25.122` edge `0.5583` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.6684` n `155` status `ready` deltaP `22.7154` edge `0.3819` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.8002` n `43` status `ready` deltaP `12.7504` edge `0.3569` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0129` n `43` status `ready` deltaP `34.1392` edge `0.354` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4078` n `43` status `ready` deltaP `36.1879` edge `0.0612` maxDD `-0.1442`
- `market_context_high->index_24h` score `2.7839` n `139` status `ready` deltaP `13.5367` edge `0.1935` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.0926` n `139` status `ready` deltaP `19.8879` edge `0.1945` maxDD `-6.8828`
- `market_context_high->index_4h` score `2.0636` n `155` status `ready` deltaP `20.1977` edge `0.1199` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.0295` n `43` status `ready` deltaP `25.9075` edge `0.0148` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.6453` n `163` status `ready` deltaP `12.0073` edge `0.1758` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5961` n `163` status `ready` deltaP `13.249` edge `0.1641` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.1236` n `155` status `ready` deltaP `10.7818` edge `0.1622` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
