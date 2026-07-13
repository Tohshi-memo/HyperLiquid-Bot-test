# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T06:52:25.585289+00:00`
- Price records: `672`
- Market context records: `6579`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `5.7818` n `147` status `ready` deltaP `9.7565` edge `0.7468` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.004` n `210` status `ready` deltaP `-5.1297` edge `0.2913` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4146` n `147` status `ready` deltaP `13.831` edge `0.2125` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3534` n `210` status `ready` deltaP `0.8583` edge `-0.0003` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4002` n `210` status `ready` deltaP `7.197` edge `0.0273` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.5368` n `210` status `ready` deltaP `5.7414` edge `0.0242` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5545` n `210` status `ready` deltaP `-0.3807` edge `0.0034` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.6149` n `210` status `ready` deltaP `-0.8583` edge `-0.0048` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9515` n `210` status `ready` deltaP `8.5323` edge `0.0091` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1657` n `210` status `ready` deltaP `2.0816` edge `0.0` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.3039` n `210` status `ready` deltaP `-3.8765` edge `-0.0021` maxDD `-2.1239`
- `market_context_high->commodity_4h` score `-1.3302` n `210` status `ready` deltaP `-1.5839` edge `-0.0105` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.5903` n `210` status `ready` deltaP `-15.9988` edge `0.2147` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.7456` n `210` status `ready` deltaP `7.7338` edge `0.0561` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.7717` n `210` status `ready` deltaP `-0.3804` edge `-0.0034` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.9576` n `210` status `ready` deltaP `5.0857` edge `0.0553` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1525` n `210` status `ready` deltaP `-1.5012` edge `0.0201` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-2.2976` n `147` status `ready` deltaP `5.2272` edge `0.0845` maxDD `-6.1985`
- `market_context_high->fx_24h` score `-3.7599` n `147` status `ready` deltaP `-3.7115` edge `-0.0038` maxDD `-9.2795`
- `market_context_high->index_24h` score `-4.0082` n `147` status `ready` deltaP `0.5217` edge `-0.0029` maxDD `-10.7676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
