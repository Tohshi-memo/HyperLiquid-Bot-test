# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T05:22:32.976370+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14779`

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

- `news_risk_high->unknown_24h` score `50.0357` n `50` status `ready` deltaP `11.5717` edge `4.0925` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.645` n `50` status `ready` deltaP `37.1054` edge `1.1005` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.384` n `50` status `ready` deltaP `26.1646` edge `0.8675` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.7141` n `50` status `ready` deltaP `27.5233` edge `0.3855` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8945` n `50` status `ready` deltaP `45.5061` edge `0.0302` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.2048` n `137` status `ready` deltaP `24.8653` edge `0.142` maxDD `-0.5894`
- `news_risk_high->metal_24h` score `3.1863` n `50` status `ready` deltaP `39.2781` edge `0.0079` maxDD `-0.0053`
- `news_risk_high->index_24h` score `3.1079` n `50` status `ready` deltaP `33.2504` edge `0.0524` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.7488` n `50` status `ready` deltaP `16.0778` edge `0.1575` maxDD `-0.8495`
- `news_risk_high->fx_1h` score `1.4557` n `50` status `ready` deltaP `19.6048` edge `0.0076` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.377` n `137` status `ready` deltaP `13.4501` edge `0.0701` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `1.3154` n `50` status `ready` deltaP `17.2635` edge `0.0224` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.2958` n `50` status `ready` deltaP `20.0549` edge `0.0506` maxDD `-2.105`
- `market_context_high->unknown_24h` score `0.8916` n `136` status `ready` deltaP `5.6893` edge `0.1096` maxDD `-3.1917`
- `news_risk_high->commodity_1h` score `0.5175` n `50` status `ready` deltaP `14.2994` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1639` n `50` status `ready` deltaP `7.9581` edge `0.0019` maxDD `-0.0486`
- `news_risk_high->index_4h` score `0.0699` n `50` status `ready` deltaP `6.4756` edge `0.0023` maxDD `-0.1719`
- `news_risk_high->metal_1h` score `0.0524` n `50` status `ready` deltaP `4.8024` edge `-0.0027` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.3329` n `137` status `ready` deltaP `4.5391` edge `0.0003` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.4022` n `50` status `ready` deltaP `5.0244` edge `-0.0139` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
