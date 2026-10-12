# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T15:22:36.809990+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7550`

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

- `market_context_high->crypto_major_24h` score `25.3111` n `47` status `ready` deltaP `44.5257` edge `1.8602` maxDD `-2.4888`
- `market_context_high->crypto_alt_24h` score `24.776` n `47` status `ready` deltaP `32.7201` edge `1.9335` maxDD `-5.2904`
- `risk_on_high->crypto_alt_4h` score `4.0404` n `48` status `ready` deltaP `18.1911` edge `0.2602` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.0404` n `48` status `ready` deltaP `18.1911` edge `0.2602` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6052` n `48` status `ready` deltaP `33.1301` edge `0.3266` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6052` n `48` status `ready` deltaP `33.1301` edge `0.3266` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.3385` n `100` status `ready` deltaP `13.2744` edge `0.3346` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.1558` n `100` status `ready` deltaP `16.9634` edge `0.3058` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6448` n `100` status `ready` deltaP `12.3533` edge `0.1498` maxDD `-4.9401`
- `market_context_high->metal_24h` score `1.0878` n `47` status `ready` deltaP `18.7832` edge `0.0704` maxDD `-1.1599`
- `risk_on_high->crypto_alt_1h` score `1.0234` n `48` status `ready` deltaP `6.6866` edge `0.1004` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.0234` n `48` status `ready` deltaP `6.6866` edge `0.1004` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.6992` n `100` status `ready` deltaP `4.497` edge `0.1046` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4428` n `48` status `ready` deltaP `5.6637` edge `0.0843` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4428` n `48` status `ready` deltaP `5.6637` edge `0.0843` maxDD `-3.2233`
- `market_context_high->index_1h` score `-0.039` n `100` status `ready` deltaP `3.7751` edge `0.0029` maxDD `-0.3122`
- `market_context_high->unknown_4h` score `-0.0779` n `100` status `ready` deltaP `-4.689` edge `0.0894` maxDD `-1.8373`
- `market_context_high->metal_1h` score `-0.1045` n `100` status `ready` deltaP `6.4012` edge `0.0047` maxDD `-0.4868`
- `risk_on_high->metal_1h` score `-0.2872` n `48` status `ready` deltaP `3.5679` edge `0.0042` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.2872` n `48` status `ready` deltaP `3.5679` edge `0.0042` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
