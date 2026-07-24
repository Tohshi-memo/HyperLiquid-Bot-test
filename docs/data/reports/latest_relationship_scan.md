# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T18:07:37.730910+00:00`
- Price records: `672`
- Market context records: `7798`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `8.031` n `132` status `ready` deltaP `28.5507` edge `0.6131` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4409` n `133` status `ready` deltaP `13.5378` edge `0.2389` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.2362` n `133` status `ready` deltaP `15.033` edge `0.1746` maxDD `-6.7444`
- `market_context_high->equity_4h` score `1.1701` n `133` status `ready` deltaP `4.036` edge `0.3144` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.1053` n `133` status `ready` deltaP `13.4573` edge `0.0465` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8914` n `133` status `ready` deltaP `8.5796` edge `0.1288` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8148` n `132` status `ready` deltaP `25.2187` edge `0.0451` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7946` n `133` status `ready` deltaP `8.3463` edge `0.0965` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4624` n `133` status `ready` deltaP `8.3981` edge `0.0419` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3902` n `133` status `ready` deltaP `8.7946` edge `0.0169` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2611` n `133` status `ready` deltaP `4.8771` edge `0.0325` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0641` n `133` status `ready` deltaP `5.647` edge `0.0136` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1377` n `133` status `ready` deltaP `11.8602` edge `0.0491` maxDD `-1.3325`
- `market_context_high->commodity_24h` score `-0.1726` n `132` status `ready` deltaP `12.7747` edge `0.0588` maxDD `-7.0012`
- `market_context_high->fx_1h` score `-0.2957` n `133` status `ready` deltaP `2.0254` edge `0.0006` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.871` n `133` status `ready` deltaP `1.2674` edge `0.0193` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.331` n `133` status `ready` deltaP `-1.5014` edge `0.0022` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5997` n `133` status `ready` deltaP `-0.1568` edge `0.0732` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.6443` n `132` status `ready` deltaP `-9.4875` edge `0.0627` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.3107` n `133` status `ready` deltaP `14.7431` edge `0.135` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
