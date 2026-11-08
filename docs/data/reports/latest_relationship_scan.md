# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T16:07:56.520651+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4825`

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

- `market_context_high->unknown_4h` score `30.0394` n `39` status `ready` deltaP `-4.6591` edge `2.5791` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.06` n `37` status `ready` deltaP `14.8931` edge `0.8352` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3835` n `39` status `ready` deltaP `12.7361` edge `0.243` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.8208` n `39` status `ready` deltaP `30.2924` edge `0.0421` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8893` n `39` status `ready` deltaP `24.789` edge `0.0392` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.1633` n `39` status `ready` deltaP `14.2139` edge `0.0837` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1237` n `39` status `ready` deltaP `11.9684` edge `0.0724` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.9594` n `37` status `ready` deltaP `11.7399` edge `0.1078` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7598` n `37` status `ready` deltaP `10.9422` edge `-0.0008` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.5075` n `39` status `ready` deltaP `8.2643` edge `0.0143` maxDD `-0.1681`
- `market_context_high->commodity_24h` score `0.441` n `37` status `ready` deltaP `4.4764` edge `0.1462` maxDD `-6.5601`
- `market_context_high->index_1h` score `0.2581` n `39` status `ready` deltaP `3.3779` edge `0.0376` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0715` n `39` status `ready` deltaP `8.0954` edge `0.0098` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0191` n `39` status `ready` deltaP `2.1803` edge `0.0158` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1421` n `39` status `ready` deltaP `0.645` edge `0.0229` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5868` n `39` status `ready` deltaP `23.1669` edge `0.0983` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7825` n `39` status `ready` deltaP `-3.0566` edge `-0.0349` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.926` n `39` status `ready` deltaP `16.1664` edge `0.0178` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-2.1085` n `37` status `ready` deltaP `3.3597` edge `-0.1428` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8426` n `39` status `ready` deltaP `1.794` edge `-0.1072` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
