# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T12:33:07.744621+00:00`
- Price records: `672`
- Market context records: `1526`
- Flow alert records: `6306`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `13.6158` n `167` status `ready` deltaP `23.4905` edge `1.0781` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.6022` n `167` status `ready` deltaP `28.9328` edge `0.9756` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.4892` n `167` status `ready` deltaP `28.2737` edge `0.7988` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8183` n `167` status `ready` deltaP `20.089` edge `0.2929` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5694` n `167` status `ready` deltaP `13.3359` edge `0.3579` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.9247` n `167` status `ready` deltaP `18.5192` edge `0.0585` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1924` n `192` status `ready` deltaP `3.7348` edge `0.0956` maxDD `-5.0239`
- `market_context_high->fx_1h` score `-0.5743` n `199` status `ready` deltaP `-1.096` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6216` n `199` status `ready` deltaP `-0.5296` edge `0.0262` maxDD `-4.1892`
- `market_context_high->commodity_1h` score `-0.7359` n `199` status `ready` deltaP `-0.3475` edge `0.0001` maxDD `-4.7041`
- `market_context_high->crypto_alt_4h` score `-0.7476` n `192` status `ready` deltaP `10.0356` edge `0.1692` maxDD `-19.5565`
- `market_context_high->index_1h` score `-0.7548` n `199` status `ready` deltaP `-0.1241` edge `0.0011` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.761` n `199` status `ready` deltaP `4.9981` edge `0.0027` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-0.7753` n `192` status `ready` deltaP `5.564` edge `0.1344` maxDD `-13.3376`
- `market_context_high->equity_1h` score `-0.9039` n `199` status `ready` deltaP `-1.7813` edge `0.0174` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.1249` n `199` status `ready` deltaP `-2.0905` edge `0.0054` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.3317` n `192` status `ready` deltaP `10.1118` edge `0.0908` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.5058` n `192` status `ready` deltaP `-5.653` edge `0.0211` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.8606` n `192` status `ready` deltaP `-7.5838` edge `-0.0116` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-4.0882` n `167` status `ready` deltaP `-1.0676` edge `-0.0606` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
