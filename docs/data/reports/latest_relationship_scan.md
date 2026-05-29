# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T18:07:22.460734+00:00`
- Price records: `672`
- Market context records: `2267`
- Flow alert records: `8422`
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

- `news_risk_high->crypto_alt_24h` score `21.4522` n `43` status `ready` deltaP `51.7724` edge `1.5014` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.7649` n `43` status `ready` deltaP `42.4661` edge `1.0746` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.4111` n `43` status `ready` deltaP `32.3966` edge `1.0164` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.2797` n `43` status `ready` deltaP `22.3716` edge `0.8489` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `8.8487` n `150` status `ready` deltaP `27.6585` edge `0.8209` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `8.7482` n `115` status `ready` deltaP `28.6307` edge `0.5793` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `8.4765` n `150` status `ready` deltaP `32.6667` edge `0.6696` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `8.3117` n `43` status `ready` deltaP `32.6752` edge `0.4974` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `5.6102` n `115` status `ready` deltaP `16.0825` edge `1.0013` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.4634` n `150` status `ready` deltaP `22.0569` edge `0.3692` maxDD `-1.8773`
- `news_risk_high->index_24h` score `3.7795` n `43` status `ready` deltaP `12.5767` edge `0.273` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7468` n `43` status `ready` deltaP `32.1575` edge `0.3331` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6255` n `43` status `ready` deltaP `37.2295` edge `0.0724` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3899` n `115` status `ready` deltaP `14.3765` edge `0.2384` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.2164` n `43` status `ready` deltaP `2.8989` edge `0.3304` maxDD `-3.202`
- `market_context_high->index_4h` score `2.6457` n `150` status `ready` deltaP `24.4735` edge `0.1399` maxDD `-2.2732`
- `market_context_high->equity_4h` score `2.4433` n `150` status `ready` deltaP `19.0427` edge `0.2171` maxDD `-5.9024`
- `market_context_high->crypto_alt_1h` score `2.2417` n `159` status `ready` deltaP `13.522` edge `0.2154` maxDD `-6.1656`
- `news_risk_high->fx_4h` score `2.0589` n `43` status `ready` deltaP `26.3648` edge `0.0142` maxDD `-0.1382`
- `market_context_high->equity_24h` score `2.0499` n `115` status `ready` deltaP `19.9396` edge `0.1906` maxDD `-6.8828`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
