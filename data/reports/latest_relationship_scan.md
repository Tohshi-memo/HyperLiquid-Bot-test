# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T12:22:26.744688+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11609`

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

- `news_risk_high->unknown_24h` score `53.5225` n `50` status `ready` deltaP `11.6118` edge `4.3828` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.9643` n `50` status `ready` deltaP `40.8873` edge `2.3519` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.213` n `52` status `ready` deltaP `24.6248` edge `0.8678` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4547` n `50` status `ready` deltaP `30.1005` edge `0.3467` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.7722` n `50` status `ready` deltaP `46.0069` edge `0.0952` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9211` n `52` status `ready` deltaP `45.5089` edge `0.0324` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `3.0337` n `50` status `ready` deltaP `19.3553` edge `0.1731` maxDD `-2.6128`
- `news_risk_high->index_24h` score `2.5511` n `50` status `ready` deltaP `28.9012` edge `0.035` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3798` n `135` status `ready` deltaP `18.243` edge `0.1174` maxDD `-0.5894`
- `market_context_high->metal_24h` score `2.2931` n `133` status `ready` deltaP `21.6911` edge `0.1484` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.1088` n `56` status `ready` deltaP `12.4251` edge `0.1286` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `1.9438` n `133` status `ready` deltaP `5.5968` edge `0.1979` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.4684` n `56` status `ready` deltaP `19.7926` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1135` n `56` status `ready` deltaP `15.601` edge `0.0193` maxDD `-0.4409`
- `news_risk_high->equity_4h` score `0.9497` n `52` status `ready` deltaP `21.4001` edge `0.0554` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.9482` n `135` status `ready` deltaP `7.0547` edge `0.077` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.4999` n `56` status `ready` deltaP `13.8473` edge `0.0038` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3794` n `56` status `ready` deltaP `7.2926` edge `0.0056` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.2725` n `52` status `ready` deltaP `11.0577` edge `0.0021` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.0587` n `56` status `ready` deltaP `6.0843` edge `0.0009` maxDD `-0.0486`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
