# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T03:07:24.859609+00:00`
- Price records: `672`
- Market context records: `6456`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.8207` n `32` status `ready` deltaP `30.5556` edge `0.7961` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.6498` n `145` status `ready` deltaP `17.0414` edge `0.8539` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3094` n `32` status `ready` deltaP `52.2569` edge `0.1774` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0718` n `32` status `ready` deltaP `42.3018` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.693` n `32` status `ready` deltaP `32.6389` edge `0.1107` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.4627` n `32` status `ready` deltaP `12.6736` edge `0.4374` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4458` n `32` status `ready` deltaP `29.491` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4959` n `173` status `ready` deltaP `-5.9153` edge `0.2542` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `1.4454` n `32` status `ready` deltaP `13.0801` edge `0.1448` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8061` n `32` status `ready` deltaP `8.9259` edge `0.09` maxDD `-1.6923`
- `market_context_high->crypto_alt_4h` score `0.348` n `173` status `ready` deltaP `8.8009` edge `0.1257` maxDD `-6.7632`
- `market_context_high->index_4h` score `0.2644` n `173` status `ready` deltaP `9.43` edge `0.0268` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.2565` n `145` status `ready` deltaP `6.1949` edge `0.1669` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `0.2273` n `173` status `ready` deltaP `-15.1338` edge `0.3604` maxDD `-10.5788`
- `market_context_high->metal_4h` score `0.0403` n `173` status `ready` deltaP `10.3315` edge `0.0433` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2835` n `32` status `ready` deltaP `5.4828` edge `-0.0257` maxDD `-0.7581`
- `market_context_high->crypto_alt_1h` score `-0.5134` n `173` status `ready` deltaP `6.7763` edge `0.0203` maxDD `-5.8368`
- `news_risk_high->metal_1h` score `-0.5145` n `32` status `ready` deltaP `1.1976` edge `-0.0242` maxDD `-1.6464`
- `news_risk_high->index_24h` score `-0.5363` n `32` status `ready` deltaP `3.6458` edge `-0.0059` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5499` n `173` status `ready` deltaP `0.9086` edge `0.0012` maxDD `-1.8877`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
