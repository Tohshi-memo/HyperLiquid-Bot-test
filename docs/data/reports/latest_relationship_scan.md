# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T15:22:28.783678+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4781`

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

- `market_context_high->unknown_4h` score `30.12` n `39` status `ready` deltaP `-4.5067` edge `2.5848` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.1581` n `37` status `ready` deltaP `15.4139` edge `0.8399` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3655` n `39` status `ready` deltaP `12.5864` edge `0.2425` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.8086` n `39` status `ready` deltaP `30.1399` edge `0.0421` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8759` n `39` status `ready` deltaP `24.6365` edge `0.0391` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2232` n `39` status `ready` deltaP `14.663` edge `0.0857` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1536` n `39` status `ready` deltaP `12.2678` edge `0.0729` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.9229` n `37` status `ready` deltaP `11.2191` edge `0.1066` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7466` n `37` status `ready` deltaP `10.9422` edge `-0.0019` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.5207` n `39` status `ready` deltaP `8.414` edge `0.0144` maxDD `-0.1681`
- `market_context_high->commodity_24h` score `0.5118` n `37` status `ready` deltaP `4.9972` edge `0.1518` maxDD `-6.5601`
- `market_context_high->index_1h` score `0.2426` n `39` status `ready` deltaP `3.0785` edge `0.0376` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0816` n `39` status `ready` deltaP `8.2451` edge `0.0101` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0354` n `39` status `ready` deltaP `1.8809` edge `0.0157` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1159` n `39` status `ready` deltaP `1.1023` edge `0.0232` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5868` n `39` status `ready` deltaP `23.1669` edge `0.0983` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.8086` n `39` status `ready` deltaP `-3.514` edge `-0.0352` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9057` n `39` status `ready` deltaP `16.1664` edge `0.0204` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-2.1754` n `37` status `ready` deltaP `2.8388` edge `-0.1449` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.81` n `39` status `ready` deltaP `1.9465` edge `-0.1055` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
