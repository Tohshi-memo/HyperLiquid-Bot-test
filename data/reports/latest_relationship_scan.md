# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T06:37:23.731943+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6337`

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

- `market_context_high->unknown_24h` score `6866.6965` n `56` status `ready` deltaP `4.8611` edge `572.1923` maxDD `0.0`
- `market_context_high->unknown_4h` score `361.3973` n `56` status `ready` deltaP `5.3789` edge `30.0849` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `80.254` n `108` status `ready` deltaP `-5.1951` edge `6.7511` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `45.8129` n `56` status `ready` deltaP `2.6091` edge `3.8114` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.338` n `56` status `ready` deltaP `45.0397` edge `1.5015` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2459` n `98` status `ready` deltaP `31.0268` edge `1.0326` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.083` n `56` status `ready` deltaP `58.8046` edge `0.2031` maxDD `-0.0568`
- `market_context_high->commodity_24h` score `6.4902` n `56` status `ready` deltaP `44.9901` edge `0.272` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.5066` n `56` status `ready` deltaP `22.3214` edge `0.3395` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.2098` n `56` status `ready` deltaP `29.2466` edge `0.2728` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.9579` n `108` status `ready` deltaP `18.75` edge `0.4268` maxDD `-7.4246`
- `market_context_high->equity_4h` score `3.239` n `56` status `ready` deltaP `5.3136` edge `0.3047` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.225` n `56` status `ready` deltaP `30.5531` edge `0.0943` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.5023` n `56` status `ready` deltaP `11.1111` edge `0.3144` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.8702` n `56` status `ready` deltaP `-4.6875` edge `0.4228` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6138` n `56` status `ready` deltaP `19.1202` edge `0.0495` maxDD `-0.7323`
- `market_context_high->crypto_major_1h` score `1.4309` n `56` status `ready` deltaP `8.7789` edge `0.1217` maxDD `-2.2118`
- `market_context_high->equity_1h` score `1.3285` n `56` status `ready` deltaP `1.1869` edge `0.1553` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.142` n `56` status `ready` deltaP `2.9833` edge `0.1485` maxDD `-2.5243`
- `market_context_high->metal_1h` score `0.9233` n `56` status `ready` deltaP `11.4735` edge `0.0253` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
