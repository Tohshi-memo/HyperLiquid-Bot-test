# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T20:52:25.705406+00:00`
- Price records: `672`
- Market context records: `4245`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10368`

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

- `risk_on_high->unknown_4h` score `130.6872` n `44` status `ready` deltaP `-3.7279` edge `11.0973` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.6872` n `44` status `ready` deltaP `-3.7279` edge `11.0973` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `29.1932` n `219` status `ready` deltaP `0.873` edge `2.5849` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `7.4511` n `219` status `ready` deltaP `-2.5344` edge `1.1808` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `6.4547` n `200` status `ready` deltaP `-11.1667` edge `1.0157` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.7901` n `44` status `ready` deltaP `31.8736` edge `-0.0586` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.7901` n `44` status `ready` deltaP `31.8736` edge `-0.0586` maxDD `-0.044`
- `risk_on_high->commodity_24h` score `1.0672` n `40` status `ready` deltaP `0.8681` edge `0.3113` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0672` n `40` status `ready` deltaP `0.8681` edge `0.3113` maxDD `-12.9187`
- `risk_on_high->crypto_major_4h` score `0.4848` n `44` status `ready` deltaP `13.7334` edge `0.0154` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.4848` n `44` status `ready` deltaP `13.7334` edge `0.0154` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.2805` n `44` status `ready` deltaP `6.546` edge `0.0027` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2805` n `44` status `ready` deltaP `6.546` edge `0.0027` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0009` n `44` status `ready` deltaP `7.0496` edge `0.0071` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0009` n `44` status `ready` deltaP `7.0496` edge `0.0071` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `-0.006` n `44` status `ready` deltaP `8.1763` edge `0.0038` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.006` n `44` status `ready` deltaP `8.1763` edge `0.0038` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.1677` n `44` status `ready` deltaP `6.7774` edge `-0.0202` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.1677` n `44` status `ready` deltaP `6.7774` edge `-0.0202` maxDD `-0.7834`
- `market_context_high->fx_1h` score `-0.4248` n `219` status `ready` deltaP `0.4231` edge `-0.0014` maxDD `-1.1377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
