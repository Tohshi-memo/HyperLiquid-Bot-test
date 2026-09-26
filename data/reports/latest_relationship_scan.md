# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T08:07:25.910118+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11858`

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

- `news_risk_high->unknown_24h` score `3289.8988` n `102` status `ready` deltaP `-0.6332` edge `274.1669` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.8769` n `47` status `ready` deltaP `8.7687` edge `5.7717` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.9446` n `47` status `ready` deltaP `23.3045` edge `3.8793` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.2001` n `47` status `ready` deltaP `21.4834` edge `2.3281` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3947` n `47` status `ready` deltaP `33.3739` edge `1.9293` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.1675` n `47` status `ready` deltaP `30.2489` edge `0.4086` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.3975` n `47` status `ready` deltaP `28.8084` edge `0.1149` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7265` n `47` status `ready` deltaP `17.2969` edge `0.1537` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5432` n `47` status `ready` deltaP `29.3007` edge `0.032` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4077` n `47` status `ready` deltaP `11.5172` edge `0.1073` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.2059` n `102` status `ready` deltaP `27.8697` edge `0.1349` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0637` n `47` status `ready` deltaP `12.2149` edge `0.0475` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7942` n `47` status `ready` deltaP `12.664` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.5956` n `47` status `ready` deltaP `5.757` edge `0.1017` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.5081` n `47` status `ready` deltaP `10.5586` edge `0.0076` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.359` n `47` status `ready` deltaP `5.351` edge `0.076` maxDD `-4.5405`
- `news_risk_high->index_24h` score `0.3086` n `102` status `ready` deltaP `13.1025` edge `0.0385` maxDD `-2.344`
- `news_risk_high->crypto_alt_1h` score `0.1138` n `137` status `ready` deltaP `6.1869` edge `0.0593` maxDD `-4.2849`
- `market_context_high->fx_4h` score `0.0493` n `47` status `ready` deltaP `9.4739` edge `0.0077` maxDD `-0.6736`
- `news_risk_high->index_1h` score `0.0431` n `137` status `ready` deltaP `4.3708` edge `0.0037` maxDD `-0.3395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
