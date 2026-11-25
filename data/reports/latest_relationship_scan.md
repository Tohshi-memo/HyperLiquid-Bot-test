# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T23:52:30.568102+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3911`

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

- `market_context_high->unknown_1h` score `32148.6158` n `45` status `ready` deltaP `1.5668` edge `2679.0503` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21799.6594` n `45` status `ready` deltaP `1.958` edge `1816.6391` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `913.6608` n `31` status `ready` deltaP `1.7819` edge `76.1441` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `546.7119` n `31` status `ready` deltaP `3.1766` edge `45.5438` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `224.7685` n `31` status `ready` deltaP `6.0764` edge `18.6902` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.5768` n `31` status `ready` deltaP `51.9097` edge `3.452` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.9003` n `31` status `ready` deltaP `52.6042` edge `3.141` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.2099` n `31` status `ready` deltaP `52.0833` edge `2.7536` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.4312` n `31` status `ready` deltaP `38.4577` edge `0.7237` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9231` n `31` status `ready` deltaP `26.6079` edge `0.8199` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4215` n `31` status `ready` deltaP `37.682` edge `0.6653` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4415` n `31` status `ready` deltaP `53.2986` edge `0.2648` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.693` n `31` status `ready` deltaP `17.2354` edge `0.8849` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.211` n `31` status `ready` deltaP `44.142` edge `0.1528` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6823` n `31` status `ready` deltaP `19.9874` edge `0.1923` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.35` n `31` status `ready` deltaP `36.4625` edge `0.0621` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6746` n `31` status `ready` deltaP `31.6931` edge `0.0201` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4719` n `31` status `ready` deltaP `10.31` edge `0.2943` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3279` n `45` status `ready` deltaP `28.8685` edge `0.03` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2791` n `31` status `ready` deltaP `13.0046` edge `0.2412` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
