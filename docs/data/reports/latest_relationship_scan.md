# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T16:53:04.949440+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12636`

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

- `market_context_high->unknown_24h` score `7173.8564` n `88` status `ready` deltaP `13.1787` edge `597.7387` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `5354.5897` n `43` status `ready` deltaP `15.4514` edge `446.1128` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5354.5897` n `43` status `ready` deltaP `15.4514` edge `446.1128` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.0283` n `82` status `ready` deltaP `-5.1008` edge `31.9952` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `22.4208` n `64` status `ready` deltaP `49.6528` edge `1.6316` maxDD `-5.8705`
- `news_risk_high->crypto_alt_24h` score `16.9784` n `64` status `ready` deltaP `28.2986` edge `1.275` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `16.5479` n `43` status `ready` deltaP `38.5457` edge `1.145` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.5479` n `43` status `ready` deltaP `38.5457` edge `1.145` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.8733` n `88` status `ready` deltaP `31.9918` edge `1.1089` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `10.8448` n `64` status `ready` deltaP `29.3403` edge `0.7477` maxDD `-1.4989`
- `risk_on_high->equity_24h` score `9.5846` n `43` status `ready` deltaP `40.2778` edge `0.5302` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.5846` n `43` status `ready` deltaP `40.2778` edge `0.5302` maxDD `0.0`
- `market_context_high->equity_24h` score `9.173` n `88` status `ready` deltaP `40.2778` edge `0.4959` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4993` n `43` status `ready` deltaP `41.3465` edge `0.4698` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4993` n `43` status `ready` deltaP `41.3465` edge `0.4698` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.3388` n `64` status `ready` deltaP `48.2639` edge `0.3033` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `7.3214` n `64` status `ready` deltaP `46.7014` edge `0.3235` maxDD `-0.3112`
- `risk_on_high->index_24h` score `4.8684` n `43` status `ready` deltaP `49.0997` edge `0.0826` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8684` n `43` status `ready` deltaP `49.0997` edge `0.0826` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1327` n `43` status `ready` deltaP `35.9721` edge `0.1139` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
