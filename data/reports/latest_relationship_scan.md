# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T17:52:34.249338+00:00`
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

- `market_context_high->unknown_1h` score `32470.0464` n `45` status `ready` deltaP `3.0638` edge `2705.8262` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22306.5438` n `45` status `ready` deltaP `3.4824` edge `1858.8693` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1260.5171` n `31` status `ready` deltaP `3.2789` edge `105.0388` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1071.1906` n `31` status `ready` deltaP `4.701` edge `89.2402` maxDD `-0.119`
- `news_risk_high->equity_24h` score `41.7658` n `31` status `ready` deltaP `46.5278` edge `3.1703` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.815` n `31` status `ready` deltaP `47.7431` edge `2.6663` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.7489` n `31` status `ready` deltaP `47.9167` edge `2.3263` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.8213` n `31` status `ready` deltaP `47.6591` edge `0.7782` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.581` n `31` status `ready` deltaP `21.5775` edge `0.7416` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5589` n `31` status `ready` deltaP `30.6698` edge `0.557` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.5077` n `31` status `ready` deltaP `44.7917` edge `0.2437` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1962` n `31` status `ready` deltaP `52.3018` edge `0.1805` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.7067` n `31` status `ready` deltaP `11.1379` edge `0.7991` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2385` n `31` status `ready` deltaP `18.0413` edge `0.1683` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1492` n `45` status `ready` deltaP `37.71` edge `0.0395` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9271` n `31` status `ready` deltaP `32.3466` edge `0.0543` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5452` n `31` status `ready` deltaP `30.3458` edge `0.0183` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3206` n `31` status `ready` deltaP `9.8609` edge `0.2779` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9426` n `31` status `ready` deltaP `8.813` edge `0.226` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `1.8225` n `38` status `ready` deltaP `4.0205` edge `0.2889` maxDD `-2.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
