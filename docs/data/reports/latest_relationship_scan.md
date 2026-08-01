# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T04:07:31.214251+00:00`
- Price records: `672`
- Market context records: `8583`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5919`

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

- `news_risk_high->unknown_24h` score `4750.5223` n `64` status `ready` deltaP `37.3264` edge `395.6701` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9582` n `64` status `ready` deltaP `21.7226` edge `0.4114` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1896` n `64` status `ready` deltaP `18.4832` edge `0.0783` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8367` n `64` status `ready` deltaP `17.2998` edge `0.0854` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.7022` n `62` status `ready` deltaP `12.2934` edge `0.1556` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.0311` n `64` status `ready` deltaP `6.593` edge `0.1658` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.5155` n `64` status `ready` deltaP `11.8902` edge `0.126` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4555` n `64` status `ready` deltaP `8.4113` edge `0.055` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3851` n `64` status `ready` deltaP `7.3634` edge `0.0515` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0893` n `64` status `ready` deltaP `5.2863` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0728` n `64` status `ready` deltaP `11.9284` edge `0.0223` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0418` n `64` status `ready` deltaP `4.2197` edge `0.0089` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0167` n `64` status `ready` deltaP `2.0198` edge `0.032` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.0954` n `62` status `ready` deltaP `8.753` edge `0.0133` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1706` n `64` status `ready` deltaP `2.8069` edge `0.0074` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2755` n `62` status `ready` deltaP `2.2117` edge `0.0002` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3566` n `62` status `ready` deltaP `3.4093` edge `-0.0059` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5213` n `62` status `ready` deltaP `-2.627` edge `0.0134` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7189` n `62` status `ready` deltaP `1.2459` edge `-0.0153` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-1.0116` n `62` status `ready` deltaP `-3.4431` edge `-0.0119` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
