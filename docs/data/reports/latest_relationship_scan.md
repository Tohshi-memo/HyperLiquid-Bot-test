# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T16:37:35.212991+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2626`

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

- `market_context_high->unknown_1h` score `12131.1063` n `107` status `ready` deltaP `0.5751` edge `1010.9415` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `8049.3958` n `102` status `ready` deltaP `-0.3736` edge `670.8139` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.9719` n `88` status `ready` deltaP `45.1073` edge `1.8396` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.7243` n `88` status `ready` deltaP `23.5322` edge `1.4855` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `2.0734` n `102` status `ready` deltaP `4.1816` edge `0.4268` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.4724` n `102` status `ready` deltaP `5.0963` edge `0.2963` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5665` n `102` status `ready` deltaP `18.8397` edge `0.0506` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.4304` n `88` status `ready` deltaP `19.0656` edge `0.2176` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.2208` n `107` status `ready` deltaP `3.7607` edge `0.0131` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2622` n `107` status `ready` deltaP `4.2825` edge `0.0775` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3288` n `107` status `ready` deltaP `2.377` edge `0.0032` maxDD `-1.2295`
- `market_context_high->index_4h` score `-1.1784` n `102` status `ready` deltaP `-2.6154` edge `0.0007` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.2583` n `107` status `ready` deltaP `-2.5589` edge `0.0344` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.5664` n `107` status `ready` deltaP `5.1807` edge `0.0128` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6651` n `107` status `ready` deltaP `-12.1272` edge `-0.0022` maxDD `-0.4566`
- `market_context_high->fx_4h` score `-2.3938` n `102` status `ready` deltaP `-15.211` edge `-0.0039` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.529` n `107` status `ready` deltaP `-10.6707` edge `-0.0318` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.1377` n `88` status `ready` deltaP `-23.5954` edge `-0.0102` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.3336` n `102` status `ready` deltaP `-30.8525` edge `-0.1269` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.0844` n `102` status `ready` deltaP `-7.6279` edge `-0.0385` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
