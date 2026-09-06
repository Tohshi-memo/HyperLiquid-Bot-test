# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T18:14:45.548027+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10137`

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

- `risk_on_high->unknown_24h` score `203.7729` n `103` status `ready` deltaP `25.2124` edge `16.8229` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `203.7729` n `103` status `ready` deltaP `25.2124` edge `16.8229` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `18.2435` n `103` status `ready` deltaP `32.376` edge `1.4546` maxDD `-9.0118`
- `risk_on_and_context->crypto_major_24h` score `18.2435` n `103` status `ready` deltaP `32.376` edge `1.4546` maxDD `-9.0118`
- `risk_on_high->crypto_alt_24h` score `9.0186` n `103` status `ready` deltaP `20.1911` edge `0.7872` maxDD `-9.6209`
- `risk_on_and_context->crypto_alt_24h` score `9.0186` n `103` status `ready` deltaP `20.1911` edge `0.7872` maxDD `-9.6209`
- `market_context_high->crypto_alt_24h` score `5.3211` n `196` status `ready` deltaP `18.5268` edge `0.5155` maxDD `-10.9804`
- `market_context_high->equity_24h` score `5.3114` n `196` status `ready` deltaP `20.061` edge `0.387` maxDD `-3.2501`
- `risk_on_high->equity_24h` score `3.9465` n `103` status `ready` deltaP `15.9149` edge `0.3009` maxDD `-3.2501`
- `risk_on_and_context->equity_24h` score `3.9465` n `103` status `ready` deltaP `15.9149` edge `0.3009` maxDD `-3.2501`
- `market_context_high->index_24h` score `0.9948` n `196` status `ready` deltaP `17.5843` edge `0.0855` maxDD `-2.9198`
- `risk_on_high->index_24h` score `0.8974` n `103` status `ready` deltaP `14.7064` edge `0.0652` maxDD `-2.4104`
- `risk_on_and_context->index_24h` score `0.8974` n `103` status `ready` deltaP `14.7064` edge `0.0652` maxDD `-2.4104`
- `risk_on_high->index_1h` score `-0.0276` n `129` status `ready` deltaP `6.6692` edge `-0.0033` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0276` n `129` status `ready` deltaP `6.6692` edge `-0.0033` maxDD `-0.5764`
- `risk_on_high->metal_24h` score `-0.219` n `103` status `ready` deltaP `14.7013` edge `0.0668` maxDD `-7.3116`
- `risk_on_and_context->metal_24h` score `-0.219` n `103` status `ready` deltaP `14.7013` edge `0.0668` maxDD `-7.3116`
- `risk_on_high->metal_1h` score `-0.2657` n `129` status `ready` deltaP `5.8569` edge `-0.0026` maxDD `-1.6408`
- `risk_on_and_context->metal_1h` score `-0.2657` n `129` status `ready` deltaP `5.8569` edge `-0.0026` maxDD `-1.6408`
- `risk_on_high->crypto_alt_1h` score `-0.3102` n `129` status `ready` deltaP `2.6006` edge `0.0585` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
