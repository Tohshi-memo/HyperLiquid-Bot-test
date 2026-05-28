# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T08:07:23.672625+00:00`
- Price records: `672`
- Market context records: `2122`
- Flow alert records: `8006`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9149`

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

- `market_context_high->crypto_alt_4h` score `13.2622` n `159` status `ready` deltaP `37.173` edge `0.951` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9254` n `159` status `ready` deltaP `41.4423` edge `0.7705` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.0649` n `159` status `ready` deltaP `24.2138` edge `0.4189` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.1384` n `159` status `ready` deltaP `26.6931` edge `0.3597` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.2416` n `159` status `ready` deltaP `22.212` edge `0.2608` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.153` n `159` status `ready` deltaP `22.7862` edge `0.1792` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.0291` n `159` status `ready` deltaP `17.0254` edge `0.1954` maxDD `-2.1846`
- `news_risk_high->unknown_1h` score `2.9367` n `32` status `ready` deltaP `32.1295` edge `0.0608` maxDD `-1.7548`
- `market_context_high->index_24h` score `2.9159` n `158` status `ready` deltaP `12.4546` edge `0.2828` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.8088` n `159` status `ready` deltaP `14.3308` edge `0.2249` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.951` n `158` status `ready` deltaP `23.8689` edge `0.4933` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.4926` n `158` status `ready` deltaP `24.3792` edge `0.4939` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.1051` n `158` status `ready` deltaP `20.3342` edge `0.8647` maxDD `-62.3533`
- `news_risk_high->commodity_1h` score `0.9902` n `32` status `ready` deltaP `9.375` edge `0.088` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7244` n `159` status `ready` deltaP `9.4509` edge `0.0762` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.5221` n `159` status `ready` deltaP `8.4604` edge `0.0541` maxDD `-2.3594`
- `market_context_high->unknown_1h` score `0.133` n `159` status `ready` deltaP `4.9872` edge `0.0498` maxDD `-3.0902`
- `news_risk_high->crypto_major_1h` score `0.0814` n `32` status `ready` deltaP `11.6205` edge `0.0015` maxDD `-3.775`
- `news_risk_high->fx_1h` score `0.0585` n `32` status `ready` deltaP `3.5741` edge `0.0067` maxDD `-0.0524`
- `market_context_high->metal_24h` score `-0.018` n `158` status `ready` deltaP `10.4858` edge `0.3179` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
