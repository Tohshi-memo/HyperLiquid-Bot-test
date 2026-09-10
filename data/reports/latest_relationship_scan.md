# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T03:07:23.667931+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.7804` n `106` status `ready` deltaP `29.1372` edge `0.9771` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.7804` n `106` status `ready` deltaP `29.1372` edge `0.9771` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.2746` n `228` status `ready` deltaP `21.5735` edge `0.7118` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2209` n `106` status `ready` deltaP `37.0513` edge `0.3919` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2209` n `106` status `ready` deltaP `37.0513` edge `0.3919` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `6.3387` n `106` status `ready` deltaP `22.3401` edge `1.0705` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.3387` n `106` status `ready` deltaP `22.3401` edge `1.0705` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.1067` n `106` status `ready` deltaP `26.9587` edge `0.3317` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.1067` n `106` status `ready` deltaP `26.9587` edge `0.3317` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.926` n `106` status `ready` deltaP `29.6351` edge `0.0505` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.926` n `106` status `ready` deltaP `29.6351` edge `0.0505` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.4758` n `228` status `ready` deltaP `13.3681` edge `0.1172` maxDD `0.0`
- `market_context_high->index_24h` score `2.2542` n `228` status `ready` deltaP `24.5706` edge `0.0634` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.2818` n `106` status `ready` deltaP `13.3681` edge `0.0177` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.2818` n `106` status `ready` deltaP `13.3681` edge `0.0177` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.1882` n `106` status `ready` deltaP `5.1379` edge `0.1` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1882` n `106` status `ready` deltaP `5.1379` edge `0.1` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.2676` n `106` status `ready` deltaP `16.6339` edge `0.039` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.2676` n `106` status `ready` deltaP `16.6339` edge `0.039` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.2286` n `106` status `ready` deltaP `13.9137` edge `-0.0103` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
