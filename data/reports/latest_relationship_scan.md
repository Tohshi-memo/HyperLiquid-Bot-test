# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T18:37:27.598648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13790`

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

- `market_context_high->unknown_1h` score `0.9876` n `133` status `ready` deltaP `8.5375` edge `0.0481` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.1818` n `133` status `ready` deltaP `10.7559` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1717` n `131` status `ready` deltaP `9.3848` edge `0.0097` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1401` n `133` status `ready` deltaP `2.0294` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2303` n `133` status `ready` deltaP `6.4146` edge `0.0347` maxDD `-5.2257`
- `market_context_high->unknown_4h` score `-0.3291` n `131` status `ready` deltaP `21.0133` edge `-0.1236` maxDD `-0.5133`
- `market_context_high->metal_1h` score `-0.3604` n `133` status `ready` deltaP `0.233` edge `-0.0059` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.5273` n `131` status `ready` deltaP `2.6846` edge `-0.0239` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.6526` n `131` status `ready` deltaP `1.6047` edge `0.0092` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6616` n `131` status `ready` deltaP `-1.1241` edge `0.0077` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6869` n `133` status `ready` deltaP `-4.7206` edge `0.0` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.6992` n `133` status `ready` deltaP `0.4199` edge `0.0191` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-0.836` n `105` status `ready` deltaP `1.4633` edge `0.1039` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.2092` n `133` status `ready` deltaP `-1.2505` edge `-0.0442` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.2176` n `131` status `ready` deltaP `3.7691` edge `0.0004` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8935` n `131` status `ready` deltaP `-2.6602` edge `0.0555` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.6749` n `105` status `ready` deltaP `-9.003` edge `-0.0019` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.8309` n `131` status `ready` deltaP `-0.0523` edge `-0.2168` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2558` n `105` status `ready` deltaP `-6.4633` edge `-0.0523` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7466` n `105` status `ready` deltaP `-18.4574` edge `-0.1547` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
