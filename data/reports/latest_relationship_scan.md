# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T21:07:24.815791+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10401`

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

- `risk_on_high->unknown_24h` score `281.7688` n `105` status `ready` deltaP `26.4782` edge `23.3089` maxDD `-0.0416`
- `risk_on_and_context->unknown_24h` score `281.7688` n `105` status `ready` deltaP `26.4782` edge `23.3089` maxDD `-0.0416`
- `risk_on_high->crypto_major_24h` score `19.8022` n `105` status `ready` deltaP `33.0109` edge `1.4818` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.8022` n `105` status `ready` deltaP `33.0109` edge `1.4818` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.2168` n `105` status `ready` deltaP `27.8721` edge `0.9314` maxDD `-0.5987`
- `risk_on_and_context->crypto_alt_24h` score `13.2168` n `105` status `ready` deltaP `27.8721` edge `0.9314` maxDD `-0.5987`
- `market_context_high->crypto_alt_24h` score `8.2997` n `196` status `ready` deltaP `22.5659` edge `0.5987` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.7852` n `196` status `ready` deltaP `23.0903` edge `0.4115` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.9668` n `105` status `ready` deltaP `23.0903` edge `0.3433` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.9668` n `105` status `ready` deltaP `23.0903` edge `0.3433` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `4.4116` n `119` status `ready` deltaP `27.8066` edge `0.292` maxDD `-7.4461`
- `risk_on_and_context->crypto_alt_4h` score `4.4116` n `119` status `ready` deltaP `27.8066` edge `0.292` maxDD `-7.4461`
- `risk_on_high->crypto_major_4h` score `2.7633` n `119` status `ready` deltaP `21.9794` edge `0.2317` maxDD `-8.8363`
- `risk_on_and_context->crypto_major_4h` score `2.7633` n `119` status `ready` deltaP `21.9794` edge `0.2317` maxDD `-8.8363`
- `risk_on_high->index_24h` score `2.3619` n `105` status `ready` deltaP `20.8482` edge `0.0797` maxDD `-0.4157`
- `risk_on_and_context->index_24h` score `2.3619` n `105` status `ready` deltaP `20.8482` edge `0.0797` maxDD `-0.4157`
- `market_context_high->index_24h` score `2.3045` n `196` status `ready` deltaP `20.9503` edge `0.0938` maxDD `-0.6478`
- `risk_on_high->metal_24h` score `0.6845` n `105` status `ready` deltaP `13.4623` edge `0.1011` maxDD `-2.2469`
- `risk_on_and_context->metal_24h` score `0.6845` n `105` status `ready` deltaP `13.4623` edge `0.1011` maxDD `-2.2469`
- `risk_on_high->crypto_alt_1h` score `0.6678` n `128` status `ready` deltaP `3.8688` edge `0.0784` maxDD `-2.2169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
