# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T07:37:30.700127+00:00`
- Price records: `672`
- Market context records: `4806`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7578`

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

- `market_context_high->unknown_1h` score `11.4375` n `118` status `ready` deltaP `11.4128` edge `0.9188` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.8486` n `117` status `ready` deltaP `18.1038` edge `0.6544` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.2257` n `111` status `ready` deltaP `12.6314` edge `0.1936` maxDD `-4.7201`
- `market_context_high->equity_4h` score `0.3298` n `117` status `ready` deltaP `9.949` edge `0.1213` maxDD `-6.9604`
- `market_context_high->commodity_4h` score `0.1134` n `117` status `ready` deltaP `12.3229` edge `0.0496` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0946` n `118` status `ready` deltaP `5.5871` edge `0.0294` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.2786` n `117` status `ready` deltaP `7.9021` edge `0.0169` maxDD `-5.4242`
- `market_context_high->fx_4h` score `-0.3084` n `117` status `ready` deltaP `5.1582` edge `0.0037` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6763` n `118` status `ready` deltaP `2.2937` edge `0.0051` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.9587` n `118` status `ready` deltaP `-1.7913` edge `-0.003` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.398` n `118` status `ready` deltaP `-1.3473` edge `-0.0071` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1275` n `111` status `ready` deltaP `19.909` edge `0.1054` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3016` n `118` status `ready` deltaP `-1.1418` edge `-0.0699` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-2.7088` n `111` status `ready` deltaP `-11.51` edge `-0.018` maxDD `-3.1464`
- `market_context_high->crypto_major_1h` score `-3.0293` n `118` status `ready` deltaP `0.0533` edge `-0.0797` maxDD `-22.0555`
- `market_context_high->crypto_alt_1h` score `-3.1529` n `118` status `ready` deltaP `1.0479` edge `-0.0493` maxDD `-14.9676`
- `market_context_high->index_24h` score `-4.3767` n `111` status `ready` deltaP `-7.0899` edge `-0.123` maxDD `-23.2678`
- `market_context_high->crypto_alt_4h` score `-4.4061` n `117` status `ready` deltaP `6.9875` edge `-0.0036` maxDD `-43.2966`
- `market_context_high->crypto_major_4h` score `-8.2072` n `117` status `ready` deltaP `4.0859` edge `-0.1639` maxDD `-67.9107`
- `market_context_high->metal_4h` score `-8.5664` n `117` status `ready` deltaP `5.2076` edge `-0.3089` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
