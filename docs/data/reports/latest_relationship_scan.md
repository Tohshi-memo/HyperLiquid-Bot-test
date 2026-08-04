# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T05:52:33.491428+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_24h` score `37.4151` n `46` status `ready` deltaP `26.2983` edge `2.9469` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.2761` n `46` status `ready` deltaP `45.0408` edge `0.4901` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.1346` n `46` status `ready` deltaP `37.7415` edge `0.4442` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.8113` n `88` status `ready` deltaP `1.9678` edge `0.5707` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.204` n `88` status `ready` deltaP `15.3687` edge `0.0825` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.384` n `88` status `ready` deltaP `18.6946` edge `0.0106` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2625` n `88` status `ready` deltaP `5.8315` edge `0.0246` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.2215` n `88` status `ready` deltaP `8.4309` edge `-0.0029` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4476` n `88` status `ready` deltaP `1.8781` edge `-0.0165` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.4526` n `88` status `ready` deltaP `6.1114` edge `0.0247` maxDD `-3.211`
- `market_context_high->metal_1h` score `-0.5284` n `88` status `ready` deltaP `-1.4698` edge `-0.0085` maxDD `-1.6224`
- `market_context_high->crypto_alt_4h` score `-0.9701` n `88` status `ready` deltaP `3.2567` edge `-0.0071` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2707` n `88` status `ready` deltaP `-3.4703` edge `-0.0117` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5097` n `88` status `ready` deltaP `5.9132` edge `-0.0794` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.6445` n `46` status `ready` deltaP `-3.8798` edge `0.0094` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.7734` n `88` status `ready` deltaP `-8.8969` edge `-0.0426` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.35` n `88` status `ready` deltaP `2.8988` edge `-0.2538` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6379` n `88` status `ready` deltaP `-12.9491` edge `-0.0795` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8662` n `46` status `ready` deltaP `-24.1621` edge `-0.1276` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.418` n `88` status `ready` deltaP `1.7045` edge `-0.3011` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
