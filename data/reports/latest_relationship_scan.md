# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T21:07:27.095783+00:00`
- Price records: `672`
- Market context records: `7068`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.7066` n `182` status `ready` deltaP `17.5473` edge `0.0119` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1478` n `182` status `ready` deltaP `4.5453` edge `0.0025` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2577` n `182` status `ready` deltaP `0.148` edge `0.0334` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.2915` n `182` status `ready` deltaP `2.0498` edge `0.0354` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5592` n `182` status `ready` deltaP `4.2969` edge `0.0349` maxDD `-7.1523`
- `market_context_high->unknown_4h` score `-0.7835` n `182` status `ready` deltaP `-5.0473` edge `0.1318` maxDD `-4.742`
- `market_context_high->index_1h` score `-0.8072` n `182` status `ready` deltaP `-1.2552` edge `-0.004` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8795` n `182` status `ready` deltaP `-4.7427` edge `-0.0195` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.32` n `182` status `ready` deltaP `-4.5026` edge `-0.0032` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.6261` n `182` status `ready` deltaP `-7.0406` edge `-0.0455` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8451` n `182` status `ready` deltaP `4.9401` edge `-0.0272` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2922` n `182` status `ready` deltaP `1.5495` edge `-0.0343` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4239` n `182` status `ready` deltaP `-2.2665` edge `-0.056` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.9454` n `182` status `ready` deltaP `0.3937` edge `-0.0017` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0846` n `182` status `ready` deltaP `2.5027` edge `0.0163` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.5773` n `182` status `ready` deltaP `-0.4349` edge `-0.0125` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.665` n `182` status `ready` deltaP `-0.449` edge `-0.0041` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-4.1887` n `182` status `ready` deltaP `-16.1305` edge `0.0852` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9121` n `182` status `ready` deltaP `4.3889` edge `-0.1566` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.6615` n `182` status `ready` deltaP `-21.8502` edge `-0.1001` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
