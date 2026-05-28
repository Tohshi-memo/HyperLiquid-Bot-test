# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T12:07:19.150175+00:00`
- Price records: `672`
- Market context records: `2140`
- Flow alert records: `8056`
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

- `market_context_high->crypto_alt_4h` score `13.1639` n `158` status `ready` deltaP `36.7687` edge `0.9455` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7672` n `158` status `ready` deltaP `41.0698` edge `0.7598` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.4586` n `158` status `ready` deltaP `24.9652` edge `0.4467` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.13` n `33` status `ready` deltaP `28.0442` edge `0.391` maxDD `-3.0367`
- `market_context_high->equity_4h` score `4.9986` n `158` status `ready` deltaP `26.6247` edge `0.3485` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.6518` n `157` status `ready` deltaP `14.8587` edge `0.3281` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.1774` n `158` status `ready` deltaP `17.2857` edge `0.2017` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.0881` n `158` status `ready` deltaP `21.4032` edge `0.2534` maxDD `-4.7664`
- `market_context_high->equity_24h` score `3.0433` n `157` status `ready` deltaP `26.3181` edge `0.568` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `3.0334` n `158` status `ready` deltaP `15.7887` edge `0.2339` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.0269` n `158` status `ready` deltaP `22.0651` edge `0.1735` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.6724` n `157` status `ready` deltaP `26.8412` edge `0.5758` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4576` n `33` status `ready` deltaP `31.7997` edge `0.0112` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `1.93` n `157` status `ready` deltaP `21.6782` edge `0.9615` maxDD `-62.3533`
- `news_risk_high->unknown_1h` score `1.6186` n `36` status `ready` deltaP `23.8024` edge `0.0148` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3524` n `33` status `ready` deltaP `17.5813` edge `0.1285` maxDD `-2.7857`
- `news_risk_high->commodity_1h` score `1.2444` n `36` status `ready` deltaP `10.8117` edge `0.0996` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.8226` n `158` status `ready` deltaP `10.1683` edge `0.0796` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.617` n `158` status `ready` deltaP `9.0919` edge `0.0578` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.5059` n `157` status `ready` deltaP `12.8207` edge `0.3695` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
