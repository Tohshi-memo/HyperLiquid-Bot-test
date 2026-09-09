# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T15:52:30.933848+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10148`

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

- `risk_on_high->crypto_alt_24h` score `9.2621` n `117` status `ready` deltaP `21.7682` edge `0.6497` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.2621` n `117` status `ready` deltaP `21.7682` edge `0.6497` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.5994` n `117` status `ready` deltaP `32.007` edge `0.2904` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5994` n `117` status `ready` deltaP `32.007` edge `0.2904` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.5024` n `117` status `ready` deltaP `17.6282` edge `0.8665` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.5024` n `117` status `ready` deltaP `17.6282` edge `0.8665` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `4.2146` n `241` status `ready` deltaP `14.4234` edge `0.3378` maxDD `-3.9523`
- `risk_on_high->crypto_major_4h` score `3.8076` n `117` status `ready` deltaP `22.7799` edge `0.2513` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.8076` n `117` status `ready` deltaP `22.7799` edge `0.2513` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.0979` n `117` status `ready` deltaP `22.0887` edge `0.0318` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.0979` n `117` status `ready` deltaP `22.0887` edge `0.0318` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.3765` n `241` status `ready` deltaP `17.1839` edge `0.0395` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9574` n `117` status `ready` deltaP `3.7976` edge `0.0897` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9574` n `117` status `ready` deltaP `3.7976` edge `0.0897` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6568` n `117` status `ready` deltaP `19.7383` edge `0.0682` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.6568` n `117` status `ready` deltaP `19.7383` edge `0.0682` maxDD `-0.9131`
- `market_context_high->equity_24h` score `0.262` n `241` status `ready` deltaP `5.5556` edge `-0.0152` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.2543` n `117` status `ready` deltaP `13.0253` edge `-0.0125` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.2543` n `117` status `ready` deltaP `13.0253` edge `-0.0125` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.2138` n `117` status `ready` deltaP `10.0172` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
