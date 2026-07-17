# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T20:32:25.010690+00:00`
- Price records: `672`
- Market context records: `7065`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.68` n `184` status `ready` deltaP `17.2455` edge `0.0117` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1648` n `184` status `ready` deltaP `4.3478` edge `0.0024` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3022` n `184` status `ready` deltaP `2.0079` edge `0.0343` maxDD `-4.5815`
- `market_context_high->unknown_1h` score `-0.3708` n `184` status `ready` deltaP `-0.2278` edge `0.0293` maxDD `-1.6942`
- `market_context_high->crypto_major_1h` score `-0.5717` n `184` status `ready` deltaP `4.2372` edge `0.0337` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.7894` n `184` status `ready` deltaP `-0.9275` edge `-0.0039` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8341` n `184` status `ready` deltaP `-4.1331` edge `-0.0026` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.8665` n `184` status `ready` deltaP `-4.5691` edge `-0.019` maxDD `-1.9306`
- `market_context_high->unknown_4h` score `-0.8736` n `184` status `ready` deltaP `-5.2889` edge `0.1259` maxDD `-4.742`
- `market_context_high->commodity_4h` score `-1.6167` n `184` status `ready` deltaP `-6.9062` edge `-0.0452` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8412` n `184` status `ready` deltaP `4.9401` edge `-0.0267` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.3172` n `184` status `ready` deltaP `1.0538` edge `-0.0342` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4267` n `184` status `ready` deltaP `-2.2721` edge `-0.0562` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.9177` n `184` status `ready` deltaP `0.6562` edge `0.0001` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0562` n `184` status `ready` deltaP `2.8698` edge `0.0175` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.5589` n `184` status `ready` deltaP `-0.2793` edge `-0.012` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.6241` n `184` status `ready` deltaP `-0.0133` edge `-0.0036` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-4.0341` n `184` status `ready` deltaP `-15.6477` edge `0.1018` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.8944` n `184` status `ready` deltaP `4.6394` edge `-0.156` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.5599` n `184` status `ready` deltaP `-21.0145` edge `-0.0972` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
