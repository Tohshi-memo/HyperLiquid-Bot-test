# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T03:52:30.536071+00:00`
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

- `risk_on_high->crypto_alt_24h` score `13.6875` n `103` status `ready` deltaP `29.5206` edge `0.9668` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.6875` n `103` status `ready` deltaP `29.5206` edge `0.9668` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.3884` n `225` status `ready` deltaP `21.9306` edge `0.7189` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2549` n `103` status `ready` deltaP `37.3712` edge `0.3926` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2549` n `103` status `ready` deltaP `37.3712` edge `0.3926` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.888` n `103` status `ready` deltaP `21.9543` edge `1.0153` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.888` n `103` status `ready` deltaP `21.9543` edge `1.0153` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.1862` n `103` status `ready` deltaP `27.1727` edge `0.3369` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.1862` n `103` status `ready` deltaP `27.1727` edge `0.3369` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.9527` n `103` status `ready` deltaP `30.0735` edge `0.0498` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9527` n `103` status `ready` deltaP `30.0735` edge `0.0498` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.5703` n `225` status `ready` deltaP `13.8889` edge `0.1216` maxDD `0.0`
- `market_context_high->index_24h` score `2.2982` n `225` status `ready` deltaP `24.9861` edge `0.0643` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.2191` n `103` status `ready` deltaP `13.8889` edge `0.009` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.2191` n `103` status `ready` deltaP `13.8889` edge `0.009` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.1196` n `103` status `ready` deltaP `4.805` edge `0.0965` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1196` n `103` status `ready` deltaP `4.805` edge `0.0965` maxDD `-1.1521`
- `risk_on_high->equity_4h` score `0.7098` n `103` status `ready` deltaP `18.155` edge `-0.0228` maxDD `-1.4601`
- `risk_on_and_context->equity_4h` score `0.7098` n `103` status `ready` deltaP `18.155` edge `-0.0228` maxDD `-1.4601`
- `risk_on_high->commodity_24h` score `0.6149` n `103` status `ready` deltaP `9.1576` edge `0.0288` maxDD `-0.7551`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
