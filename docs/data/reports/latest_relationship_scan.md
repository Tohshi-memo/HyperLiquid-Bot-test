# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T14:37:30.366659+00:00`
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

- `news_risk_high->unknown_24h` score `53.6989` n `50` status `ready` deltaP `11.6118` edge `4.3975` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.5967` n `50` status `ready` deltaP `42.4471` edge `2.3942` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.0074` n `56` status `ready` deltaP `22.365` edge `0.7824` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4499` n `50` status `ready` deltaP `30.1005` edge `0.3463` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.4722` n `50` status `ready` deltaP `44.4471` edge `0.0806` maxDD `-0.0053`
- `news_risk_high->crypto_major_24h` score `3.945` n `50` status `ready` deltaP `20.7418` edge `0.2398` maxDD `-2.6128`
- `news_risk_high->fx_4h` score `3.9347` n `56` status `ready` deltaP `45.7534` edge `0.0319` maxDD `-0.0559`
- `market_context_high->metal_24h` score `2.822` n `126` status `ready` deltaP `25.8122` edge `0.165` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.4396` n `126` status `ready` deltaP `17.9999` edge `0.124` maxDD `-0.5894`
- `market_context_high->unknown_24h` score `2.4247` n `126` status `ready` deltaP `5.2626` edge `0.2402` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.4126` n `50` status `ready` deltaP `27.5147` edge `0.0327` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.2576` n `56` status `ready` deltaP `13.024` edge `0.137` maxDD `-0.8558`
- `news_risk_high->fx_1h` score `1.4935` n `56` status `ready` deltaP `20.092` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0836` n `56` status `ready` deltaP `15.4513` edge `0.0178` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.9518` n `126` status `ready` deltaP `7.8653` edge `0.0719` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.7677` n `56` status `ready` deltaP `19.2945` edge `0.0461` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.5985` n `56` status `ready` deltaP `13.3929` edge `0.0137` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.4991` n `56` status `ready` deltaP `13.8473` edge `0.0037` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3435` n `56` status `ready` deltaP `6.8435` edge `0.0056` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0928` n `56` status `ready` deltaP `7.0993` edge `0.0003` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
