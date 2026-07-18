# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T21:07:24.678063+00:00`
- Price records: `672`
- Market context records: `7181`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `risk_on_high->commodity_1h` score `2.0388` n `34` status `ready` deltaP `22.1293` edge `0.0374` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.0388` n `34` status `ready` deltaP `22.1293` edge `0.0374` maxDD `-0.2021`
- `risk_on_high->crypto_major_1h` score `0.4313` n `34` status `ready` deltaP `8.9732` edge `0.0245` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.4313` n `34` status `ready` deltaP `8.9732` edge `0.0245` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.4293` n `34` status `ready` deltaP `4.6935` edge `0.0345` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.4293` n `34` status `ready` deltaP `4.6935` edge `0.0345` maxDD `-0.7345`
- `market_context_high->fx_1h` score `-0.3359` n `177` status `ready` deltaP `2.9915` edge `0.001` maxDD `-0.5817`
- `market_context_high->crypto_major_1h` score `-0.4997` n `177` status `ready` deltaP `5.5169` edge `0.0402` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.5309` n `177` status `ready` deltaP `1.0986` edge `0.0285` maxDD `-5.9775`
- `market_context_high->commodity_1h` score `-0.5903` n `177` status `ready` deltaP `-0.104` edge `-0.0129` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-0.7326` n `177` status `ready` deltaP `-1.6586` edge `0.0142` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.8624` n `177` status `ready` deltaP `-0.2098` edge `-0.004` maxDD `-2.3175`
- `market_context_high->fx_4h` score `-0.9405` n `166` status `ready` deltaP `8.3915` edge `0.0085` maxDD `-1.4253`
- `risk_on_high->fx_1h` score `-1.0315` n `34` status `ready` deltaP `-8.3744` edge `-0.0023` maxDD `-0.2261`
- `risk_on_and_context->fx_1h` score `-1.0315` n `34` status `ready` deltaP `-8.3744` edge `-0.0023` maxDD `-0.2261`
- `risk_on_high->crypto_alt_1h` score `-1.5319` n `34` status `ready` deltaP `-12.7598` edge `-0.0004` maxDD `-1.3755`
- `risk_on_and_context->crypto_alt_1h` score `-1.5319` n `34` status `ready` deltaP `-12.7598` edge `-0.0004` maxDD `-1.3755`
- `risk_on_high->index_1h` score `-1.5454` n `34` status `ready` deltaP `-14.3008` edge `-0.0004` maxDD `-0.3101`
- `risk_on_and_context->index_1h` score `-1.5454` n `34` status `ready` deltaP `-14.3008` edge `-0.0004` maxDD `-0.3101`
- `market_context_high->commodity_4h` score `-1.707` n `166` status `ready` deltaP `-2.2223` edge `-0.0239` maxDD `-2.9494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
