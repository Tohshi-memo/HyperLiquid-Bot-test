# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T08:07:26.849873+00:00`
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

- `news_risk_high->unknown_24h` score `50.5505` n `50` status `ready` deltaP `11.5717` edge `4.1354` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.0508` n `50` status `ready` deltaP `37.6235` edge `1.2142` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.5896` n `50` status `ready` deltaP `26.4695` edge `0.8826` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.1625` n `50` status `ready` deltaP `25.6235` edge `0.3522` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9553` n `50` status `ready` deltaP `46.1159` edge `0.0312` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.5566` n `50` status `ready` deltaP `41.1779` edge `0.0261` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.538` n `133` status `ready` deltaP `24.9507` edge `0.1692` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.8875` n `50` status `ready` deltaP `31.3506` edge `0.0467` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.8652` n `50` status `ready` deltaP `16.0778` edge `0.1672` maxDD `-0.8495`
- `market_context_high->unknown_1h` score `1.5337` n `133` status `ready` deltaP `12.7695` edge `0.0877` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `1.4701` n `50` status `ready` deltaP `19.7545` edge `0.0078` maxDD `-0.0257`
- `market_context_high->unknown_24h` score `1.3741` n `132` status `ready` deltaP `5.5111` edge `0.151` maxDD `-3.1917`
- `news_risk_high->equity_1h` score `1.2422` n `50` status `ready` deltaP `16.8144` edge `0.0193` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.1839` n `50` status `ready` deltaP `19.75` edge `0.0433` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.6016` n `50` status `ready` deltaP `15.6467` edge `0.0041` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.146` n `50` status `ready` deltaP `7.6587` edge `0.0016` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0913` n `50` status `ready` deltaP `5.4012` edge `-0.0017` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0529` n `50` status `ready` deltaP `6.3232` edge `0.0019` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2858` n `50` status `ready` deltaP `5.939` edge `-0.0103` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3987` n `133` status `ready` deltaP `3.3936` edge `-0.0005` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
