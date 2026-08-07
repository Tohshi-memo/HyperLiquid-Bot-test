# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T22:07:31.315860+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `7.9034` n `82` status `ready` deltaP `6.5252` edge `0.9211` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.977` n `82` status `ready` deltaP `14.0117` edge `0.2956` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.6629` n `82` status `ready` deltaP `32.7151` edge `0.0659` maxDD `-1.9977`
- `market_context_high->index_24h` score `1.5773` n `82` status `ready` deltaP `11.1831` edge `0.2082` maxDD `-5.7715`
- `market_context_high->commodity_4h` score `1.4518` n `104` status `ready` deltaP `15.537` edge `0.0847` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.1031` n `104` status `ready` deltaP `13.2485` edge `0.0379` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.0996` n `104` status `ready` deltaP `6.6387` edge `0.0303` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4491` n `104` status `ready` deltaP `-2.5679` edge `-0.0057` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.4516` n `104` status `ready` deltaP `2.5219` edge `-0.0049` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5301` n `104` status `ready` deltaP `0.0821` edge `-0.008` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.5692` n `104` status `ready` deltaP `-2.6543` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.6733` n `104` status `ready` deltaP `3.213` edge `-0.0022` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.8848` n `104` status `ready` deltaP `-0.3987` edge `-0.0099` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.3028` n `104` status `ready` deltaP `6.1444` edge `-0.0158` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.5844` n `104` status `ready` deltaP `-7.3526` edge `-0.0201` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-1.8331` n `82` status `ready` deltaP `10.6665` edge `-0.0567` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1913` n `104` status `ready` deltaP `-5.7692` edge `-0.0445` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5466` n `82` status `ready` deltaP `-21.5236` edge `-0.1669` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.67` n `104` status `ready` deltaP `-7.446` edge `-0.091` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.0735` n `104` status `ready` deltaP `-8.7008` edge `-0.1897` maxDD `-18.34`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
