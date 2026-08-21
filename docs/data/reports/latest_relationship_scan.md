# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T14:49:53.781073+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13774`

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

- `market_context_high->fx_4h` score `0.1069` n `116` status `ready` deltaP `8.1686` edge `0.0095` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0819` n `128` status `ready` deltaP `9.1083` edge `0.003` maxDD `-0.9245`
- `market_context_high->fx_1h` score `-0.1091` n `128` status `ready` deltaP `2.6104` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2436` n `128` status `ready` deltaP `5.9974` edge `0.0319` maxDD `-4.9161`
- `market_context_high->metal_1h` score `-0.3236` n `128` status `ready` deltaP `0.5146` edge `-0.0053` maxDD `-0.503`
- `market_context_high->metal_4h` score `-0.4264` n `116` status `ready` deltaP `3.7374` edge `-0.022` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.5032` n `116` status `ready` deltaP `3.1907` edge `0.0112` maxDD `-2.0923`
- `market_context_high->commodity_24h` score `-0.5113` n `105` status `ready` deltaP `4.0675` edge `0.1136` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.5986` n `128` status `ready` deltaP `8.7201` edge `-0.0853` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.6745` n `128` status `ready` deltaP `-4.5565` edge `0.0005` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7043` n `116` status `ready` deltaP `-2.1552` edge `0.0091` maxDD `-2.4692`
- `market_context_high->equity_4h` score `-0.7378` n `116` status `ready` deltaP `1.3509` edge `0.0905` maxDD `-10.861`
- `market_context_high->crypto_alt_1h` score `-0.7898` n `128` status `ready` deltaP `0.1263` edge `0.0135` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.2648` n `128` status `ready` deltaP `-1.7496` edge `-0.048` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-2.1005` n `116` status `ready` deltaP `1.2826` edge `-0.0566` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.924` n `105` status `ready` deltaP `-11.6072` edge `-0.0053` maxDD `-2.2121`
- `market_context_high->unknown_4h` score `-3.8365` n `116` status `ready` deltaP `19.8013` edge `-0.4078` maxDD `-0.5133`
- `market_context_high->index_24h` score `-4.2018` n `105` status `ready` deltaP `-5.7689` edge `-0.05` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.3524` n `116` status `ready` deltaP `-1.2458` edge `-0.2523` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.5535` n `105` status `ready` deltaP `-17.0685` edge `-0.1392` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
