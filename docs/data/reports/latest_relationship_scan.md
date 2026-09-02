# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T08:37:34.814916+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11475`

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

- `risk_on_high->unknown_4h` score `7.4311` n `107` status `ready` deltaP `18.8483` edge `0.5554` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4311` n `107` status `ready` deltaP `18.8483` edge `0.5554` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.4656` n `148` status `ready` deltaP `14.7248` edge `0.4268` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `3.5422` n `107` status `ready` deltaP `21.2714` edge `0.5698` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `3.5422` n `107` status `ready` deltaP `21.2714` edge `0.5698` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.8384` n `107` status `ready` deltaP `3.2221` edge `0.1894` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.8384` n `107` status `ready` deltaP `3.2221` edge `0.1894` maxDD `-1.9475`
- `news_risk_high->unknown_1h` score `1.1281` n `59` status `ready` deltaP `0.6876` edge `0.1241` maxDD `-1.1072`
- `market_context_high->equity_24h` score `0.744` n `148` status `ready` deltaP `17.5394` edge `0.4617` maxDD `-24.6594`
- `news_risk_high->equity_24h` score `0.5173` n `59` status `ready` deltaP `7.221` edge `0.2432` maxDD `-15.5253`
- `market_context_high->unknown_1h` score `0.5087` n `148` status `ready` deltaP `1.8329` edge `0.0932` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2372` n `59` status `ready` deltaP `11.2495` edge `0.0041` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0932` n `107` status `ready` deltaP `7.9439` edge `0.0035` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0932` n `107` status `ready` deltaP `7.9439` edge `0.0035` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0585` n `107` status `ready` deltaP `11.3465` edge `0.0031` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0585` n `107` status `ready` deltaP `11.3465` edge `0.0031` maxDD `-1.699`
- `risk_on_high->index_4h` score `0.0585` n `107` status `ready` deltaP `19.8684` edge `0.0081` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0585` n `107` status `ready` deltaP `19.8684` edge `0.0081` maxDD `-3.6448`
- `risk_on_high->equity_1h` score `-0.1597` n `107` status `ready` deltaP `7.5676` edge `0.012` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1597` n `107` status `ready` deltaP `7.5676` edge `0.012` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
