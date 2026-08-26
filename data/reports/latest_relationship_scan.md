# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T17:22:47.591621+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `45.6545` n `53` status `ready` deltaP `11.5717` edge `3.7274` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.255` n `53` status `ready` deltaP `34.3957` edge `0.9194` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.4777` n `53` status `ready` deltaP `26.6613` edge `0.872` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `6.902` n `53` status `ready` deltaP `29.6771` edge `0.4704` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9165` n `53` status `ready` deltaP `38.9644` edge `0.0818` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.0659` n `137` status `ready` deltaP `25.0224` edge `0.1295` maxDD `-0.5994`
- `news_risk_high->fx_4h` score `3.0` n `53` status `ready` deltaP `36.1096` edge `0.0227` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.8454` n `53` status `ready` deltaP `16.0123` edge `0.1659` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.1073` n `53` status `ready` deltaP `31.1011` edge `-0.0275` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7974` n `53` status `ready` deltaP `20.1506` edge `0.0925` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.1579` n `137` status `ready` deltaP `12.2525` edge `0.0597` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.1297` n `53` status `ready` deltaP `15.7694` edge `0.006` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4715` n `53` status `ready` deltaP `13.3742` edge `0.0077` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.396` n `53` status `ready` deltaP `10.5271` edge `-0.0059` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.144` n `53` status `ready` deltaP `9.0474` edge `0.0048` maxDD `-0.249`
- `news_risk_high->index_4h` score `0.1093` n `53` status `ready` deltaP `6.442` edge `0.0059` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0807` n `53` status `ready` deltaP `3.7002` edge `0.0003` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.1455` n `53` status `ready` deltaP `2.2314` edge `-0.0044` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4263` n `137` status `ready` deltaP `2.8924` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.8403` n `137` status `ready` deltaP `6.0864` edge `-0.0234` maxDD `-2.9763`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
