# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T07:37:29.341793+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10437`

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

- `risk_on_high->unknown_24h` score `481.9001` n `93` status `ready` deltaP `26.7361` edge `39.9801` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `481.9001` n `93` status `ready` deltaP `26.7361` edge `39.9801` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.192` n `241` status `ready` deltaP `-2.3778` edge `2.1043` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `21.77` n `93` status `ready` deltaP `36.5032` edge `1.6225` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `21.77` n `93` status `ready` deltaP `36.5032` edge `1.6225` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `14.9104` n `93` status `ready` deltaP `31.25` edge `1.0342` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.9104` n `93` status `ready` deltaP `31.25` edge `1.0342` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.1315` n `187` status `ready` deltaP `24.8329` edge `0.6529` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.58` n `187` status `ready` deltaP `23.0903` edge `0.3944` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.6392` n `117` status `ready` deltaP `30.3302` edge `0.3049` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.6392` n `117` status `ready` deltaP `30.3302` edge `0.3049` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.41` n `93` status `ready` deltaP `23.0903` edge `0.2969` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.41` n `93` status `ready` deltaP `23.0903` edge `0.2969` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.2998` n `117` status `ready` deltaP `23.847` edge `0.2852` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.2998` n `117` status `ready` deltaP `23.847` edge `0.2852` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7215` n `93` status `ready` deltaP `23.1631` edge `0.0766` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7215` n `93` status `ready` deltaP `23.1631` edge `0.0766` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.5453` n `187` status `ready` deltaP `21.0413` edge `0.0933` maxDD `-0.0505`
- `risk_on_high->metal_24h` score `1.05` n `93` status `ready` deltaP `17.5348` edge `0.1333` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `1.05` n `93` status `ready` deltaP `17.5348` edge `0.1333` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
