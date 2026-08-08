# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T11:16:25.021227+00:00`
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

- `market_context_high->equity_24h` score `6.108` n `81` status `ready` deltaP `1.9483` edge `0.802` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.8598` n `81` status `ready` deltaP `13.6574` edge `0.2882` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7123` n `81` status `ready` deltaP `33.6034` edge `0.0655` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.4288` n `103` status `ready` deltaP `13.5241` edge `0.0962` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1784` n `81` status `ready` deltaP `7.0216` edge `0.2027` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.9794` n `103` status `ready` deltaP `11.3874` edge `0.04` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.4041` n `103` status `ready` deltaP `4.0478` edge `0.0222` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4968` n `103` status `ready` deltaP `-3.3341` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.4986` n `103` status `ready` deltaP `2.0551` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5772` n `103` status `ready` deltaP `-0.5091` edge `-0.0101` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6724` n `103` status `ready` deltaP `-4.6087` edge `-0.0059` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8651` n `103` status `ready` deltaP `1.1751` edge `-0.0046` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0819` n `103` status `ready` deltaP `-3.6778` edge `-0.0133` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.7547` n `103` status `ready` deltaP `3.9605` edge `-0.0389` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.8331` n `103` status `ready` deltaP `-9.9805` edge `-0.0233` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.3702` n `103` status `ready` deltaP `-7.1362` edge `-0.0503` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.652` n `81` status `ready` deltaP `6.6937` edge `-0.1352` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.7923` n `81` status `ready` deltaP `-22.9938` edge `-0.1886` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.9145` n `103` status `ready` deltaP `-9.5119` edge `-0.0976` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.576` n `103` status `ready` deltaP `-12.1196` edge `-0.2114` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
