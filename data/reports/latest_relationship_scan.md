# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T18:07:33.053853+00:00`
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

- `market_context_high->unknown_1h` score `32464.3308` n `45` status `ready` deltaP `2.9141` edge `2705.3509` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22300.6542` n `45` status `ready` deltaP `3.4824` edge `1858.3785` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1254.8015` n `31` status `ready` deltaP `3.1292` edge `104.5635` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1065.301` n `31` status `ready` deltaP `4.701` edge `88.7494` maxDD `-0.119`
- `news_risk_high->equity_24h` score `41.5863` n `31` status `ready` deltaP `46.3542` edge `3.1565` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.7388` n `31` status `ready` deltaP `47.5694` edge `2.6611` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.6738` n `31` status `ready` deltaP `47.7431` edge `2.3212` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.793` n `31` status `ready` deltaP `47.4855` edge `0.777` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.61` n `31` status `ready` deltaP `21.7299` edge `0.743` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5517` n `31` status `ready` deltaP `30.6698` edge `0.5564` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.477` n `31` status `ready` deltaP `44.6181` edge `0.2423` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.2125` n `31` status `ready` deltaP `52.4754` edge `0.1807` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.7427` n `31` status `ready` deltaP `11.2903` edge `0.8027` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2373` n `31` status `ready` deltaP `18.0413` edge `0.1682` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1504` n `45` status `ready` deltaP `37.71` edge `0.0396` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9247` n `31` status `ready` deltaP `32.3466` edge `0.0541` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5452` n `31` status `ready` deltaP `30.3458` edge `0.0183` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3362` n `31` status `ready` deltaP `10.0106` edge `0.2789` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9589` n `31` status `ready` deltaP `8.9627` edge `0.2271` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `1.8495` n `38` status `ready` deltaP `4.1941` edge `0.2912` maxDD `-2.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
