# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T10:37:30.262836+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `44.5542` n `53` status `ready` deltaP `11.6319` edge `3.6353` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.837` n `53` status `ready` deltaP `23.303` edge `0.841` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `8.3563` n `53` status `ready` deltaP `29.907` edge `0.5411` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.0641` n `53` status `ready` deltaP `30.1134` edge `0.481` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0083` n `53` status `ready` deltaP `39.7668` edge `0.0841` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.8085` n `53` status `ready` deltaP `33.8962` edge `0.0215` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7519` n `53` status `ready` deltaP `15.4135` edge `0.1621` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.4701` n `136` status `ready` deltaP `21.6105` edge `0.1026` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7779` n `53` status `ready` deltaP `20.0414` edge `0.0916` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.6976` n `53` status `ready` deltaP `29.1896` edge `-0.0489` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.0902` n `53` status `ready` deltaP `15.3203` edge `0.0057` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0702` n `136` status `ready` deltaP `11.4873` edge `0.0575` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.4895` n `53` status `ready` deltaP `11.2756` edge `-0.0031` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4295` n `53` status `ready` deltaP `12.7754` edge `0.0063` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1705` n `53` status `ready` deltaP `6.9662` edge `0.0075` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0721` n `53` status `ready` deltaP `3.8499` edge `0.0004` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.3935` n `53` status `ready` deltaP `0.1356` edge `-0.0111` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.4174` n `53` status `ready` deltaP `5.1196` edge `-0.0158` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4302` n `136` status `ready` deltaP `2.8619` edge `-0.001` maxDD `-0.8587`
- `news_risk_high->commodity_4h` score `-0.9519` n `53` status `ready` deltaP `-0.7536` edge `0.0063` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
