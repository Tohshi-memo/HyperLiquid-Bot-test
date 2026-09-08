# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T23:52:29.586816+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10176`

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

- `risk_on_high->crypto_alt_24h` score `6.906` n `117` status `ready` deltaP `16.2126` edge `0.4904` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `6.906` n `117` status `ready` deltaP `16.2126` edge `0.4904` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.698` n `117` status `ready` deltaP `31.2448` edge `0.3037` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.698` n `117` status `ready` deltaP `31.2448` edge `0.3037` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.1584` n `117` status `ready` deltaP `23.9994` edge `0.2724` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.1584` n `117` status `ready` deltaP `23.9994` edge `0.2724` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.1093` n `117` status `ready` deltaP `17.6282` edge `0.8161` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.1093` n `117` status `ready` deltaP `17.6282` edge `0.8161` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `1.8586` n `241` status `ready` deltaP `8.8678` edge `0.1785` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.1902` n `117` status `ready` deltaP `14.1026` edge `0.0094` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.1902` n `117` status `ready` deltaP `14.1026` edge `0.0094` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.9274` n `117` status `ready` deltaP `3.9473` edge `0.0862` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9274` n `117` status `ready` deltaP `3.9473` edge `0.0862` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.4688` n `241` status `ready` deltaP `9.1978` edge `0.0171` maxDD `-0.1483`
- `risk_on_high->equity_1h` score `0.2435` n `117` status `ready` deltaP `13.0253` edge `-0.0134` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.2435` n `117` status `ready` deltaP `13.0253` edge `-0.0134` maxDD `-2.2516`
- `risk_on_high->metal_1h` score `0.2077` n `117` status `ready` deltaP `8.7812` edge `0.0011` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.2077` n `117` status `ready` deltaP `8.7812` edge `0.0011` maxDD `-0.3081`
- `risk_on_high->index_1h` score `0.1826` n `117` status `ready` deltaP `9.5681` edge `-0.004` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1826` n `117` status `ready` deltaP `9.5681` edge `-0.004` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
