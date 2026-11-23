# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T23:37:31.671591+00:00`
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

- `market_context_high->unknown_1h` score `32421.9913` n `45` status `ready` deltaP `2.6147` edge `2701.8246` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22250.4642` n `45` status `ready` deltaP `3.4824` edge `1854.196` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1212.4619` n `31` status `ready` deltaP `2.8298` edge `101.0372` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1015.111` n `31` status `ready` deltaP `4.701` edge `84.5669` maxDD `-0.119`
- `news_risk_high->equity_24h` score `38.3336` n `31` status `ready` deltaP `43.75` edge `2.9028` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9109` n `31` status `ready` deltaP `45.4861` edge `2.606` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.9072` n `31` status `ready` deltaP `45.6597` edge `2.2712` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.3123` n `31` status `ready` deltaP `44.8813` edge `0.7543` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.43` n `31` status `ready` deltaP `22.9494` edge `0.8032` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6887` n `31` status `ready` deltaP `30.8222` edge `0.5668` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.5865` n `31` status `ready` deltaP `56.2948` edge `0.1864` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.3474` n `31` status `ready` deltaP `12.5098` edge `0.8721` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9337` n `31` status `ready` deltaP `41.6667` edge `0.2167` maxDD `0.0`
- `market_context_high->fx_4h` score `3.3085` n `45` status `ready` deltaP `39.3868` edge `0.0416` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.1521` n `31` status `ready` deltaP `17.4425` edge `0.1651` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9295` n `31` status `ready` deltaP `32.3466` edge `0.0545` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4793` n `31` status `ready` deltaP `29.5973` edge `0.0178` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4641` n `31` status `ready` deltaP `10.7591` edge `0.2903` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1187` n `31` status `ready` deltaP `10.31` edge `0.2386` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5461` n `31` status `ready` deltaP `29.8821` edge `0.0269` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
