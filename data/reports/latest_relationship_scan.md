# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T11:52:27.949247+00:00`
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

- `news_risk_high->unknown_24h` score `53.4853` n `50` status `ready` deltaP `11.6118` edge `4.3797` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.8694` n `50` status `ready` deltaP `40.5407` edge `2.3463` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.213` n `52` status `ready` deltaP `24.6248` edge `0.8678` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4583` n `50` status `ready` deltaP `30.1005` edge `0.347` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.8395` n `50` status `ready` deltaP `46.3536` edge `0.0985` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9467` n `52` status `ready` deltaP `45.8138` edge `0.0325` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `2.9202` n `50` status `ready` deltaP `19.182` edge `0.1648` maxDD `-2.6128`
- `news_risk_high->index_24h` score `2.5547` n `50` status `ready` deltaP `28.9012` edge `0.0353` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3219` n `137` status `ready` deltaP `18.4485` edge `0.1112` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.11` n `56` status `ready` deltaP `12.4251` edge `0.1287` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `2.0686` n `133` status `ready` deltaP `5.5968` edge `0.2083` maxDD `-3.1917`
- `market_context_high->metal_24h` score `1.9697` n `133` status `ready` deltaP `20.5341` edge `0.1375` maxDD `-3.1535`
- `news_risk_high->fx_1h` score `1.4432` n `56` status `ready` deltaP `19.4932` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0992` n `56` status `ready` deltaP `15.4513` edge `0.0191` maxDD `-0.4409`
- `news_risk_high->equity_4h` score `0.9709` n `52` status `ready` deltaP `21.5525` edge `0.0571` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.944` n `137` status `ready` deltaP `7.4981` edge `0.0737` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.489` n `56` status `ready` deltaP `13.6976` edge `0.0034` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3938` n `56` status `ready` deltaP `7.4423` edge `0.0058` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.3065` n `52` status `ready` deltaP `11.3626` edge `0.0029` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.0587` n `56` status `ready` deltaP `6.0843` edge `0.0009` maxDD `-0.0486`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
