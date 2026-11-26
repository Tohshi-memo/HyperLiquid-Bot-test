# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T10:52:42.977874+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3455`

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

- `news_risk_high->unknown_4h` score `3240.1807` n `31` status `ready` deltaP `3.4815` edge `269.9975` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3233.1505` n `31` status `ready` deltaP `1.4825` edge `269.4369` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `102.8587` n `31` status `ready` deltaP `1.4825` edge `8.5711` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `37.0469` n `31` status `ready` deltaP `44.2708` edge `2.7921` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.6567` n `31` status `ready` deltaP `45.1389` edge `2.7538` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.954` n `31` status `ready` deltaP `44.4444` edge `2.2832` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.0436` n `31` status `ready` deltaP `27.9799` edge `0.8208` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.8488` n `31` status `ready` deltaP `39.6637` edge `0.6877` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.9073` n `31` status `ready` deltaP `30.8188` edge `0.5643` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `7.0524` n `31` status `ready` deltaP `19.8269` edge `0.9137` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.1548` n `31` status `ready` deltaP `45.6597` edge `0.2085` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1056` n `31` status `ready` deltaP `43.274` edge `0.1498` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8801` n `31` status `ready` deltaP `21.3347` edge `0.1998` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5829` n `31` status `ready` deltaP `38.4442` edge `0.0683` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.8028` n `31` status `ready` deltaP `33.0404` edge `0.0218` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5008` n `31` status `ready` deltaP `10.0106` edge `0.3` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2892` n `31` status `ready` deltaP `13.1543` edge `0.2415` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.0264` n `31` status `ready` deltaP `25.895` edge `0.0247` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5134` n `31` status `ready` deltaP `29.5827` edge `0.0247` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0652` n `31` status `ready` deltaP `16.1683` edge `0.0845` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
