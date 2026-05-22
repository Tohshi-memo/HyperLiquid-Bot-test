# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T21:37:13.397774+00:00`
- Price records: `672`
- Market context records: `1566`
- Flow alert records: `6420`
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

- `market_context_high->metal_24h` score `12.8821` n `182` status `ready` deltaP `25.5532` edge `1.0032` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.133` n `182` status `ready` deltaP `26.9974` edge `0.9494` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.6237` n `182` status `ready` deltaP `26.7399` edge `0.7369` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0188` n `182` status `ready` deltaP `20.7799` edge `0.305` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.3239` n `182` status `ready` deltaP `16.1516` edge `0.402` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.6138` n `199` status `ready` deltaP `6.6154` edge `0.1165` maxDD `-5.0894`
- `market_context_high->fx_24h` score `0.3842` n `182` status `ready` deltaP `13.5779` edge `0.0464` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.1381` n `199` status `ready` deltaP `13.2545` edge `0.2613` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.0322` n `199` status `ready` deltaP `9.2796` edge `0.2049` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.3176` n `199` status `ready` deltaP `0.9674` edge `0.0552` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6335` n `199` status `ready` deltaP `-2.1439` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->equity_1h` score `-0.6918` n `199` status `ready` deltaP `-0.2843` edge `0.0251` maxDD `-2.8014`
- `market_context_high->commodity_1h` score `-0.6993` n `199` status `ready` deltaP `0.1016` edge `0.0018` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7166` n `199` status `ready` deltaP `5.4472` edge `0.0054` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7225` n `199` status `ready` deltaP `0.1753` edge `0.0018` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.8786` n `199` status `ready` deltaP `-0.4438` edge `0.026` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.309` n `199` status `ready` deltaP `-3.3728` edge `0.0223` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3306` n `199` status `ready` deltaP `10.516` edge `0.0882` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3775` n `199` status `ready` deltaP `-10.3973` edge `-0.0144` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.0416` n `199` status `ready` deltaP `-13.3281` edge `-0.0948` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
