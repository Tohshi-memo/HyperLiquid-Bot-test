# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T12:22:23.765327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `44.8338` n `53` status `ready` deltaP `11.6319` edge `3.6586` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.0554` n `53` status `ready` deltaP `24.2176` edge `0.8531` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `9.7447` n `53` status `ready` deltaP `31.1222` edge `0.6487` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `6.9828` n `53` status `ready` deltaP `29.5925` edge `0.4777` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0409` n `53` status `ready` deltaP `40.114` edge `0.0845` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.9023` n `53` status `ready` deltaP `34.9632` edge `0.0222` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7375` n `53` status `ready` deltaP `15.2638` edge `0.1619` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.6885` n `136` status `ready` deltaP `22.5251` edge `0.1147` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.7936` n `53` status `ready` deltaP `29.1896` edge `-0.0409` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7549` n `53` status `ready` deltaP `19.889` edge `0.0907` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.0758` n `53` status `ready` deltaP `15.1706` edge `0.0055` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.05` n `137` status `ready` deltaP `11.504` edge `0.0557` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `0.4864` n `53` status `ready` deltaP `12.9251` edge `0.0126` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4308` n `53` status `ready` deltaP `10.6768` edge `-0.004` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1997` n `53` status `ready` deltaP `7.2711` edge `0.0079` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0573` n `53` status `ready` deltaP `3.9996` edge `0.0013` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.2264` n `53` status `ready` deltaP `6.1867` edge `-0.007` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3408` n `53` status `ready` deltaP `0.435` edge `-0.0087` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4613` n `137` status `ready` deltaP `2.2936` edge `-0.0012` maxDD `-0.8587`
- `news_risk_high->commodity_4h` score `-0.9504` n `53` status `ready` deltaP `-0.7536` edge `0.0065` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
