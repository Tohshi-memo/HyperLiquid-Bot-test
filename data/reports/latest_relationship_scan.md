# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T13:22:29.565116+00:00`
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

- `news_risk_high->unknown_24h` score `51.4193` n `50` status `ready` deltaP `11.5717` edge `4.2078` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.4568` n `50` status `ready` deltaP `37.6235` edge `1.4147` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6374` n `50` status `ready` deltaP `26.3171` edge `0.8876` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.6117` n `50` status `ready` deltaP `25.6235` edge `0.3063` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.3952` n `50` status `ready` deltaP `44.8048` edge `0.0718` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0223` n `50` status `ready` deltaP `46.878` edge `0.0317` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.2858` n `134` status `ready` deltaP `24.1081` edge `0.1538` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9802` n `50` status `ready` deltaP `17.1257` edge `0.1698` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6864` n `50` status `ready` deltaP `30.1416` edge `0.038` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.995` n `128` status `ready` deltaP `5.3217` edge `0.204` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5551` n `50` status `ready` deltaP `20.8024` edge `0.0079` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.199` n `50` status `ready` deltaP `17.2635` edge `0.0127` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `1.0008` n `146` status `ready` deltaP `10.4134` edge `0.059` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.6029` n `50` status `ready` deltaP `17.7683` edge `0.0081` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.572` n `50` status `ready` deltaP `15.1976` edge `0.0033` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1538` n `50` status `ready` deltaP `7.9581` edge `0.0006` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.11` n `50` status `ready` deltaP `5.7006` edge `-0.0013` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0653` n `50` status `ready` deltaP `7.6159` edge `-0.0031` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1281` n `50` status `ready` deltaP `4.6463` edge `-0.002` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.5329` n `146` status `ready` deltaP `0.8572` edge `-0.0008` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
