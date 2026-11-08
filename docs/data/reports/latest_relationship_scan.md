# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T13:22:27.856285+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4735`

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

- `market_context_high->unknown_4h` score `61.1435` n `37` status `ready` deltaP `-4.8533` edge `5.1724` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.1173` n `37` status `ready` deltaP `15.4139` edge `0.8365` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3368` n `39` status `ready` deltaP `12.287` edge `0.2421` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1339` n `37` status `ready` deltaP `33.7714` edge `0.045` maxDD `-0.0521`
- `news_risk_high->fx_4h` score `2.7744` n `30` status `ready` deltaP `32.5101` edge `0.023` maxDD `-0.016`
- `market_context_high->index_4h` score `2.1498` n `37` status `ready` deltaP `27.8799` edge `0.0403` maxDD `-2.4279`
- `news_risk_high->fx_1h` score `1.661` n `30` status `ready` deltaP `20.6787` edge `0.0096` maxDD `-0.0567`
- `market_context_high->crypto_alt_1h` score `1.1848` n `39` status `ready` deltaP `14.5133` edge `0.0835` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1093` n `39` status `ready` deltaP `11.9684` edge `0.0712` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.8662` n `37` status `ready` deltaP `10.6982` edge `0.1028` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7022` n `37` status `ready` deltaP `10.9422` edge `-0.0056` maxDD `-0.0397`
- `market_context_high->commodity_24h` score `0.6651` n `37` status `ready` deltaP `6.3861` edge `0.1622` maxDD `-6.5601`
- `market_context_high->fx_1h` score `0.4944` n `39` status `ready` deltaP `8.1146` edge `0.0142` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.2013` n `39` status `ready` deltaP `2.33` edge `0.0373` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.073` n `39` status `ready` deltaP `8.0954` edge `0.01` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0616` n `30` status `ready` deltaP `7.7146` edge `0.0018` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0518` n `39` status `ready` deltaP `1.5815` edge `0.0156` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.0599` n `37` status `ready` deltaP `2.2248` edge `0.0229` maxDD `-1.633`
- `news_risk_high->equity_4h` score `-0.4664` n `30` status `ready` deltaP `-4.9899` edge `0.0683` maxDD `-4.2454`
- `news_risk_high->equity_1h` score `-0.5282` n `30` status `ready` deltaP `-5.9182` edge `0.0263` maxDD `-1.3653`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
