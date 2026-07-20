# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T12:58:04.212735+00:00`
- Price records: `672`
- Market context records: `7356`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14631`

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

- `risk_on_high->crypto_major_4h` score `6.9713` n `32` status `ready` deltaP `38.4909` edge `0.3436` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.9713` n `32` status `ready` deltaP `38.4909` edge `0.3436` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.7219` n `32` status `ready` deltaP `31.7835` edge `0.2893` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.7219` n `32` status `ready` deltaP `31.7835` edge `0.2893` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.3373` n `32` status `ready` deltaP `18.2927` edge `0.3658` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.3373` n `32` status `ready` deltaP `18.2927` edge `0.3658` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2199` n `32` status `ready` deltaP `19.9289` edge `0.048` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2199` n `32` status `ready` deltaP `19.9289` edge `0.048` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2463` n `32` status `ready` deltaP `4.1479` edge `0.0208` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2463` n `32` status `ready` deltaP `4.1479` edge `0.0208` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1811` n `32` status `ready` deltaP `4.2042` edge `0.0329` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1811` n `32` status `ready` deltaP `4.2042` edge `0.0329` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1157` n `32` status `ready` deltaP `0.5988` edge `0.0479` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1157` n `32` status `ready` deltaP `0.5988` edge `0.0479` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.1298` n `32` status `ready` deltaP `-0.6098` edge `0.0756` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1298` n `32` status `ready` deltaP `-0.6098` edge `0.0756` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1715` n `129` status `ready` deltaP `4.089` edge `-0.0003` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5737` n `129` status `ready` deltaP `6.2287` edge `0.1208` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7159` n `129` status `ready` deltaP `-3.2649` edge `-0.0128` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.8093` n `129` status `ready` deltaP `-5.3111` edge `-0.0075` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
