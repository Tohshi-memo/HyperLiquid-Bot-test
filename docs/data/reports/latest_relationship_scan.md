# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T06:22:25.137137+00:00`
- Price records: `672`
- Market context records: `5013`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10194`

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

- `market_context_high->unknown_1h` score `15.4123` n `93` status `ready` deltaP `3.9679` edge `1.308` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0071` n `93` status `ready` deltaP `21.602` edge `0.7088` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.7257` n `93` status `ready` deltaP `17.8616` edge `0.5165` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3144` n `93` status `ready` deltaP `14.4834` edge `0.4857` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `2.1395` n `74` status `ready` deltaP `28.2517` edge `0.0242` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3791` n `93` status `ready` deltaP `14.7636` edge `0.1244` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.9591` n `93` status `ready` deltaP `9.085` edge `0.0767` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8872` n `93` status `ready` deltaP `6.8524` edge `0.12` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5603` n `93` status `ready` deltaP `4.7978` edge `0.178` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3784` n `93` status `ready` deltaP `6.4033` edge `0.0385` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1882` n `93` status `ready` deltaP `5.2604` edge `0.0913` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0413` n `93` status `ready` deltaP `4.7813` edge `0.0408` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1243` n `74` status `ready` deltaP `8.1691` edge `0.0058` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.2948` n `93` status `ready` deltaP `2.0073` edge `0.0148` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5323` n `93` status `ready` deltaP `2.5111` edge `0.013` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7861` n `93` status `ready` deltaP `4.0028` edge `-0.0022` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.984` n `93` status `ready` deltaP `-3.7634` edge `-0.0022` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.733` n `93` status `ready` deltaP `-11.6992` edge `-0.0054` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.9966` n `74` status `ready` deltaP `2.4306` edge `0.0169` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.3331` n `74` status `ready` deltaP `4.0587` edge `-0.0717` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
