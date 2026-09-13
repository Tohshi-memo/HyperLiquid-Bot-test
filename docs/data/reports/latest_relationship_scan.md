# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T13:37:26.814005+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13342`

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

- `market_context_high->unknown_24h` score `18055.9697` n `56` status `ready` deltaP `10.2093` edge `1504.6156` maxDD `-0.5614`
- `news_risk_high->unknown_1h` score `414.0062` n `82` status `ready` deltaP `-4.6517` edge `34.5737` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.1579` n `82` status `ready` deltaP `34.4785` edge `1.3321` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.1522` n `82` status `ready` deltaP `37.8512` edge `1.4074` maxDD `-9.098`
- `news_risk_high->equity_24h` score `8.2321` n `82` status `ready` deltaP `23.8225` edge `0.7052` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.733` n `82` status `ready` deltaP `47.767` edge `0.2603` maxDD `-0.0797`
- `market_context_high->crypto_alt_24h` score `6.2592` n `56` status `ready` deltaP `21.1946` edge `0.7516` maxDD `-4.5683`
- `news_risk_high->metal_24h` score `4.5612` n `82` status `ready` deltaP `24.2431` edge `0.2639` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.079` n `56` status `ready` deltaP `39.8276` edge `0.0744` maxDD `0.0`
- `market_context_high->equity_24h` score `3.8242` n `56` status `ready` deltaP `38.2389` edge `0.4232` maxDD `-12.0271`
- `market_context_high->index_24h` score `2.4542` n `56` status `ready` deltaP `45.7636` edge `0.0711` maxDD `-1.9235`
- `market_context_high->metal_24h` score `1.5566` n `56` status `ready` deltaP `17.0567` edge `0.1287` maxDD `-0.7609`
- `risk_on_high->crypto_alt_4h` score `0.4878` n `65` status `ready` deltaP `11.2195` edge `0.1552` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.4878` n `65` status `ready` deltaP `11.2195` edge `0.1552` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4164` n `82` status `ready` deltaP `12.3475` edge `0.0339` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0233` n `65` status `ready` deltaP `4.362` edge `0.002` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0233` n `65` status `ready` deltaP `4.362` edge `0.002` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.0556` n `144` status `ready` deltaP `3.7841` edge `-0.0007` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
