# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T07:37:30.040154+00:00`
- Price records: `672`
- Market context records: `6897`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11702`

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

- `market_context_high->unknown_24h` score `0.5133` n `185` status `ready` deltaP `-4.4752` edge `0.483` maxDD `-13.3224`
- `market_context_high->fx_1h` score `-0.2214` n `224` status `ready` deltaP `2.6866` edge `0.0022` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5074` n `224` status `ready` deltaP `2.5102` edge `0.0174` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.5769` n `224` status `ready` deltaP `-0.2994` edge `-0.0035` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.5934` n `224` status `ready` deltaP `3.9965` edge `0.0143` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.7946` n `224` status `ready` deltaP `-1.1789` edge `-0.0029` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8263` n `224` status `ready` deltaP `13.8502` edge `0.0081` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8721` n `224` status `ready` deltaP `-4.1435` edge `-0.0074` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.324` n `224` status `ready` deltaP `-1.8838` edge `-0.0082` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7344` n `224` status `ready` deltaP `-4.0098` edge `-0.0277` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8066` n `224` status `ready` deltaP `1.7857` edge `-0.0255` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9851` n `224` status `ready` deltaP `3.9417` edge `-0.0228` maxDD `-11.3047`
- `market_context_high->commodity_24h` score `-2.002` n `185` status `ready` deltaP `1.1981` edge `0.012` maxDD `-5.2791`
- `market_context_high->metal_4h` score `-2.2787` n `224` status `ready` deltaP `1.557` edge `-0.0042` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.9197` n `224` status `ready` deltaP `1.1433` edge `-0.0236` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.9889` n `224` status `ready` deltaP `-1.0018` edge `-0.0438` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0861` n `224` status `ready` deltaP `-8.7326` edge `0.0376` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.265` n `185` status `ready` deltaP `-6.7029` edge `-0.0071` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3301` n `224` status `ready` deltaP `1.3393` edge `-0.1542` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.4751` n `185` status `ready` deltaP `-14.1881` edge `-0.1334` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
