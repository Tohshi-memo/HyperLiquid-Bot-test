# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T20:22:32.887341+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_4h` score `45.6678` n `46` status `ready` deltaP `7.0122` edge `3.7589` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.4971` n `46` status `ready` deltaP `12.8397` edge `2.3881` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2157` n `46` status `ready` deltaP `12.1453` edge `1.2804` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.894` n `46` status `ready` deltaP `11.2847` edge `1.0826` maxDD `0.0`
- `market_context_high->index_24h` score `5.5203` n `46` status `ready` deltaP `19.6105` edge `0.338` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.2233` n `96` status `ready` deltaP `38.8889` edge `0.2939` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.8036` n `96` status `ready` deltaP `-9.8958` edge `1.1521` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `2.9571` n `96` status `ready` deltaP `14.6341` edge `0.2066` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.8825` n `96` status `ready` deltaP `11.2805` edge `0.2648` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.2114` n `96` status `ready` deltaP `12.4314` edge `0.1368` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8608` n `46` status `ready` deltaP `22.2494` edge `0.0201` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.559` n `96` status `ready` deltaP `13.9284` edge `0.0764` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.21` n `96` status `ready` deltaP `18.7246` edge `0.0396` maxDD `-0.421`
- `news_risk_high->crypto_alt_24h` score `1.003` n `96` status `ready` deltaP `-8.507` edge `0.6284` maxDD `-32.7147`
- `market_context_high->metal_24h` score `0.9647` n `46` status `ready` deltaP `21.7467` edge `-0.0412` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.7118` n `46` status `ready` deltaP `6.4632` edge `0.0405` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6303` n `46` status `ready` deltaP `10.2057` edge `0.0098` maxDD `-0.0249`
- `news_risk_high->fx_24h` score `0.5953` n `96` status `ready` deltaP `20.4861` edge `0.0987` maxDD `-1.7159`
- `news_risk_high->metal_1h` score `0.5933` n `96` status `ready` deltaP `14.7268` edge `0.0106` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.458` n `96` status `ready` deltaP `18.5764` edge `0.0193` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
