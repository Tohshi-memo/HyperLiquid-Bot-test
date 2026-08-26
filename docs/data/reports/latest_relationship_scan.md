# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T11:37:29.201079+00:00`
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

- `news_risk_high->unknown_24h` score `44.7102` n `53` status `ready` deltaP `11.6319` edge `3.6483` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.9444` n `53` status `ready` deltaP `23.7603` edge `0.8469` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `9.1691` n `53` status `ready` deltaP `30.6014` edge `0.6042` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.0593` n `53` status `ready` deltaP `30.1134` edge `0.4806` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0433` n `53` status `ready` deltaP `40.114` edge `0.0847` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.8621` n `53` status `ready` deltaP `34.5059` edge `0.0219` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7363` n `53` status `ready` deltaP `15.2638` edge `0.1618` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.5775` n `136` status `ready` deltaP `22.0678` edge `0.1085` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.7612` n `53` status `ready` deltaP `29.1896` edge `-0.0436` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7259` n `53` status `ready` deltaP `19.7365` edge `0.0893` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.0758` n `53` status `ready` deltaP `15.1706` edge `0.0055` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0547` n `136` status `ready` deltaP `11.3376` edge `0.0572` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.4715` n `53` status `ready` deltaP `11.1259` edge `-0.0036` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.41` n `53` status `ready` deltaP `12.476` edge `0.0058` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1851` n `53` status `ready` deltaP `7.1186` edge `0.0077` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0799` n `53` status `ready` deltaP `3.7002` edge `0.0004` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.311` n `53` status `ready` deltaP `5.7294` edge `-0.011` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3875` n `53` status `ready` deltaP `0.1356` edge `-0.0106` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4395` n `136` status `ready` deltaP `2.7122` edge `-0.0012` maxDD `-0.8587`
- `news_risk_high->commodity_4h` score `-0.9496` n `53` status `ready` deltaP `-0.7536` edge `0.0066` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
