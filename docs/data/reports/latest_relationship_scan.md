# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T16:37:35.778970+00:00`
- Price records: `672`
- Market context records: `4109`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10552`

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

- `risk_on_high->unknown_4h` score `144.7211` n `40` status `ready` deltaP `-9.1159` edge `12.3025` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7211` n `40` status `ready` deltaP `-9.1159` edge `12.3025` maxDD `-10.864`
- `market_context_high->unknown_1h` score `43.6667` n `188` status `ready` deltaP `1.8538` edge `3.7843` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `34.6127` n `147` status `ready` deltaP `-8.7372` edge `3.3455` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `15.3437` n `179` status `ready` deltaP `-1.8114` edge `1.833` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.7109` n `40` status `ready` deltaP `36.8293` edge `-0.0149` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.7109` n `40` status `ready` deltaP `36.8293` edge `-0.0149` maxDD `-0.0446`
- `risk_on_high->crypto_major_4h` score `0.1965` n `40` status `ready` deltaP `17.1646` edge `-0.0315` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.1965` n `40` status `ready` deltaP `17.1646` edge `-0.0315` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.1508` n `40` status `ready` deltaP `10.7635` edge `-0.0201` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.1508` n `40` status `ready` deltaP `10.7635` edge `-0.0201` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.0906` n `40` status `ready` deltaP `10.2439` edge `0.0024` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0906` n `40` status `ready` deltaP `10.2439` edge `0.0024` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0474` n `40` status `ready` deltaP `4.2515` edge `0.0007` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0474` n `40` status `ready` deltaP `4.2515` edge `0.0007` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0573` n `40` status `ready` deltaP `10.0599` edge `-0.0202` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0573` n `40` status `ready` deltaP `10.0599` edge `-0.0202` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `-0.1973` n `40` status `ready` deltaP `-2.0833` edge `0.2256` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `-0.1973` n `40` status `ready` deltaP `-2.0833` edge `0.2256` maxDD `-12.9187`
- `market_context_high->fx_1h` score `-0.2757` n `188` status `ready` deltaP `1.9111` edge `0.0004` maxDD `-0.546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
