# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T08:37:21.080270+00:00`
- Price records: `672`
- Market context records: `2228`
- Flow alert records: `8307`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `26.1873` n `33` status `ready` deltaP `56.9602` edge `1.8614` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.731` n `33` status `ready` deltaP `47.3169` edge `0.9561` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `12.9577` n `33` status `ready` deltaP `38.2891` edge `0.856` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.8425` n `132` status `ready` deltaP `36.9965` edge `0.9172` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6438` n `132` status `ready` deltaP `41.6713` edge `0.7455` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.7551` n `33` status `ready` deltaP `37.863` edge `0.5831` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.7024` n `33` status `ready` deltaP `19.8075` edge `0.9135` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.3006` n `132` status `ready` deltaP `20.6116` edge `0.3722` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.9377` n `43` status `ready` deltaP `32.9197` edge `0.3525` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.2299` n `132` status `ready` deltaP `22.5009` edge `0.2286` maxDD `-5.0894`
- `market_context_high->index_4h` score `3.1712` n `132` status `ready` deltaP `26.1641` edge `0.1582` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.1215` n `141` status `ready` deltaP `17.2262` edge `0.193` maxDD `-1.817`
- `news_risk_high->fx_24h` score `2.9664` n `33` status `ready` deltaP `31.0606` edge `0.0586` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.8126` n `141` status `ready` deltaP `15.3979` edge `0.2181` maxDD `-4.9097`
- `news_risk_high->commodity_24h` score `2.4515` n `33` status `ready` deltaP `-1.2469` edge `0.2943` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.1756` n `43` status `ready` deltaP `27.5843` edge `0.0158` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.5776` n `132` status `ready` deltaP `8.4753` edge `0.1978` maxDD `-4.1604`
- `news_risk_high->index_24h` score `1.5056` n `33` status `ready` deltaP `10.7481` edge `0.0957` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `1.4481` n `132` status `ready` deltaP `23.4691` edge `0.4457` maxDD `-32.8525`
- `news_risk_high->unknown_1h` score `1.2945` n `43` status `ready` deltaP `20.596` edge `0.0175` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
