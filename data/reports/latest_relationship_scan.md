# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T11:37:26.530455+00:00`
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

- `news_risk_high->unknown_24h` score `53.4685` n `50` status `ready` deltaP `11.6118` edge `4.3783` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.8268` n `50` status `ready` deltaP `40.3674` edge `2.3439` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.4745` n `51` status `ready` deltaP `24.474` edge `0.8906` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4619` n `50` status `ready` deltaP `30.1005` edge `0.3473` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.8702` n `50` status `ready` deltaP `46.5269` edge `0.0999` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.942` n `51` status `ready` deltaP `45.8154` edge `0.0321` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `2.8746` n `50` status `ready` deltaP `19.182` edge `0.161` maxDD `-2.6128`
- `news_risk_high->index_24h` score `2.5571` n `50` status `ready` deltaP `28.9012` edge `0.0355` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2975` n `138` status `ready` deltaP `18.549` edge `0.1085` maxDD `-0.5894`
- `market_context_high->unknown_24h` score `2.1262` n `133` status `ready` deltaP `5.5968` edge `0.2131` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.11` n `56` status `ready` deltaP `12.4251` edge `0.1287` maxDD `-0.8558`
- `market_context_high->metal_24h` score `1.8158` n `133` status `ready` deltaP `19.9555` edge `0.1327` maxDD `-3.1535`
- `news_risk_high->equity_4h` score `1.6695` n `51` status `ready` deltaP `22.9854` edge `0.0622` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.4432` n `56` status `ready` deltaP `19.4932` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.098` n `56` status `ready` deltaP `15.4513` edge `0.019` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.9494` n `138` status `ready` deltaP `7.715` edge `0.0727` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.4875` n `56` status `ready` deltaP `13.6976` edge `0.0032` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3938` n `56` status `ready` deltaP `7.4423` edge `0.0058` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.2398` n `51` status `ready` deltaP `10.874` edge `0.0006` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.0579` n `56` status `ready` deltaP `6.0843` edge `0.0008` maxDD `-0.0486`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
