# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T17:22:38.225529+00:00`
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

- `market_context_high->unknown_1h` score `32469.888` n `45` status `ready` deltaP `3.0638` edge `2705.813` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22312.3398` n `45` status `ready` deltaP `3.4824` edge `1859.3523` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1260.3587` n `31` status `ready` deltaP `3.2789` edge `105.0256` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1076.9866` n `31` status `ready` deltaP `4.701` edge `89.7232` maxDD `-0.119`
- `news_risk_high->equity_24h` score `42.1404` n `31` status `ready` deltaP `46.875` edge `3.1992` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.97` n `31` status `ready` deltaP `48.0903` edge `2.6769` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.8967` n `31` status `ready` deltaP `48.2639` edge `2.3363` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.8803` n `31` status `ready` deltaP `48.0063` edge `0.7808` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.6858` n `31` status `ready` deltaP `21.8823` edge `0.7483` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.7873` n `31` status `ready` deltaP `30.9747` edge `0.574` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.5703` n `31` status `ready` deltaP `45.1389` edge `0.2466` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1648` n `31` status `ready` deltaP `51.9545` edge `0.1802` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.7583` n `31` status `ready` deltaP `11.2903` edge `0.8047` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2708` n `31` status `ready` deltaP `18.191` edge `0.17` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1456` n `45` status `ready` deltaP `37.71` edge `0.0392` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9767` n `31` status `ready` deltaP `32.6515` edge `0.0564` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5596` n `31` status `ready` deltaP `30.4955` edge `0.0185` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3144` n `31` status `ready` deltaP `9.8609` edge `0.2771` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9363` n `31` status `ready` deltaP `8.813` edge `0.2252` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `1.7784` n `38` status `ready` deltaP `3.8469` edge `0.2844` maxDD `-2.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
