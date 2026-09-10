# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T00:37:32.237683+00:00`
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

- `risk_on_high->crypto_alt_24h` score `13.9452` n `116` status `ready` deltaP `27.8078` edge `0.9997` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.9452` n `116` status `ready` deltaP `27.8078` edge `0.9997` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `8.7582` n `238` status `ready` deltaP `20.3534` edge `0.6769` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `7.5696` n `116` status `ready` deltaP `23.2878` edge `1.222` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.5696` n `116` status `ready` deltaP `23.2878` edge `1.222` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `7.0239` n `116` status `ready` deltaP `36.2385` edge `0.3809` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.0239` n `116` status `ready` deltaP `36.2385` edge `0.3809` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.9225` n `116` status `ready` deltaP `26.2615` edge `0.321` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9225` n `116` status `ready` deltaP `26.2615` edge `0.321` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.8283` n `116` status `ready` deltaP `28.143` edge `0.0523` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8283` n `116` status `ready` deltaP `28.143` edge `0.0523` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.1486` n `238` status `ready` deltaP `11.6319` edge `0.1015` maxDD `0.0`
- `market_context_high->index_24h` score `2.0963` n `238` status `ready` deltaP `23.1662` edge `0.0596` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.4886` n `116` status `ready` deltaP `11.6319` edge `0.0465` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.4886` n `116` status `ready` deltaP `11.6319` edge `0.0465` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.1713` n `116` status `ready` deltaP `4.6562` edge `0.1018` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1713` n `116` status `ready` deltaP `4.6562` edge `0.1018` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.769` n `116` status `ready` deltaP `19.4804` edge `0.0843` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.769` n `116` status `ready` deltaP `19.4804` edge `0.0843` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.4673` n `116` status `ready` deltaP `14.5933` edge `-0.0052` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
