# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T02:22:23.805037+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32385.1933` n `45` status `ready` deltaP `2.465` edge `2698.7591` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22235.5134` n `45` status `ready` deltaP `3.4824` edge `1852.9501` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1175.664` n `31` status `ready` deltaP `2.6801` edge `97.9717` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1000.1602` n `31` status `ready` deltaP `4.701` edge `83.321` maxDD `-0.119`
- `news_risk_high->equity_24h` score `37.1639` n `31` status `ready` deltaP `43.2292` edge `2.8088` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.8821` n `31` status `ready` deltaP `45.4861` edge `2.6036` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.8304` n `31` status `ready` deltaP `45.6597` edge `2.2648` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.9891` n `31` status `ready` deltaP `42.9716` edge `0.7401` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.67` n `31` status `ready` deltaP `23.864` edge `0.8171` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6563` n `31` status `ready` deltaP `30.8222` edge `0.5641` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6243` n `31` status `ready` deltaP `56.4684` edge `0.1884` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.5458` n `31` status `ready` deltaP `13.7293` edge `0.8894` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.7347` n `31` status `ready` deltaP `40.7986` edge `0.2059` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2493` n `31` status `ready` deltaP `18.0413` edge `0.1692` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.249` n `45` status `ready` deltaP `38.7771` edge `0.0407` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8324` n `31` status `ready` deltaP `31.432` edge `0.0525` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4889` n `31` status `ready` deltaP `29.747` edge `0.0176` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4633` n `31` status `ready` deltaP `10.7591` edge `0.2902` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.086` n `31` status `ready` deltaP `10.0106` edge `0.2364` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5757` n `31` status `ready` deltaP `30.3312` edge `0.0277` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
