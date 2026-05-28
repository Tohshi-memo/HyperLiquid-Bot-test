# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T12:37:21.587991+00:00`
- Price records: `672`
- Market context records: `2142`
- Flow alert records: `8062`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9158`

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

- `market_context_high->crypto_alt_4h` score `13.1663` n `158` status `ready` deltaP `36.7687` edge `0.9457` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.754` n `158` status `ready` deltaP `41.0698` edge `0.7587` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.549` n `158` status `ready` deltaP `25.2701` edge `0.4522` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.1828` n `33` status `ready` deltaP `28.0442` edge `0.3954` maxDD `-3.0367`
- `market_context_high->equity_4h` score `4.9732` n `158` status `ready` deltaP `26.4722` edge `0.3474` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.7492` n `157` status `ready` deltaP `15.2059` edge `0.3339` maxDD `-4.1604`
- `market_context_high->equity_24h` score `3.1743` n `157` status `ready` deltaP `26.6653` edge `0.5766` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `3.1666` n `158` status `ready` deltaP `17.2857` edge `0.2008` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.0713` n `158` status `ready` deltaP `21.4032` edge `0.252` maxDD `-4.7664`
- `market_context_high->crypto_alt_1h` score `3.0238` n `158` status `ready` deltaP `15.7887` edge `0.2331` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.0015` n `158` status `ready` deltaP `21.9126` edge `0.1724` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.8202` n `157` status `ready` deltaP `27.1884` edge `0.5858` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4309` n `33` status `ready` deltaP `31.4948` edge `0.011` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.0666` n `157` status `ready` deltaP `22.0254` edge `0.9767` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.4112` n `33` status `ready` deltaP `17.8862` edge `0.134` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0659` n `38` status `ready` deltaP `20.1544` edge `0.0014` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.7795` n `158` status `ready` deltaP `9.8689` edge `0.078` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.7043` n `38` status `ready` deltaP `10.2269` edge `0.0901` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.5955` n `158` status `ready` deltaP `8.9422` edge `0.057` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.5601` n `157` status `ready` deltaP `12.9943` edge `0.3753` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
