# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T10:07:27.171937+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11908`

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

- `risk_on_high->crypto_alt_24h` score `16.0967` n `91` status `ready` deltaP `33.2208` edge `1.1429` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.0967` n `91` status `ready` deltaP `33.2208` edge `1.1429` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `11.508` n `201` status `ready` deltaP `24.785` edge `0.8765` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.7809` n `91` status `ready` deltaP `39.5068` edge `0.4222` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.7809` n `91` status `ready` deltaP `39.5068` edge `0.4222` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.9364` n `91` status `ready` deltaP `29.3052` edge `0.3852` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.9364` n `91` status `ready` deltaP `29.3052` edge `0.3852` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.2123` n `91` status `ready` deltaP `22.0696` edge `0.9279` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.2123` n `91` status `ready` deltaP `22.0696` edge `0.9279` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.2344` n `91` status `ready` deltaP `34.0297` edge `0.0469` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.2344` n `91` status `ready` deltaP `34.0297` edge `0.0469` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.8395` n `201` status `ready` deltaP `18.2292` edge `0.1151` maxDD `0.0`
- `market_context_high->index_24h` score `2.3627` n `201` status `ready` deltaP `28.3712` edge `0.0471` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `1.9608` n `91` status `ready` deltaP `26.181` edge `-0.0018` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `1.9608` n `91` status `ready` deltaP `26.181` edge `-0.0018` maxDD `-0.0802`
- `market_context_high->commodity_24h` score `1.8947` n `201` status `ready` deltaP `18.452` edge `0.0488` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.8785` n `91` status `ready` deltaP `18.1185` edge `0.0451` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.8785` n `91` status `ready` deltaP `18.1185` edge `0.0451` maxDD `-0.0811`
- `risk_on_high->equity_24h` score `1.2339` n `91` status `ready` deltaP `18.2292` edge `-0.0187` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.2339` n `91` status `ready` deltaP `18.2292` edge `-0.0187` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
