# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T20:37:21.767799+00:00`
- Price records: `672`
- Market context records: `1562`
- Flow alert records: `6407`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.7065` n `182` status `ready` deltaP `24.8588` edge `0.9932` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.0142` n `182` status `ready` deltaP `26.9974` edge `0.9395` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.5013` n `182` status `ready` deltaP `26.7399` edge `0.7267` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0332` n `182` status `ready` deltaP `20.7799` edge `0.3062` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.0931` n `182` status `ready` deltaP `15.4571` edge `0.3874` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.487` n `199` status `ready` deltaP `6.0056` edge `0.11` maxDD `-5.0894`
- `market_context_high->fx_24h` score `0.4541` n `182` status `ready` deltaP `14.2723` edge `0.0476` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.0492` n `199` status `ready` deltaP `13.2545` edge `0.2499` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.1118` n `199` status `ready` deltaP `9.1272` edge `0.1957` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.2973` n `199` status `ready` deltaP `1.1171` edge `0.0568` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6576` n `199` status `ready` deltaP `-2.593` edge `-0.0038` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.6876` n `199` status `ready` deltaP `0.1016` edge `0.0033` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7345` n `199` status `ready` deltaP `5.1478` edge `0.0051` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.738` n `199` status `ready` deltaP `0.0256` edge `0.0015` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.7433` n `199` status `ready` deltaP `-0.8831` edge `0.0248` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.8732` n `199` status `ready` deltaP `-0.4438` edge `0.0267` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3768` n `199` status `ready` deltaP `-10.3973` edge `-0.0143` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.3842` n `199` status `ready` deltaP `-3.9826` edge `0.0201` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3887` n `199` status `ready` deltaP `10.0587` edge `0.0864` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.0276` n `199` status `ready` deltaP `-13.3281` edge `-0.093` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
