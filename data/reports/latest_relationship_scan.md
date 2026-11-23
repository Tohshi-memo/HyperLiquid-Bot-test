# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T20:52:45.139106+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4652`

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

- `market_context_high->unknown_1h` score `32446.0357` n `45` status `ready` deltaP `2.465` edge `2703.8293` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22284.549` n `45` status `ready` deltaP `3.4824` edge `1857.0364` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1236.5064` n `31` status `ready` deltaP `2.6801` edge `103.0419` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1049.1958` n `31` status `ready` deltaP `4.701` edge `87.4073` maxDD `-0.119`
- `news_risk_high->equity_24h` score `39.6768` n `31` status `ready` deltaP `44.4444` edge `3.0101` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.1302` n `31` status `ready` deltaP `46.0069` edge `2.6208` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.9986` n `31` status `ready` deltaP `46.0069` edge `2.2765` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.5145` n `31` status `ready` deltaP `45.923` edge `0.7642` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.1066` n `31` status `ready` deltaP `22.4921` edge `0.7793` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6151` n `31` status `ready` deltaP `30.5173` edge `0.5627` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.3929` n `31` status `ready` deltaP `54.3851` edge `0.183` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2233` n `31` status `ready` deltaP `12.3574` edge `0.8572` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.1491` n `31` status `ready` deltaP `42.7083` edge `0.2277` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2505` n `31` status `ready` deltaP `18.0413` edge `0.1693` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.2258` n `45` status `ready` deltaP `38.4722` edge `0.0408` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9003` n `31` status `ready` deltaP `32.0417` edge `0.0541` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.532` n `31` status `ready` deltaP `30.1961` edge `0.0182` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4781` n `31` status `ready` deltaP `11.0585` edge `0.2901` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0867` n `31` status `ready` deltaP `10.0106` edge `0.2365` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.536` n `31` status `ready` deltaP `29.7324` edge `0.0266` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
