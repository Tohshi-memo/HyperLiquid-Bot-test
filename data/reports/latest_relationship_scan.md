# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T16:22:27.009901+00:00`
- Price records: `672`
- Market context records: `7267`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13759`

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

- `risk_on_high->crypto_major_4h` score `6.2886` n `33` status `ready` deltaP `28.0442` edge `0.3754` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.2886` n `33` status `ready` deltaP `28.0442` edge `0.3754` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.8477` n `33` status `ready` deltaP `20.9535` edge `0.2979` maxDD `-1.0224`
- `risk_on_and_context->crypto_alt_4h` score `4.8477` n `33` status `ready` deltaP `20.9535` edge `0.2979` maxDD `-1.0224`
- `risk_on_high->commodity_1h` score `2.048` n `33` status `ready` deltaP `22.0038` edge `0.039` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.048` n `33` status `ready` deltaP `22.0038` edge `0.039` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `0.9768` n `33` status `ready` deltaP `4.323` edge `0.1369` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `0.9768` n `33` status `ready` deltaP `4.323` edge `0.1369` maxDD `-2.412`
- `risk_on_high->equity_1h` score `0.4251` n `33` status `ready` deltaP `5.0914` edge `0.0315` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.4251` n `33` status `ready` deltaP `5.0914` edge `0.0315` maxDD `-0.7345`
- `risk_on_high->crypto_major_1h` score `0.2861` n `33` status `ready` deltaP `7.2764` edge `0.0172` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2861` n `33` status `ready` deltaP `7.2764` edge `0.0172` maxDD `-0.9888`
- `risk_on_high->unknown_4h` score `-0.0311` n `33` status `ready` deltaP `3.7047` edge `0.0251` maxDD `-1.3027`
- `risk_on_and_context->unknown_4h` score `-0.0311` n `33` status `ready` deltaP `3.7047` edge `0.0251` maxDD `-1.3027`
- `market_context_high->fx_1h` score `-0.2166` n `142` status `ready` deltaP `3.0706` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6344` n `142` status `ready` deltaP `-0.9369` edge `-0.013` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.7558` n `33` status `ready` deltaP `-1.2927` edge `-0.0116` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.7558` n `33` status `ready` deltaP `-1.2927` edge `-0.0116` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.7954` n `142` status `ready` deltaP `-1.3642` edge `0.011` maxDD `-5.9775`
- `market_context_high->unknown_4h` score `-0.9292` n `142` status `ready` deltaP `6.3509` edge `0.0744` maxDD `-6.2026`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
