# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T22:52:32.354391+00:00`
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

- `market_context_high->equity_24h` score `8.1416` n `81` status `ready` deltaP `6.983` edge `0.9379` maxDD `-21.1456`
- `market_context_high->metal_24h` score `4.0189` n `81` status `ready` deltaP `13.831` edge `0.3003` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7248` n `81` status `ready` deltaP `33.6034` edge `0.0671` maxDD `-1.9329`
- `market_context_high->index_24h` score `1.6523` n `81` status `ready` deltaP `11.5355` edge `0.2121` maxDD `-5.7715`
- `market_context_high->commodity_4h` score `1.4759` n `103` status `ready` deltaP `15.6583` edge `0.0859` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0967` n `103` status `ready` deltaP `13.1838` edge `0.0378` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.1488` n `103` status `ready` deltaP `6.2933` edge `0.0285` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4687` n `103` status `ready` deltaP `-2.885` edge `-0.0061` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5201` n `103` status `ready` deltaP `1.7557` edge `-0.0055` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5655` n `103` status `ready` deltaP `-0.5091` edge `-0.0086` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.5922` n `103` status `ready` deltaP `-3.1117` edge `-0.0056` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.746` n `103` status `ready` deltaP `2.3946` edge `-0.0028` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.9079` n `103` status `ready` deltaP `-0.7814` edge `-0.0103` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.3868` n `103` status `ready` deltaP `5.4848` edge `-0.0184` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.5875` n `103` status `ready` deltaP `-7.4356` edge `-0.0198` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-1.7409` n `81` status `ready` deltaP `11.5548` edge `-0.0508` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1162` n `103` status `ready` deltaP `-5.0404` edge `-0.0431` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5462` n `81` status `ready` deltaP `-21.6049` edge `-0.1663` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.6937` n `103` status `ready` deltaP `-7.6827` edge `-0.0914` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.0617` n `103` status `ready` deltaP `-8.766` edge `-0.1909` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
