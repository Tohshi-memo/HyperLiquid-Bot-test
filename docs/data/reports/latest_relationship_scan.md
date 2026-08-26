# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T09:37:24.397664+00:00`
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

- `news_risk_high->unknown_24h` score `45.6438` n `52` status `ready` deltaP `11.6319` edge `3.7261` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.756` n `53` status `ready` deltaP `22.8457` edge `0.8373` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `8.8666` n `52` status `ready` deltaP `31.063` edge `0.5543` maxDD `-1.4667`
- `news_risk_high->equity_24h` score `7.0314` n `52` status `ready` deltaP `29.5406` edge `0.4821` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0954` n `52` status `ready` deltaP `40.7052` edge `0.0851` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.7561` n `53` status `ready` deltaP `33.2864` edge `0.0212` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7267` n `53` status `ready` deltaP `15.2638` edge `0.161` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.3891` n `136` status `ready` deltaP `21.1532` edge `0.0989` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.8611` n `53` status `ready` deltaP `20.3463` edge `0.0965` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.6131` n `52` status `ready` deltaP `29.1533` edge `-0.0557` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.065` n `53` status `ready` deltaP `15.0209` edge `0.0056` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0451` n `136` status `ready` deltaP `11.3376` edge `0.0564` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.517` n `53` status `ready` deltaP `11.575` edge `-0.0028` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4263` n `53` status `ready` deltaP `12.7754` edge `0.0059` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1449` n `53` status `ready` deltaP `6.6613` edge `0.0074` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0885` n `53` status `ready` deltaP `3.5505` edge `0.0003` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.4331` n `53` status `ready` deltaP `-0.3135` edge `-0.0114` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4466` n `136` status `ready` deltaP `2.5625` edge `-0.0011` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.5226` n `53` status `ready` deltaP `4.5099` edge `-0.0205` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-0.9835` n `53` status `ready` deltaP `-1.2109` edge `0.0053` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
