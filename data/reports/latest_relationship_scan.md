# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T22:07:15.981848+00:00`
- Price records: `672`
- Market context records: `1980`
- Flow alert records: `7592`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7584`

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

- `market_context_high->crypto_alt_4h` score `7.394` n `234` status `ready` deltaP `22.5649` edge `0.5802` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8468` n `234` status `ready` deltaP `26.3511` edge `0.5195` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4865` n `234` status `ready` deltaP `13.5906` edge `0.319` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.1797` n `234` status `ready` deltaP `13.7534` edge `0.1994` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.7509` n `199` status `ready` deltaP `16.0967` edge `0.2812` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.6705` n `199` status `ready` deltaP `16.7627` edge `0.5595` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.1167` n `199` status `ready` deltaP `14.7751` edge `0.4844` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.0136` n `234` status `ready` deltaP `9.4017` edge `0.1204` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.7752` n `234` status `ready` deltaP `8.0954` edge `0.122` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.4753` n `199` status `ready` deltaP `4.1922` edge `0.1345` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `0.2339` n `199` status `ready` deltaP `19.3167` edge `0.7493` maxDD `-62.3533`
- `market_context_high->index_4h` score `0.0553` n `234` status `ready` deltaP `6.9158` edge `0.0674` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.1808` n `199` status `ready` deltaP `10.446` edge `0.0202` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1893` n `234` status `ready` deltaP `4.2006` edge `0.0356` maxDD `-2.6836`
- `market_context_high->fx_1h` score `-0.66` n `234` status `ready` deltaP `-3.1629` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6796` n `234` status `ready` deltaP `-0.2635` edge `0.0083` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-1.1697` n `234` status `ready` deltaP `-8.6017` edge `-0.0038` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.3623` n `234` status `ready` deltaP `2.6486` edge `0.0024` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4712` n `234` status `ready` deltaP `0.9584` edge `-0.0338` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.883` n `234` status `ready` deltaP `2.0088` edge `0.001` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
