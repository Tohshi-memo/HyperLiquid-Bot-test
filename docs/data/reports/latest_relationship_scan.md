# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T03:07:27.481545+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3899`

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

- `market_context_high->unknown_1h` score `35607.9766` n `41` status `ready` deltaP `0.7667` edge `2967.3357` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3196.5785` n `31` status `ready` deltaP `3.3291` edge `266.365` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `886.3933` n `31` status `ready` deltaP `1.6322` edge `73.8728` maxDD `-0.7395`
- `news_risk_high->equity_24h` score `43.5626` n `31` status `ready` deltaP `49.6528` edge `3.2992` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.7689` n `31` status `ready` deltaP `50.5208` edge `3.0606` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.5401` n `31` status `ready` deltaP `49.8264` edge `2.6295` maxDD `0.0`
- `news_risk_high->unknown_24h` score `19.4089` n `31` status `ready` deltaP `6.0764` edge `1.5769` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8235` n `31` status `ready` deltaP `26.6079` edge `0.8116` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `10.7635` n `31` status `ready` deltaP `36.2008` edge `0.6831` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.1761` n `31` status `ready` deltaP `37.2247` edge `0.6479` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.1169` n `31` status `ready` deltaP `51.0417` edge `0.2528` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7663` n `31` status `ready` deltaP `17.2354` edge `0.8943` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3329` n `31` status `ready` deltaP `45.5309` edge `0.1537` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5683` n `31` status `ready` deltaP `19.688` edge `0.1848` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3196` n `31` status `ready` deltaP `36.1576` edge `0.0616` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6542` n `31` status `ready` deltaP `31.5434` edge `0.0194` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.4982` n `41` status `ready` deltaP `30.4878` edge `0.0334` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.3917` n `31` status `ready` deltaP `9.5615` edge `0.289` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1941` n `31` status `ready` deltaP `12.2561` edge `0.2353` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4581` n `31` status `ready` deltaP `28.8342` edge `0.0226` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
