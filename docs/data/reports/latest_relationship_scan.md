# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T02:37:27.980304+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11484`

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

- `news_risk_high->unknown_24h` score `2810.478` n `102` status `ready` deltaP `1.2153` edge `234.1984` maxDD `0.0`
- `market_context_high->unknown_1h` score `75.1083` n `44` status `ready` deltaP `10.1524` edge `6.196` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.4841` n `44` status `ready` deltaP `28.2829` edge `4.1369` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.8058` n `44` status `ready` deltaP `14.9148` edge `2.2557` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.7492` n `44` status `ready` deltaP `36.0954` edge `2.1032` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.727` n `44` status `ready` deltaP `32.1023` edge `0.4387` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.7285` n `44` status `ready` deltaP `32.481` edge `0.118` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.358` n `44` status `ready` deltaP `37.6801` edge `0.0357` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.9627` n `44` status `ready` deltaP `17.9739` edge `0.1647` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.2534` n `44` status `ready` deltaP `9.0078` edge `0.107` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.1151` n `102` status `ready` deltaP `16.7279` edge `0.0426` maxDD `-2.2287`
- `market_context_high->equity_1h` score `1.0515` n `44` status `ready` deltaP `11.8672` edge `0.0488` maxDD `-1.5564`
- `market_context_high->crypto_major_1h` score `1.0376` n `44` status `ready` deltaP `8.669` edge `0.1021` maxDD `-4.5405`
- `news_risk_high->metal_24h` score `0.987` n `102` status `ready` deltaP `23.8358` edge `0.1324` maxDD `-6.8481`
- `market_context_high->crypto_major_4h` score `0.8996` n `44` status `ready` deltaP `7.0676` edge `0.1183` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.7996` n `44` status `ready` deltaP `12.1666` edge `0.0092` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2336` n `44` status `ready` deltaP `6.0152` edge `0.011` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1469` n `44` status `ready` deltaP `7.2128` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `-0.0101` n `44` status `ready` deltaP `3.8514` edge `0.0624` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.1534` n `140` status `ready` deltaP `1.9718` edge `0.0032` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
