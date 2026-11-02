# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T05:52:26.196085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5111`

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

- `market_context_high->unknown_24h` score `6723.8947` n `38` status `ready` deltaP `1.3889` edge `560.3153` maxDD `0.0`
- `market_context_high->unknown_4h` score `504.0283` n `43` status `ready` deltaP `8.9939` edge `41.9424` maxDD `0.0`
- `market_context_high->unknown_1h` score `111.1899` n `43` status `ready` deltaP `6.2666` edge `9.2351` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.0969` n `38` status `ready` deltaP `41.9865` edge `1.3351` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.915` n `94` status `ready` deltaP `34.2605` edge `1.0668` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `7.1316` n `38` status `ready` deltaP `43.9327` edge `0.3325` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.6342` n `38` status `ready` deltaP `49.1319` edge `0.2253` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.3561` n `43` status `ready` deltaP `27.166` edge `0.378` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.6184` n `43` status `ready` deltaP `13.0212` edge `0.4516` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `5.0354` n `43` status `ready` deltaP `25.7161` edge `0.2818` maxDD `-1.6901`
- `market_context_high->equity_1h` score `2.3197` n `43` status `ready` deltaP `5.3649` edge `0.1976` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `2.305` n `126` status `ready` deltaP `9.3181` edge `0.2686` maxDD `-7.4246`
- `market_context_high->metal_4h` score `2.0025` n `43` status `ready` deltaP `22.9297` edge `0.0565` maxDD `-0.7323`
- `market_context_high->crypto_alt_24h` score `1.8263` n `38` status `ready` deltaP `-7.1729` edge `0.3518` maxDD `-8.8096`
- `market_context_high->crypto_alt_1h` score `1.515` n `43` status `ready` deltaP `3.7878` edge `0.147` maxDD `-1.6799`
- `market_context_high->commodity_4h` score `1.3777` n `43` status `ready` deltaP `25.1808` edge `0.05` maxDD `-1.633`
- `market_context_high->crypto_major_1h` score `1.3572` n `43` status `ready` deltaP `5.5146` edge `0.117` maxDD `-1.2532`
- `market_context_high->index_4h` score `0.9417` n `43` status `ready` deltaP `13.326` edge `0.0349` maxDD `-1.2876`
- `market_context_high->metal_1h` score `0.6877` n `43` status `ready` deltaP `9.5565` edge `0.0193` maxDD `-0.3895`
- `market_context_high->fx_1h` score `0.5974` n `43` status `ready` deltaP `12.7907` edge `0.0089` maxDD `-0.0736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
