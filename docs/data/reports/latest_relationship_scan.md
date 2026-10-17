# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T15:07:26.648048+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9440`

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

- `risk_on_high->commodity_24h` score `6.9477` n `54` status `ready` deltaP `38.5017` edge `0.3223` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9477` n `54` status `ready` deltaP `38.5017` edge `0.3223` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.8171` n `160` status `ready` deltaP `17.2104` edge `0.3933` maxDD `-8.1957`
- `risk_on_high->crypto_major_4h` score `1.8815` n `86` status `ready` deltaP `18.1261` edge `0.2259` maxDD `-8.1957`
- `risk_on_and_context->crypto_major_4h` score `1.8815` n `86` status `ready` deltaP `18.1261` edge `0.2259` maxDD `-8.1957`
- `market_context_high->crypto_alt_4h` score `1.4146` n `160` status `ready` deltaP `9.939` edge `0.4437` maxDD `-20.6993`
- `market_context_high->crypto_major_1h` score `0.5664` n `172` status `ready` deltaP `5.9985` edge `0.0961` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.0404` n `172` status `ready` deltaP `7.1787` edge `0.1055` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0363` n `90` status `ready` deltaP `5.4054` edge `0.0054` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0363` n `90` status `ready` deltaP `5.4054` edge `0.0054` maxDD `-0.7394`
- `market_context_high->metal_4h` score `0.0174` n `160` status `ready` deltaP `9.1921` edge `0.0447` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.1737` n `172` status `ready` deltaP `7.1496` edge `0.0049` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2599` n `90` status `ready` deltaP `1.1711` edge `-0.0031` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2599` n `90` status `ready` deltaP `1.1711` edge `-0.0031` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.2847` n `172` status `ready` deltaP `6.3675` edge `0.008` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.342` n `172` status `ready` deltaP `10.3028` edge `0.0389` maxDD `-7.1141`
- `risk_on_high->equity_1h` score `-0.4687` n `90` status `ready` deltaP `9.6697` edge `0.0261` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4687` n `90` status `ready` deltaP `9.6697` edge `0.0261` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5048` n `90` status `ready` deltaP `0.7086` edge `0.0037` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5048` n `90` status `ready` deltaP `0.7086` edge `0.0037` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
