# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T18:52:28.838150+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10256`

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

- `risk_on_high->crypto_alt_24h` score `6.8791` n `117` status `ready` deltaP `16.3862` edge `0.487` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `6.8791` n `117` status `ready` deltaP `16.3862` edge `0.487` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.3362` n `117` status `ready` deltaP `29.8728` edge `0.2827` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3362` n `117` status `ready` deltaP `29.8728` edge `0.2827` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.2623` n `117` status `ready` deltaP `19.1907` edge `0.8253` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.2623` n `117` status `ready` deltaP `19.1907` edge `0.8253` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.0278` n `117` status `ready` deltaP `23.2372` edge `0.2666` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.0278` n `117` status `ready` deltaP `23.2372` edge `0.2666` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `1.8317` n `241` status `ready` deltaP `9.0414` edge `0.1751` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `0.8938` n `117` status `ready` deltaP `3.9473` edge `0.0834` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8938` n `117` status `ready` deltaP `3.9473` edge `0.0834` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.7985` n `117` status `ready` deltaP `10.6303` edge `-0.0001` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.7985` n `117` status `ready` deltaP `10.6303` edge `-0.0001` maxDD `-0.0051`
- `risk_on_high->metal_1h` score `0.1843` n `117` status `ready` deltaP `8.4818` edge `0.0001` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1843` n `117` status `ready` deltaP `8.4818` edge `0.0001` maxDD `-0.3081`
- `risk_on_high->equity_1h` score `0.174` n `117` status `ready` deltaP `12.5762` edge `-0.0162` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.174` n `117` status `ready` deltaP `12.5762` edge `-0.0162` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.1211` n `117` status `ready` deltaP `8.5202` edge `-0.0049` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1211` n `117` status `ready` deltaP `8.5202` edge `-0.0049` maxDD `-0.5764`
- `market_context_high->index_24h` score `0.077` n `241` status `ready` deltaP `5.7255` edge `0.0076` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
