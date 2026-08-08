# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T07:07:29.364017+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11572`

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

- `market_context_high->equity_24h` score `6.1776` n `81` status `ready` deltaP `1.9483` edge `0.8078` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.5905` n `81` status `ready` deltaP `11.4005` edge `0.2808` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7225` n `81` status `ready` deltaP `33.6034` edge `0.0668` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.6125` n `103` status `ready` deltaP `15.5058` edge `0.0983` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1515` n `81` status `ready` deltaP `7.1952` edge `0.1993` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.11` n `103` status `ready` deltaP `12.8844` edge `0.0409` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.2675` n `103` status `ready` deltaP `5.5448` edge `0.0236` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4641` n `103` status `ready` deltaP `-2.7353` edge `-0.0065` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5249` n `103` status `ready` deltaP `1.7557` edge `-0.0059` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5448` n `103` status `ready` deltaP `0.1006` edge `-0.01` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6319` n `103` status `ready` deltaP `-3.8602` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.9553` n `103` status `ready` deltaP `0.108` edge `-0.005` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0565` n `103` status `ready` deltaP `-3.2204` edge `-0.0131` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.7049` n `103` status `ready` deltaP `4.4178` edge `-0.0378` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.7456` n `103` status `ready` deltaP `-9.0823` edge `-0.022` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.2708` n `103` status `ready` deltaP `-6.238` edge `-0.048` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.5601` n `81` status `ready` deltaP `7.5617` edge `-0.1292` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.6781` n `103` status `ready` deltaP `-7.6827` edge `-0.0901` maxDD `-6.5487`
- `market_context_high->crypto_alt_24h` score `-3.7767` n `81` status `ready` deltaP `-22.9938` edge `-0.1866` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-7.2801` n `103` status `ready` deltaP `-9.6806` edge `-0.203` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
