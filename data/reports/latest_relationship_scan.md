# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T08:37:29.664224+00:00`
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

- `news_risk_high->unknown_24h` score `50.6321` n `50` status `ready` deltaP `11.5717` edge `4.1422` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.2944` n `50` status `ready` deltaP `37.6235` edge `1.2345` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6052` n `50` status `ready` deltaP `26.4695` edge `0.8839` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.0797` n `50` status `ready` deltaP `25.6235` edge `0.3453` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9833` n `50` status `ready` deltaP `46.4207` edge `0.0315` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.6299` n `50` status `ready` deltaP `41.5233` edge `0.0299` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.5385` n `131` status `ready` deltaP `24.8359` edge `0.17` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.8628` n `50` status `ready` deltaP `16.0778` edge `0.167` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.8467` n `50` status `ready` deltaP `31.0052` edge `0.0456` maxDD `-0.2064`
- `market_context_high->unknown_1h` score `1.5508` n `132` status `ready` deltaP `12.593` edge `0.0903` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `1.4953` n `50` status `ready` deltaP `20.0539` edge `0.0079` maxDD `-0.0257`
- `market_context_high->unknown_24h` score `1.4195` n `130` status `ready` deltaP `5.4179` edge `0.1554` maxDD `-3.1917`
- `news_risk_high->equity_1h` score `1.1811` n `50` status `ready` deltaP `16.515` edge `0.0162` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.1055` n `50` status `ready` deltaP `19.4451` edge `0.0388` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.6032` n `50` status `ready` deltaP `15.6467` edge `0.0043` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1273` n `50` status `ready` deltaP `7.3593` edge `0.0012` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0913` n `50` status `ready` deltaP `5.4012` edge `-0.0017` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0213` n `50` status `ready` deltaP `6.0183` edge `0.0013` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2676` n `50` status `ready` deltaP `6.0915` edge `-0.0098` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4439` n `132` status `ready` deltaP `2.5994` edge `-0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
