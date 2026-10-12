# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T12:37:27.178278+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7870`

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

- `market_context_high->crypto_alt_24h` score `29.5422` n `41` status `ready` deltaP `36.7717` edge `2.2617` maxDD `-2.2663`
- `market_context_high->crypto_major_24h` score `27.8516` n `41` status `ready` deltaP `48.4036` edge `2.036` maxDD `-1.6845`
- `risk_on_high->crypto_alt_4h` score `3.924` n `48` status `ready` deltaP `18.1911` edge `0.2505` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.924` n `48` status `ready` deltaP `18.1911` edge `0.2505` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.5239` n `48` status `ready` deltaP `32.9777` edge `0.3172` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.5239` n `48` status `ready` deltaP `32.9777` edge `0.3172` maxDD `-4.1548`
- `market_context_high->metal_24h` score `3.3795` n `41` status `ready` deltaP `29.9924` edge `0.0991` maxDD `-0.3941`
- `market_context_high->crypto_major_4h` score `2.525` n `103` status `ready` deltaP `15.9469` edge `0.2819` maxDD `-8.5569`
- `market_context_high->crypto_alt_4h` score `2.483` n `103` status `ready` deltaP `11.2938` edge `0.2993` maxDD `-11.0808`
- `market_context_high->crypto_alt_1h` score `1.4808` n `103` status `ready` deltaP `11.6825` edge `0.1406` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.8675` n `48` status `ready` deltaP `5.9381` edge `0.0924` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8675` n `48` status `ready` deltaP `5.9381` edge `0.0924` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.5884` n `103` status `ready` deltaP `4.1466` edge `0.0977` maxDD `-3.4384`
- `market_context_high->index_24h` score `0.4205` n `41` status `ready` deltaP `11.6446` edge `0.063` maxDD `-1.2711`
- `risk_on_high->crypto_major_1h` score `0.3641` n `48` status `ready` deltaP `4.9152` edge `0.0792` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3641` n `48` status `ready` deltaP `4.9152` edge `0.0792` maxDD `-3.2233`
- `market_context_high->index_1h` score `-0.0044` n `103` status `ready` deltaP `4.4416` edge `0.0029` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.0474` n `103` status `ready` deltaP `7.0548` edge `0.0051` maxDD `-0.4868`
- `market_context_high->unknown_4h` score `-0.15` n `103` status `ready` deltaP `-4.8395` edge `0.0844` maxDD `-1.8373`
- `risk_on_high->metal_1h` score `-0.3411` n `48` status `ready` deltaP `2.9691` edge `0.0037` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
