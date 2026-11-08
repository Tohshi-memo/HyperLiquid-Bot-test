# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T11:07:28.477103+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4713`

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

- `market_context_high->unknown_4h` score `99.9956` n `37` status `ready` deltaP `-4.0911` edge `8.405` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.6348` n `36` status `ready` deltaP `14.0625` edge `0.8053` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.282` n `37` status `ready` deltaP `10.6571` edge `0.2484` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1205` n `37` status `ready` deltaP `33.619` edge `0.0449` maxDD `-0.0521`
- `news_risk_high->fx_4h` score `2.4102` n `39` status `ready` deltaP `28.768` edge `0.0176` maxDD `-0.016`
- `market_context_high->index_4h` score `2.0682` n `37` status `ready` deltaP `26.9652` edge `0.0396` maxDD `-2.4279`
- `market_context_high->crypto_major_1h` score `0.861` n `37` status `ready` deltaP `10.3496` edge `0.0613` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.7718` n `36` status `ready` deltaP `9.7222` edge `0.0972` maxDD `-2.7123`
- `news_risk_high->fx_24h` score `0.7295` n `36` status `ready` deltaP `2.0833` edge `0.069` maxDD `-0.1014`
- `market_context_high->commodity_24h` score `0.7065` n `36` status `ready` deltaP `6.5972` edge `0.1661` maxDD `-6.5601`
- `market_context_high->fx_24h` score `0.611` n `36` status `ready` deltaP `10.4167` edge `-0.0097` maxDD `-0.0397`
- `market_context_high->crypto_alt_1h` score `0.5807` n `37` status `ready` deltaP `12.5951` edge `0.072` maxDD `-3.1881`
- `news_risk_high->fx_1h` score `0.5806` n `39` status `ready` deltaP `13.3925` edge `0.0067` maxDD `-0.0567`
- `market_context_high->fx_1h` score `0.3607` n `37` status `ready` deltaP `6.3239` edge `0.015` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.3105` n `37` status `ready` deltaP `2.0999` edge `0.0389` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.1109` n `37` status `ready` deltaP `8.8688` edge `0.0097` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0366` n `39` status `ready` deltaP `7.1588` edge `0.0023` maxDD `-0.2931`
- `news_risk_high->equity_4h` score `-0.0441` n `39` status `ready` deltaP `-3.9713` edge `0.0967` maxDD `-4.2454`
- `market_context_high->metal_1h` score `-0.0474` n `37` status `ready` deltaP `1.5011` edge `0.0167` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.0607` n `37` status `ready` deltaP `2.2248` edge `0.0228` maxDD `-1.633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
