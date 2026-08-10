# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T23:52:40.481218+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `1.1037` n `145` status `ready` deltaP `20.4064` edge `0.0367` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.7742` n `174` status `ready` deltaP `10.7812` edge `0.0641` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.5082` n `180` status `ready` deltaP `7.2821` edge `0.0281` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.0277` n `180` status `ready` deltaP `6.151` edge `0.0006` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.0546` n `174` status `ready` deltaP `7.2032` edge `0.0074` maxDD `-0.4647`
- `market_context_high->index_4h` score `-1.2012` n `174` status `ready` deltaP `-6.907` edge `-0.0175` maxDD `-1.5693`
- `market_context_high->index_1h` score `-1.2275` n `180` status `ready` deltaP `-7.0758` edge `-0.0057` maxDD `-0.9534`
- `market_context_high->metal_1h` score `-1.2936` n `180` status `ready` deltaP `-5.2195` edge `-0.0094` maxDD `-2.0884`
- `market_context_high->index_24h` score `-1.2951` n `145` status `ready` deltaP `-4.977` edge `0.042` maxDD `-6.3222`
- `market_context_high->metal_24h` score `-1.4046` n `145` status `ready` deltaP `2.5482` edge `-0.0016` maxDD `-2.9283`
- `market_context_high->equity_1h` score `-1.4708` n `180` status `ready` deltaP `-6.4604` edge `-0.0231` maxDD `-6.792`
- `market_context_high->crypto_alt_1h` score `-2.9617` n `180` status `ready` deltaP `-11.9494` edge `-0.0474` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.1351` n `174` status `ready` deltaP `-7.0455` edge `-0.0379` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.8565` n `180` status `ready` deltaP `-11.0479` edge `-0.0573` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.4225` n `174` status `ready` deltaP `-16.1375` edge `-0.1485` maxDD `-15.8728`
- `market_context_high->commodity_24h` score `-4.9618` n `145` status `ready` deltaP `2.6128` edge `-0.024` maxDD `-37.6966`
- `market_context_high->crypto_major_24h` score `-5.0309` n `145` status `ready` deltaP `-7.5623` edge `-0.1379` maxDD `-27.2006`
- `market_context_high->equity_24h` score `-5.6151` n `145` status `ready` deltaP `-4.8216` edge `-0.0382` maxDD `-40.2963`
- `market_context_high->crypto_alt_4h` score `-7.2555` n `174` status `ready` deltaP `-16.1725` edge `-0.162` maxDD `-20.1177`
- `market_context_high->crypto_alt_24h` score `-8.2099` n `145` status `ready` deltaP `-12.8226` edge `-0.2174` maxDD `-22.8356`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
