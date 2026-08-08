# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T01:52:26.788470+00:00`
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

- `market_context_high->equity_24h` score `7.1997` n `81` status `ready` deltaP `4.8997` edge `0.8733` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.7432` n `81` status `ready` deltaP `12.0949` edge `0.2889` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.7443` n `103` status `ready` deltaP `17.1826` edge `0.0981` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.7201` n `81` status `ready` deltaP `33.6034` edge `0.0665` maxDD `-1.9329`
- `market_context_high->index_24h` score `1.416` n `81` status `ready` deltaP `9.4521` edge `0.2063` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.1003` n `103` status `ready` deltaP `13.1838` edge `0.0381` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.2699` n `103` status `ready` deltaP `5.3951` edge `0.0244` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4789` n `103` status `ready` deltaP `-3.0347` edge `-0.0064` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5094` n `103` status `ready` deltaP `1.9054` edge `-0.0056` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.6065` n `103` status `ready` deltaP `-0.9665` edge `-0.0108` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6163` n `103` status `ready` deltaP `-3.5608` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.9151` n `103` status `ready` deltaP `0.5653` edge `-0.0047` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.9979` n `103` status `ready` deltaP `-2.1534` edge `-0.0127` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.6905` n `103` status `ready` deltaP `-8.3338` edge `-0.0224` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-1.7599` n `103` status `ready` deltaP `3.6556` edge `-0.0373` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-1.9555` n `81` status `ready` deltaP `11.2076` edge `-0.076` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1989` n `103` status `ready` deltaP `-5.6392` edge `-0.046` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5715` n `81` status `ready` deltaP `-21.4313` edge `-0.1707` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.7189` n `103` status `ready` deltaP `-7.6827` edge `-0.0935` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.1597` n `103` status `ready` deltaP `-9.3757` edge `-0.195` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
