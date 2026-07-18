# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T14:07:28.929230+00:00`
- Price records: `672`
- Market context records: `7147`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11692`

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

- `market_context_high->fx_4h` score `0.4986` n `148` status `ready` deltaP `14.663` edge `0.0138` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1585` n `158` status `ready` deltaP `4.3963` edge `0.0026` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4859` n `158` status `ready` deltaP `-1.6202` edge `0.0345` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6565` n `158` status `ready` deltaP `-0.5514` edge `0.0234` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.673` n `158` status `ready` deltaP `3.2801` edge `0.0329` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7355` n `158` status `ready` deltaP `-2.327` edge `-0.0167` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7758` n `158` status `ready` deltaP `0.9929` edge `-0.0048` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.4298` n `158` status `ready` deltaP `-5.7038` edge `-0.005` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.6622` n `148` status `ready` deltaP `-5.8956` edge `0.0148` maxDD `-5.7541`
- `market_context_high->commodity_4h` score `-2.0012` n `148` status `ready` deltaP `-3.9799` edge `-0.0367` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.8799` n `148` status `ready` deltaP `-9.3853` edge `-0.0118` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5926` n `158` status `ready` deltaP `-1.0081` edge `-0.0434` maxDD `-15.2742`
- `market_context_high->index_4h` score `-3.9041` n `148` status `ready` deltaP `-1.4008` edge `-0.0461` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4988` n `133` status `ready` deltaP `-13.4581` edge `-0.1543` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9887` n `133` status `ready` deltaP `-16.0518` edge `-0.026` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-5.2338` n `148` status `ready` deltaP `0.1483` edge `-0.0018` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.6878` n `148` status `ready` deltaP `-4.4537` edge `-0.0393` maxDD `-24.3993`
- `market_context_high->unknown_24h` score `-10.1028` n `133` status `ready` deltaP `-32.7029` edge `-0.1092` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.4297` n `148` status `ready` deltaP `-3.8439` edge `-0.2369` maxDD `-65.5294`
- `market_context_high->metal_24h` score `-14.6218` n `133` status `ready` deltaP `-30.908` edge `-0.1943` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
