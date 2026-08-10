# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T22:37:26.237456+00:00`
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

- `market_context_high->fx_24h` score `1.0485` n `145` status `ready` deltaP `20.4064` edge `0.0321` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.8441` n `176` status `ready` deltaP `11.6408` edge `0.0642` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6549` n `180` status `ready` deltaP `8.9055` edge `0.0295` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0122` n `176` status `ready` deltaP `7.7189` edge `0.0075` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1161` n `180` status `ready` deltaP `4.5276` edge `0.0001` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.7123` n `180` status `ready` deltaP `-5.8583` edge `-0.0041` maxDD `-0.8531`
- `market_context_high->index_24h` score `-0.8113` n `145` status `ready` deltaP `-2.3952` edge `0.0652` maxDD `-5.9262`
- `market_context_high->index_4h` score `-1.0202` n `176` status `ready` deltaP `-5.3769` edge `-0.0147` maxDD `-1.4198`
- `market_context_high->metal_24h` score `-1.137` n `145` status `ready` deltaP `2.5482` edge `0.0207` maxDD `-2.9283`
- `market_context_high->equity_1h` score `-1.1395` n `180` status `ready` deltaP `-4.4311` edge `-0.012` maxDD `-6.0304`
- `market_context_high->metal_1h` score `-1.2552` n `180` status `ready` deltaP `-4.8137` edge `-0.0089` maxDD `-2.0884`
- `market_context_high->crypto_alt_1h` score `-2.8547` n `180` status `ready` deltaP `-11.1377` edge `-0.0439` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.0732` n `176` status `ready` deltaP `-6.7212` edge `-0.0349` maxDD `-6.1111`
- `market_context_high->equity_24h` score `-3.2416` n `145` status `ready` deltaP `-2.2399` edge `0.116` maxDD `-31.333`
- `market_context_high->crypto_major_1h` score `-3.7663` n `180` status `ready` deltaP `-10.2362` edge `-0.0552` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.0155` n `176` status `ready` deltaP `-14.5094` edge `-0.1292` maxDD `-14.1098`
- `market_context_high->crypto_major_24h` score `-4.2606` n `145` status `ready` deltaP `-4.9806` edge `-0.1154` maxDD `-24.143`
- `market_context_high->commodity_24h` score `-6.1782` n `145` status `ready` deltaP `0.0311` edge `-0.0732` maxDD `-43.1932`
- `market_context_high->crypto_alt_4h` score `-6.8534` n `176` status `ready` deltaP `-14.551` edge `-0.1534` maxDD `-18.9899`
- `market_context_high->crypto_alt_24h` score `-7.3812` n `145` status `ready` deltaP `-12.8226` edge `-0.2066` maxDD `-19.8414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
