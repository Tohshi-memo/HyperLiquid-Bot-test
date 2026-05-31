# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T05:07:19.283857+00:00`
- Price records: `672`
- Market context records: `2425`
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

- `news_risk_high->crypto_alt_24h` score `19.6379` n `43` status `ready` deltaP `44.828` edge `1.3965` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.659` n `43` status `ready` deltaP `51.1466` edge `1.2579` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0127` n `43` status `ready` deltaP `29.7925` edge `1.0839` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.2636` n `43` status `ready` deltaP `18.2049` edge `0.792` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.6812` n `43` status `ready` deltaP `25.9044` edge `0.49` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.9241` n `101` status `ready` deltaP `24.615` edge `0.3624` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.0741` n `43` status `ready` deltaP `9.799` edge `0.3994` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.6759` n `124` status `ready` deltaP `22.733` edge `0.506` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.5774` n `124` status `ready` deltaP `21.2333` edge `0.4209` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.4733` n `43` status `ready` deltaP `36.3615` edge `0.0655` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1959` n `43` status `ready` deltaP `29.1087` edge `0.2828` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7034` n `124` status `ready` deltaP `13.8376` edge `0.194` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.5747` n `101` status `ready` deltaP `13.8975` edge `0.1476` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.5501` n `101` status `ready` deltaP `10.8137` edge `0.6441` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.111` n `43` status `ready` deltaP `26.8221` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7737` n `43` status `ready` deltaP `16.1444` edge `0.1125` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.212` n `124` status `ready` deltaP `11.2227` edge `0.1456` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1468` n `43` status `ready` deltaP `20.7457` edge `0.0042` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0305` n `124` status `ready` deltaP `8.8372` edge `0.1457` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5593` n `43` status `ready` deltaP `9.4172` edge `0.0769` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
