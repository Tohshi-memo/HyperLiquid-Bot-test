# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T03:22:25.907872+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10425`

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

- `risk_on_high->unknown_24h` score `531.3761` n `94` status `ready` deltaP `26.7361` edge `44.1031` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `531.3761` n `94` status `ready` deltaP `26.7361` edge `44.1031` maxDD `0.0`
- `market_context_high->unknown_1h` score `23.5639` n `242` status `ready` deltaP `-2.6983` edge `2.0541` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `20.6829` n `94` status `ready` deltaP `33.6547` edge `1.5509` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `20.6829` n `94` status `ready` deltaP `33.6547` edge `1.5509` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `14.2152` n `94` status `ready` deltaP `30.5556` edge `0.9809` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.2152` n `94` status `ready` deltaP `30.5556` edge `0.9809` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.9795` n `183` status `ready` deltaP `23.9982` edge `0.6458` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.5716` n `183` status `ready` deltaP `23.0903` edge `0.3937` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.3429` n `118` status `ready` deltaP `29.1468` edge `0.2881` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3429` n `118` status `ready` deltaP `29.1468` edge `0.2881` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.314` n `94` status `ready` deltaP `23.0903` edge `0.2889` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.314` n `94` status `ready` deltaP `23.0903` edge `0.2889` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.8347` n `118` status `ready` deltaP `22.039` edge `0.2585` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.8347` n `118` status `ready` deltaP `22.039` edge `0.2585` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7412` n `94` status `ready` deltaP `23.5446` edge `0.0757` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7412` n `94` status `ready` deltaP `23.5446` edge `0.0757` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6339` n `183` status `ready` deltaP `21.8181` edge `0.0955` maxDD `-0.0505`
- `risk_on_high->metal_24h` score `1.0102` n `94` status `ready` deltaP `17.3685` edge `0.1293` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `1.0102` n `94` status `ready` deltaP `17.3685` edge `0.1293` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
