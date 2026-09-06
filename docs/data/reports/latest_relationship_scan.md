# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T22:37:25.538316+00:00`
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

- `risk_on_high->unknown_24h` score `325.2312` n `107` status `ready` deltaP `26.9097` edge `26.9232` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `325.2312` n `107` status `ready` deltaP `26.9097` edge `26.9232` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.5389` n `107` status `ready` deltaP `33.9499` edge `1.4536` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.5389` n `107` status `ready` deltaP `33.9499` edge `1.4536` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.7968` n `107` status `ready` deltaP `30.0347` edge `0.9495` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.7968` n `107` status `ready` deltaP `30.0347` edge `0.9495` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.6966` n `196` status `ready` deltaP `23.9123` edge `0.6228` maxDD `-2.5998`
- `market_context_high->unknown_1h` score `8.1679` n `250` status `ready` deltaP `-4.109` edge `0.7805` maxDD `-2.4626`
- `market_context_high->equity_24h` score `6.8128` n `196` status `ready` deltaP `23.0903` edge `0.4138` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.5646` n `121` status `ready` deltaP `30.2951` edge `0.3507` maxDD `-0.116`
- `risk_on_and_context->crypto_alt_4h` score `6.5646` n `121` status `ready` deltaP `30.2951` edge `0.3507` maxDD `-0.116`
- `risk_on_high->equity_24h` score `5.9176` n `107` status `ready` deltaP `23.0903` edge `0.3392` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.9176` n `107` status `ready` deltaP `23.0903` edge `0.3392` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3299` n `121` status `ready` deltaP `24.0438` edge `0.2864` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3299` n `121` status `ready` deltaP `24.0438` edge `0.2864` maxDD `-3.8693`
- `market_context_high->index_24h` score `2.8489` n `196` status `ready` deltaP `22.6332` edge `0.096` maxDD `-0.0918`
- `risk_on_high->index_24h` score `2.7561` n `107` status `ready` deltaP `22.8907` edge `0.0813` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7561` n `107` status `ready` deltaP `22.8907` edge `0.0813` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.0794` n `130` status `ready` deltaP `4.802` edge `0.0895` maxDD `-0.8585`
- `risk_on_and_context->crypto_alt_1h` score `1.0794` n `130` status `ready` deltaP `4.802` edge `0.0895` maxDD `-0.8585`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
