# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T17:22:45.540384+00:00`
- Price records: `672`
- Market context records: `4112`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10592`

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

- `risk_on_high->unknown_4h` score `144.7151` n `40` status `ready` deltaP `-9.1159` edge `12.302` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7151` n `40` status `ready` deltaP `-9.1159` edge `12.302` maxDD `-10.864`
- `market_context_high->unknown_1h` score `42.3924` n `191` status `ready` deltaP `1.6742` edge `3.6793` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `34.5597` n `147` status `ready` deltaP `-9.0844` edge `3.3434` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `14.962` n `181` status `ready` deltaP `-1.4225` edge `1.7986` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.9502` n `40` status `ready` deltaP `37.2866` edge `0.002` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.9502` n `40` status `ready` deltaP `37.2866` edge `0.002` maxDD `-0.0446`
- `risk_on_high->crypto_major_4h` score `0.3867` n `40` status `ready` deltaP `17.622` edge `-0.0187` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.3867` n `40` status `ready` deltaP `17.622` edge `-0.0187` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.272` n `40` status `ready` deltaP `11.0629` edge `-0.012` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.272` n `40` status `ready` deltaP `11.0629` edge `-0.012` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.0614` n `40` status `ready` deltaP `9.7866` edge `0.0017` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0614` n `40` status `ready` deltaP `9.7866` edge `0.0017` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0389` n `40` status `ready` deltaP `4.1018` edge `0.0006` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0389` n `40` status `ready` deltaP `4.1018` edge `0.0006` maxDD `-0.1704`
- `risk_on_high->commodity_24h` score `0.022` n `40` status `ready` deltaP `-1.5625` edge `0.2404` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.022` n `40` status `ready` deltaP `-1.5625` edge `0.2404` maxDD `-12.9187`
- `risk_on_high->crypto_major_1h` score `0.005` n `40` status `ready` deltaP `10.509` edge `-0.0152` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.005` n `40` status `ready` deltaP `10.509` edge `-0.0152` maxDD `-2.3372`
- `market_context_high->equity_4h` score `-0.2457` n `181` status `ready` deltaP `11.0573` edge `0.0589` maxDD `-6.9137`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
