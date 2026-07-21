# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T01:37:25.561421+00:00`
- Price records: `672`
- Market context records: `7412`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14677`

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

- `risk_on_high->crypto_major_4h` score `6.3602` n `32` status `ready` deltaP `36.3567` edge `0.3069` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.3602` n `32` status `ready` deltaP `36.3567` edge `0.3069` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `5.3351` n `32` status `ready` deltaP `16.7732` edge `0.4349` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `5.3351` n `32` status `ready` deltaP `16.7732` edge `0.4349` maxDD `-5.8371`
- `risk_on_high->unknown_4h` score `5.0601` n `32` status `ready` deltaP `16.4634` edge `0.3549` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.0601` n `32` status `ready` deltaP `16.4634` edge `0.3549` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.8314` n `32` status `ready` deltaP `27.9726` edge `0.2405` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.8314` n `32` status `ready` deltaP `27.9726` edge `0.2405` maxDD `-0.9492`
- `risk_on_high->crypto_alt_24h` score `2.7699` n `32` status `ready` deltaP `17.0927` edge `0.334` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.7699` n `32` status `ready` deltaP `17.0927` edge `0.334` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.1201` n `32` status `ready` deltaP `19.3301` edge `0.0392` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.1201` n `32` status `ready` deltaP `19.3301` edge `0.0392` maxDD `-0.957`
- `risk_on_high->equity_24h` score `0.4934` n `31` status `ready` deltaP `12.9257` edge `0.2263` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `0.4934` n `31` status `ready` deltaP `12.9257` edge `0.2263` maxDD `-19.375`
- `risk_on_high->commodity_1h` score `0.4409` n `32` status `ready` deltaP `5.6494` edge `0.027` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.4409` n `32` status `ready` deltaP `5.6494` edge `0.027` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1249` n `32` status `ready` deltaP `3.4535` edge `0.0307` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1249` n `32` status `ready` deltaP `3.4535` edge `0.0307` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0192` n `32` status `ready` deltaP `-0.4491` edge `0.0376` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0192` n `32` status `ready` deltaP `-0.4491` edge `0.0376` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
