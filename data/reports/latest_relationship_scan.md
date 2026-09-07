# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T03:52:25.688104+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10425`

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

- `risk_on_high->unknown_24h` score `549.7649` n `93` status `ready` deltaP `26.7361` edge `45.6355` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `549.7649` n `93` status `ready` deltaP `26.7361` edge `45.6355` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.1477` n `241` status `ready` deltaP `-2.9766` edge `2.1046` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `20.8608` n `93` status `ready` deltaP `33.899` edge `1.5641` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `20.8608` n `93` status `ready` deltaP `33.899` edge `1.5641` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `14.3654` n `93` status `ready` deltaP `30.9028` edge `0.9911` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.3654` n `93` status `ready` deltaP `30.9028` edge `0.9911` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.0884` n `182` status `ready` deltaP `24.3094` edge `0.6528` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.5848` n `182` status `ready` deltaP `23.0903` edge `0.3948` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.4004` n `117` status `ready` deltaP `29.4155` edge `0.2911` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.4004` n `117` status `ready` deltaP `29.4155` edge `0.2911` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.2864` n `93` status `ready` deltaP `23.0903` edge `0.2866` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.2864` n `93` status `ready` deltaP `23.0903` edge `0.2866` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.8812` n `117` status `ready` deltaP `22.1701` edge `0.2615` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.8812` n `117` status `ready` deltaP `22.1701` edge `0.2615` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7559` n `93` status `ready` deltaP `23.6839` edge `0.076` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7559` n `93` status `ready` deltaP `23.6839` edge `0.076` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6516` n `182` status `ready` deltaP `21.9646` edge `0.096` maxDD `-0.0505`
- `risk_on_high->metal_24h` score `1.0269` n `93` status `ready` deltaP `17.3611` edge `0.1315` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `1.0269` n `93` status `ready` deltaP `17.3611` edge `0.1315` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
