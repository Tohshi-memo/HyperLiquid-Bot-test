# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T08:52:25.180788+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14747`

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

- `news_risk_high->unknown_24h` score `50.6729` n `50` status `ready` deltaP `11.5717` edge `4.1456` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.4096` n `50` status `ready` deltaP `37.6235` edge `1.2441` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6052` n `50` status `ready` deltaP `26.4695` edge `0.8839` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.0389` n `50` status `ready` deltaP `25.6235` edge `0.3419` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9967` n `50` status `ready` deltaP `46.5732` edge `0.0316` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.6665` n `50` status `ready` deltaP `41.696` edge `0.0318` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.5746` n `130` status `ready` deltaP `24.7772` edge `0.1734` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.8616` n `50` status `ready` deltaP `16.0778` edge `0.1669` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.8256` n `50` status `ready` deltaP `30.8325` edge `0.045` maxDD `-0.2064`
- `market_context_high->unknown_1h` score `1.5544` n `132` status `ready` deltaP `12.593` edge `0.0906` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `1.5084` n `50` status `ready` deltaP `20.2036` edge `0.008` maxDD `-0.0257`
- `market_context_high->unknown_24h` score `1.4445` n `129` status `ready` deltaP `5.3701` edge `0.1578` maxDD `-3.1917`
- `news_risk_high->equity_1h` score `1.1559` n `50` status `ready` deltaP `16.3653` edge `0.0151` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.0573` n `50` status `ready` deltaP `19.2927` edge `0.0358` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.6047` n `50` status `ready` deltaP `15.6467` edge `0.0045` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.118` n `50` status `ready` deltaP `7.2096` edge `0.001` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0835` n `50` status `ready` deltaP `5.2515` edge `-0.0017` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0031` n `50` status `ready` deltaP `5.8659` edge `0.0008` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2688` n `50` status `ready` deltaP `6.0915` edge `-0.0099` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.477` n `132` status `ready` deltaP `1.9915` edge `-0.0012` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
