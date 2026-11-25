# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T02:07:26.367153+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4068`

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

- `market_context_high->unknown_1h` score `32251.7509` n `45` status `ready` deltaP `2.0159` edge `2687.6419` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21993.7237` n `45` status `ready` deltaP `3.1776` edge `1832.803` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1016.796` n `31` status `ready` deltaP `2.231` edge `84.7357` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `740.7762` n `31` status `ready` deltaP `4.3962` edge `61.7077` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.8847` n `31` status `ready` deltaP `50.1736` edge `2.9059` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.3979` n `31` status `ready` deltaP `43.9236` edge `2.907` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.9763` n `31` status `ready` deltaP `48.9583` edge `2.5883` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.7901` n `31` status `ready` deltaP `27.0653` edge `0.8891` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.177` n `31` status `ready` deltaP `41.2355` edge `0.684` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.2518` n `31` status `ready` deltaP `34.4808` edge `0.6725` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.2984` n `31` status `ready` deltaP `17.3879` edge `0.9615` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.7368` n `31` status `ready` deltaP `42.5347` edge `0.1945` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.5527` n `31` status `ready` deltaP `47.0934` edge `0.1616` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6153` n `31` status `ready` deltaP `18.7898` edge `0.1947` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0759` n `31` status `ready` deltaP `33.2612` edge `0.0606` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7447` n `31` status `ready` deltaP `12.5555` edge `0.3143` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.6126` n `45` status `ready` deltaP `31.9173` edge `0.0334` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5716` n `31` status `ready` deltaP `30.4955` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3977` n `31` status `ready` deltaP `12.5555` edge `0.2594` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5898` n `31` status `ready` deltaP `30.1815` edge `0.0305` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
