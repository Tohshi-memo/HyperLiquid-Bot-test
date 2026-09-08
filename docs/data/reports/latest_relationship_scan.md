# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T20:07:29.354922+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10296`

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

- `risk_on_high->crypto_alt_24h` score `6.8333` n `117` status `ready` deltaP `16.039` edge `0.4855` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `6.8333` n `117` status `ready` deltaP `16.039` edge `0.4855` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.446` n `117` status `ready` deltaP `30.3302` edge `0.2888` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.446` n `117` status `ready` deltaP `30.3302` edge `0.2888` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.2255` n `117` status `ready` deltaP `18.8435` edge `0.8229` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.2255` n `117` status `ready` deltaP `18.8435` edge `0.8229` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.0592` n `117` status `ready` deltaP `23.3896` edge `0.2682` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.0592` n `117` status `ready` deltaP `23.3896` edge `0.2682` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `1.7859` n `241` status `ready` deltaP `8.6942` edge `0.1736` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `0.9202` n `117` status `ready` deltaP `3.9473` edge `0.0856` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9202` n `117` status `ready` deltaP `3.9473` edge `0.0856` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.8967` n `117` status `ready` deltaP `11.4984` edge `0.0023` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.8967` n `117` status `ready` deltaP `11.4984` edge `0.0023` maxDD `-0.0051`
- `risk_on_high->equity_1h` score `0.2579` n `117` status `ready` deltaP `13.175` edge `-0.0132` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.2579` n `117` status `ready` deltaP `13.175` edge `-0.0132` maxDD `-2.2516`
- `risk_on_high->metal_1h` score `0.2061` n `117` status `ready` deltaP `8.7812` edge `0.0009` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.2061` n `117` status `ready` deltaP `8.7812` edge `0.0009` maxDD `-0.3081`
- `market_context_high->index_24h` score `0.1752` n `241` status `ready` deltaP `6.5936` edge `0.01` maxDD `-0.1483`
- `risk_on_high->index_1h` score `0.1569` n `117` status `ready` deltaP `9.119` edge `-0.0043` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1569` n `117` status `ready` deltaP `9.119` edge `-0.0043` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
