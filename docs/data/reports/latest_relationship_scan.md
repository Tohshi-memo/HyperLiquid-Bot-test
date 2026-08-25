# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T18:53:31.781112+00:00`
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

- `news_risk_high->unknown_24h` score `44.5412` n `51` status `ready` deltaP `6.25` edge `3.6701` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5594` n `53` status `ready` deltaP `24.2176` edge `0.8951` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.8132` n `51` status `ready` deltaP `30.6883` edge `0.5396` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1076` n `51` status `ready` deltaP `40.962` edge `0.0844` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1742` n `53` status `ready` deltaP `16.162` edge `0.1923` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0392` n `53` status `ready` deltaP `36.0303` edge `0.0265` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6008` n `133` status `ready` deltaP `22.3592` edge `0.1085` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.6417` n `53` status `ready` deltaP `19.5841` edge `0.0833` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1752` n `53` status `ready` deltaP `16.2185` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4723` n `53` status `ready` deltaP `13.8233` edge `0.0048` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3816` n `53` status `ready` deltaP `10.3774` edge `-0.0061` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2159` n `53` status `ready` deltaP `7.7284` edge `0.0062` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.1566` n `133` status `ready` deltaP `11.7216` edge `-0.0202` maxDD `-1.5916`
- `news_risk_high->crypto_alt_24h` score `0.107` n `51` status `ready` deltaP `22.7431` edge `-0.1427` maxDD `0.0`
- `news_risk_high->metal_24h` score `0.044` n `51` status `ready` deltaP `25.4698` edge `-0.1619` maxDD `-0.0053`
- `news_risk_high->index_1h` score `-0.0488` n `53` status `ready` deltaP `4.299` edge `0.0004` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4273` n `133` status `ready` deltaP `2.7982` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.4822` n `53` status `ready` deltaP `-0.9123` edge `-0.0115` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6022` n `53` status `ready` deltaP `4.205` edge `-0.0251` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-1.066` n `125` status `ready` deltaP `6.25` edge `-0.1305` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
