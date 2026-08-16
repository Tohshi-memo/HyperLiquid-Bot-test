# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T19:37:26.395018+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11830`

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

- `market_context_high->unknown_24h` score `217.2406` n `85` status `ready` deltaP `-23.6376` edge `28.2773` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.7973` n `85` status `ready` deltaP `41.2235` edge `0.3807` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.3527` n `122` status `ready` deltaP `13.4596` edge `0.0701` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0814` n `125` status `ready` deltaP `2.2575` edge `0.0193` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.2708` n `122` status `ready` deltaP `4.7106` edge `0.0065` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.2797` n `125` status `ready` deltaP `1.7521` edge `0.0015` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5043` n `125` status `ready` deltaP `1.9533` edge `-0.0061` maxDD `-1.7257`
- `market_context_high->metal_4h` score `-0.7467` n `122` status `ready` deltaP `8.9789` edge `-0.0107` maxDD `-4.5909`
- `market_context_high->index_1h` score `-0.7885` n `125` status `ready` deltaP `-6.8886` edge `-0.003` maxDD `-0.5064`
- `market_context_high->fx_24h` score `-1.3886` n `85` status `ready` deltaP `-6.8975` edge `0.0287` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6565` n `125` status `ready` deltaP `-9.4335` edge `-0.0455` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.917` n `85` status `ready` deltaP `-9.7324` edge `0.0703` maxDD `-7.0954`
- `market_context_high->index_24h` score `-1.928` n `85` status `ready` deltaP `-6.3787` edge `-0.0665` maxDD `-2.0524`
- `market_context_high->index_4h` score `-1.9313` n `122` status `ready` deltaP `-10.8232` edge `-0.0079` maxDD `-0.8045`
- `market_context_high->crypto_alt_1h` score `-2.0829` n `125` status `ready` deltaP `-2.7485` edge `-0.0213` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-2.2049` n `125` status `ready` deltaP `-6.4491` edge `-0.0341` maxDD `-5.5318`
- `market_context_high->crypto_major_4h` score `-3.5293` n `122` status `ready` deltaP `-1.7917` edge `-0.0641` maxDD `-12.4452`
- `market_context_high->crypto_major_24h` score `-4.3344` n `85` status `ready` deltaP `-5.7762` edge `0.0061` maxDD `-31.1961`
- `market_context_high->unknown_1h` score `-6.8747` n `125` status `ready` deltaP `1.8036` edge `-0.5452` maxDD `-0.8437`
- `market_context_high->crypto_alt_4h` score `-7.8932` n `122` status `ready` deltaP `-10.7132` edge `-0.1012` maxDD `-26.1449`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
