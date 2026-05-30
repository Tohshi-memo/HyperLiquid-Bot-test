# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T06:07:23.047627+00:00`
- Price records: `672`
- Market context records: `2320`
- Flow alert records: `8570`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9168`

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

- `news_risk_high->crypto_alt_24h` score `20.7301` n `43` status `ready` deltaP `50.0363` edge `1.4528` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.1873` n `43` status `ready` deltaP `42.4661` edge `1.1098` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.9399` n `43` status `ready` deltaP `29.7925` edge `0.9945` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3982` n `43` status `ready` deltaP `19.7674` edge `0.7928` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.4456` n `118` status `ready` deltaP `23.6435` edge `0.504` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `7.1299` n `159` status `ready` deltaP `23.3941` edge `0.7061` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.1145` n `159` status `ready` deltaP `27.9116` edge `0.5878` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `6.8582` n `43` status `ready` deltaP `27.4669` edge `0.411` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.3748` n `159` status `ready` deltaP `21.8505` edge `0.3632` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.2914` n `118` status `ready` deltaP `14.4068` edge `0.9716` maxDD `-25.1408`
- `news_risk_high->index_24h` score `4.0905` n `43` status `ready` deltaP `11.7087` edge `0.3047` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.9978` n `43` status `ready` deltaP `33.8343` edge `0.3541` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.5765` n `118` status `ready` deltaP `13.9948` edge `0.2565` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4083` n `43` status `ready` deltaP `36.0142` edge `0.0624` maxDD `-0.1442`
- `market_context_high->index_4h` score `2.2286` n `159` status `ready` deltaP `21.7192` edge `0.1235` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.2208` n `43` status `ready` deltaP `28.1941` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->commodity_24h` score `2.1419` n `43` status `ready` deltaP `4.2878` edge `0.2316` maxDD `-3.202`
- `market_context_high->crypto_alt_1h` score `1.9646` n `159` status `ready` deltaP `12.7735` edge `0.1973` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.7248` n `159` status `ready` deltaP `13.0729` edge `0.176` maxDD `-4.2199`
- `market_context_high->equity_24h` score `1.6065` n `118` status `ready` deltaP `17.7113` edge `0.1685` maxDD `-6.8828`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
