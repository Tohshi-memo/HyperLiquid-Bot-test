# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T01:57:35.870215+00:00`
- Price records: `672`
- Market context records: `8151`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `23.0476` n `79` status `ready` deltaP `44.2137` edge `1.7169` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0644` n `80` status `ready` deltaP `37.1951` edge `0.6142` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.8973` n `79` status `ready` deltaP `38.5417` edge `0.4845` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.2498` n `43` status `ready` deltaP `31.8172` edge `0.4959` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.9962` n `43` status `ready` deltaP `18.509` edge `0.3535` maxDD `-2.1767`
- `market_context_high->index_24h` score `3.9708` n `79` status `ready` deltaP `25.0242` edge `0.2311` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.9397` n `80` status `ready` deltaP `35.5488` edge `0.0956` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.7991` n `43` status `ready` deltaP `29.3796` edge `0.1516` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.4237` n `80` status `ready` deltaP `18.1587` edge `0.1892` maxDD `-0.9962`
- `market_context_high->metal_4h` score `2.6155` n `80` status `ready` deltaP `24.3598` edge `0.1178` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.6141` n `43` status `ready` deltaP `21.9441` edge `0.0906` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.5395` n `80` status `ready` deltaP `11.6463` edge `0.2457` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `2.3105` n `80` status `ready` deltaP `13.5671` edge `0.2739` maxDD `-6.7444`
- `market_context_high->fx_24h` score `2.1739` n `79` status `ready` deltaP `29.3864` edge `0.0556` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `1.8197` n `79` status `ready` deltaP `32.9158` edge `0.3024` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.6358` n `80` status `ready` deltaP `19.2515` edge `0.0276` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.4291` n `43` status `ready` deltaP `14.1272` edge `0.0717` maxDD `-0.7433`
- `market_context_high->crypto_major_1h` score `1.3354` n `80` status `ready` deltaP `12.6946` edge `0.0677` maxDD `-1.6171`
- `news_risk_high->crypto_major_1h` score `1.3307` n `43` status `ready` deltaP `6.183` edge `0.1094` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0695` n `80` status `ready` deltaP `14.0045` edge `0.0336` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
