# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T22:22:14.494374+00:00`
- Price records: `672`
- Market context records: `1160`
- Flow alert records: `5242`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8750`

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

- `market_context_high->crypto_major_24h` score `20.6185` n `143` status `ready` deltaP `45.1195` edge `1.5306` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.0883` n `143` status `ready` deltaP `21.5132` edge `0.8989` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.7609` n `143` status `ready` deltaP `20.9924` edge `0.5998` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.9653` n `143` status `ready` deltaP `19.6035` edge `0.4222` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.5539` n `143` status `ready` deltaP `-2.9332` edge `0.6491` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4283` n `159` status `ready` deltaP `11.9832` edge `0.1888` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1341` n `159` status `ready` deltaP `8.9718` edge `0.103` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4351` n `159` status `ready` deltaP `7.0274` edge `0.0211` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3232` n `159` status `ready` deltaP `3.1343` edge `0.0438` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.1803` n `159` status `ready` deltaP `8.7955` edge `0.1566` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.1049` n `159` status `ready` deltaP `8.0424` edge `0.0007` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0417` n `159` status `ready` deltaP `7.4728` edge `0.0321` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3072` n `159` status `ready` deltaP `2.9517` edge `0.039` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.3611` n `159` status `ready` deltaP `6.0671` edge `-0.0095` maxDD `-2.2164`
- `market_context_high->unknown_24h` score `-0.4545` n `143` status `ready` deltaP `3.3739` edge `0.2126` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.8661` n `159` status `ready` deltaP `-3.6691` edge `-0.0058` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.9309` n `159` status `ready` deltaP `-2.5052` edge `-0.003` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.1036` n `159` status `ready` deltaP `5.1762` edge `0.1205` maxDD `-16.7194`
- `market_context_high->unknown_4h` score `-1.5835` n `159` status `ready` deltaP `7.0045` edge `-0.057` maxDD `-6.7322`
- `market_context_high->metal_4h` score `-1.7684` n `159` status `ready` deltaP `5.8627` edge `-0.0704` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
