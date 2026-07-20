# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T23:22:27.020003+00:00`
- Price records: `672`
- Market context records: `7401`
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

- `risk_on_high->crypto_major_4h` score `6.3362` n `32` status `ready` deltaP `36.3567` edge `0.3049` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.3362` n `32` status `ready` deltaP `36.3567` edge `0.3049` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.9633` n `32` status `ready` deltaP `15.8537` edge `0.3509` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9633` n `32` status `ready` deltaP `15.8537` edge `0.3509` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.794` n `32` status `ready` deltaP `27.8201` edge `0.2384` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.794` n `32` status `ready` deltaP `27.8201` edge `0.2384` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.11` n `32` status `ready` deltaP `19.3301` edge `0.0379` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.11` n `32` status `ready` deltaP `19.3301` edge `0.0379` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.4048` n `32` status `ready` deltaP `5.3491` edge `0.026` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.4048` n `32` status `ready` deltaP `5.3491` edge `0.026` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1421` n `32` status `ready` deltaP `3.7538` edge `0.0309` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1421` n `32` status `ready` deltaP `3.7538` edge `0.0309` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0457` n `32` status `ready` deltaP `-0.5988` edge `0.0352` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0457` n `32` status `ready` deltaP `-0.5988` edge `0.0352` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.1326` n `32` status `ready` deltaP `0.0` edge `0.0713` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1326` n `32` status `ready` deltaP `0.0` edge `0.0713` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1639` n `132` status `ready` deltaP `4.2315` edge `-0.0001` maxDD `-0.5967`
- `market_context_high->commodity_1h` score `-0.5244` n `132` status `ready` deltaP `-0.9009` edge `-0.004` maxDD `-1.5775`
- `market_context_high->unknown_4h` score `-0.7933` n `132` status `ready` deltaP `4.3007` edge `0.1055` maxDD `-6.2031`
- `market_context_high->commodity_4h` score `-0.9215` n `132` status `ready` deltaP `1.3275` edge `0.0112` maxDD `-2.4139`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
