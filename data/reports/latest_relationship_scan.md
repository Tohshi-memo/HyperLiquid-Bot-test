# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T15:07:22.993431+00:00`
- Price records: `672`
- Market context records: `1537`
- Flow alert records: `6338`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8803`

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

- `market_context_high->metal_24h` score `12.7151` n `177` status `ready` deltaP `22.9108` edge `1.0069` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.6714` n `177` status `ready` deltaP `28.687` edge `0.983` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.9308` n `177` status `ready` deltaP `28.1191` edge `0.7533` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0734` n `177` status `ready` deltaP `20.5626` edge `0.311` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7472` n `177` status `ready` deltaP `13.8772` edge `0.3691` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.7964` n `177` status `ready` deltaP `17.5612` edge `0.0542` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1665` n `199` status `ready` deltaP `4.0239` edge `0.0965` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.4929` n `199` status `ready` deltaP `11.4253` edge `0.1926` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.5515` n `199` status `ready` deltaP `-0.2302` edge `0.0332` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-0.5586` n `199` status `ready` deltaP `7.4503` edge `0.1496` maxDD `-13.3376`
- `market_context_high->fx_1h` score `-0.5829` n `199` status `ready` deltaP `-1.2457` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7345` n `199` status `ready` deltaP `0.1753` edge `0.0008` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7516` n `199` status `ready` deltaP `4.8484` edge `0.0049` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7601` n `199` status `ready` deltaP `-0.6469` edge `-0.001` maxDD `-4.7041`
- `market_context_high->equity_1h` score `-0.8715` n `199` status `ready` deltaP `-1.6316` edge `0.0191` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.079` n `199` status `ready` deltaP `-1.7911` edge `0.0093` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.285` n `199` status `ready` deltaP `-8.8729` edge `-0.0127` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.3946` n `199` status `ready` deltaP `-4.5923` edge `0.0233` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.5171` n `199` status `ready` deltaP `9.1441` edge `0.0818` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.3317` n `199` status `ready` deltaP `-16.072` edge `-0.1137` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
