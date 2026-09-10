# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T03:22:28.033722+00:00`
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

- `risk_on_high->crypto_alt_24h` score `13.7535` n `105` status `ready` deltaP `29.2659` edge `0.974` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.7535` n `105` status `ready` deltaP `29.2659` edge `0.974` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.3118` n `227` status `ready` deltaP `21.693` edge `0.7141` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2307` n `105` status `ready` deltaP `37.1588` edge `0.392` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2307` n `105` status `ready` deltaP `37.1588` edge `0.392` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `6.1973` n `105` status `ready` deltaP `22.2172` edge `1.0532` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.1973` n `105` status `ready` deltaP `22.2172` edge `1.0532` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.1017` n `105` status `ready` deltaP `26.761` edge `0.3326` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.1017` n `105` status `ready` deltaP `26.761` edge `0.3326` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.9342` n `105` status `ready` deltaP `29.7818` edge `0.0502` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9342` n `105` status `ready` deltaP `29.7818` edge `0.0502` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.5089` n `227` status `ready` deltaP `13.5417` edge `0.1188` maxDD `0.0`
- `market_context_high->index_24h` score `2.2689` n `227` status `ready` deltaP `24.7094` edge `0.0637` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.2621` n `105` status `ready` deltaP `13.5417` edge `0.0149` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.2621` n `105` status `ready` deltaP `13.5417` edge `0.0149` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.221` n `105` status `ready` deltaP `5.5632` edge `0.0999` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.221` n `105` status `ready` deltaP `5.5632` edge `0.0999` maxDD `-1.1521`
- `risk_on_high->commodity_24h` score `0.3116` n `105` status `ready` deltaP `7.6042` edge `0.0251` maxDD `-0.9865`
- `risk_on_and_context->commodity_24h` score `0.3116` n `105` status `ready` deltaP `7.6042` edge `0.0251` maxDD `-0.9865`
- `risk_on_high->equity_4h` score `0.3067` n `105` status `ready` deltaP `16.5461` edge `-0.0297` maxDD `-2.0704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
