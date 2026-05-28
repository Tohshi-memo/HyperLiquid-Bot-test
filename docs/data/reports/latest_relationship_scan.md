# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T12:02:01.893452+00:00`
- Price records: `672`
- Market context records: `2139`
- Flow alert records: `8054`
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

- `market_context_high->crypto_alt_4h` score `13.1627` n `158` status `ready` deltaP `36.7687` edge `0.9454` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7672` n `158` status `ready` deltaP `41.0698` edge `0.7598` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.4598` n `158` status `ready` deltaP `24.9652` edge `0.4468` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.1288` n `33` status `ready` deltaP `28.0442` edge `0.3909` maxDD `-3.0367`
- `market_context_high->equity_4h` score `5.001` n `158` status `ready` deltaP `26.6247` edge `0.3487` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.653` n `157` status `ready` deltaP `14.8587` edge `0.3282` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.1762` n `158` status `ready` deltaP `17.2857` edge `0.2016` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.0881` n `158` status `ready` deltaP `21.4032` edge `0.2534` maxDD `-4.7664`
- `market_context_high->equity_24h` score `3.0445` n `157` status `ready` deltaP `26.3181` edge `0.5681` maxDD `-33.1875`
- `market_context_high->index_4h` score `3.0281` n `158` status `ready` deltaP `22.0651` edge `0.1736` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.0191` n `158` status `ready` deltaP `15.639` edge `0.2337` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `2.6724` n `157` status `ready` deltaP `26.8412` edge `0.5758` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4576` n `33` status `ready` deltaP `31.7997` edge `0.0112` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `1.9292` n `157` status `ready` deltaP `21.6782` edge `0.9614` maxDD `-62.3533`
- `news_risk_high->unknown_1h` score `1.6138` n `36` status `ready` deltaP `23.8024` edge `0.0144` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3532` n `33` status `ready` deltaP `17.5813` edge `0.1286` maxDD `-2.7857`
- `news_risk_high->commodity_1h` score `1.2768` n `36` status `ready` deltaP `10.8117` edge `0.1023` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.8238` n `158` status `ready` deltaP `10.1683` edge `0.0797` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.617` n `158` status `ready` deltaP `9.0919` edge `0.0578` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.5051` n `157` status `ready` deltaP `12.8207` edge `0.3694` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
