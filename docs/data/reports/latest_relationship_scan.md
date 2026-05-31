# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T02:22:21.510285+00:00`
- Price records: `672`
- Market context records: `2414`
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

- `news_risk_high->crypto_alt_24h` score `20.1762` n `43` status `ready` deltaP `46.2169` edge `1.4321` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.3583` n `43` status `ready` deltaP `49.7577` edge `1.2421` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1759` n `43` status `ready` deltaP `29.7925` edge `1.0975` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.8484` n `43` status `ready` deltaP `18.8993` edge `0.8361` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.164` n `43` status `ready` deltaP `27.8141` edge `0.5175` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6442` n `105` status `ready` deltaP `22.9415` edge `0.3544` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.2881` n `43` status `ready` deltaP `11.7087` edge `0.4045` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.7467` n `128` status `ready` deltaP `22.5991` edge `0.4259` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.5206` n `128` status `ready` deltaP `22.1418` edge `0.497` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6151` n `43` status `ready` deltaP `37.924` edge `0.0669` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2874` n `43` status `ready` deltaP `30.3282` edge `0.2864` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.8491` n `105` status `ready` deltaP `11.989` edge `0.6746` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.4875` n `128` status `ready` deltaP `12.7287` edge `0.1834` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.2342` n `105` status `ready` deltaP `12.6389` edge `0.1318` maxDD `-0.7236`
- `news_risk_high->fx_4h` score `2.1524` n `43` status `ready` deltaP `27.2794` edge `0.0159` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.8181` n `43` status `ready` deltaP `16.1444` edge `0.1162` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.3066` n `128` status `ready` deltaP `11.8498` edge `0.1493` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.0581` n `43` status `ready` deltaP `20.1469` edge `0.0008` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0343` n `128` status `ready` deltaP `8.8089` edge `0.1462` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5359` n `43` status `ready` deltaP `9.1178` edge `0.0759` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
