# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T10:44:15.886916+00:00`
- Price records: `672`
- Market context records: `8188`
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

- `news_risk_high->unknown_24h` score `8586.1311` n `43` status `ready` deltaP `36.9792` edge `715.2644` maxDD `0.0`
- `market_context_high->equity_24h` score `20.1085` n `46` status `ready` deltaP `43.0254` edge `1.4799` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.9759` n `47` status `ready` deltaP `44.976` edge `0.6191` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.7174` n `46` status `ready` deltaP `44.6181` edge `0.429` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8909` n `50` status `ready` deltaP `29.1037` edge `0.4929` maxDD `-1.3479`
- `market_context_high->crypto_alt_24h` score `4.9125` n `46` status `ready` deltaP `11.8886` edge `0.7977` maxDD `-11.7722`
- `market_context_high->index_4h` score `4.2698` n `47` status `ready` deltaP `38.1292` edge `0.1059` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.4383` n `47` status `ready` deltaP `33.7279` edge `0.0812` maxDD `-0.2287`
- `market_context_high->equity_1h` score `3.1751` n `47` status `ready` deltaP `15.9893` edge `0.1769` maxDD `-0.512`
- `news_risk_high->crypto_major_4h` score `3.0712` n `50` status `ready` deltaP `16.2683` edge `0.3484` maxDD `-2.382`
- `news_risk_high->equity_1h` score `2.9322` n `54` status `ready` deltaP `21.9783` edge `0.1287` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.8411` n `50` status `ready` deltaP `24.5122` edge `0.0924` maxDD `-0.191`
- `market_context_high->index_24h` score `2.2485` n `46` status `ready` deltaP `20.237` edge `0.2196` maxDD `-1.2995`
- `news_risk_high->crypto_major_1h` score `1.9733` n `54` status `ready` deltaP `13.4509` edge `0.1145` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8411` n `54` status `ready` deltaP `14.8536` edge `0.0978` maxDD `-1.1388`
- `market_context_high->crypto_major_24h` score `1.6088` n `46` status `ready` deltaP `11.3678` edge `0.5737` maxDD `-27.4584`
- `news_risk_high->crypto_alt_4h` score `1.394` n `50` status `ready` deltaP `16.7256` edge `0.2064` maxDD `-5.8012`
- `market_context_high->fx_24h` score `1.3266` n `46` status `ready` deltaP `25.8756` edge `0.0624` maxDD `-0.5196`
- `news_risk_high->metal_4h` score `1.3128` n `50` status `ready` deltaP `12.4939` edge `0.0729` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2012` n `47` status `ready` deltaP `21.2607` edge `0.0261` maxDD `-0.1069`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
