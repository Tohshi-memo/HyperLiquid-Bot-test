# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T00:07:33.749634+00:00`
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

- `market_context_high->fx_24h` score `1.1121` n `145` status `ready` deltaP `20.4064` edge `0.0374` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.774` n `173` status `ready` deltaP `10.7641` edge `0.0642` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.5046` n `180` status `ready` deltaP `7.2821` edge `0.0278` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.0066` n `180` status `ready` deltaP `6.5569` edge `0.0006` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.0723` n `173` status `ready` deltaP `6.9972` edge `0.0073` maxDD `-0.4647`
- `market_context_high->index_4h` score `-1.2088` n `173` status `ready` deltaP `-7.0536` edge `-0.0175` maxDD `-1.5693`
- `market_context_high->index_1h` score `-1.2878` n `180` status `ready` deltaP `-7.0758` edge `-0.0058` maxDD `-1.0144`
- `market_context_high->metal_1h` score `-1.2984` n `180` status `ready` deltaP `-5.2195` edge `-0.0098` maxDD `-2.0884`
- `market_context_high->index_24h` score `-1.4066` n `145` status `ready` deltaP `-5.4934` edge `0.0372` maxDD `-6.4731`
- `market_context_high->metal_24h` score `-1.4514` n `145` status `ready` deltaP `2.5482` edge `-0.0055` maxDD `-2.9283`
- `market_context_high->equity_1h` score `-1.5074` n `180` status `ready` deltaP `-6.4604` edge `-0.0225` maxDD `-6.8818`
- `market_context_high->crypto_alt_1h` score `-2.9641` n `180` status `ready` deltaP `-11.9494` edge `-0.0476` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.1617` n `173` status `ready` deltaP `-7.288` edge `-0.0385` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.8613` n `180` status `ready` deltaP `-11.0479` edge `-0.0577` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.439` n `173` status `ready` deltaP `-16.3338` edge `-0.1493` maxDD `-15.8728`
- `market_context_high->commodity_24h` score `-4.7136` n `145` status `ready` deltaP `3.1292` edge `-0.0137` maxDD `-36.5838`
- `market_context_high->crypto_major_24h` score `-5.1929` n `145` status `ready` deltaP `-8.0787` edge `-0.1429` maxDD `-27.8535`
- `market_context_high->equity_24h` score `-6.094` n `145` status `ready` deltaP `-5.338` edge `-0.0673` maxDD `-42.2719`
- `market_context_high->crypto_alt_4h` score `-7.2309` n `173` status `ready` deltaP `-15.94` edge `-0.1615` maxDD `-20.1177`
- `market_context_high->crypto_alt_24h` score `-8.3379` n `145` status `ready` deltaP `-12.8226` edge `-0.2187` maxDD `-23.2513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
