# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T21:07:34.238494+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2832`

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

- `news_risk_high->unknown_1h` score `3290.7337` n `31` status `ready` deltaP `1.6322` edge `274.2345` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3173.6001` n `31` status `ready` deltaP `3.3191` edge `264.4502` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.9108` n `31` status `ready` deltaP `26.6898` edge `1.2313` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.3521` n `31` status `ready` deltaP `23.9168` edge `0.8699` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.2913` n `31` status `ready` deltaP `26.5165` edge `0.8475` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2243` n `31` status `ready` deltaP `21.0438` edge `0.6321` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4545` n `31` status `ready` deltaP `29.6853` edge `0.3047` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1241` n `31` status `ready` deltaP `14.2583` edge `0.7036` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6658` n `31` status `ready` deltaP `38.6762` edge `0.1438` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.6836` n `31` status `ready` deltaP `12.1877` edge `0.2532` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3438` n `31` status `ready` deltaP `28.9243` edge `0.0285` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2337` n `31` status `ready` deltaP `27.5015` edge `0.0113` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.2136` n `31` status `ready` deltaP `24.6101` edge `0.0204` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.1615` n `31` status `ready` deltaP `14.7479` edge `0.1005` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8608` n `31` status `ready` deltaP `5.9687` edge `0.2449` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6447` n `31` status `ready` deltaP `8.3639` edge `0.1908` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1208` n `31` status `ready` deltaP `24.4929` edge `0.0083` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4559` n `31` status `ready` deltaP `10.7281` edge `0.0267` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3664` n `31` status `ready` deltaP `11.6708` edge `0.0249` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3256` n `31` status `ready` deltaP `-1.9123` edge `0.0118` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
