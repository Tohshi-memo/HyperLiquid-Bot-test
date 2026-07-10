# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T15:07:26.565669+00:00`
- Price records: `672`
- Market context records: `6294`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11116`

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

- `news_risk_high->crypto_alt_24h` score `15.231` n `32` status `ready` deltaP `43.2292` edge `0.9958` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9701` n `32` status `ready` deltaP `50.5208` edge `0.1607` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1901` n `32` status `ready` deltaP `43.8262` edge `0.0616` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1282` n `32` status `ready` deltaP `16.6667` edge `0.4961` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.9727` n `32` status `ready` deltaP `27.4306` edge `0.0854` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3871` n `32` status `ready` deltaP `28.7425` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4312` n `32` status `ready` deltaP `14.2777` edge `0.135` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.2388` n `208` status `ready` deltaP `-0.8176` edge `0.2095` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.9244` n `32` status `ready` deltaP `11.7702` edge `0.0862` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.0699` n `196` status `ready` deltaP `6.9562` edge `0.0632` maxDD `-3.633`
- `market_context_high->unknown_4h` score `-0.0813` n `196` status `ready` deltaP `-4.7318` edge `0.278` maxDD `-11.925`
- `market_context_high->metal_4h` score `-0.1337` n `196` status `ready` deltaP `7.5722` edge `0.0347` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1594` n `177` status `ready` deltaP `20.3566` edge `0.1007` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.3407` n `32` status `ready` deltaP `6.5972` edge `-0.0005` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.431` n `208` status `ready` deltaP `3.256` edge `0.0008` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5` n `208` status `ready` deltaP `-0.0864` edge `-0.0003` maxDD `-1.7253`
- `market_context_high->fx_1h` score `-0.6806` n `208` status `ready` deltaP `-0.5844` edge `-0.0018` maxDD `-0.748`
- `news_risk_high->metal_1h` score `-0.7348` n `32` status `ready` deltaP `-2.994` edge `-0.0245` maxDD `-1.6464`
- `market_context_high->commodity_4h` score `-0.9681` n `196` status `ready` deltaP `-3.7705` edge `0.0014` maxDD `-2.0306`
- `market_context_high->crypto_alt_1h` score `-0.9755` n `208` status `ready` deltaP `4.799` edge `0.0182` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
