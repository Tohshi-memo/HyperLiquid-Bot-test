# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T11:52:39.290195+00:00`
- Price records: `672`
- Market context records: `4089`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10240`

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

- `risk_on_high->unknown_4h` score `144.6315` n `40` status `ready` deltaP `-8.811` edge `12.293` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.6315` n `40` status `ready` deltaP `-8.811` edge `12.293` maxDD `-10.864`
- `market_context_high->unknown_1h` score `48.6468` n `177` status `ready` deltaP `2.199` edge `4.197` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.0637` n `144` status `ready` deltaP `-9.2396` edge `3.5531` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `16.6659` n `172` status `ready` deltaP `-2.9389` edge `1.9507` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.2891` n `40` status `ready` deltaP `36.6768` edge `0.0343` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2891` n `40` status `ready` deltaP `36.6768` edge `0.0343` maxDD `-0.0446`
- `market_context_high->equity_4h` score `0.9138` n `172` status `ready` deltaP `13.5954` edge `0.1386` maxDD `-6.9137`
- `market_context_high->equity_1h` score `0.6508` n `177` status `ready` deltaP `5.1448` edge `0.0759` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.452` n `40` status `ready` deltaP `11.0629` edge `0.003` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.452` n `40` status `ready` deltaP `11.0629` edge `0.003` maxDD `-0.7937`
- `market_context_high->index_24h` score `0.3782` n `144` status `ready` deltaP `15.078` edge `-0.069` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `0.2475` n `40` status `ready` deltaP `16.7073` edge `-0.0242` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.2475` n `40` status `ready` deltaP `16.7073` edge `-0.0242` maxDD `-2.6576`
- `risk_on_high->fx_4h` score `0.1816` n `40` status `ready` deltaP `11.7683` edge `0.0039` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1816` n `40` status `ready` deltaP `11.7683` edge `0.0039` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0661` n `40` status `ready` deltaP `4.5509` edge `0.0011` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0661` n `40` status `ready` deltaP `4.5509` edge `0.0011` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.0416` n `40` status `ready` deltaP `10.9581` edge `-0.0135` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0416` n `40` status `ready` deltaP `10.9581` edge `-0.0135` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
