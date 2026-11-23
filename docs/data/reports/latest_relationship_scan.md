# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T17:37:42.910311+00:00`
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

- `market_context_high->unknown_1h` score `32469.8796` n `45` status `ready` deltaP `3.0638` edge `2705.8123` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22306.4802` n `45` status `ready` deltaP `3.4824` edge `1858.864` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1260.3503` n `31` status `ready` deltaP `3.2789` edge `105.0249` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1071.127` n `31` status `ready` deltaP `4.701` edge `89.2349` maxDD `-0.119`
- `news_risk_high->equity_24h` score `41.9429` n `31` status `ready` deltaP `46.7014` edge `3.1839` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.8913` n `31` status `ready` deltaP `47.9167` edge `2.6715` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.818` n `31` status `ready` deltaP `48.0903` edge `2.3309` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.8496` n `31` status `ready` deltaP `47.8327` edge `0.7794` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.6316` n `31` status `ready` deltaP `21.7299` edge `0.7448` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6695` n `31` status `ready` deltaP `30.8222` edge `0.5652` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.5372` n `31` status `ready` deltaP `44.9653` edge `0.245` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1811` n `31` status `ready` deltaP `52.1282` edge `0.1804` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.7365` n `31` status `ready` deltaP `11.2903` edge `0.8019` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2445` n `31` status `ready` deltaP `18.0413` edge `0.1688` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.148` n `45` status `ready` deltaP `37.71` edge `0.0394` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9513` n `31` status `ready` deltaP `32.499` edge `0.0553` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5464` n `31` status `ready` deltaP `30.3458` edge `0.0184` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3175` n `31` status `ready` deltaP `9.8609` edge `0.2775` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9379` n `31` status `ready` deltaP `8.813` edge `0.2254` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `1.7963` n `38` status `ready` deltaP `3.8469` edge `0.2867` maxDD `-2.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
