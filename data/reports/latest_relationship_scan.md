# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T23:22:32.953402+00:00`
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

- `market_context_high->unknown_1h` score `32419.0921` n `45` status `ready` deltaP `2.6147` edge `2701.583` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22253.5374` n `45` status `ready` deltaP `3.4824` edge `1854.4521` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1209.5627` n `31` status `ready` deltaP `2.8298` edge `100.7956` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1018.1842` n `31` status `ready` deltaP `4.701` edge `84.823` maxDD `-0.119`
- `news_risk_high->equity_24h` score `38.4032` n `31` status `ready` deltaP `43.75` edge `2.9086` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.8917` n `31` status `ready` deltaP `45.4861` edge `2.6044` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.8892` n `31` status `ready` deltaP `45.6597` edge `2.2697` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.3159` n `31` status `ready` deltaP `44.8813` edge `0.7546` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.3902` n `31` status `ready` deltaP `22.797` edge `0.8009` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6683` n `31` status `ready` deltaP `30.8222` edge `0.5651` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.5678` n `31` status `ready` deltaP `56.1212` edge `0.186` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.3262` n `31` status `ready` deltaP `12.3574` edge `0.8704` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9409` n `31` status `ready` deltaP `41.6667` edge `0.2173` maxDD `0.0`
- `market_context_high->fx_4h` score `3.3073` n `45` status `ready` deltaP `39.3868` edge `0.0415` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.1282` n `31` status `ready` deltaP `17.2928` edge `0.1641` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9271` n `31` status `ready` deltaP `32.3466` edge `0.0543` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.4781` n `31` status `ready` deltaP `10.9088` edge `0.2911` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.465` n `31` status `ready` deltaP `29.4476` edge `0.0176` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1265` n `31` status `ready` deltaP `10.31` edge `0.2396` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5376` n `31` status `ready` deltaP `29.7324` edge `0.0268` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
