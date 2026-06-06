# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T23:52:21.562626+00:00`
- Price records: `672`
- Market context records: `3125`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7027`

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

- `market_context_high->commodity_24h` score `14.4311` n `102` status `ready` deltaP `47.2529` edge `0.9304` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9007` n `102` status `ready` deltaP `20.6291` edge `0.903` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.454` n `102` status `ready` deltaP `10.3146` edge `2.3253` maxDD `-65.3814`
- `market_context_high->index_24h` score `6.6193` n `102` status `ready` deltaP `32.547` edge `0.8871` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6332` n `102` status `ready` deltaP `11.6523` edge `1.319` maxDD `-51.8817`
- `market_context_high->commodity_4h` score `3.0418` n `128` status `ready` deltaP `19.093` edge `0.172` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0092` n `140` status `ready` deltaP `2.3396` edge `0.0259` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.438` n `140` status `ready` deltaP `4.6535` edge `0.0191` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5113` n `102` status `ready` deltaP `4.7181` edge `-0.0013` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.6692` n `140` status `ready` deltaP `4.089` edge `0.0999` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.9567` n `140` status `ready` deltaP `1.5783` edge `0.0154` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.1587` n `140` status `ready` deltaP `-11.2104` edge `-0.0057` maxDD `-0.7828`
- `market_context_high->crypto_major_1h` score `-1.2328` n `140` status `ready` deltaP `0.9067` edge `0.0622` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.2718` n `128` status `ready` deltaP `11.5282` edge `0.051` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4543` n `128` status `ready` deltaP `-14.1006` edge `-0.0078` maxDD `-1.1045`
- `market_context_high->metal_1h` score `-2.1819` n `140` status `ready` deltaP `-5.5432` edge `-0.0055` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.2105` n `128` status `ready` deltaP `2.4771` edge `0.0215` maxDD `-14.7778`
- `market_context_high->unknown_1h` score `-3.0339` n `140` status `ready` deltaP `1.9376` edge `-0.0631` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.5087` n `128` status `ready` deltaP `14.9771` edge `0.2548` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.6822` n `128` status `ready` deltaP `8.7271` edge `0.0003` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
