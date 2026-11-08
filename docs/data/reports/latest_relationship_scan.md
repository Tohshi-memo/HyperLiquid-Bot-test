# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T13:07:26.869279+00:00`
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

- `market_context_high->unknown_4h` score `65.1684` n `37` status `ready` deltaP `-4.7009` edge `5.5068` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.1029` n `37` status `ready` deltaP `15.4139` edge `0.8353` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3368` n `39` status `ready` deltaP `12.287` edge `0.2421` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1327` n `37` status `ready` deltaP `33.7714` edge `0.0449` maxDD `-0.0521`
- `news_risk_high->fx_4h` score `2.7868` n `31` status `ready` deltaP `32.7252` edge `0.0226` maxDD `-0.016`
- `market_context_high->index_4h` score `2.1498` n `37` status `ready` deltaP `27.8799` edge `0.0403` maxDD `-2.4279`
- `news_risk_high->fx_1h` score `1.72` n `31` status `ready` deltaP `21.4314` edge `0.0095` maxDD `-0.0567`
- `market_context_high->crypto_alt_1h` score `1.174` n `39` status `ready` deltaP `14.5133` edge `0.0826` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1105` n `39` status `ready` deltaP `11.9684` edge `0.0713` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.8631` n `37` status `ready` deltaP `10.6982` edge `0.1024` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.6962` n `37` status `ready` deltaP `10.9422` edge `-0.0061` maxDD `-0.0397`
- `market_context_high->commodity_24h` score `0.682` n `37` status `ready` deltaP `6.5597` edge `0.1632` maxDD `-6.5601`
- `market_context_high->fx_1h` score `0.4956` n `39` status `ready` deltaP `8.1146` edge `0.0143` maxDD `-0.1681`
- `news_risk_high->index_1h` score `0.209` n `31` status `ready` deltaP `9.1124` edge `0.002` maxDD `-0.2931`
- `market_context_high->index_1h` score `0.2013` n `39` status `ready` deltaP `2.33` edge `0.0373` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.073` n `39` status `ready` deltaP `8.0954` edge `0.01` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0596` n `39` status `ready` deltaP `1.4318` edge `0.0156` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.0599` n `37` status `ready` deltaP `2.2248` edge `0.0229` maxDD `-1.633`
- `news_risk_high->equity_4h` score `-0.2374` n `31` status `ready` deltaP `-3.1619` edge `0.0752` maxDD `-4.2454`
- `news_risk_high->equity_1h` score `-0.4082` n `31` status `ready` deltaP `-4.0902` edge `0.0295` maxDD `-1.3653`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
