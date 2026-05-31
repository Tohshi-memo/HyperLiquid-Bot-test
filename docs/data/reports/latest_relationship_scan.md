# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T12:52:15.701726+00:00`
- Price records: `672`
- Market context records: `2458`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `21.0201` n `37` status `ready` deltaP `45.5612` edge `1.5068` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `20.583` n `37` status `ready` deltaP `55.457` edge `1.3895` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `17.007` n `37` status `ready` deltaP `29.4154` edge `1.2526` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.3405` n `37` status `ready` deltaP `21.8563` edge `0.8574` maxDD `-3.3119`
- `news_risk_high->index_24h` score `7.488` n `37` status `ready` deltaP `21.753` edge `0.5042` maxDD `-1.3507`
- `news_risk_high->unknown_24h` score `7.3872` n `37` status `ready` deltaP `24.5542` edge `0.4745` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8179` n `110` status `ready` deltaP `21.8024` edge `0.3723` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.0989` n `134` status `ready` deltaP `20.6066` edge `0.4721` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.0966` n `134` status `ready` deltaP `18.7773` edge `0.3972` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.6705` n `37` status `ready` deltaP `37.7769` edge `0.0725` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `2.9334` n `37` status `ready` deltaP `25.6345` edge `0.2723` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.4196` n `110` status `ready` deltaP `11.6351` edge `0.6219` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `1.9623` n `37` status `ready` deltaP `24.8723` edge `0.0161` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `1.7832` n `37` status `ready` deltaP `21.6257` edge `0.0476` maxDD `-1.4536`
- `market_context_high->unknown_4h` score `1.6213` n `134` status `ready` deltaP `9.9176` edge `0.1612` maxDD `-2.7098`
- `news_risk_high->metal_4h` score `1.3345` n `37` status `ready` deltaP `6.8392` edge `0.2615` maxDD `-6.2136`
- `market_context_high->index_24h` score `1.2389` n `110` status `ready` deltaP `6.2247` edge `0.1082` maxDD `-0.7163`
- `news_risk_high->unknown_4h` score `0.8614` n `37` status `ready` deltaP `12.6607` edge `0.0597` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `0.8429` n `136` status `ready` deltaP `9.0833` edge `0.1291` maxDD `-4.2199`
- `news_risk_high->fx_1h` score `0.7229` n `37` status `ready` deltaP `11.1143` edge `0.0118` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
