# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T08:07:30.119747+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `risk_on_high->unknown_4h` score `7.2583` n `107` status `ready` deltaP `20.6776` edge `0.5288` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2583` n `107` status `ready` deltaP `20.6776` edge `0.5288` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8049` n `151` status `ready` deltaP `16.9702` edge `0.4401` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.1622` n `107` status `ready` deltaP `4.7191` edge `0.2064` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.1622` n `107` status `ready` deltaP `4.7191` edge `0.2064` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0314` n `151` status `ready` deltaP `4.0816` edge `0.2051` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.2562` n `61` status `ready` deltaP `1.8234` edge `0.1272` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.8924` n `107` status `ready` deltaP `10.6893` edge `0.1019` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8924` n `107` status `ready` deltaP `10.6893` edge `0.1019` maxDD `-0.5706`
- `market_context_high->commodity_24h` score `0.2963` n `151` status `ready` deltaP `10.0579` edge `0.0772` maxDD `-1.2314`
- `news_risk_high->fx_4h` score `0.1535` n `61` status `ready` deltaP `10.6533` edge `0.0011` maxDD `-0.7461`
- `risk_on_high->crypto_alt_24h` score `0.0225` n `107` status `ready` deltaP `11.7082` edge `0.6152` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.0225` n `107` status `ready` deltaP `11.7082` edge `0.6152` maxDD `-42.8959`
- `market_context_high->commodity_1h` score `0.0154` n `151` status `ready` deltaP `7.8241` edge `0.0141` maxDD `-1.5315`
- `risk_on_high->index_1h` score `0.0076` n `107` status `ready` deltaP `6.7463` edge `0.0005` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0076` n `107` status `ready` deltaP `6.7463` edge `0.0005` maxDD `-0.5605`
- `risk_on_high->commodity_1h` score `-0.0633` n `107` status `ready` deltaP `4.7233` edge `0.0126` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0633` n `107` status `ready` deltaP `4.7233` edge `0.0126` maxDD `-0.8428`
- `risk_on_high->metal_1h` score `-0.0653` n `107` status `ready` deltaP `9.8495` edge `-0.0028` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0653` n `107` status `ready` deltaP `9.8495` edge `-0.0028` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
