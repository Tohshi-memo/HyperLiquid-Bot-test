# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T11:22:27.883477+00:00`
- Price records: `672`
- Market context records: `7979`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11790`

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

- `market_context_high->equity_24h` score `16.1277` n `83` status `ready` deltaP `24.1884` edge `1.3169` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0504` n `83` status `ready` deltaP `35.8752` edge `0.4317` maxDD `0.0`
- `market_context_high->equity_4h` score `6.5254` n `96` status `ready` deltaP `25.5248` edge `0.4629` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.7092` n `83` status `ready` deltaP `27.4452` edge `0.2794` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.6743` n `96` status `ready` deltaP `27.8323` edge `0.0733` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5513` n `96` status `ready` deltaP `22.9421` edge `0.1219` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6836` n `103` status `ready` deltaP `14.288` edge `0.1268` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.1475` n `83` status `ready` deltaP `9.2307` edge `0.1526` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.101` n `83` status `ready` deltaP `24.7971` edge `0.0352` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.0687` n `96` status `ready` deltaP `9.1463` edge `0.1398` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.9868` n `103` status `ready` deltaP `15.6374` edge `0.021` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.855` n `96` status `ready` deltaP `9.9085` edge `0.177` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.7237` n `103` status `ready` deltaP `10.4165` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5887` n `103` status `ready` deltaP `11.3874` edge `0.0406` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0764` n `103` status `ready` deltaP `0.1134` edge `0.0327` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2755` n `103` status `ready` deltaP `0.0466` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.6239` n `96` status `ready` deltaP `2.861` edge `0.0037` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.7749` n `103` status `ready` deltaP `0.1819` edge `-0.004` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.9543` n `96` status `ready` deltaP `2.2312` edge `0.0088` maxDD `-3.589`
- `market_context_high->unknown_1h` score `-1.9829` n `103` status `ready` deltaP `6.315` edge `-0.165` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
