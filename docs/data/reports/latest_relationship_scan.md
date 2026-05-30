# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T06:37:16.113723+00:00`
- Price records: `672`
- Market context records: `2322`
- Flow alert records: `8576`
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

- `news_risk_high->crypto_alt_24h` score `20.7193` n `43` status `ready` deltaP `50.0363` edge `1.4519` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.254` n `43` status `ready` deltaP `42.6397` edge `1.1142` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.9963` n `43` status `ready` deltaP `29.7925` edge `0.9992` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.4138` n `43` status `ready` deltaP `19.7674` edge `0.7941` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.5265` n `120` status `ready` deltaP `23.7848` edge `0.5098` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `7.0987` n `159` status `ready` deltaP `23.3941` edge `0.7035` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.0661` n `159` status `ready` deltaP `27.6068` edge `0.5858` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `6.8822` n `43` status `ready` deltaP `27.4669` edge `0.413` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `5.4393` n `120` status `ready` deltaP `15.0` edge `0.9866` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.3471` n `159` status `ready` deltaP `21.6981` edge `0.3619` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.1512` n `43` status `ready` deltaP `11.8823` edge `0.3086` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0065` n `43` status `ready` deltaP `33.9868` edge `0.3542` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4898` n `120` status `ready` deltaP `13.6458` edge `0.2516` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4083` n `43` status `ready` deltaP `36.0142` edge `0.0624` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.2208` n `43` status `ready` deltaP `28.1941` edge `0.0155` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.1958` n `159` status `ready` deltaP `21.4143` edge `0.1228` maxDD `-2.2732`
- `news_risk_high->commodity_24h` score `2.0315` n `43` status `ready` deltaP `4.2878` edge `0.2224` maxDD `-3.202`
- `market_context_high->crypto_alt_1h` score `1.9191` n `159` status `ready` deltaP `12.4741` edge `0.1955` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.6913` n `159` status `ready` deltaP `12.7735` edge `0.1752` maxDD `-4.2199`
- `market_context_high->equity_24h` score `1.6497` n `120` status `ready` deltaP `17.9514` edge `0.1705` maxDD `-6.8828`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
