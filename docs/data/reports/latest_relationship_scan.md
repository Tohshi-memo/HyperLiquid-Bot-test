# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T05:37:14.017639+00:00`
- Price records: `672`
- Market context records: `1291`
- Flow alert records: `5628`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.4721` n `128` status `ready` deltaP `41.5798` edge `1.292` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.0639` n `128` status `ready` deltaP `9.2014` edge `1.1107` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.3137` n `128` status `ready` deltaP `26.9965` edge `0.7978` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.7636` n `128` status `ready` deltaP `30.0347` edge `0.3887` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9756` n `128` status `ready` deltaP `25.3472` edge `0.5734` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3727` n `149` status `ready` deltaP `12.1532` edge `0.1872` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3658` n `128` status `ready` deltaP `1.5625` edge `0.4597` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.1022` n `128` status `ready` deltaP `-14.7569` edge `0.3384` maxDD `-6.8535`
- `market_context_high->unknown_4h` score `0.7163` n `149` status `ready` deltaP `3.1071` edge `0.2661` maxDD `-11.1695`
- `market_context_high->fx_24h` score `0.4472` n `128` status `ready` deltaP `6.8577` edge `0.038` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.178` n `157` status `ready` deltaP `3.5174` edge `0.0341` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1398` n `149` status `ready` deltaP `5.9584` edge `0.0871` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.1045` n `157` status `ready` deltaP `6.2121` edge `0.0174` maxDD `-1.6329`
- `market_context_high->metal_1h` score `0.0831` n `157` status `ready` deltaP `10.1396` edge `0.0083` maxDD `-2.8509`
- `market_context_high->metal_4h` score `0.017` n `149` status `ready` deltaP `12.6617` edge `0.0601` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.5493` n `157` status `ready` deltaP `0.5092` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5953` n `157` status `ready` deltaP `0.8467` edge `0.0318` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.7901` n `149` status `ready` deltaP `9.399` edge `0.168` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-0.8112` n `157` status `ready` deltaP `-0.1688` edge `-0.0008` maxDD `-5.8323`
- `market_context_high->crypto_major_4h` score `-0.8957` n `149` status `ready` deltaP `5.2433` edge `0.1211` maxDD `-13.3376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
