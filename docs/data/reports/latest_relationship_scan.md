# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T23:46:28.714131+00:00`
- Price records: `672`
- Market context records: `2402`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9202`

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

- `news_risk_high->crypto_alt_24h` score `20.8851` n `43` status `ready` deltaP `47.953` edge `1.4796` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1769` n `43` status `ready` deltaP `49.4105` edge `1.2293` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3271` n `43` status `ready` deltaP `29.7925` edge `1.1101` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.3249` n `43` status `ready` deltaP `19.2466` edge `0.8735` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2721` n `43` status `ready` deltaP `28.1613` edge `0.5242` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4244` n `43` status `ready` deltaP `13.0976` edge `0.4066` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.2887` n `115` status `ready` deltaP `22.3777` edge `0.3327` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.9028` n `138` status `ready` deltaP `24.145` edge `0.4286` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `3.6553` n `138` status `ready` deltaP `18.496` edge `0.4492` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6019` n `43` status `ready` deltaP `37.924` edge `0.0658` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2608` n `43` status `ready` deltaP `30.1758` edge `0.284` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.979` n `115` status `ready` deltaP `13.827` edge `0.679` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.4681` n `138` status `ready` deltaP `13.4611` edge `0.1769` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1268` n `43` status `ready` deltaP `26.9746` edge `0.0158` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6983` n `43` status `ready` deltaP `15.3822` edge `0.1113` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.3135` n `115` status `ready` deltaP `8.8104` edge `0.0993` maxDD `-1.2193`
- `market_context_high->crypto_major_1h` score `1.3088` n `138` status `ready` deltaP `12.6725` edge `0.144` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1241` n `43` status `ready` deltaP `20.1469` edge `0.0063` maxDD `-1.7548`
- `market_context_high->index_4h` score `0.8268` n `138` status `ready` deltaP `13.8123` edge `0.0594` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `0.8021` n `138` status `ready` deltaP `8.2466` edge `0.1306` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
