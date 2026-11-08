# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T16:22:24.138790+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4839`

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

- `market_context_high->unknown_4h` score `30.043` n `39` status `ready` deltaP `-4.6591` edge `2.5794` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.0413` n `37` status `ready` deltaP `14.7195` edge `0.8348` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3835` n `39` status `ready` deltaP `12.7361` edge `0.243` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.822` n `39` status `ready` deltaP `30.2924` edge `0.0422` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8881` n `39` status `ready` deltaP `24.789` edge `0.0391` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.1609` n `39` status `ready` deltaP `14.2139` edge `0.0835` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1105` n `39` status `ready` deltaP `11.8187` edge `0.0723` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.9723` n `37` status `ready` deltaP `11.9135` edge `0.1083` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7646` n `37` status `ready` deltaP `10.9422` edge `-0.0004` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.5075` n `39` status `ready` deltaP `8.2643` edge `0.0143` maxDD `-0.1681`
- `market_context_high->commodity_24h` score `0.4172` n `37` status `ready` deltaP `4.3028` edge `0.1443` maxDD `-6.5601`
- `market_context_high->index_1h` score `0.2581` n `39` status `ready` deltaP `3.3779` edge `0.0376` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0621` n `39` status `ready` deltaP `7.9457` edge `0.0096` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0269` n `39` status `ready` deltaP `2.0306` edge `0.0158` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1508` n `39` status `ready` deltaP `0.4925` edge `0.0228` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5884` n `39` status `ready` deltaP `23.1669` edge `0.0981` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7825` n `39` status `ready` deltaP `-3.0566` edge `-0.0349` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9361` n `39` status `ready` deltaP `16.1664` edge `0.0165` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-2.0862` n `37` status `ready` deltaP `3.5333` edge `-0.1421` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8522` n `39` status `ready` deltaP `1.794` edge `-0.108` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
