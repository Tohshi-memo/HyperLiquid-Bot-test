# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T11:37:25.223911+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `news_risk_high->unknown_24h` score `51.1397` n `50` status `ready` deltaP `11.5717` edge `4.1845` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.5904` n `50` status `ready` deltaP `37.6235` edge `1.3425` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6448` n `50` status `ready` deltaP `26.4695` edge `0.8872` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.7113` n `50` status `ready` deltaP `25.6235` edge `0.3146` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.1017` n `50` status `ready` deltaP `43.5959` edge `0.0554` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0612` n `50` status `ready` deltaP `47.3354` edge `0.0319` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.613` n `129` status `ready` deltaP `24.7176` edge `0.177` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9263` n `50` status `ready` deltaP `16.6766` edge `0.1683` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.7056` n `50` status `ready` deltaP `30.1416` edge `0.0396` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.7154` n `128` status `ready` deltaP `5.3217` edge `0.1807` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5707` n `50` status `ready` deltaP `20.9521` edge `0.0082` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.2771` n `139` status `ready` deltaP `11.4967` edge `0.0748` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `1.1822` n `50` status `ready` deltaP `16.8144` edge `0.0143` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `0.5991` n `50` status `ready` deltaP `17.6159` edge `0.0088` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5946` n `50` status `ready` deltaP `15.497` edge `0.0042` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1398` n `50` status `ready` deltaP `7.6587` edge `0.0008` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0921` n `50` status `ready` deltaP `5.4012` edge `-0.0016` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.1695` n `50` status `ready` deltaP `4.189` edge `-0.0024` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2082` n `50` status `ready` deltaP `6.5488` edge `-0.0079` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.5415` n `139` status `ready` deltaP `0.7507` edge `-0.0012` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
