# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T10:22:32.362561+00:00`
- Price records: `672`
- Market context records: `8186`
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

- `news_risk_high->unknown_24h` score `8606.9235` n `43` status `ready` deltaP `36.9792` edge `716.9971` maxDD `0.0`
- `market_context_high->equity_24h` score `19.9938` n `46` status `ready` deltaP `42.8518` edge `1.4715` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.9529` n `47` status `ready` deltaP `44.8235` edge `0.6182` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.682` n `46` status `ready` deltaP `44.4444` edge `0.4272` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8679` n `50` status `ready` deltaP `28.9512` edge `0.492` maxDD `-1.3479`
- `market_context_high->crypto_alt_24h` score `4.875` n `46` status `ready` deltaP `11.8886` edge `0.7929` maxDD `-11.7722`
- `market_context_high->index_4h` score `4.2564` n `47` status `ready` deltaP `37.9768` edge `0.1058` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.4383` n `47` status `ready` deltaP `33.7279` edge `0.0812` maxDD `-0.2287`
- `market_context_high->equity_1h` score `3.1691` n `47` status `ready` deltaP `15.9893` edge `0.1764` maxDD `-0.512`
- `news_risk_high->crypto_major_4h` score `3.0704` n `50` status `ready` deltaP `16.2683` edge `0.3483` maxDD `-2.382`
- `news_risk_high->equity_1h` score `2.9262` n `54` status `ready` deltaP `21.9783` edge `0.1282` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.8277` n `50` status `ready` deltaP `24.3598` edge `0.0923` maxDD `-0.191`
- `market_context_high->index_24h` score `2.2368` n `46` status `ready` deltaP `20.237` edge `0.2181` maxDD `-1.2995`
- `news_risk_high->crypto_major_1h` score `1.9757` n `54` status `ready` deltaP `13.4509` edge `0.1147` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8423` n `54` status `ready` deltaP `14.8536` edge `0.0979` maxDD `-1.1388`
- `market_context_high->crypto_major_24h` score `1.5807` n `46` status `ready` deltaP `11.3678` edge `0.5701` maxDD `-27.4584`
- `news_risk_high->crypto_alt_4h` score `1.3933` n `50` status `ready` deltaP `16.7256` edge `0.2063` maxDD `-5.8012`
- `market_context_high->fx_24h` score `1.3243` n `46` status `ready` deltaP `25.8756` edge `0.0621` maxDD `-0.5196`
- `news_risk_high->metal_4h` score `1.3128` n `50` status `ready` deltaP `12.4939` edge `0.0729` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.1926` n `47` status `ready` deltaP `21.111` edge `0.026` maxDD `-0.1069`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
