# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T23:01:23.911424+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `1.0689` n `145` status `ready` deltaP `20.4064` edge `0.0338` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.8061` n `176` status `ready` deltaP `11.225` edge `0.0638` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6164` n `180` status `ready` deltaP `8.4997` edge `0.029` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0466` n `176` status `ready` deltaP `7.3032` edge `0.0074` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.0723` n `180` status `ready` deltaP `5.3393` edge `0.0003` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.9843` n `145` status `ready` deltaP `-3.428` edge `0.0558` maxDD `-6.0641`
- `market_context_high->index_4h` score `-1.1166` n `176` status `ready` deltaP `-6.2084` edge `-0.0163` maxDD `-1.5035`
- `market_context_high->index_1h` score `-1.1798` n `180` status `ready` deltaP `-6.67` edge `-0.0052` maxDD `-0.892`
- `market_context_high->metal_1h` score `-1.2203` n `180` status `ready` deltaP `-4.4078` edge `-0.0087` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-1.2414` n `145` status `ready` deltaP `2.5482` edge `0.012` maxDD `-2.9283`
- `market_context_high->equity_1h` score `-1.2547` n `180` status `ready` deltaP `-5.2428` edge `-0.0187` maxDD `-6.2436`
- `market_context_high->crypto_alt_1h` score `-2.8992` n `180` status `ready` deltaP `-11.5436` edge `-0.0449` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.084` n `176` status `ready` deltaP `-6.7212` edge `-0.0358` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.8156` n `180` status `ready` deltaP `-10.642` edge `-0.0566` maxDD `-11.9002`
- `market_context_high->equity_24h` score `-4.188` n `145` status `ready` deltaP `-3.2726` edge `0.0533` maxDD `-34.8054`
- `market_context_high->equity_4h` score `-4.2484` n `176` status `ready` deltaP `-15.3409` edge `-0.1406` maxDD `-15.1433`
- `market_context_high->crypto_major_24h` score `-4.6349` n `145` status `ready` deltaP `-6.0133` edge `-0.1271` maxDD `-25.8289`
- `market_context_high->commodity_24h` score `-5.7038` n `145` status `ready` deltaP `1.0638` edge `-0.0538` maxDD `-41.0973`
- `market_context_high->crypto_alt_4h` score `-7.0906` n `176` status `ready` deltaP `-15.3825` edge `-0.1581` maxDD `-19.7517`
- `market_context_high->crypto_alt_24h` score `-7.8722` n `145` status `ready` deltaP `-12.8226` edge `-0.2149` maxDD `-21.7842`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
