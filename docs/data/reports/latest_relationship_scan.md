# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T02:07:20.785143+00:00`
- Price records: `672`
- Market context records: `2413`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9202`

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

- `news_risk_high->crypto_alt_24h` score `20.2297` n `43` status `ready` deltaP `46.3905` edge `1.4354` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.3216` n `43` status `ready` deltaP `49.5841` edge `1.2402` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1891` n `43` status `ready` deltaP `29.7925` edge `1.0986` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.8796` n `43` status `ready` deltaP `18.8993` edge `0.8387` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2091` n `43` status `ready` deltaP `27.9877` edge `0.5201` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.4762` n `106` status `ready` deltaP `22.2615` edge `0.3491` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.308` n `43` status `ready` deltaP `11.8823` edge `0.405` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.7636` n `129` status `ready` deltaP `22.7808` edge `0.4261` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.4291` n `129` status `ready` deltaP `21.7491` edge `0.492` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6151` n `43` status `ready` deltaP `37.924` edge `0.0669` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2764` n `43` status `ready` deltaP `30.1758` edge `0.286` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.8923` n `106` status `ready` deltaP `12.3394` edge `0.6778` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.4051` n `129` status `ready` deltaP `12.2684` edge `0.1796` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1646` n `43` status `ready` deltaP `27.4319` edge `0.0159` maxDD `-0.1382`
- `market_context_high->index_24h` score `2.1102` n `106` status `ready` deltaP `12.0578` edge `0.1274` maxDD `-0.8879`
- `news_risk_high->unknown_4h` score `1.8205` n `43` status `ready` deltaP `16.1444` edge `0.1164` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.338` n `129` status `ready` deltaP `12.1223` edge `0.1501` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.0941` n `43` status `ready` deltaP `20.2966` edge `0.0028` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0554` n `129` status `ready` deltaP `9.1178` edge `0.1459` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5242` n `43` status `ready` deltaP `8.9681` edge `0.0754` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
