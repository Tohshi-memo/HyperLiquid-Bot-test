# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T02:22:35.138285+00:00`
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

- `risk_on_high->crypto_alt_24h` score `13.8127` n `109` status `ready` deltaP `28.7461` edge `0.9824` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.8127` n `109` status `ready` deltaP `28.7461` edge `0.9824` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.1257` n `231` status `ready` deltaP `21.2121` edge `0.7018` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.1915` n `109` status `ready` deltaP `37.0287` edge `0.3896` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.1915` n `109` status `ready` deltaP `37.0287` edge `0.3896` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `6.6845` n `109` status `ready` deltaP `22.6762` edge `1.1126` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.6845` n `109` status `ready` deltaP `22.6762` edge `1.1126` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.024` n `109` status `ready` deltaP `26.765` edge `0.3261` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.024` n `109` status `ready` deltaP `26.765` edge `0.3261` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.9014` n `109` status `ready` deltaP `29.1921` edge `0.0514` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9014` n `109` status `ready` deltaP `29.1921` edge `0.0514` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.3802` n `231` status `ready` deltaP `12.8472` edge `0.1127` maxDD `0.0`
- `market_context_high->index_24h` score `2.2087` n `231` status `ready` deltaP `24.1522` edge `0.0624` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.3578` n `109` status `ready` deltaP `12.8472` edge `0.0275` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.3578` n `109` status `ready` deltaP `12.8472` edge `0.0275` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0492` n `109` status `ready` deltaP `3.9252` edge `0.0965` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0492` n `109` status `ready` deltaP `3.9252` edge `0.0965` maxDD `-1.1521`
- `risk_on_high->equity_1h` score `0.4837` n `109` status `ready` deltaP `14.6927` edge `-0.0045` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.4837` n `109` status `ready` deltaP `14.6927` edge `-0.0045` maxDD `-2.2516`
- `risk_on_high->metal_24h` score `0.414` n `109` status `ready` deltaP `17.5427` edge `0.0517` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
