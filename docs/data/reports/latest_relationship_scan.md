# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T12:07:25.665387+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `5.6401` n `84` status `ready` deltaP `2.6538` edge `0.7583` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.673` n `84` status `ready` deltaP `14.1865` edge `0.2691` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.4608` n `84` status `ready` deltaP `31.002` edge `0.0631` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.4276` n `103` status `ready` deltaP `13.5241` edge `0.0961` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1359` n `84` status `ready` deltaP `8.0357` edge `0.1924` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.9926` n `103` status `ready` deltaP `11.5371` edge `0.0401` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.4005` n `103` status `ready` deltaP `4.0478` edge `0.0225` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4968` n `103` status `ready` deltaP `-3.3341` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5106` n `103` status `ready` deltaP `1.9054` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5693` n `103` status `ready` deltaP `-0.3567` edge `-0.0101` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6646` n `103` status `ready` deltaP `-4.459` edge `-0.0059` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8395` n `103` status `ready` deltaP `1.4799` edge `-0.0045` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0898` n `103` status `ready` deltaP `-3.8302` edge `-0.0133` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.7631` n `103` status `ready` deltaP `3.9605` edge `-0.0396` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.8594` n `103` status `ready` deltaP `-10.2799` edge `-0.0235` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.3666` n `103` status `ready` deltaP `-7.1362` edge `-0.05` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.642` n `84` status `ready` deltaP `6.6468` edge `-0.1336` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.6905` n `84` status `ready` deltaP `-21.2301` edge `-0.1873` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.9822` n `103` status `ready` deltaP `-9.9692` edge `-0.1002` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.6354` n `103` status `ready` deltaP `-12.577` edge `-0.2133` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
