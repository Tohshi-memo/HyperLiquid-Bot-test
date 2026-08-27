# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T07:52:27.646408+00:00`
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

- `news_risk_high->unknown_24h` score `50.5121` n `50` status `ready` deltaP `11.5717` edge `4.1322` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.9344` n `50` status `ready` deltaP `37.6235` edge `1.2045` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.5884` n `50` status `ready` deltaP `26.4695` edge `0.8825` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.2171` n `50` status `ready` deltaP `25.7962` edge `0.3556` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9541` n `50` status `ready` deltaP `46.1159` edge `0.0311` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.52` n `50` status `ready` deltaP `41.0052` edge `0.0242` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.5005` n `134` status `ready` deltaP `25.0068` edge `0.1657` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.9085` n `50` status `ready` deltaP `31.5233` edge `0.0473` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.8664` n `50` status `ready` deltaP `16.0778` edge `0.1673` maxDD `-0.8495`
- `market_context_high->unknown_1h` score `1.5213` n `134` status `ready` deltaP `12.9435` edge `0.0855` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `1.4569` n `50` status `ready` deltaP `19.6048` edge `0.0077` maxDD `-0.0257`
- `market_context_high->unknown_24h` score `1.3454` n `133` status `ready` deltaP `5.5567` edge `0.1483` maxDD `-3.1917`
- `news_risk_high->equity_1h` score `1.2698` n `50` status `ready` deltaP `16.9641` edge `0.0206` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.2176` n `50` status `ready` deltaP `19.9024` edge `0.0451` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.6024` n `50` status `ready` deltaP `15.6467` edge `0.0042` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1553` n `50` status `ready` deltaP `7.8084` edge `0.0018` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.082` n `50` status `ready` deltaP `5.2515` edge `-0.0019` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0675` n `50` status `ready` deltaP `6.4756` edge `0.0021` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.3028` n `50` status `ready` deltaP `5.7866` edge `-0.0107` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3892` n `134` status `ready` deltaP `3.5749` edge `-0.0005` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
