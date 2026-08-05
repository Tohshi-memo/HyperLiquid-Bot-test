# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T02:22:29.803182+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `15.3523` n `88` status `ready` deltaP `15.8775` edge `1.1778` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.6371` n `90` status `ready` deltaP `2.2053` edge `0.5546` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5459` n `90` status `ready` deltaP `16.9276` edge `0.1006` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.4346` n `88` status `ready` deltaP `3.488` edge `0.2775` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.0758` n `88` status `ready` deltaP `25.9943` edge `0.0852` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2773` n `90` status `ready` deltaP `5.642` edge `0.0271` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1039` n `90` status `ready` deltaP `7.006` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.057` n `90` status `ready` deltaP `13.0048` edge `0.0066` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5254` n `90` status `ready` deltaP `-1.3074` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6367` n `90` status `ready` deltaP `-1.0545` edge `-0.0212` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.6951` n `90` status `ready` deltaP `3.4891` edge `0.0111` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-0.7481` n `88` status `ready` deltaP `6.3447` edge `0.0061` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-0.8037` n `90` status `ready` deltaP `-2.9075` edge `-0.0126` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.2313` n `90` status `ready` deltaP `2.4187` edge `-0.035` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.6929` n `88` status `ready` deltaP `-5.2872` edge `0.0377` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8022` n `90` status `ready` deltaP `3.4531` edge `-0.1005` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1811` n `90` status `ready` deltaP `-13.1978` edge `-0.0662` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3136` n `90` status `ready` deltaP `2.0492` edge `-0.2451` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3937` n `90` status `ready` deltaP `-11.2608` edge `-0.0704` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-7.1334` n `88` status `ready` deltaP `4.577` edge `-0.1489` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
