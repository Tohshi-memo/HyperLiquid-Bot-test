# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T00:52:31.201778+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5392`

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

- `market_context_high->unknown_1h` score `101.5615` n `97` status `ready` deltaP `0.1389` edge `8.504` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `99.9638` n `97` status `ready` deltaP `2.7564` edge `8.3431` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `9.6926` n `65` status `ready` deltaP `33.7711` edge `0.6029` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.7295` n `49` status `ready` deltaP `26.9487` edge `0.5297` maxDD `-4.5519`
- `news_risk_high->crypto_alt_4h` score `6.7271` n `65` status `ready` deltaP `21.6159` edge `0.5509` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `6.4918` n `49` status `ready` deltaP `21.0424` edge `0.528` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `5.1097` n `65` status `ready` deltaP `17.2837` edge `0.3206` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.0261` n `97` status `ready` deltaP `17.7521` edge `0.2875` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.56` n `65` status `ready` deltaP `25.0` edge `0.13` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.0701` n `65` status `ready` deltaP `22.2537` edge `0.1685` maxDD `-2.881`
- `news_risk_high->index_4h` score `2.9898` n `65` status `ready` deltaP `32.8284` edge `0.0565` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.7099` n `65` status `ready` deltaP `11.2137` edge `0.1866` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.2033` n `65` status `ready` deltaP `19.993` edge `0.0919` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1393` n `65` status `ready` deltaP `26.3657` edge `0.0175` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9714` n `97` status `ready` deltaP `14.1321` edge `0.1151` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5211` n `65` status `ready` deltaP `5.0184` edge `0.1452` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.4808` n `49` status `ready` deltaP `27.8912` edge `0.1057` maxDD `-1.8102`
- `market_context_high->fx_4h` score `1.4552` n `97` status `ready` deltaP `25.4306` edge `0.0274` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.9791` n `97` status `ready` deltaP `15.166` edge `0.0069` maxDD `-0.113`
- `market_context_high->crypto_alt_4h` score `0.8404` n `97` status `ready` deltaP `3.4716` edge `0.2258` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
