# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T09:52:37.958462+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4482`

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

- `market_context_high->unknown_1h` score `20114.5443` n `69` status `ready` deltaP `1.1845` edge `1676.2203` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `13371.7573` n `69` status `ready` deltaP `3.7315` edge `1114.3021` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1297.8263` n `31` status `ready` deltaP `3.4286` edge `108.1469` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1149.6636` n `31` status `ready` deltaP `4.8535` edge `95.7786` maxDD `-0.119`
- `news_risk_high->equity_24h` score `46.4211` n `31` status `ready` deltaP `52.0833` edge `3.5212` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.0437` n `31` status `ready` deltaP `48.6111` edge `2.7629` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.6152` n `31` status `ready` deltaP `48.7847` edge `2.3927` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.6933` n `31` status `ready` deltaP `52.6938` edge `0.8173` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.7008` n `31` status `ready` deltaP `34.3283` edge `0.7111` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.2352` n `31` status `ready` deltaP `22.6445` edge `0.789` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.318` n `31` status `ready` deltaP `50.0` edge `0.2765` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.5079` n `31` status `ready` deltaP `55.2532` edge `0.1868` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2276` n `31` status `ready` deltaP `11.9001` edge `0.8608` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.6536` n `31` status `ready` deltaP `18.3407` edge `0.2009` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.3994` n `31` status `ready` deltaP `35.7003` edge `0.0713` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6495` n `31` status `ready` deltaP `31.0943` edge `0.022` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3176` n `31` status `ready` deltaP `8.6633` edge `0.2855` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9256` n `31` status `ready` deltaP `7.316` edge `0.2338` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.508` n `31` status `ready` deltaP `28.8342` edge `0.029` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4183` n `31` status `ready` deltaP `19.6744` edge `0.1064` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
