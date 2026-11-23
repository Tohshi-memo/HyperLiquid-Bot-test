# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T23:07:32.309955+00:00`
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

- `market_context_high->unknown_1h` score `32419.1485` n `45` status `ready` deltaP `2.6147` edge `2701.5877` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22256.5254` n `45` status `ready` deltaP `3.4824` edge `1854.7011` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1209.6191` n `31` status `ready` deltaP `2.8298` edge `100.8003` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1021.1722` n `31` status `ready` deltaP `4.701` edge `85.072` maxDD `-0.119`
- `news_risk_high->equity_24h` score `38.492` n `31` status `ready` deltaP `43.75` edge `2.916` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.8893` n `31` status `ready` deltaP `45.4861` edge `2.6042` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.8796` n `31` status `ready` deltaP `45.6597` edge `2.2689` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.3195` n `31` status `ready` deltaP `44.8813` edge `0.7549` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.3492` n `31` status `ready` deltaP `22.6445` edge `0.7985` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6563` n `31` status `ready` deltaP `30.8222` edge `0.5641` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.5503` n `31` status `ready` deltaP `55.9476` edge `0.1857` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.3161` n `31` status `ready` deltaP `12.3574` edge `0.8691` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9505` n `31` status `ready` deltaP `41.6667` edge `0.2181` maxDD `0.0`
- `market_context_high->fx_4h` score `3.3073` n `45` status `ready` deltaP `39.3868` edge `0.0415` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.127` n `31` status `ready` deltaP `17.2928` edge `0.164` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9259` n `31` status `ready` deltaP `32.3466` edge `0.0542` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.4851` n `31` status `ready` deltaP `10.9088` edge `0.292` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4769` n `31` status `ready` deltaP `29.5973` edge `0.0176` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1397` n `31` status `ready` deltaP `10.4597` edge `0.2403` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5453` n `31` status `ready` deltaP `29.8821` edge `0.0268` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
