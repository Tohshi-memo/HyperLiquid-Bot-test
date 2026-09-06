# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T22:07:26.133810+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10593`

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

- `risk_on_high->unknown_24h` score `329.9126` n `105` status `ready` deltaP `27.2569` edge `27.311` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `329.9126` n `105` status `ready` deltaP `27.2569` edge `27.311` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `20.0372` n `105` status `ready` deltaP `34.5685` edge `1.491` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `20.0372` n `105` status `ready` deltaP `34.5685` edge `1.491` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `14.1215` n `105` status `ready` deltaP `30.2083` edge `0.9754` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.1215` n `105` status `ready` deltaP `30.2083` edge `0.9754` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.6085` n `196` status `ready` deltaP `23.5756` edge `0.6177` maxDD `-2.5998`
- `market_context_high->unknown_1h` score `8.1559` n `250` status `ready` deltaP `-4.109` edge `0.7795` maxDD `-2.4626`
- `market_context_high->equity_24h` score `6.8176` n `196` status `ready` deltaP `23.0903` edge `0.4142` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.7153` n `119` status `ready` deltaP `30.5583` edge `0.3615` maxDD `-0.116`
- `risk_on_and_context->crypto_alt_4h` score `6.7153` n `119` status `ready` deltaP `30.5583` edge `0.3615` maxDD `-0.116`
- `risk_on_high->equity_24h` score `6.0412` n `105` status `ready` deltaP `23.0903` edge `0.3495` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.0412` n `105` status `ready` deltaP `23.0903` edge `0.3495` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.5301` n `119` status `ready` deltaP `24.7309` edge `0.2985` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.5301` n `119` status `ready` deltaP `24.7309` edge `0.2985` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.8719` n `105` status `ready` deltaP `23.9633` edge `0.0838` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8719` n `105` status `ready` deltaP `23.9633` edge `0.0838` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6949` n `196` status `ready` deltaP `22.2967` edge `0.0955` maxDD `-0.232`
- `risk_on_high->crypto_alt_1h` score `1.306` n `128` status `ready` deltaP `5.7635` edge `0.1003` maxDD `-0.7247`
- `risk_on_and_context->crypto_alt_1h` score `1.306` n `128` status `ready` deltaP `5.7635` edge `0.1003` maxDD `-0.7247`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
