# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T07:37:27.414947+00:00`
- Price records: `672`
- Market context records: `8174`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8805.385` n `42` status `ready` deltaP `37.1528` edge `733.5344` maxDD `0.0`
- `market_context_high->equity_24h` score `18.9291` n `56` status `ready` deltaP `44.0476` edge `1.3748` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.2309` n `57` status `ready` deltaP `38.0269` edge `0.5392` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.3813` n `46` status `ready` deltaP `31.5814` edge `0.5169` maxDD `-1.3202`
- `market_context_high->metal_24h` score `8.1584` n `56` status `ready` deltaP `42.5347` edge `0.3963` maxDD `0.0`
- `market_context_high->index_4h` score `4.0598` n `57` status `ready` deltaP `36.8849` edge `0.0967` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.4286` n `57` status `ready` deltaP `19.0855` edge `0.1788` maxDD `-0.6254`
- `news_risk_high->crypto_major_4h` score `3.3765` n `46` status `ready` deltaP `18.7235` edge `0.3686` maxDD `-2.1767`
- `news_risk_high->equity_1h` score `3.37` n `50` status `ready` deltaP `25.1557` edge `0.144` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6868` n `46` status `ready` deltaP `22.1633` edge `0.0952` maxDD `-0.191`
- `market_context_high->index_1h` score `1.9267` n `57` status `ready` deltaP `22.2292` edge `0.0262` maxDD `-0.1069`
- `news_risk_high->crypto_major_1h` score `1.8247` n `50` status `ready` deltaP `11.4431` edge `0.1155` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.814` n `46` status `ready` deltaP `16.9737` edge `0.0848` maxDD `-0.7433`
- `market_context_high->index_24h` score `1.7475` n `56` status `ready` deltaP `14.9801` edge `0.1912` maxDD `-1.3621`
- `news_risk_high->crypto_alt_1h` score `1.5981` n `50` status `ready` deltaP `12.0419` edge `0.0963` maxDD `-1.1388`
- `market_context_high->metal_4h` score `1.4758` n `57` status `ready` deltaP `19.3383` edge `0.0563` maxDD `-0.979`
- `news_risk_high->crypto_alt_4h` score `1.3514` n `46` status `ready` deltaP `15.2903` edge `0.2105` maxDD `-5.8012`
- `market_context_high->crypto_alt_24h` score `1.003` n `56` status `ready` deltaP `3.3482` edge `0.5218` maxDD `-21.9091`
- `market_context_high->fx_24h` score `0.7909` n `56` status `ready` deltaP `17.7828` edge `0.0532` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `0.6518` n `56` status `ready` deltaP `25.4712` edge `0.2023` maxDD `-15.7497`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
