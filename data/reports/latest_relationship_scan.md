# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T19:37:21.164063+00:00`
- Price records: `672`
- Market context records: `1558`
- Flow alert records: `6394`
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

- `market_context_high->metal_24h` score `12.5405` n `182` status `ready` deltaP `24.1643` edge `0.984` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.8858` n `182` status `ready` deltaP `26.9974` edge `0.9288` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.3657` n `182` status `ready` deltaP `26.7399` edge `0.7154` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0548` n `182` status `ready` deltaP `20.7799` edge `0.308` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8732` n `182` status `ready` deltaP `14.7627` edge `0.3737` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.5265` n `182` status `ready` deltaP `14.9668` edge `0.049` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.3785` n `199` status `ready` deltaP `5.5483` edge `0.104` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.0608` n `199` status `ready` deltaP `13.2545` edge `0.2358` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.1805` n `199` status `ready` deltaP `9.1272` edge `0.1869` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.3199` n `199` status `ready` deltaP `1.1171` edge `0.0539` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6421` n `199` status `ready` deltaP `-2.2936` edge `-0.0038` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7063` n `199` status `ready` deltaP `-0.1978` edge `0.0029` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7376` n `199` status `ready` deltaP `5.1478` edge `0.0047` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7596` n `199` status `ready` deltaP `-0.1241` edge `0.0007` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.7768` n `199` status `ready` deltaP `-1.0328` edge `0.023` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.8919` n `199` status `ready` deltaP `-0.5935` edge `0.0253` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3752` n `199` status `ready` deltaP `-10.3973` edge `-0.0141` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4055` n `199` status `ready` deltaP `10.0587` edge `0.085` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4376` n `199` status `ready` deltaP `-4.4399` edge `0.0187` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.052` n `199` status `ready` deltaP `-13.633` edge `-0.0941` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
