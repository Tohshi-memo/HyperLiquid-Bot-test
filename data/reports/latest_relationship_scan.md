# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T15:37:28.373520+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11634`

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

- `news_risk_high->unknown_24h` score `53.7661` n `50` status `ready` deltaP `11.6118` edge `4.4031` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.8022` n `50` status `ready` deltaP `43.1404` edge `2.4067` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.0694` n `56` status `ready` deltaP `22.9747` edge `0.7835` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4751` n `50` status `ready` deltaP `30.1005` edge `0.3484` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.3543` n `50` status `ready` deltaP `43.7539` edge `0.0754` maxDD `-0.0053`
- `news_risk_high->crypto_major_24h` score `4.3221` n `50` status `ready` deltaP `21.435` edge `0.2666` maxDD `-2.6128`
- `news_risk_high->fx_4h` score `3.9883` n `56` status `ready` deltaP `46.3632` edge `0.0323` maxDD `-0.0559`
- `market_context_high->metal_24h` score `3.0203` n `122` status `ready` deltaP `27.7211` edge `0.1688` maxDD `-3.1535`
- `market_context_high->unknown_24h` score `2.8916` n `122` status `ready` deltaP `5.0544` edge `0.2805` maxDD `-3.1917`
- `market_context_high->unknown_4h` score `2.6552` n `122` status `ready` deltaP `18.1152` edge `0.1412` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.359` n `50` status `ready` deltaP `26.9948` edge `0.0317` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.0374` n `58` status `ready` deltaP `11.8625` edge `0.1264` maxDD `-0.8558`
- `news_risk_high->fx_1h` score `1.5461` n `58` status `ready` deltaP `20.6897` edge `0.0079` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1823` n `122` status `ready` deltaP `9.0361` edge `0.0833` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.7975` n `56` status `ready` deltaP `19.5993` edge `0.0479` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.6119` n `56` status `ready` deltaP `13.5453` edge `0.0138` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.5703` n `58` status `ready` deltaP `14.9907` edge `0.0052` maxDD `-0.5618`
- `news_risk_high->equity_1h` score `0.4848` n `58` status `ready` deltaP `13.1995` edge `0.0094` maxDD `-0.8191`
- `news_risk_high->metal_1h` score `0.319` n `58` status `ready` deltaP `6.4475` edge `0.0062` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.088` n `56` status `ready` deltaP `7.0993` edge `-0.0001` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
