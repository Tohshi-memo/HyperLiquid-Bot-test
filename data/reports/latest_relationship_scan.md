# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T04:07:26.034179+00:00`
- Price records: `672`
- Market context records: `7212`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `12810`

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

- `risk_on_high->crypto_major_4h` score `5.9031` n `34` status `ready` deltaP `27.0804` edge `0.3497` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.9031` n `34` status `ready` deltaP `27.0804` edge `0.3497` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.3956` n `34` status `ready` deltaP `17.8623` edge `0.2865` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.3956` n `34` status `ready` deltaP `17.8623` edge `0.2865` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.064` n `34` status `ready` deltaP `22.1293` edge `0.0395` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.064` n `34` status `ready` deltaP `22.1293` edge `0.0395` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.2336` n `34` status `ready` deltaP `6.6625` edge `0.1427` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.2336` n `34` status `ready` deltaP `6.6625` edge `0.1427` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.33` n `34` status `ready` deltaP `8.2247` edge `0.0165` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.33` n `34` status `ready` deltaP `8.2247` edge `0.0165` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.3274` n `34` status `ready` deltaP `3.7953` edge `0.032` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3274` n `34` status `ready` deltaP `3.7953` edge `0.032` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.2701` n `34` status `ready` deltaP `3.9814` edge `-0.0013` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.2701` n `34` status `ready` deltaP `3.9814` edge `-0.0013` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.329` n `178` status `ready` deltaP `3.1084` edge `0.0008` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.5792` n `178` status `ready` deltaP `1.2346` edge `0.0214` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.5864` n `178` status `ready` deltaP `5.0192` edge `0.0324` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.5937` n `178` status `ready` deltaP `-0.4087` edge `-0.0113` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-0.6828` n `178` status `ready` deltaP `-1.3507` edge `0.0163` maxDD `-1.4688`
- `risk_on_high->commodity_4h` score `-0.7` n `34` status `ready` deltaP `-0.4753` edge `-0.0124` maxDD `-0.7546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
