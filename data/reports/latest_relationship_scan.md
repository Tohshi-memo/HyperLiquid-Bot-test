# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T21:22:19.360482+00:00`
- Price records: `672`
- Market context records: `1155`
- Flow alert records: `5229`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `20.2822` n `147` status `ready` deltaP `44.5011` edge `1.5067` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.8873` n `147` status `ready` deltaP `20.8759` edge `0.8864` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.8167` n `147` status `ready` deltaP `20.355` edge `0.6087` maxDD `-6.4404`
- `market_context_high->index_24h` score `6.1279` n `147` status `ready` deltaP `18.9661` edge `0.44` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.6315` n `147` status `ready` deltaP `-2.3243` edge `0.6515` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4914` n `163` status `ready` deltaP `12.2765` edge `0.1921` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1818` n `163` status `ready` deltaP `9.3577` edge `0.1044` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5123` n `163` status `ready` deltaP `7.7219` edge `0.0229` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3814` n `163` status `ready` deltaP `3.4422` edge `0.0466` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.2259` n `163` status `ready` deltaP `8.892` edge `0.1618` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.1455` n `163` status `ready` deltaP `8.5348` edge `0.0008` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0815` n `163` status `ready` deltaP `7.5484` edge `0.0367` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.2519` n `163` status `ready` deltaP `3.0427` edge `0.043` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.2978` n `163` status `ready` deltaP `6.4831` edge `-0.007` maxDD `-2.2164`
- `market_context_high->fx_4h` score `-0.8969` n `163` status `ready` deltaP `-1.9574` edge `-0.0023` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-0.9705` n `163` status `ready` deltaP `6.0405` edge `0.1318` maxDD `-16.7194`
- `market_context_high->commodity_1h` score `-1.2226` n `163` status `ready` deltaP `-2.6257` edge `-0.0036` maxDD `-3.7959`
- `market_context_high->unknown_24h` score `-1.6834` n `147` status `ready` deltaP `4.0923` edge `0.1054` maxDD `-10.1706`
- `market_context_high->unknown_4h` score `-2.4128` n `163` status `ready` deltaP `7.9923` edge `-0.1327` maxDD `-6.7322`
- `market_context_high->metal_4h` score `-2.5172` n `163` status `ready` deltaP `6.6653` edge `-0.0588` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
