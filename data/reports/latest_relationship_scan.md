# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T07:07:25.064564+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3714`

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

- `news_risk_high->unknown_1h` score `3357.5461` n `31` status `ready` deltaP `1.4825` edge `279.8032` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3230.0133` n `31` status `ready` deltaP `3.634` edge `269.1492` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.3806` n `31` status `ready` deltaP `31.5425` edge `1.4881` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.3402` n `31` status `ready` deltaP `29.4627` edge `0.9986` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.7995` n `31` status `ready` deltaP `25.3033` edge `0.8146` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.8975` n `31` status `ready` deltaP `20.6628` edge `0.6074` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.2031` n `31` status `ready` deltaP `28.6881` edge `0.2904` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8844` n `31` status `ready` deltaP `14.644` edge `0.6703` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.7907` n `31` status `ready` deltaP `39.0228` edge `0.1519` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.5047` n `31` status `ready` deltaP `13.4008` edge `0.2302` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.3127` n `31` status `ready` deltaP `28.3997` edge `0.0119` maxDD `-0.0136`
- `news_risk_high->index_4h` score `2.2713` n `31` status `ready` deltaP `28.0783` edge `0.0281` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2655` n `31` status `ready` deltaP `25.3033` edge `0.0201` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.1496` n `31` status `ready` deltaP `14.2988` edge `0.1025` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8367` n `31` status `ready` deltaP `5.5196` edge `0.2448` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6906` n `31` status `ready` deltaP `8.6633` edge `0.1947` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1076` n `31` status `ready` deltaP `24.1935` edge `0.0086` maxDD `-0.2315`
- `market_context_high->fx_1h` score `0.6038` n `33` status `ready` deltaP `10.157` edge `0.004` maxDD `-0.0451`
- `market_context_high->equity_1h` score `0.4001` n `33` status `ready` deltaP `10.1933` edge `0.0242` maxDD `-1.2685`
- `news_risk_high->commodity_4h` score `0.3001` n `31` status `ready` deltaP `7.9121` edge `0.0255` maxDD `-0.5151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
