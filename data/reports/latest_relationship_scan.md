# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T03:07:36.657787+00:00`
- Price records: `672`
- Market context records: `4052`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10432`

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

- `risk_on_high->unknown_4h` score `144.9365` n `40` status `ready` deltaP `-7.7439` edge `12.3113` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.9365` n `40` status `ready` deltaP `-7.7439` edge `12.3113` maxDD `-10.864`
- `market_context_high->unknown_24h` score `40.1469` n `141` status `ready` deltaP `-7.8248` edge `3.8006` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `20.7175` n `160` status `ready` deltaP `0.3811` edge `2.2662` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.7628` n `40` status `ready` deltaP `38.3537` edge `0.0626` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.7628` n `40` status `ready` deltaP `38.3537` edge `0.0626` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `3.7427` n `40` status `ready` deltaP `33.4489` edge `0.0889` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.7427` n `40` status `ready` deltaP `33.4489` edge `0.0889` maxDD `0.0`
- `market_context_high->index_24h` score `2.1231` n `141` status `ready` deltaP `20.4346` edge `0.0619` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.5676` n `160` status `ready` deltaP `15.2287` edge `0.1697` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.303` n `40` status `ready` deltaP `20.061` edge `0.0414` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.303` n `40` status `ready` deltaP `20.061` edge `0.0414` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8041` n `172` status `ready` deltaP `6.2213` edge `0.0815` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4867` n `40` status `ready` deltaP `11.512` edge `0.0029` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4867` n `40` status `ready` deltaP `11.512` edge `0.0029` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.2271` n `40` status `ready` deltaP `12.7545` edge `-0.0017` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2271` n `40` status `ready` deltaP `12.7545` edge `-0.0017` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.1404` n `40` status `ready` deltaP `10.9451` edge `-0.0214` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1404` n `40` status `ready` deltaP `10.9451` edge `-0.0214` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `0.003` n `40` status `ready` deltaP `3.503` edge `0.0` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
