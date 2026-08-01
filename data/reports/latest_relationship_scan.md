# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T04:37:50.257796+00:00`
- Price records: `672`
- Market context records: `8585`
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

- `news_risk_high->unknown_24h` score `4750.2834` n `64` status `ready` deltaP `36.9792` edge `395.6525` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9302` n `64` status `ready` deltaP `21.4177` edge `0.4111` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1896` n `64` status `ready` deltaP `18.4832` edge `0.0783` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8499` n `64` status `ready` deltaP `17.4495` edge `0.0855` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.6502` n `62` status `ready` deltaP `11.9886` edge `0.1533` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.0027` n `64` status `ready` deltaP `6.2881` edge `0.1642` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.4817` n `64` status `ready` deltaP `11.5854` edge `0.1237` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4547` n `64` status `ready` deltaP `8.4113` edge `0.0549` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3843` n `64` status `ready` deltaP `7.3634` edge `0.0514` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.085` n `64` status `ready` deltaP `12.0808` edge `0.0223` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.0815` n `64` status `ready` deltaP `5.1366` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0418` n `64` status `ready` deltaP `4.2197` edge `0.0089` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0088` n `64` status `ready` deltaP `2.1723` edge `0.032` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.0832` n `62` status `ready` deltaP `8.9054` edge `0.0133` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1455` n `64` status `ready` deltaP `3.1063` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2832` n `62` status `ready` deltaP `2.062` edge `0.0002` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3395` n `62` status `ready` deltaP `3.7087` edge `-0.0057` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5221` n `62` status `ready` deltaP `-2.627` edge `0.0133` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7189` n `62` status `ready` deltaP `1.2459` edge `-0.0153` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9865` n `62` status `ready` deltaP `-3.1437` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
