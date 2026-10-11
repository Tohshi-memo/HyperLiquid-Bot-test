# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T05:22:27.890563+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5933`

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

- `market_context_high->unknown_4h` score `37.8229` n `85` status `ready` deltaP `-11.51` edge `3.2781` maxDD `-1.9565`
- `market_context_high->crypto_major_24h` score `8.2981` n `80` status `ready` deltaP `16.5278` edge `1.2685` maxDD `-17.8526`
- `market_context_high->equity_24h` score `2.1928` n `80` status `ready` deltaP `22.1875` edge `0.2159` maxDD `-2.6148`
- `market_context_high->crypto_major_4h` score `1.0372` n `85` status `ready` deltaP `12.7009` edge `0.1915` maxDD `-7.7892`
- `market_context_high->crypto_major_1h` score `0.1477` n `97` status `ready` deltaP `8.4295` edge `0.045` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `-0.5989` n `80` status `ready` deltaP `4.1319` edge `0.5069` maxDD `-35.5652`
- `market_context_high->metal_1h` score `-0.7178` n `97` status `ready` deltaP `-5.8368` edge `-0.0007` maxDD `-0.1927`
- `market_context_high->metal_4h` score `-1.1679` n `85` status `ready` deltaP `-10.2619` edge `-0.0016` maxDD `-0.3771`
- `market_context_high->crypto_alt_1h` score `-1.2176` n `97` status `ready` deltaP `-1.747` edge `0.0261` maxDD `-4.9401`
- `market_context_high->equity_1h` score `-2.1365` n `97` status `ready` deltaP `-13.4036` edge `-0.012` maxDD `-1.8011`
- `market_context_high->metal_24h` score `-2.3101` n `80` status `ready` deltaP `-16.9792` edge `-0.0113` maxDD `-1.0674`
- `market_context_high->crypto_alt_4h` score `-3.0616` n `85` status `ready` deltaP `-12.482` edge `0.0436` maxDD `-10.5748`
- `market_context_high->unknown_1h` score `-3.6438` n `97` status `ready` deltaP `-7.343` edge `-0.2226` maxDD `-0.9012`
- `market_context_high->equity_4h` score `-3.6587` n `85` status `ready` deltaP `-11.0438` edge `-0.0457` maxDD `-5.8456`
- `market_context_high->commodity_24h` score `-4.0` n `80` status `ready` deltaP `0.0` edge `0.0` maxDD `0.0`
- `market_context_high->index_24h` score `-4.0` n `80` status `ready` deltaP `0.0` edge `0.0` maxDD `0.0`
- `market_context_high->fx_24h` score `-4.0` n `80` status `ready` deltaP `0.0` edge `0.0` maxDD `0.0`
- `market_context_high->commodity_4h` score `-4.25` n `85` status `ready` deltaP `0.0` edge `0.0` maxDD `0.0`
- `market_context_high->index_4h` score `-4.25` n `85` status `ready` deltaP `0.0` edge `0.0` maxDD `0.0`
- `market_context_high->fx_4h` score `-4.25` n `85` status `ready` deltaP `0.0` edge `0.0` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
