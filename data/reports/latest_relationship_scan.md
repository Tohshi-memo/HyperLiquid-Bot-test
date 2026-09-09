# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T19:22:28.498679+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10148`

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

- `risk_on_high->crypto_alt_24h` score `11.0021` n `117` status `ready` deltaP `24.1987` edge `0.7785` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `11.0021` n `117` status `ready` deltaP `24.1987` edge `0.7785` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `5.9547` n `241` status `ready` deltaP `16.8539` edge `0.4666` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `5.8987` n `117` status `ready` deltaP `33.3789` edge `0.3062` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8987` n `117` status `ready` deltaP `33.3789` edge `0.3062` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.6868` n `117` status `ready` deltaP `19.8852` edge `1.0033` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.6868` n `117` status `ready` deltaP `19.8852` edge `1.0033` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.086` n `117` status `ready` deltaP `23.6945` edge `0.2684` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.086` n `117` status `ready` deltaP `23.6945` edge `0.2684` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4136` n `117` status `ready` deltaP `24.5192` edge `0.0419` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4136` n `117` status `ready` deltaP `24.5192` edge `0.0419` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.6921` n `241` status `ready` deltaP `19.6144` edge `0.0496` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.1525` n `241` status `ready` deltaP `7.9861` edge `0.0428` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `0.9322` n `117` status `ready` deltaP `3.9473` edge `0.0866` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9322` n `117` status `ready` deltaP `3.9473` edge `0.0866` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7504` n `117` status `ready` deltaP `19.7383` edge `0.0802` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7504` n `117` status `ready` deltaP `19.7383` edge `0.0802` maxDD `-0.9131`
- `risk_on_high->equity_24h` score `0.4673` n `117` status `ready` deltaP `7.9861` edge `-0.0143` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.4673` n `117` status `ready` deltaP `7.9861` edge `-0.0143` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.3646` n `117` status `ready` deltaP `13.7738` edge `-0.0083` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
