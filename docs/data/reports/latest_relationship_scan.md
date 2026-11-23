# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T16:22:27.092616+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4470`

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

- `market_context_high->unknown_1h` score `31697.0829` n `46` status `ready` deltaP `1.1845` edge `2641.4251` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `21759.2423` n `46` status `ready` deltaP `3.579` edge `1813.2602` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1266.3779` n `31` status `ready` deltaP `3.4286` edge `105.5262` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1088.5834` n `31` status `ready` deltaP `4.701` edge `90.6896` maxDD `-0.119`
- `news_risk_high->equity_24h` score `42.9664` n `31` status `ready` deltaP `47.5694` edge `3.2634` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.263` n `31` status `ready` deltaP `48.4375` edge `2.699` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.1609` n `31` status `ready` deltaP `48.6111` edge `2.356` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.9856` n `31` status `ready` deltaP `48.5271` edge `0.7861` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.8202` n `31` status `ready` deltaP `21.8823` edge `0.7595` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.2513` n `31` status `ready` deltaP `31.5844` edge `0.6086` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.7063` n `31` status `ready` deltaP `45.8333` edge `0.2533` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1172` n `31` status `ready` deltaP `51.4337` edge `0.1797` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.8355` n `31` status `ready` deltaP `11.2903` edge `0.8146` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2444` n `31` status `ready` deltaP `18.191` edge `0.1678` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.0783` n `31` status `ready` deltaP `33.2612` edge `0.0608` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.9738` n `46` status `ready` deltaP `35.9226` edge `0.0368` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5596` n `31` status `ready` deltaP `30.4955` edge `0.0185` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2037` n `31` status `ready` deltaP `9.2621` edge `0.2669` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8568` n `31` status `ready` deltaP `8.2142` edge `0.219` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `1.5561` n `39` status `ready` deltaP `2.4974` edge `0.2662` maxDD `-2.6678`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
