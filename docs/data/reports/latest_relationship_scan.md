# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T11:04:22.479277+00:00`
- Price records: `672`
- Market context records: `2342`
- Flow alert records: `8632`
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

- `news_risk_high->crypto_alt_24h` score `21.0481` n `43` status `ready` deltaP `50.0363` edge `1.4793` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.835` n `43` status `ready` deltaP `44.2022` edge `1.1522` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.4883` n `43` status `ready` deltaP `29.7925` edge `1.0402` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.8146` n `43` status `ready` deltaP `19.7674` edge `0.8275` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `10.2501` n `138` status `ready` deltaP `19.5652` edge `1.113` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.4769` n `43` status `ready` deltaP `27.6405` edge `0.4614` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `7.2202` n `138` status `ready` deltaP `24.3207` edge `0.4807` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.5472` n `159` status `ready` deltaP `22.7843` edge `0.6616` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.4634` n `159` status `ready` deltaP `25.4726` edge `0.5498` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.4484` n `159` status `ready` deltaP `22.1554` edge `0.3673` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.5971` n `43` status `ready` deltaP `12.0559` edge `0.3446` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0152` n `43` status `ready` deltaP `34.1392` edge `0.3543` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4114` n `43` status `ready` deltaP `36.1879` edge `0.0615` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3409` n `138` status `ready` deltaP `15.5948` edge `0.2262` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.3723` n `138` status `ready` deltaP `19.7993` edge `0.2184` maxDD `-6.8828`
- `news_risk_high->fx_4h` score `2.0307` n `43` status `ready` deltaP `25.9075` edge `0.0149` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.0102` n `159` status `ready` deltaP `19.8899` edge `0.1175` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.6905` n `166` status `ready` deltaP `12.362` edge `0.1772` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5302` n `166` status `ready` deltaP `12.8147` edge `0.1615` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.1142` n `159` status `ready` deltaP `11.2201` edge `0.1585` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
