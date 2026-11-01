# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T03:22:27.636798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6285`

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

- `market_context_high->unknown_24h` score `5169.1326` n `69` status `ready` deltaP `-4.0685` edge `430.8131` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `234.1971` n `69` status `ready` deltaP `0.528` edge `19.5262` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `81.502` n `108` status `ready` deltaP `-5.0454` edge `6.8541` maxDD `-0.9571`
- `market_context_high->equity_24h` score `15.0166` n `69` status `ready` deltaP `29.129` edge `1.2122` maxDD `-7.7343`
- `news_risk_high->crypto_alt_24h` score `14.6389` n `92` status `ready` deltaP `35.0921` edge `1.1033` maxDD `-6.3871`
- `market_context_high->index_24h` score `5.7985` n `69` status `ready` deltaP `49.9245` edge `0.1682` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.4307` n `108` status `ready` deltaP `20.5793` edge `0.454` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `2.8047` n `69` status `ready` deltaP `27.6489` edge `0.0828` maxDD `-0.3387`
- `market_context_high->commodity_24h` score `1.327` n `69` status `ready` deltaP `29.8611` edge `0.1356` maxDD `-8.4967`
- `market_context_high->metal_4h` score `1.2999` n `69` status `ready` deltaP `15.9773` edge `0.0443` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.8876` n `108` status `ready` deltaP `9.1761` edge `0.1082` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7404` n `69` status `ready` deltaP `10.3662` edge `0.0216` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.6831` n `69` status `ready` deltaP `15.8704` edge `0.0002` maxDD `-0.1407`
- `market_context_high->equity_4h` score `0.6809` n `69` status `ready` deltaP `-3.4708` edge `0.2156` maxDD `-3.747`
- `market_context_high->fx_4h` score `0.3219` n `69` status `ready` deltaP `9.5749` edge `0.0021` maxDD `-0.1285`
- `market_context_high->equity_1h` score `0.241` n `69` status `ready` deltaP `-0.1258` edge `0.1193` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.1184` n `69` status `ready` deltaP `3.0721` edge `0.0671` maxDD `-5.2213`
- `market_context_high->crypto_major_4h` score `-0.1226` n `69` status `ready` deltaP `14.9899` edge `0.0877` maxDD `-11.2677`
- `market_context_high->commodity_1h` score `-0.2219` n `69` status `ready` deltaP `1.97` edge `0.0198` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.6014` n `69` status `ready` deltaP `-3.3238` edge `0.0009` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
