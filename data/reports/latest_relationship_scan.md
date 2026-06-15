# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T13:22:34.960548+00:00`
- Price records: `672`
- Market context records: `3995`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10098`

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

- `risk_on_high->unknown_4h` score `147.0296` n `40` status `ready` deltaP `-2.1037` edge `12.4477` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.0296` n `40` status `ready` deltaP `-2.1037` edge `12.4477` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `41.8157` n `142` status `ready` deltaP `-4.6949` edge `3.9178` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `23.6096` n `154` status `ready` deltaP `1.4353` edge `2.4988` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2987` n `40` status `ready` deltaP `42.0139` edge `0.4948` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2987` n `40` status `ready` deltaP `42.0139` edge `0.4948` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.0446` n `40` status `ready` deltaP `38.3537` edge `0.0861` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.0446` n `40` status `ready` deltaP `38.3537` edge `0.0861` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.0773` n `142` status `ready` deltaP `15.4563` edge `0.3049` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.0403` n `142` status `ready` deltaP `25.6357` edge `0.1964` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.7693` n `40` status `ready` deltaP `29.8611` edge `0.0317` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7693` n `40` status `ready` deltaP `29.8611` edge `0.0317` maxDD `0.0`
- `market_context_high->equity_4h` score `2.1824` n `154` status `ready` deltaP `20.0745` edge `0.1783` maxDD `-7.0879`
- `market_context_high->equity_24h` score `2.1204` n `142` status `ready` deltaP `17.366` edge `0.3639` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.7984` n `40` status `ready` deltaP `20.8232` edge `0.0776` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7984` n `40` status `ready` deltaP `20.8232` edge `0.0776` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.27` n `154` status `ready` deltaP `17.8037` edge `0.1438` maxDD `-7.8662`
- `market_context_high->crypto_major_1h` score `1.1939` n `154` status `ready` deltaP `11.0409` edge `0.0801` maxDD `-2.3372`
- `market_context_high->metal_1h` score `1.1064` n `154` status `ready` deltaP `12.0869` edge `0.0591` maxDD `-1.7983`
- `market_context_high->equity_1h` score `1.0788` n `154` status `ready` deltaP `9.647` edge `0.082` maxDD `-2.1799`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
