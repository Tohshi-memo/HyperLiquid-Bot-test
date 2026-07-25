# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T11:07:30.355170+00:00`
- Price records: `672`
- Market context records: `7871`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14667`

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

- `market_context_high->equity_24h` score `12.6691` n `118` status `ready` deltaP `29.182` edge `0.9954` maxDD `-6.0681`
- `market_context_high->metal_24h` score `2.798` n `119` status `ready` deltaP `15.6911` edge `0.2706` maxDD `-1.6965`
- `market_context_high->equity_4h` score `2.4757` n `119` status `ready` deltaP `10.35` edge `0.3632` maxDD `-5.518`
- `market_context_high->crypto_major_4h` score `1.6404` n `119` status `ready` deltaP `17.4613` edge `0.1921` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `1.4343` n `119` status `ready` deltaP `12.9509` edge `0.1449` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.3891` n `118` status `ready` deltaP `21.2262` edge `0.1326` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.224` n `119` status `ready` deltaP `13.7158` edge `0.0505` maxDD `-1.5286`
- `market_context_high->fx_24h` score `1.0746` n `118` status `ready` deltaP `29.6742` edge `0.0487` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7119` n `119` status `ready` deltaP `10.1433` edge `0.1054` maxDD `-4.2072`
- `market_context_high->crypto_alt_1h` score `0.3112` n `119` status `ready` deltaP `4.5879` edge `0.0386` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.285` n `119` status `ready` deltaP `6.6007` edge `0.0391` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.2021` n `119` status `ready` deltaP `7.804` edge `0.0169` maxDD `-0.7743`
- `market_context_high->commodity_1h` score `-0.0421` n `119` status `ready` deltaP `4.4691` edge `0.0126` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1157` n `119` status `ready` deltaP `10.8088` edge `0.0538` maxDD `-1.2551`
- `market_context_high->fx_1h` score `-0.2678` n `119` status `ready` deltaP `0.6915` edge `-0.0003` maxDD `-0.4251`
- `market_context_high->metal_4h` score `-0.4738` n `119` status `ready` deltaP `5.2278` edge `0.088` maxDD `-1.3203`
- `market_context_high->metal_1h` score `-0.9408` n `119` status `ready` deltaP `-0.039` edge `0.0222` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.0161` n `118` status `ready` deltaP `-2.5821` edge `0.1064` maxDD `-1.9088`
- `market_context_high->fx_4h` score `-1.2129` n `119` status `ready` deltaP `-2.1715` edge `0.0002` maxDD `-1.6307`
- `market_context_high->crypto_alt_24h` score `-1.5563` n `119` status `ready` deltaP `14.0411` edge `0.2364` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
