# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T14:07:34.548625+00:00`
- Price records: `672`
- Market context records: `7885`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14677`

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

- `market_context_high->equity_24h` score `13.957` n `110` status `ready` deltaP `29.74` edge `1.099` maxDD `-6.0681`
- `market_context_high->equity_4h` score `4.7641` n `110` status `ready` deltaP `14.4483` edge `0.3983` maxDD `-5.1426`
- `market_context_high->metal_24h` score `4.2394` n `110` status `ready` deltaP `21.3935` edge `0.3047` maxDD `-0.8563`
- `market_context_high->crypto_alt_4h` score `1.7318` n `110` status `ready` deltaP `14.7654` edge `0.1576` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.644` n `110` status `ready` deltaP `21.6827` edge `0.1508` maxDD `-7.0012`
- `market_context_high->crypto_major_4h` score `1.6117` n `110` status `ready` deltaP `16.4273` edge `0.1966` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.1769` n `110` status `ready` deltaP `31.6717` edge `0.0485` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.1552` n `114` status `ready` deltaP `12.8585` edge `0.0514` maxDD `-1.6021`
- `market_context_high->equity_1h` score `0.8798` n `114` status `ready` deltaP `12.3834` edge `0.112` maxDD `-4.2072`
- `market_context_high->index_4h` score `0.6902` n `110` status `ready` deltaP `14.7536` edge `0.0594` maxDD `-1.0191`
- `market_context_high->commodity_4h` score `0.6643` n `110` status `ready` deltaP `10.0069` edge `0.048` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.4869` n `114` status `ready` deltaP `9.823` edge `0.0181` maxDD `-0.7743`
- `market_context_high->metal_4h` score `0.4412` n `110` status `ready` deltaP `8.8709` edge `0.0982` maxDD `-0.979`
- `market_context_high->crypto_alt_1h` score `0.4388` n `114` status `ready` deltaP `5.5836` edge `0.0426` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.1628` n `114` status `ready` deltaP `3.9908` edge `0.0076` maxDD `-0.8216`
- `market_context_high->index_24h` score `-0.1781` n `110` status `ready` deltaP `0.3971` edge `0.1187` maxDD `-1.562`
- `market_context_high->metal_1h` score `-0.3515` n `114` status `ready` deltaP `2.1168` edge `0.0236` maxDD `-0.6936`
- `market_context_high->fx_1h` score `-0.3541` n `114` status `ready` deltaP `1.3751` edge `-0.0002` maxDD `-0.4112`
- `market_context_high->fx_4h` score `-0.7371` n `110` status `ready` deltaP `1.1937` edge `0.0003` maxDD `-1.5544`
- `market_context_high->crypto_alt_24h` score `-1.6165` n `110` status `ready` deltaP `12.7619` edge `0.2372` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
