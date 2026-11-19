# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T13:07:31.044037+00:00`
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

- `market_context_high->unknown_1h` score `12549.6587` n `104` status `ready` deltaP `0.3743` edge `1045.8222` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7827.264` n `104` status `ready` deltaP `-0.2228` edge `652.3019` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `24.8783` n `90` status `ready` deltaP `45.3472` edge `1.8302` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.6254` n `90` status `ready` deltaP `24.1666` edge `1.4686` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.7696` n `104` status `ready` deltaP `3.3537` edge `0.407` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.1033` n `104` status `ready` deltaP `3.9634` edge `0.2731` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.3445` n `104` status `ready` deltaP `17.4601` edge `0.0413` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.2529` n `90` status `ready` deltaP `17.9861` edge `0.21` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.1396` n `104` status `ready` deltaP `5.0668` edge `0.0148` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.3345` n `104` status `ready` deltaP `3.5064` edge `0.0834` maxDD `-7.3061`
- `market_context_high->index_1h` score `-0.4874` n `104` status `ready` deltaP `0.4721` edge `0.0039` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.6821` n `104` status `ready` deltaP `-1.2379` edge `0.043` maxDD `-5.4428`
- `market_context_high->index_4h` score `-1.2381` n `104` status `ready` deltaP `-3.3889` edge `-0.0018` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.4505` n `104` status `ready` deltaP `-9.8687` edge `-0.0006` maxDD `-0.3584`
- `market_context_high->equity_1h` score `-2.0023` n `104` status `ready` deltaP `3.3567` edge `-0.0022` maxDD `-10.9626`
- `market_context_high->fx_4h` score `-2.3849` n `104` status `ready` deltaP `-14.939` edge `-0.0038` maxDD `-1.8558`
- `market_context_high->commodity_1h` score `-2.4693` n `104` status `ready` deltaP `-10.4042` edge `-0.0286` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-6.8898` n `90` status `ready` deltaP `-20.7986` edge `-0.008` maxDD `-5.5326`
- `market_context_high->commodity_4h` score `-8.1576` n `104` status `ready` deltaP `-29.3269` edge `-0.1224` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.3829` n `104` status `ready` deltaP `-7.9268` edge `-0.0581` maxDD `-43.344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
