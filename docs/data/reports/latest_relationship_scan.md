# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T06:07:27.254011+00:00`
- Price records: `672`
- Market context records: `7221`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13676`

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

- `risk_on_high->crypto_major_4h` score `5.7674` n `34` status `ready` deltaP `26.0133` edge `0.3455` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.7674` n `34` status `ready` deltaP `26.0133` edge `0.3455` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.2831` n `34` status `ready` deltaP `17.1001` edge `0.2822` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.2831` n `34` status `ready` deltaP `17.1001` edge `0.2822` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1048` n `34` status `ready` deltaP `22.5784` edge `0.0399` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1048` n `34` status `ready` deltaP `22.5784` edge `0.0399` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.094` n `34` status `ready` deltaP `5.4429` edge `0.1392` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.094` n `34` status `ready` deltaP `5.4429` edge `0.1392` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.277` n `34` status `ready` deltaP `7.6259` edge `0.0137` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.277` n `34` status `ready` deltaP `7.6259` edge `0.0137` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2675` n `34` status `ready` deltaP `3.1965` edge `0.031` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2675` n `34` status `ready` deltaP `3.1965` edge `0.031` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.2271` n `34` status `ready` deltaP `4.1338` edge `0.0032` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.2271` n `34` status `ready` deltaP `4.1338` edge `0.0032` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.341` n `178` status `ready` deltaP `2.9587` edge `0.0008` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5672` n `178` status `ready` deltaP `0.0404` edge `-0.0109` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.5809` n `34` status `ready` deltaP `0.7442` edge `-0.0106` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.5809` n `34` status `ready` deltaP `0.7442` edge `-0.0106` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.6306` n `178` status `ready` deltaP `0.6358` edge `0.0188` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6394` n `178` status `ready` deltaP `4.4204` edge `0.0296` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
