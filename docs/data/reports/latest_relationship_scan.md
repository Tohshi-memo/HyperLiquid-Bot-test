# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T10:52:36.730453+00:00`
- Price records: `672`
- Market context records: `8189`
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

- `news_risk_high->unknown_24h` score `8565.3687` n `43` status `ready` deltaP `36.9792` edge `713.5342` maxDD `0.0`
- `market_context_high->equity_24h` score `20.2187` n `45` status `ready` deltaP `42.8125` edge `1.4905` maxDD `-4.9489`
- `market_context_high->equity_4h` score `11.0228` n `46` status `ready` deltaP `45.0822` edge `0.6223` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.7565` n `45` status `ready` deltaP `44.7917` edge `0.4311` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.9163` n `50` status `ready` deltaP `29.2561` edge `0.494` maxDD `-1.3479`
- `market_context_high->crypto_alt_24h` score `5.2904` n `45` status `ready` deltaP `12.9514` edge `0.8251` maxDD `-10.9882`
- `market_context_high->index_4h` score `4.2913` n `46` status `ready` deltaP `38.1429` edge `0.1076` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.6561` n `46` status `ready` deltaP `35.6243` edge `0.0853` maxDD `-0.1165`
- `market_context_high->equity_1h` score `3.4177` n `46` status `ready` deltaP `17.4694` edge `0.1846` maxDD `-0.3004`
- `news_risk_high->crypto_major_4h` score `3.0751` n `50` status `ready` deltaP `16.2683` edge `0.3489` maxDD `-2.382`
- `news_risk_high->equity_1h` score `2.9334` n `54` status `ready` deltaP `21.9783` edge `0.1288` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.8545` n `50` status `ready` deltaP `24.6646` edge `0.0925` maxDD `-0.191`
- `market_context_high->index_24h` score `2.3372` n `45` status `ready` deltaP `21.4931` edge `0.2226` maxDD `-1.2995`
- `market_context_high->crypto_major_24h` score `2.1565` n `45` status `ready` deltaP `12.4306` edge `0.6135` maxDD `-25.9252`
- `news_risk_high->crypto_major_1h` score `1.9697` n `54` status `ready` deltaP `13.4509` edge `0.1142` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8375` n `54` status `ready` deltaP `14.8536` edge `0.0975` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.3964` n `50` status `ready` deltaP `16.7256` edge `0.2067` maxDD `-5.8012`
- `market_context_high->fx_24h` score `1.3964` n `45` status `ready` deltaP `27.0834` edge `0.0633` maxDD `-0.5196`
- `news_risk_high->metal_4h` score `1.314` n `50` status `ready` deltaP `12.4939` edge `0.073` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2845` n `46` status `ready` deltaP `22.787` edge `0.0266` maxDD `-0.1069`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
