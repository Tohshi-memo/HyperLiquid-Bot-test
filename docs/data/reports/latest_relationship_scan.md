# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T03:37:20.136494+00:00`
- Price records: `672`
- Market context records: `2419`
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

- `news_risk_high->crypto_alt_24h` score `20.0068` n `43` status `ready` deltaP `45.8696` edge `1.4203` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.5357` n `43` status `ready` deltaP `50.6258` edge `1.2511` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1135` n `43` status `ready` deltaP `29.7925` edge `1.0923` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.672` n `43` status `ready` deltaP `18.8993` edge `0.8214` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.9241` n `43` status `ready` deltaP `26.946` edge `0.5033` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.7701` n `103` status `ready` deltaP `23.8302` edge `0.3548` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.1922` n `43` status `ready` deltaP `10.8406` edge `0.4023` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.6543` n `126` status `ready` deltaP `22.0746` edge `0.4217` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.5837` n `126` status `ready` deltaP `22.4957` edge `0.4999` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.5674` n `43` status `ready` deltaP `37.4031` edge `0.0664` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2645` n `43` status `ready` deltaP `30.0233` edge `0.2855` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.6954` n `103` status `ready` deltaP `11.2678` edge `0.6597` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.6601` n `126` status `ready` deltaP `13.6712` edge `0.1915` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4352` n `103` status `ready` deltaP `13.3242` edge `0.1398` maxDD `-0.3888`
- `news_risk_high->fx_4h` score `2.139` n `43` status `ready` deltaP `27.127` edge `0.0158` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7725` n `43` status `ready` deltaP `16.1444` edge `0.1124` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2235` n `126` status `ready` deltaP `11.4414` edge `0.1451` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.033` n `43` status `ready` deltaP `19.9972` edge `-0.0003` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0076` n `126` status `ready` deltaP `8.6256` edge `0.1452` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5585` n `43` status `ready` deltaP `9.4172` edge `0.0768` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
