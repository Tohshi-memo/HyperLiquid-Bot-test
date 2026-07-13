# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T06:37:25.628415+00:00`
- Price records: `672`
- Market context records: `6578`
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

- `market_context_high->unknown_24h` score `5.9209` n `146` status `ready` deltaP `10.1758` edge `0.7556` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7808` n `210` status `ready` deltaP `-5.1297` edge `0.2727` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4199` n `146` status `ready` deltaP `13.6726` edge `0.214` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3534` n `210` status `ready` deltaP `0.8583` edge `-0.0003` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.3971` n `210` status `ready` deltaP `7.197` edge `0.0277` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.5235` n `210` status `ready` deltaP `5.8911` edge `0.0249` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5553` n `210` status `ready` deltaP `-0.3807` edge `0.0033` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.6242` n `210` status `ready` deltaP `-1.008` edge `-0.005` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9568` n `210` status `ready` deltaP `8.4606` edge `0.0089` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1861` n `210` status `ready` deltaP `1.9319` edge `-0.0007` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2907` n `210` status `ready` deltaP `-3.7268` edge `-0.002` maxDD `-2.1239`
- `market_context_high->commodity_4h` score `-1.3351` n `210` status `ready` deltaP `-1.6482` edge `-0.0107` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.5702` n `210` status `ready` deltaP `-15.9274` edge `0.2159` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.7324` n `210` status `ready` deltaP `7.8083` edge `0.0573` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.7758` n `210` status `ready` deltaP `-0.4588` edge `-0.0034` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.9419` n `210` status `ready` deltaP `5.162` edge `0.0568` maxDD `-19.2145`
- `market_context_high->metal_24h` score `-2.1359` n `146` status `ready` deltaP `5.5114` edge `0.0867` maxDD `-5.7816`
- `market_context_high->metal_4h` score `-2.1485` n `210` status `ready` deltaP `-1.4395` edge `0.0202` maxDD `-5.2172`
- `market_context_high->fx_24h` score `-3.7774` n `146` status `ready` deltaP `-3.9581` edge `-0.0044` maxDD `-9.2795`
- `market_context_high->index_24h` score `-3.9064` n `146` status `ready` deltaP `0.8245` edge `-0.0006` maxDD `-10.7676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
