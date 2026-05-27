# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T01:07:17.180250+00:00`
- Price records: `672`
- Market context records: `1994`
- Flow alert records: `7630`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7585`

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

- `market_context_high->crypto_major_4h` score `8.3465` n `225` status `ready` deltaP `29.21` edge `0.5538` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `7.8598` n `225` status `ready` deltaP `23.9024` edge `0.6101` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `4.3656` n `225` status `ready` deltaP `16.2073` edge `0.3643` maxDD `-5.3506`
- `market_context_high->equity_4h` score `2.4135` n `225` status `ready` deltaP `14.7561` edge `0.2122` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.2717` n `190` status `ready` deltaP `16.0724` edge `0.6142` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.7672` n `190` status `ready` deltaP `16.8854` edge `0.2773` maxDD `-12.7414`
- `market_context_high->equity_24h` score `1.2318` n `190` status `ready` deltaP `14.9693` edge `0.4927` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.153` n `225` status `ready` deltaP `10.2901` edge `0.1261` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.9319` n `225` status `ready` deltaP `8.6294` edge `0.1315` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.637` n `225` status `ready` deltaP `8.3815` edge `0.0746` maxDD `-2.5246`
- `market_context_high->crypto_major_24h` score `0.6051` n `190` status `ready` deltaP `20.1766` edge `0.7745` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.5182` n `190` status `ready` deltaP `14.0879` edge `0.0267` maxDD `-1.1952`
- `market_context_high->index_24h` score `0.2362` n `190` status `ready` deltaP `3.2877` edge `0.1206` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1548` n `225` status `ready` deltaP `4.2648` edge `0.0375` maxDD `-2.6402`
- `market_context_high->fx_1h` score `-0.6065` n `225` status `ready` deltaP `-2.1637` edge `-0.0001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7157` n `225` status `ready` deltaP `-0.6101` edge `0.0076` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.9774` n `225` status `ready` deltaP `1.3919` edge `-0.001` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.0245` n `225` status `ready` deltaP `1.6634` edge `-0.0245` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-1.1748` n `225` status `ready` deltaP `-8.8468` edge `-0.0035` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9141` n `225` status `ready` deltaP `1.5602` edge `0.0` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
