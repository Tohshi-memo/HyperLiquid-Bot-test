# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T10:22:24.659514+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8030`

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

- `market_context_high->unknown_4h` score `23.4361` n `112` status `ready` deltaP `-3.3537` edge `2.04` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `21.7503` n `45` status `ready` deltaP `30.8333` edge `1.7501` maxDD `-7.1173`
- `market_context_high->crypto_alt_24h` score `20.6826` n `45` status `ready` deltaP `19.2014` edge `1.7832` maxDD `-10.6793`
- `risk_on_high->crypto_alt_4h` score `3.7776` n `48` status `ready` deltaP `18.1911` edge `0.2383` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.7776` n `48` status `ready` deltaP `18.1911` edge `0.2383` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.441` n `48` status `ready` deltaP `32.6728` edge `0.3086` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.441` n `48` status `ready` deltaP `32.6728` edge `0.3086` maxDD `-4.1548`
- `market_context_high->unknown_1h` score `2.6609` n `112` status `ready` deltaP `-3.4538` edge `0.2784` maxDD `-1.024`
- `market_context_high->equity_24h` score `2.6268` n `45` status `ready` deltaP `3.0556` edge `0.4567` maxDD `-7.5571`
- `market_context_high->index_24h` score `1.766` n `45` status `ready` deltaP `25.3125` edge `0.1137` maxDD `-0.4833`
- `market_context_high->crypto_major_4h` score `1.4848` n `112` status `ready` deltaP `12.4347` edge `0.2437` maxDD `-10.5626`
- `market_context_high->metal_24h` score `0.9784` n `45` status `ready` deltaP `14.5139` edge `0.0581` maxDD `-1.866`
- `market_context_high->crypto_alt_1h` score `0.8998` n `112` status `ready` deltaP `8.0197` edge `0.1166` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.816` n `48` status `ready` deltaP `5.6387` edge `0.0901` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.816` n `48` status `ready` deltaP `5.6387` edge `0.0901` maxDD `-2.4421`
- `market_context_high->crypto_alt_4h` score `0.7599` n `112` status `ready` deltaP `5.9887` edge `0.2512` maxDD `-12.8907`
- `risk_on_high->crypto_major_1h` score `0.3469` n `48` status `ready` deltaP `4.7655` edge `0.078` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3469` n `48` status `ready` deltaP `4.7655` edge `0.078` maxDD `-3.2233`
- `market_context_high->crypto_major_1h` score `0.1442` n `112` status `ready` deltaP `2.3845` edge `0.0789` maxDD `-3.4384`
- `market_context_high->metal_1h` score `-0.2071` n `112` status `ready` deltaP `4.1595` edge `0.0018` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
