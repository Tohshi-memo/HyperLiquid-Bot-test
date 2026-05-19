# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T05:37:16.863166+00:00`
- Price records: `672`
- Market context records: `1190`
- Flow alert records: `5332`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.4632` n `139` status `ready` deltaP `44.4432` edge `1.3555` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.7858` n `139` status `ready` deltaP `22.1473` edge `0.7028` maxDD `-15.1306`
- `market_context_high->metal_24h` score `4.2556` n `139` status `ready` deltaP `-3.5772` edge `0.5452` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `3.9585` n `139` status `ready` deltaP `4.4141` edge `0.4221` maxDD `-6.7322`
- `market_context_high->equity_4h` score `2.8547` n `139` status `ready` deltaP `15.1232` edge `0.2034` maxDD `-3.6396`
- `market_context_high->equity_24h` score `2.3178` n `139` status `ready` deltaP `15.9198` edge `0.3197` maxDD `-14.2815`
- `market_context_high->index_24h` score `2.1902` n `139` status `ready` deltaP `15.6225` edge `0.187` maxDD `-5.3574`
- `market_context_high->index_4h` score `1.038` n `139` status `ready` deltaP `10.7398` edge `0.0832` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6044` n `139` status `ready` deltaP `9.1888` edge `0.0208` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5475` n `139` status `ready` deltaP `4.8141` edge `0.0513` maxDD `-1.3546`
- `market_context_high->commodity_24h` score `0.2284` n `139` status `ready` deltaP `-4.1017` edge `0.5058` maxDD `-30.9337`
- `market_context_high->crypto_major_4h` score `-0.0688` n `139` status `ready` deltaP `7.5298` edge `0.1331` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1097` n `139` status `ready` deltaP `4.8303` edge `-0.0007` maxDD `-0.3124`
- `market_context_high->fx_24h` score `-0.1835` n `139` status `ready` deltaP `7.534` edge `0.0419` maxDD `-5.5859`
- `market_context_high->metal_1h` score `-0.1948` n `139` status `ready` deltaP `8.4608` edge `-0.0116` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3352` n `139` status `ready` deltaP `3.6284` edge `0.0094` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.4737` n `139` status `ready` deltaP `-0.4135` edge `0.0263` maxDD `-3.4088`
- `market_context_high->unknown_24h` score `-0.9343` n `139` status `ready` deltaP `2.9414` edge `0.1755` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.9416` n `139` status `ready` deltaP `-3.2374` edge `0.0046` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.1652` n `139` status `ready` deltaP `4.6204` edge `0.1163` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
