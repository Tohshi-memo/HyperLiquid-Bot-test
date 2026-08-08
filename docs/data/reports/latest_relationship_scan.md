# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T10:22:39.426036+00:00`
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

- `market_context_high->equity_24h` score `6.1092` n `81` status `ready` deltaP `1.9483` edge `0.8021` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.793` n `81` status `ready` deltaP `13.1366` edge `0.2861` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.717` n `81` status `ready` deltaP `33.6034` edge `0.0661` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.447` n `103` status `ready` deltaP `13.6765` edge `0.0967` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1628` n `81` status `ready` deltaP `7.0216` edge `0.2014` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.0225` n `103` status `ready` deltaP `11.8365` edge `0.0406` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.3609` n `103` status `ready` deltaP `4.4969` edge `0.0228` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4874` n `103` status `ready` deltaP `-3.1844` edge `-0.0065` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5237` n `103` status `ready` deltaP `1.7557` edge `-0.0058` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5606` n `103` status `ready` deltaP `-0.2043` edge `-0.01` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6895` n `103` status `ready` deltaP `-4.9081` edge `-0.0061` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.9151` n `103` status `ready` deltaP `0.5653` edge `-0.0047` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0819` n `103` status `ready` deltaP `-3.6778` edge `-0.0133` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.7171` n `103` status `ready` deltaP `4.2653` edge `-0.0378` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.7983` n `103` status `ready` deltaP `-9.6811` edge `-0.0224` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.3055` n `103` status `ready` deltaP `-6.5374` edge `-0.0489` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6637` n `81` status `ready` deltaP `6.6937` edge `-0.1367` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.8006` n `81` status `ready` deltaP `-23.1674` edge `-0.1885` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.8345` n `103` status `ready` deltaP `-8.9022` edge `-0.095` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.4936` n `103` status `ready` deltaP `-11.5099` edge `-0.2086` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
