# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T12:37:33.150505+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10224`

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

- `risk_on_high->crypto_alt_24h` score `8.3843` n `117` status `ready` deltaP `20.7265` edge `0.5835` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.3843` n `117` status `ready` deltaP `20.7265` edge `0.5835` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.4438` n `117` status `ready` deltaP `31.3972` edge `0.2815` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.4438` n `117` status `ready` deltaP `31.3972` edge `0.2815` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.0276` n `117` status `ready` deltaP `17.1074` edge `0.8091` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.0276` n `117` status `ready` deltaP `17.1074` edge `0.8091` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `3.6602` n `117` status `ready` deltaP `22.0177` edge `0.2441` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.6602` n `117` status `ready` deltaP `22.0177` edge `0.2441` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.3369` n `241` status `ready` deltaP `13.3817` edge `0.2716` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.872` n `117` status `ready` deltaP `20.179` edge `0.0257` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.872` n `117` status `ready` deltaP `20.179` edge `0.0257` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.1505` n `241` status `ready` deltaP `15.2742` edge `0.0334` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.7691` n `117` status `ready` deltaP `3.1988` edge `0.078` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.7691` n `117` status `ready` deltaP `3.1988` edge `0.078` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.5698` n `117` status `ready` deltaP `19.5647` edge `0.0582` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.5698` n `117` status `ready` deltaP `19.5647` edge `0.0582` maxDD `-0.9131`
- `risk_on_high->metal_1h` score `0.2092` n `117` status `ready` deltaP `8.7812` edge `0.0013` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.2092` n `117` status `ready` deltaP `8.7812` edge `0.0013` maxDD `-0.3081`
- `risk_on_high->index_1h` score `0.192` n `117` status `ready` deltaP `9.7178` edge `-0.0038` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.192` n `117` status `ready` deltaP `9.7178` edge `-0.0038` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
