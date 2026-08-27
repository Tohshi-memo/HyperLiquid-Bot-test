# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T19:37:34.888037+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14777`

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

- `news_risk_high->unknown_24h` score `52.1514` n `50` status `ready` deltaP `11.6319` edge `4.2684` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.8574` n `50` status `ready` deltaP `37.8403` edge `1.6133` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.9242` n `50` status `ready` deltaP `26.3171` edge `0.9115` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.8244` n `50` status `ready` deltaP `46.0903` edge `0.099` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.5163` n `50` status `ready` deltaP `25.8403` edge `0.2969` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9711` n `50` status `ready` deltaP `46.2683` edge `0.0315` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.0295` n `50` status `ready` deltaP `16.8263` edge `0.1759` maxDD `-0.8495`
- `market_context_high->unknown_24h` score `2.727` n `128` status `ready` deltaP `5.3819` edge `0.2646` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.6299` n `50` status `ready` deltaP `29.8403` edge `0.0353` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.4811` n `148` status `ready` deltaP `19.4793` edge `0.1176` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5456` n `50` status `ready` deltaP `20.6527` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1511` n `50` status `ready` deltaP `16.6647` edge `0.0127` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.9061` n `148` status `ready` deltaP `9.1236` edge `0.0597` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.8397` n `50` status `ready` deltaP `18.9878` edge `0.0197` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.53` n `50` status `ready` deltaP `14.5988` edge `0.0019` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.139` n `50` status `ready` deltaP `7.6587` edge `0.0007` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0617` n `50` status `ready` deltaP `4.8024` edge `-0.0015` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1111` n `50` status `ready` deltaP `7.4634` edge `-0.0059` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1427` n `50` status `ready` deltaP `4.4939` edge `-0.0022` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4534` n `148` status `ready` deltaP `6.3283` edge `-0.0086` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
