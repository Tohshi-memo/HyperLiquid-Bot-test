# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T04:52:23.788802+00:00`
- Price records: `672`
- Market context records: `7216`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13810`

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

- `risk_on_high->crypto_major_4h` score `5.8341` n `34` status `ready` deltaP `26.623` edge `0.347` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.8341` n `34` status `ready` deltaP `26.623` edge `0.347` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.3594` n `34` status `ready` deltaP `17.7098` edge `0.2845` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.3594` n `34` status `ready` deltaP `17.7098` edge `0.2845` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1048` n `34` status `ready` deltaP `22.5784` edge `0.0399` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1048` n `34` status `ready` deltaP `22.5784` edge `0.0399` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.1766` n `34` status `ready` deltaP `6.2051` edge `0.141` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.1766` n `34` status `ready` deltaP `6.2051` edge `0.141` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.3152` n `34` status `ready` deltaP `8.075` edge `0.0156` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3152` n `34` status `ready` deltaP `8.075` edge `0.0156` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2975` n `34` status `ready` deltaP `3.4959` edge `0.0315` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2975` n `34` status `ready` deltaP `3.4959` edge `0.0315` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.2575` n `34` status `ready` deltaP `4.1338` edge `-0.0007` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.2575` n `34` status `ready` deltaP `4.1338` edge `-0.0007` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.329` n `178` status `ready` deltaP `3.1084` edge `0.0008` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5672` n `178` status `ready` deltaP `0.0404` edge `-0.0109` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.5901` n `178` status `ready` deltaP `1.0849` edge `0.021` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6013` n `178` status `ready` deltaP `4.8695` edge `0.0315` maxDD `-7.6171`
- `risk_on_high->commodity_4h` score `-0.6538` n `34` status `ready` deltaP `-0.018` edge `-0.0116` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6538` n `34` status `ready` deltaP `-0.018` edge `-0.0116` maxDD `-0.7546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
