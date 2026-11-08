# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T21:07:26.791080+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6549`

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

- `market_context_high->unknown_4h` score `81.7234` n `39` status `ready` deltaP `-4.6591` edge `6.8861` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.1457` n `37` status `ready` deltaP `11.5945` edge `0.781` maxDD `-31.3588`
- `market_context_high->fx_4h` score `2.705` n `39` status `ready` deltaP `28.9204` edge `0.0416` maxDD `-0.0521`
- `market_context_high->equity_1h` score `2.2031` n `49` status `ready` deltaP `8.0411` edge `0.1801` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8176` n `39` status `ready` deltaP `24.0268` edge `0.0383` maxDD `-2.4279`
- `market_context_high->index_24h` score `1.1522` n `37` status `ready` deltaP `14.5177` edge `0.114` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.845` n `37` status `ready` deltaP `10.9422` edge `0.0063` maxDD `-0.0397`
- `market_context_high->crypto_alt_1h` score `0.3866` n `49` status `ready` deltaP `6.4096` edge `0.071` maxDD `-3.1881`
- `market_context_high->commodity_1h` score `0.1581` n `49` status `ready` deltaP `9.8222` edge `0.0094` maxDD `-1.7019`
- `market_context_high->index_1h` score `0.1132` n `49` status `ready` deltaP `2.218` edge `0.0278` maxDD `-0.2457`
- `market_context_high->crypto_major_1h` score `0.0566` n `49` status `ready` deltaP `4.0144` edge `0.049` maxDD `-3.0172`
- `market_context_high->commodity_24h` score `0.0474` n `37` status `ready` deltaP `3.0875` edge `0.105` maxDD `-6.5601`
- `market_context_high->metal_1h` score `0.023` n `49` status `ready` deltaP `3.5103` edge `0.0113` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.056` n `39` status `ready` deltaP `1.8645` edge `0.0258` maxDD `-1.633`
- `market_context_high->fx_1h` score `-0.2498` n `49` status `ready` deltaP `-0.4369` edge `0.0092` maxDD `-0.1681`
- `market_context_high->equity_4h` score `-0.6546` n `39` status `ready` deltaP `22.4047` edge `0.0947` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.811` n `39` status `ready` deltaP `-3.6664` edge `-0.0345` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9588` n `39` status `ready` deltaP `16.1664` edge `0.0136` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.6819` n `37` status `ready` deltaP `6.8319` edge `-0.1304` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.7976` n `39` status `ready` deltaP `2.2514` edge `-0.1065` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
