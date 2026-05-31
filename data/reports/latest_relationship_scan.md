# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T02:37:15.691334+00:00`
- Price records: `672`
- Market context records: `2415`
- Flow alert records: `8640`
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

- `news_risk_high->crypto_alt_24h` score `20.1522` n `43` status `ready` deltaP `46.2169` edge `1.4301` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.395` n `43` status `ready` deltaP `49.9313` edge `1.244` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1627` n `43` status `ready` deltaP `29.7925` edge `1.0964` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.822` n `43` status `ready` deltaP `18.8993` edge `0.8339` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.1213` n `43` status `ready` deltaP `27.6405` edge `0.5151` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8087` n `104` status `ready` deltaP `23.6379` edge `0.3593` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.2682` n `43` status `ready` deltaP `11.5351` edge `0.404` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.7295` n `127` status `ready` deltaP `22.4146` edge `0.4257` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.6102` n `127` status `ready` deltaP `22.5429` edge `0.5018` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6139` n `43` status `ready` deltaP `37.924` edge `0.0668` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2969` n `43` status `ready` deltaP `30.4807` edge `0.2866` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.8141` n `104` status `ready` deltaP `11.6319` edge `0.6725` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.5945` n `127` status `ready` deltaP `13.1962` edge `0.1892` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.3728` n `104` status `ready` deltaP `13.2345` edge `0.1367` maxDD `-0.5091`
- `news_risk_high->fx_4h` score `2.1512` n `43` status `ready` deltaP `27.2794` edge `0.0158` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.8097` n `43` status `ready` deltaP `16.1444` edge `0.1155` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2784` n `127` status `ready` deltaP `11.7226` edge `0.1478` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.0282` n `43` status `ready` deltaP `19.9972` edge `-0.0007` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.02` n `127` status `ready` deltaP `8.6449` edge `0.1461` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5491` n `43` status `ready` deltaP `9.2675` edge `0.0766` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
