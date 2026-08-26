# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T07:22:26.976798+00:00`
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

- `news_risk_high->unknown_24h` score `46.647` n `51` status `ready` deltaP `11.6319` edge `3.8097` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.7294` n `53` status `ready` deltaP `22.6933` edge `0.8361` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `8.5295` n `51` status `ready` deltaP `31.4236` edge `0.5013` maxDD `0.0`
- `news_risk_high->equity_24h` score `7.0977` n `51` status `ready` deltaP `29.9939` edge `0.4846` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0568` n `51` status `ready` deltaP `40.2676` edge `0.0848` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.7755` n `53` status `ready` deltaP `33.4388` edge `0.0218` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7387` n `53` status `ready` deltaP `15.4135` edge `0.161` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.4546` n `134` status `ready` deltaP `20.891` edge `0.1061` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7787` n `53` status `ready` deltaP `19.7365` edge `0.0937` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.4517` n `51` status `ready` deltaP `29.1156` edge `-0.0689` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.0686` n `53` status `ready` deltaP `15.0209` edge `0.0059` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.057` n `136` status `ready` deltaP `11.4873` edge `0.0564` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `0.4661` n `53` status `ready` deltaP `13.0748` edge `0.009` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4523` n `53` status `ready` deltaP `10.9762` edge `-0.0042` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.0695` n `53` status `ready` deltaP `5.8991` edge `0.0062` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0721` n `53` status `ready` deltaP `3.8499` edge `0.0004` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4442` n `136` status `ready` deltaP `2.5625` edge `-0.0008` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.475` n `53` status `ready` deltaP `-0.7626` edge `-0.0119` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7043` n `53` status `ready` deltaP `3.1379` edge `-0.0265` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0466` n `53` status `ready` deltaP `-2.1255` edge `0.0033` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
