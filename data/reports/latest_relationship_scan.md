# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T22:06:19.170181+00:00`
- Price records: `672`
- Market context records: `1568`
- Flow alert records: `6426`
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

- `market_context_high->metal_24h` score `12.9758` n `182` status `ready` deltaP `25.9004` edge `1.0087` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1858` n `182` status `ready` deltaP `26.9974` edge `0.9538` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.6741` n `182` status `ready` deltaP `26.7399` edge `0.7411` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0164` n `182` status `ready` deltaP `20.7799` edge `0.3048` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.4405` n `182` status `ready` deltaP `16.4988` edge `0.4094` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.673` n `199` status `ready` deltaP `6.9203` edge `0.1194` maxDD `-5.0894`
- `market_context_high->fx_24h` score `0.348` n `182` status `ready` deltaP `13.2307` edge `0.0457` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.1568` n `199` status `ready` deltaP `13.2545` edge `0.2637` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.0127` n `199` status `ready` deltaP `9.2796` edge `0.2074` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.348` n `199` status `ready` deltaP `0.668` edge `0.0533` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6335` n `199` status `ready` deltaP `-2.1439` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->equity_1h` score `-0.6654` n `199` status `ready` deltaP `0.0151` edge `0.0253` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6961` n `199` status `ready` deltaP `0.4747` edge `0.002` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.7017` n `199` status `ready` deltaP `0.1016` edge `0.0015` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7251` n `199` status `ready` deltaP `5.2975` edge `0.0053` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-0.9051` n `199` status `ready` deltaP `-0.7432` edge `0.0246` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.2678` n `199` status `ready` deltaP `-3.068` edge `0.0237` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3222` n `199` status `ready` deltaP `10.516` edge `0.0889` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3783` n `199` status `ready` deltaP `-10.3973` edge `-0.0145` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.0533` n `199` status `ready` deltaP `-13.3281` edge `-0.0963` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
