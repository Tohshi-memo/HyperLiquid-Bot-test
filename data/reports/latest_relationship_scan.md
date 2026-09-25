# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T10:07:28.582031+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11286`

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

- `market_context_high->unknown_1h` score `84.739` n `47` status `ready` deltaP `8.1698` edge `7.0142` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2357` n `47` status `ready` deltaP `30.9434` edge `4.0193` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.1172` n `47` status `ready` deltaP `24.782` edge `2.5492` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5963` n `47` status `ready` deltaP `34.5892` edge `1.938` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.3289` n `111` status `ready` deltaP `3.4161` edge `0.9352` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.906` n `47` status `ready` deltaP `35.8045` edge `0.4331` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.587` n `47` status `ready` deltaP `38.8778` edge `0.1469` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.7002` n `47` status `ready` deltaP `30.5962` edge `0.1392` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.7017` n `47` status `ready` deltaP `31.2824` edge `0.032` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.156` n `47` status `ready` deltaP `15.0103` edge `0.1214` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.978` n `47` status `ready` deltaP `9.5355` edge `0.0847` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.9164` n `47` status `ready` deltaP `14.161` edge `0.0098` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9091` n `47` status `ready` deltaP `11.3167` edge `0.0406` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.7302` n `111` status `ready` deltaP `7.9814` edge `0.0987` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4709` n `47` status `ready` deltaP `10.1095` edge `0.0075` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.0299` n `111` status `ready` deltaP `4.0595` edge `0.0066` maxDD `-0.3863`
- `market_context_high->metal_1h` score `0.0219` n `47` status `ready` deltaP `3.4272` edge `0.0116` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0112` n `111` status `ready` deltaP `8.5451` edge `0.0069` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.0559` n `47` status `ready` deltaP `3.2552` edge `0.0554` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.0642` n `111` status `ready` deltaP `2.1161` edge `0.0284` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
