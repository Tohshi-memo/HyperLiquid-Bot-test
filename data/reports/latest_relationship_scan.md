# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T04:22:27.071402+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10200`

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

- `risk_on_high->crypto_alt_24h` score `7.586` n `117` status `ready` deltaP `18.8168` edge `0.5297` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `7.586` n `117` status `ready` deltaP `18.8168` edge `0.5297` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `6.1059` n `117` status `ready` deltaP `33.0741` edge `0.3255` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.1059` n `117` status `ready` deltaP `33.0741` edge `0.3255` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.1326` n `117` status `ready` deltaP `23.5421` edge `0.2733` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.1326` n `117` status `ready` deltaP `23.5421` edge `0.2733` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.0909` n `117` status `ready` deltaP `17.4546` edge `0.8149` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.0909` n `117` status `ready` deltaP `17.4546` edge `0.8149` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `2.5385` n `241` status `ready` deltaP `11.472` edge `0.2178` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.5506` n `117` status `ready` deltaP `17.2276` edge `0.0186` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.5506` n `117` status `ready` deltaP `17.2276` edge `0.0186` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.052` n `117` status `ready` deltaP `4.6958` edge `0.0916` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.052` n `117` status `ready` deltaP `4.6958` edge `0.0916` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.8292` n `241` status `ready` deltaP `12.3228` edge `0.0263` maxDD `-0.1483`
- `risk_on_high->metal_1h` score `0.1804` n `117` status `ready` deltaP `8.4818` edge `-0.0004` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1804` n `117` status `ready` deltaP `8.4818` edge `-0.0004` maxDD `-0.3081`
- `risk_on_high->index_1h` score `0.1281` n `117` status `ready` deltaP `8.6699` edge `-0.005` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1281` n `117` status `ready` deltaP `8.6699` edge `-0.005` maxDD `-0.5764`
- `risk_on_high->equity_1h` score `0.1272` n `117` status `ready` deltaP `12.1271` edge `-0.0171` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.1272` n `117` status `ready` deltaP `12.1271` edge `-0.0171` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
