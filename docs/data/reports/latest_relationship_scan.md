# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T12:37:29.452492+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `12267.0884` n `106` status `ready` deltaP `0.6101` edge `1022.2731` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7629.0968` n `106` status `ready` deltaP `-0.0777` edge `635.787` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `23.7925` n `92` status `ready` deltaP `43.9311` edge `1.789` maxDD `-5.933`
- `market_context_high->crypto_alt_24h` score `11.5643` n `92` status `ready` deltaP `24.0262` edge `1.4617` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.4617` n `106` status `ready` deltaP `2.7151` edge `0.3856` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.5436` n `106` status `ready` deltaP `3.3249` edge `0.2551` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.1682` n `106` status `ready` deltaP `16.426` edge `0.0335` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.1524` n `92` status `ready` deltaP `17.2856` edge `0.2063` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.1898` n `106` status `ready` deltaP `4.2368` edge `0.0139` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.3556` n `106` status `ready` deltaP `3.4883` edge `0.0822` maxDD `-7.4169`
- `market_context_high->index_1h` score `-0.6027` n `106` status `ready` deltaP `-0.435` edge `0.0035` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.7493` n `106` status `ready` deltaP `-1.9772` edge `0.0397` maxDD `-5.4736`
- `market_context_high->index_4h` score `-1.1783` n `106` status `ready` deltaP `-2.3729` edge `-0.0009` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.4999` n `106` status `ready` deltaP `-10.4084` edge `-0.0009` maxDD `-0.3762`
- `market_context_high->equity_1h` score `-2.2848` n `106` status `ready` deltaP `2.3952` edge `-0.011` maxDD `-10.9626`
- `market_context_high->fx_4h` score `-2.415` n `106` status `ready` deltaP `-15.2583` edge `-0.0044` maxDD `-1.9458`
- `market_context_high->commodity_1h` score `-2.5067` n `106` status `ready` deltaP `-10.8123` edge `-0.029` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-6.8624` n `92` status `ready` deltaP `-20.5238` edge `-0.007` maxDD `-5.5768`
- `market_context_high->commodity_4h` score `-7.9624` n `106` status `ready` deltaP `-27.7123` edge `-0.1169` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.4896` n `106` status `ready` deltaP `-8.3295` edge `-0.0643` maxDD `-43.344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
