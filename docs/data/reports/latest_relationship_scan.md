# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T15:07:25.393889+00:00`
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

- `market_context_high->unknown_24h` score `5688.3766` n `95` status `ready` deltaP `13.3461` edge `473.9476` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `3107.7949` n `49` status `ready` deltaP `15.4514` edge `258.8799` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `3107.7949` n `49` status `ready` deltaP `15.4514` edge `258.8799` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.1099` n `82` status `ready` deltaP `-5.2505` edge `32.003` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.9266` n `59` status `ready` deltaP `55.7203` edge `1.7958` maxDD `-5.8705`
- `news_risk_high->crypto_alt_24h` score `17.9164` n `59` status `ready` deltaP `31.0087` edge `1.3351` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `17.7673` n `49` status `ready` deltaP `39.4487` edge `1.2406` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.7673` n `49` status `ready` deltaP `39.4487` edge `1.2406` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.5292` n `95` status `ready` deltaP `32.8107` edge `1.1581` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.5588` n `59` status `ready` deltaP `35.6727` edge `0.8186` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.161` n `49` status `ready` deltaP `39.0625` edge `0.503` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.161` n `49` status `ready` deltaP `39.0625` edge `0.503` maxDD `0.0`
- `market_context_high->equity_24h` score `8.8754` n `95` status `ready` deltaP `39.0625` edge `0.4792` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6673` n `49` status `ready` deltaP `42.2008` edge `0.4781` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6673` n `49` status `ready` deltaP `42.2008` edge `0.4781` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.5066` n `59` status `ready` deltaP `54.6875` edge `0.3443` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9522` n `59` status `ready` deltaP `51.9921` edge `0.3254` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8512` n `49` status `ready` deltaP `49.2595` edge `0.0801` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8512` n `49` status `ready` deltaP `49.2595` edge `0.0801` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1117` n `49` status `ready` deltaP `36.6538` edge `0.1076` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
