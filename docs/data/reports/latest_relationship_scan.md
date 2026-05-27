# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T22:07:17.302768+00:00`
- Price records: `672`
- Market context records: `2080`
- Flow alert records: `7883`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_major_4h` score `10.0813` n `199` status `ready` deltaP `35.8507` edge `0.6541` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.627` n `199` status `ready` deltaP `28.7872` edge `0.7248` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.2915` n `199` status `ready` deltaP `24.1405` edge `0.5216` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.5184` n `198` status `ready` deltaP `21.1666` edge `0.8508` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.7673` n `199` status `ready` deltaP `20.3694` edge `0.2876` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.1736` n `199` status `ready` deltaP `16.3945` edge `0.1402` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.01` n `199` status `ready` deltaP `14.867` edge `0.167` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.8154` n `198` status `ready` deltaP `21.4235` edge `0.4983` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.7346` n `198` status `ready` deltaP `10.3929` edge `0.1981` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.6576` n `199` status `ready` deltaP `11.5202` edge `0.1727` maxDD `-4.9097`
- `market_context_high->equity_1h` score `0.5395` n `199` status `ready` deltaP `8.9535` edge `0.0641` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.4464` n `199` status `ready` deltaP `4.9446` edge `0.0762` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.34` n `198` status `ready` deltaP `21.137` edge `0.746` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.1378` n `199` status `ready` deltaP `3.6079` edge `0.0235` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.1597` n `198` status `ready` deltaP `14.6238` edge `0.0285` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.307` n `199` status `ready` deltaP `12.4074` edge `0.1462` maxDD `-11.3602`
- `market_context_high->metal_1h` score `-0.6866` n `199` status `ready` deltaP `4.3142` edge `0.0286` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.9052` n `199` status `ready` deltaP `-2.0048` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3672` n `199` status `ready` deltaP `-3.9887` edge `0.0008` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.5461` n `198` status `ready` deltaP `11.1111` edge `0.1872` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
