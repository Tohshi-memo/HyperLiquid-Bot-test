# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T15:07:31.644917+00:00`
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

- `news_risk_high->unknown_24h` score `53.7193` n `50` status `ready` deltaP `11.6118` edge `4.3992` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.7025` n `50` status `ready` deltaP `42.7938` edge `2.4007` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.039` n `56` status `ready` deltaP `22.6698` edge `0.783` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4523` n `50` status `ready` deltaP `30.1005` edge `0.3465` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.4108` n `50` status `ready` deltaP `44.1005` edge `0.0778` maxDD `-0.0053`
- `news_risk_high->crypto_major_24h` score `4.1336` n `50` status `ready` deltaP `21.0884` edge `0.2532` maxDD `-2.6128`
- `news_risk_high->fx_4h` score `3.9615` n `56` status `ready` deltaP `46.0583` edge `0.0321` maxDD `-0.0559`
- `market_context_high->metal_24h` score `2.9146` n `124` status `ready` deltaP `26.7457` edge `0.1665` maxDD `-3.1535`
- `market_context_high->unknown_24h` score `2.6961` n `124` status `ready` deltaP `5.1602` edge `0.2635` maxDD `-3.1917`
- `market_context_high->unknown_4h` score `2.5489` n `124` status `ready` deltaP `18.0615` edge `0.1327` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3777` n `50` status `ready` deltaP `27.1681` edge `0.0321` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.224` n `56` status `ready` deltaP `12.7246` edge `0.1362` maxDD `-0.8558`
- `news_risk_high->fx_1h` score `1.4684` n `56` status `ready` deltaP `19.7926` edge `0.0074` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0876` n `124` status `ready` deltaP `8.6923` edge `0.0777` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `1.0476` n `56` status `ready` deltaP `15.3016` edge `0.0158` maxDD `-0.4409`
- `news_risk_high->equity_4h` score `0.7677` n `56` status `ready` deltaP `19.2945` edge `0.0461` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.5973` n `56` status `ready` deltaP `13.3929` edge `0.0136` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.489` n `56` status `ready` deltaP `13.6976` edge `0.0034` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3267` n `56` status `ready` deltaP `6.6938` edge `0.0052` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0892` n `56` status `ready` deltaP `7.0993` edge `0.0` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
