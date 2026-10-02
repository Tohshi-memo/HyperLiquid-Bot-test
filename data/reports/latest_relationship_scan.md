# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T20:52:28.248396+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4876`

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

- `market_context_high->unknown_1h` score `364.7579` n `50` status `ready` deltaP `10.4251` edge `30.3319` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.8111` n `50` status `ready` deltaP `10.2134` edge `24.2495` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.4073` n `73` status `ready` deltaP `41.5311` edge `1.1113` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.082` n `50` status `ready` deltaP `18.2708` edge `0.8887` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0354` n `50` status `ready` deltaP `31.8264` edge `0.6824` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.6964` n `73` status `ready` deltaP `31.0169` edge `0.5664` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.6735` n `50` status `ready` deltaP `18.9146` edge `0.5837` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.0349` n `50` status `ready` deltaP `17.1037` edge `0.5178` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `5.8559` n `116` status `ready` deltaP `22.9658` edge `0.4693` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3009` n `50` status `ready` deltaP `15.1018` edge `0.2407` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1032` n `50` status `ready` deltaP `14.2994` edge `0.2083` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7263` n `50` status `ready` deltaP `30.4024` edge `0.038` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.5229` n `116` status `ready` deltaP `22.2508` edge `0.1315` maxDD `-2.9013`
- `news_risk_high->crypto_major_4h` score `1.5572` n `116` status `ready` deltaP `15.5698` edge `0.3268` maxDD `-10.477`
- `news_risk_high->crypto_major_24h` score `1.5378` n `73` status `ready` deltaP `5.9908` edge `0.4726` maxDD `-15.8971`
- `market_context_high->equity_24h` score `1.4792` n `50` status `ready` deltaP `7.2361` edge `0.3276` maxDD `-11.8957`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.366` n `73` status `ready` deltaP `13.009` edge `0.2158` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.1535` n `116` status `ready` deltaP `5.9984` edge `0.1122` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.8911` n `50` status `ready` deltaP `18.7708` edge `0.0909` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
