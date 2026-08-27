# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T07:37:28.514640+00:00`
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

- `news_risk_high->unknown_24h` score `50.4725` n `50` status `ready` deltaP `11.5717` edge `4.1289` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.812` n `50` status `ready` deltaP `37.6235` edge `1.1943` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.5884` n `50` status `ready` deltaP `26.4695` edge `0.8825` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.2706` n `50` status `ready` deltaP `25.9689` edge `0.3589` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9407` n `50` status `ready` deltaP `45.9634` edge `0.031` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.4834` n `50` status `ready` deltaP `40.8325` edge `0.0223` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.4666` n `135` status `ready` deltaP `25.0621` edge `0.1625` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.9295` n `50` status `ready` deltaP `31.696` edge `0.0479` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.8652` n `50` status `ready` deltaP `16.0778` edge `0.1672` maxDD `-0.8495`
- `market_context_high->unknown_1h` score `1.5098` n `135` status `ready` deltaP `13.1148` edge `0.0834` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `1.445` n `50` status `ready` deltaP `19.4551` edge `0.0077` maxDD `-0.0257`
- `market_context_high->unknown_24h` score `1.3142` n `134` status `ready` deltaP `5.6016` edge `0.1454` maxDD `-3.1917`
- `news_risk_high->equity_1h` score `1.2914` n `50` status `ready` deltaP `17.1138` edge `0.0214` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.2442` n `50` status `ready` deltaP `20.0549` edge `0.0463` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.6024` n `50` status `ready` deltaP `15.6467` edge `0.0042` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1639` n `50` status `ready` deltaP `7.9581` edge `0.0019` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0726` n `50` status `ready` deltaP `5.1018` edge `-0.0021` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0687` n `50` status `ready` deltaP `6.4756` edge `0.0022` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.3198` n `50` status `ready` deltaP `5.6341` edge `-0.0111` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3777` n `135` status `ready` deltaP `3.7514` edge `-0.0002` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
