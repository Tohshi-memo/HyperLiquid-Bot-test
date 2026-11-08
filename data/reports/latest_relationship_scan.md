# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T09:52:32.068821+00:00`
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

- `market_context_high->unknown_4h` score `121.2262` n `37` status `ready` deltaP `-3.9387` edge `10.1732` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2844` n `37` status `ready` deltaP `10.6571` edge `0.2486` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1449` n `37` status `ready` deltaP `33.9239` edge `0.0449` maxDD `-0.0521`
- `market_context_high->equity_24h` score `2.2566` n `31` status `ready` deltaP `5.998` edge `0.6788` maxDD `-31.3588`
- `market_context_high->index_4h` score `2.0548` n `37` status `ready` deltaP `26.8128` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_4h` score `1.6559` n `44` status `ready` deltaP `21.1475` edge `0.014` maxDD `-0.0259`
- `news_risk_high->fx_24h` score `1.2177` n `41` status `ready` deltaP `5.4709` edge `0.0871` maxDD `-0.1014`
- `market_context_high->crypto_major_1h` score `0.8262` n `37` status `ready` deltaP `10.0502` edge `0.0604` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.5488` n `37` status `ready` deltaP `12.146` edge `0.0709` maxDD `-3.1881`
- `news_risk_high->equity_4h` score `0.4587` n `44` status `ready` deltaP `0.3188` edge `0.11` maxDD `-4.2454`
- `market_context_high->index_24h` score `0.3854` n `31` status `ready` deltaP `3.8978` edge `0.0865` maxDD `-2.7123`
- `market_context_high->fx_1h` score `0.3727` n `37` status `ready` deltaP `6.4736` edge `0.015` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.3596` n `37` status `ready` deltaP `2.6987` edge `0.039` maxDD `-0.1621`
- `market_context_high->fx_24h` score `0.3241` n `31` status `ready` deltaP `7.2805` edge `-0.0127` maxDD `-0.0397`
- `news_risk_high->fx_1h` score `0.2874` n `44` status `ready` deltaP `7.9478` edge `0.0054` maxDD `-0.0567`
- `market_context_high->commodity_1h` score `0.135` n `37` status `ready` deltaP `9.3179` edge `0.0098` maxDD `-1.7019`
- `market_context_high->commodity_24h` score `0.1217` n `31` status `ready` deltaP `-0.5992` edge `0.1391` maxDD `-6.5601`
- `news_risk_high->index_4h` score `0.0333` n `44` status `ready` deltaP `4.8226` edge `0.02` maxDD `-0.4975`
- `market_context_high->commodity_4h` score `-0.0338` n `37` status `ready` deltaP `2.6821` edge `0.0232` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0801` n `37` status `ready` deltaP `0.9023` edge `0.0165` maxDD `-0.6226`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
