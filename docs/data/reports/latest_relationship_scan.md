# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T06:22:22.886095+00:00`
- Price records: `672`
- Market context records: `2840`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->unknown_24h` score `2.4392` n `142` status `ready` deltaP `3.4697` edge `0.2266` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.3208` n `142` status `ready` deltaP `0.9659` edge `0.4953` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8512` n `142` status `ready` deltaP `6.4904` edge `0.133` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.7207` n `142` status `ready` deltaP `11.2114` edge `0.2947` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3309` n `142` status `ready` deltaP `13.3009` edge `0.0379` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0814` n `142` status `ready` deltaP `4.4805` edge `0.05` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0953` n `142` status `ready` deltaP `4.0483` edge `0.0102` maxDD `-1.2855`
- `market_context_high->index_24h` score `-0.1262` n `142` status `ready` deltaP `4.509` edge `0.0575` maxDD `-2.5127`
- `market_context_high->fx_1h` score `-0.5766` n `142` status `ready` deltaP `-0.9867` edge `0.0029` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6117` n `142` status `ready` deltaP `-0.2825` edge `-0.0012` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7058` n `142` status `ready` deltaP `0.1328` edge `-0.0068` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7568` n `142` status `ready` deltaP `4.6471` edge `0.048` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.9698` n `142` status `ready` deltaP `-2.8991` edge `0.0218` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9802` n `142` status `ready` deltaP `3.6266` edge `0.0371` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.0498` n `142` status `ready` deltaP `1.9624` edge `0.0374` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1445` n `142` status `ready` deltaP `-3.6005` edge `0.0065` maxDD `-0.5631`
- `market_context_high->equity_24h` score `-1.2908` n `142` status `ready` deltaP `2.3107` edge `0.0774` maxDD `-12.6963`
- `market_context_high->commodity_4h` score `-1.3782` n `142` status `ready` deltaP `1.5329` edge `0.0051` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4788` n `142` status `ready` deltaP `-2.4061` edge `-0.02` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.4837` n `142` status `ready` deltaP `13.8805` edge `0.2179` maxDD `-28.7261`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
