# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T14:22:30.333305+00:00`
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

- `market_context_high->unknown_24h` score `5116.6165` n `98` status `ready` deltaP `13.4106` edge `426.3005` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `2476.3885` n `51` status `ready` deltaP `15.4514` edge `206.2627` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `2476.3885` n `51` status `ready` deltaP `15.4514` edge `206.2627` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.2731` n `82` status `ready` deltaP `-4.8014` edge `32.0136` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.7602` n `59` status `ready` deltaP `55.1995` edge `1.7854` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `17.7961` n `51` status `ready` deltaP `39.328` edge `1.2438` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.7961` n `51` status `ready` deltaP `39.328` edge `1.2438` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.7907` n `59` status `ready` deltaP `30.4878` edge `1.3281` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `15.5492` n `98` status `ready` deltaP `32.8054` edge `1.1598` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.4872` n `59` status `ready` deltaP `35.1519` edge `0.8161` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0317` n `51` status `ready` deltaP `38.5417` edge `0.4957` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0317` n `51` status `ready` deltaP `38.5417` edge `0.4957` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7557` n `98` status `ready` deltaP `38.5417` edge `0.4727` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6697` n `51` status `ready` deltaP `42.4408` edge `0.4767` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6697` n `51` status `ready` deltaP `42.4408` edge `0.4767` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.4855` n `59` status `ready` deltaP `54.5139` edge `0.3437` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9534` n `59` status `ready` deltaP `51.9921` edge `0.3255` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8644` n `51` status `ready` deltaP `49.4995` edge `0.0796` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8644` n `51` status `ready` deltaP `49.4995` edge `0.0796` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1457` n `51` status `ready` deltaP `36.974` edge `0.1083` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
