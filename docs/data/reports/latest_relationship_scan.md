# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T17:07:42.491596+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4518`

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

- `market_context_high->unknown_1h` score `32472.684` n `45` status `ready` deltaP `3.0638` edge `2706.046` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22315.2702` n `45` status `ready` deltaP `3.4824` edge `1859.5965` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1263.1547` n `31` status `ready` deltaP `3.2789` edge `105.2586` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1079.917` n `31` status `ready` deltaP `4.701` edge `89.9674` maxDD `-0.119`
- `news_risk_high->equity_24h` score `42.3511` n `31` status `ready` deltaP `47.0486` edge `3.2156` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.0607` n `31` status `ready` deltaP `48.2639` edge `2.6833` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.9766` n `31` status `ready` deltaP `48.4375` edge `2.3418` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.911` n `31` status `ready` deltaP `48.1799` edge `0.7822` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.7146` n `31` status `ready` deltaP `21.8823` edge `0.7507` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.8943` n `31` status `ready` deltaP `31.1271` edge `0.5819` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.6046` n `31` status `ready` deltaP `45.3125` edge `0.2483` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1497` n `31` status `ready` deltaP `51.7809` edge `0.1801` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.7747` n `31` status `ready` deltaP `11.2903` edge `0.8068` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.266` n `31` status `ready` deltaP `18.191` edge `0.1696` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.142` n `45` status `ready` deltaP `37.71` edge `0.0389` maxDD `-0.2774`
- `news_risk_high->index_4h` score `3.0009` n `31` status `ready` deltaP `32.8039` edge `0.0574` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5596` n `31` status `ready` deltaP `30.4955` edge `0.0185` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2918` n `31` status `ready` deltaP `9.7112` edge `0.2752` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9168` n `31` status `ready` deltaP `8.6633` edge `0.2237` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `1.7605` n `38` status `ready` deltaP `3.8469` edge `0.2821` maxDD `-2.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
