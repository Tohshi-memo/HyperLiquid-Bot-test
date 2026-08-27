# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T07:22:25.071645+00:00`
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

- `news_risk_high->unknown_24h` score `50.4365` n `50` status `ready` deltaP `11.5717` edge `4.1259` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.6944` n `50` status `ready` deltaP `37.6235` edge `1.1845` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.5848` n `50` status `ready` deltaP `26.4695` edge `0.8822` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.3288` n `50` status `ready` deltaP `26.1416` edge `0.3626` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9273` n `50` status `ready` deltaP `45.811` edge `0.0309` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.448` n `50` status `ready` deltaP `40.6598` edge `0.0205` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.4289` n `136` status `ready` deltaP `25.1166` edge `0.159` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.9505` n `50` status `ready` deltaP `31.8687` edge `0.0485` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.8652` n `50` status `ready` deltaP `16.0778` edge `0.1672` maxDD `-0.8495`
- `market_context_high->unknown_1h` score `1.4969` n `136` status `ready` deltaP `13.2837` edge `0.0812` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `1.4318` n `50` status `ready` deltaP `19.3054` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.313` n `50` status `ready` deltaP `17.2635` edge `0.0222` maxDD `-0.2301`
- `market_context_high->unknown_24h` score `1.2757` n `135` status `ready` deltaP `5.6458` edge `0.1419` maxDD `-3.1917`
- `news_risk_high->equity_4h` score `1.2538` n `50` status `ready` deltaP `20.0549` edge `0.0471` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5931` n `50` status `ready` deltaP `15.497` edge `0.004` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1725` n `50` status `ready` deltaP `8.1078` edge `0.002` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0719` n `50` status `ready` deltaP `5.1018` edge `-0.0022` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0687` n `50` status `ready` deltaP `6.4756` edge `0.0022` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.3392` n `50` status `ready` deltaP `5.4817` edge `-0.0117` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.368` n `136` status `ready` deltaP `3.923` edge `-0.0001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
