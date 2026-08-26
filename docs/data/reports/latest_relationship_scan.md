# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T08:37:30.225033+00:00`
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

- `news_risk_high->unknown_24h` score `45.5214` n `52` status `ready` deltaP `11.6319` edge `3.7159` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.7318` n `53` status `ready` deltaP `22.6933` edge `0.8363` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `8.0275` n `52` status `ready` deltaP `30.3686` edge `0.489` maxDD `-1.4667`
- `news_risk_high->equity_24h` score `7.0832` n `52` status `ready` deltaP `29.8879` edge `0.4841` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0652` n `52` status `ready` deltaP `40.3579` edge `0.0849` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.7585` n `53` status `ready` deltaP `33.2864` edge `0.0214` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7267` n `53` status `ready` deltaP `15.2638` edge `0.161` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.365` n `136` status `ready` deltaP `21.0008` edge `0.0979` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7789` n `53` status `ready` deltaP `19.889` edge `0.0927` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.5507` n `52` status `ready` deltaP `29.1533` edge `-0.0609` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.0674` n `53` status `ready` deltaP `15.0209` edge `0.0058` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0451` n `136` status `ready` deltaP `11.3376` edge `0.0564` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.5003` n `53` status `ready` deltaP `11.4253` edge `-0.0032` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4762` n `53` status `ready` deltaP `13.2245` edge `0.0093` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.0853` n `53` status `ready` deltaP `6.0516` edge `0.0065` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.062` n `53` status `ready` deltaP `3.9996` edge `0.0007` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.445` n `136` status `ready` deltaP `2.5625` edge `-0.0009` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.4738` n `53` status `ready` deltaP `-0.7626` edge `-0.0118` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6205` n `53` status `ready` deltaP `3.9001` edge `-0.0246` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0143` n `53` status `ready` deltaP `-1.6682` edge `0.0044` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
