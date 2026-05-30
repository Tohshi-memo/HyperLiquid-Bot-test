# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T07:07:15.494766+00:00`
- Price records: `672`
- Market context records: `2324`
- Flow alert records: `8583`
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

- `news_risk_high->crypto_alt_24h` score `20.7265` n `43` status `ready` deltaP `50.0363` edge `1.4525` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.3382` n `43` status `ready` deltaP `42.9869` edge `1.1189` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.0515` n `43` status `ready` deltaP `29.7925` edge `1.0038` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.4282` n `43` status `ready` deltaP `19.7674` edge `0.7953` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.5206` n `122` status `ready` deltaP `23.9214` edge `0.5084` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `7.0159` n `159` status `ready` deltaP `23.3941` edge `0.6966` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.0001` n `159` status `ready` deltaP `27.6068` edge `0.5803` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `6.923` n `43` status `ready` deltaP `27.4669` edge `0.4164` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `5.5635` n `122` status `ready` deltaP `15.5738` edge `0.9987` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.3181` n `159` status `ready` deltaP `21.5457` edge `0.3605` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.1956` n `43` status `ready` deltaP `11.8823` edge `0.3123` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0057` n `43` status `ready` deltaP `33.9868` edge `0.3541` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4621` n `122` status `ready` deltaP `13.96` edge `0.2472` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4083` n `43` status `ready` deltaP `36.0142` edge `0.0624` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.2086` n `43` status `ready` deltaP `28.0416` edge `0.0155` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.1582` n `159` status `ready` deltaP `21.1094` edge `0.1217` maxDD `-2.2732`
- `news_risk_high->commodity_24h` score `1.9163` n `43` status `ready` deltaP `4.2878` edge `0.2128` maxDD `-3.202`
- `market_context_high->crypto_alt_1h` score `1.9095` n `159` status `ready` deltaP `12.4741` edge `0.1947` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.6779` n `122` status `ready` deltaP `18.1837` edge `0.1713` maxDD `-6.8828`
- `market_context_high->crypto_major_1h` score `1.6661` n `159` status `ready` deltaP `12.6238` edge `0.1741` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
