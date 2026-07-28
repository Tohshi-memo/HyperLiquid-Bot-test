# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T03:22:33.774196+00:00`
- Price records: `672`
- Market context records: `8157`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `21.0747` n `73` status `ready` deltaP `44.423` edge `1.5511` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.785` n `74` status `ready` deltaP `37.603` edge `0.5882` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.6277` n `43` status `ready` deltaP `32.7319` edge `0.5213` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.5847` n `73` status `ready` deltaP `39.5833` edge `0.4515` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.277` n `43` status `ready` deltaP `19.4236` edge `0.3708` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9577` n `74` status `ready` deltaP `36.058` edge `0.0937` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.883` n `43` status `ready` deltaP `29.8287` edge `0.1556` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.7632` n `74` status `ready` deltaP `20.4321` edge `0.1977` maxDD `-0.6254`
- `market_context_high->index_24h` score `3.5366` n `73` status `ready` deltaP `23.2568` edge `0.2067` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.7412` n `43` status `ready` deltaP `22.8587` edge `0.0951` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.409` n `74` status `ready` deltaP `23.6528` edge `0.1053` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.0351` n `73` status `ready` deltaP `27.3069` edge `0.0579` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.9719` n `74` status `ready` deltaP `9.2164` edge `0.2146` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.8884` n `74` status `ready` deltaP `11.4412` edge `0.2529` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.6957` n `74` status `ready` deltaP `20.1206` edge `0.0268` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.6059` n `73` status `ready` deltaP `31.6686` edge `0.2833` maxDD `-15.7497`
- `news_risk_high->metal_4h` score `1.5754` n `43` status `ready` deltaP `15.0418` edge `0.0778` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.3475` n `43` status `ready` deltaP `6.3327` edge `0.1098` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `1.3366` n `74` status `ready` deltaP `13.6551` edge `0.0614` maxDD `-1.6171`
- `news_risk_high->crypto_alt_4h` score `1.074` n `43` status `ready` deltaP `11.9505` edge `0.1972` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
