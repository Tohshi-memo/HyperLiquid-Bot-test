# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T22:22:26.146695+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3336`

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

- `news_risk_high->unknown_1h` score `3216.294` n `31` status `ready` deltaP `2.0813` edge `268.0282` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3192.765` n `31` status `ready` deltaP `4.3962` edge `266.0401` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `28.0534` n `31` status `ready` deltaP `37.1528` edge `2.0901` maxDD `0.0`
- `news_risk_high->equity_24h` score `25.1436` n `31` status `ready` deltaP `36.2847` edge `1.8534` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.9031` n `31` status `ready` deltaP `36.4583` edge `1.5822` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.8614` n `31` status `ready` deltaP `24.0165` edge `0.7487` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5227` n `31` status `ready` deltaP `35.5478` edge `0.5213` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.4312` n `31` status `ready` deltaP `22.8327` edge `0.4112` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.3583` n `31` status `ready` deltaP `17.083` edge `0.843` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9929` n `31` status `ready` deltaP `42.4059` edge `0.1462` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.4479` n `31` status `ready` deltaP `37.6736` edge `0.1195` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1893` n `31` status `ready` deltaP `18.6401` edge `0.1602` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0167` n `31` status `ready` deltaP `33.871` edge `0.0516` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.55` n `31` status `ready` deltaP `30.4955` edge `0.0177` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.267` n `31` status `ready` deltaP `7.9148` edge `0.284` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0578` n `31` status `ready` deltaP `11.0585` edge `0.2258` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3623` n `31` status `ready` deltaP `27.4869` edge `0.0193` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.722` n `31` status `ready` deltaP `13.4244` edge `0.0588` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2613` n `31` status `ready` deltaP `10.0462` edge `0.0063` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.3916` n `31` status `ready` deltaP `-2.062` edge `0.0073` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
