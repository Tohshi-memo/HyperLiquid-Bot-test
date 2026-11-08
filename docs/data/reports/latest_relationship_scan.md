# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T10:22:27.778736+00:00`
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

- `market_context_high->unknown_4h` score `113.1166` n `37` status `ready` deltaP `-3.9387` edge `9.4974` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2676` n `37` status `ready` deltaP `10.5074` edge `0.2482` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1449` n `37` status `ready` deltaP `33.9239` edge `0.0449` maxDD `-0.0521`
- `market_context_high->equity_24h` score `2.8771` n `33` status `ready` deltaP `9.517` edge `0.7349` maxDD `-31.3588`
- `news_risk_high->fx_4h` score `2.0856` n `42` status `ready` deltaP `25.0436` edge `0.0154` maxDD `-0.0177`
- `market_context_high->index_4h` score `2.0548` n `37` status `ready` deltaP `26.8128` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.0348` n `39` status `ready` deltaP `4.2201` edge `0.0802` maxDD `-0.1014`
- `market_context_high->crypto_major_1h` score `0.8274` n `37` status `ready` deltaP `10.0502` edge `0.0605` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.555` n `33` status `ready` deltaP `6.4394` edge `0.0913` maxDD `-2.7123`
- `market_context_high->crypto_alt_1h` score `0.5503` n `37` status `ready` deltaP `12.146` edge `0.0711` maxDD `-3.1881`
- `news_risk_high->fx_1h` score `0.4489` n `42` status `ready` deltaP `10.9781` edge `0.0059` maxDD `-0.0567`
- `market_context_high->fx_24h` score `0.4456` n `33` status `ready` deltaP `8.649` edge `-0.0117` maxDD `-0.0397`
- `market_context_high->commodity_24h` score `0.3849` n `33` status `ready` deltaP `2.5726` edge `0.1517` maxDD `-6.5601`
- `market_context_high->fx_1h` score `0.3727` n `37` status `ready` deltaP `6.4736` edge `0.015` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.3356` n `37` status `ready` deltaP `2.3993` edge `0.039` maxDD `-0.1621`
- `news_risk_high->equity_4h` score `0.202` n `42` status `ready` deltaP `-2.1704` edge `0.1052` maxDD `-4.2454`
- `market_context_high->commodity_1h` score `0.1187` n `37` status `ready` deltaP `9.0185` edge `0.0097` maxDD `-1.7019`
- `news_risk_high->index_4h` score `0.0589` n `42` status `ready` deltaP `5.2555` edge `0.0204` maxDD `-0.4975`
- `news_risk_high->index_1h` score `-0.0327` n `42` status `ready` deltaP `5.8098` edge `0.0024` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `-0.052` n `37` status `ready` deltaP `2.3773` edge `0.0229` maxDD `-1.633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
