# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T14:22:35.974382+00:00`
- Price records: `672`
- Market context records: `7257`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13759`

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

- `risk_on_high->crypto_major_4h` score `6.1687` n `34` status `ready` deltaP `28.2999` edge `0.3637` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.1687` n `34` status `ready` deltaP `28.2999` edge `0.3637` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.499` n `34` status `ready` deltaP `18.9293` edge `0.288` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.499` n `34` status `ready` deltaP `18.9293` edge `0.288` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1531` n `34` status `ready` deltaP `23.1673` edge `0.04` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1531` n `34` status `ready` deltaP `23.1673` edge `0.04` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.111` n `34` status `ready` deltaP `5.6848` edge `0.139` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.111` n `34` status `ready` deltaP `5.6848` edge `0.139` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.3245` n `34` status `ready` deltaP `8.2247` edge `0.0158` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3245` n `34` status `ready` deltaP `8.2247` edge `0.0158` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2414` n `34` status `ready` deltaP `2.9147` edge `0.0307` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2414` n `34` status `ready` deltaP `2.9147` edge `0.0307` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1698` n `34` status `ready` deltaP `2.6094` edge `0.0207` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1698` n `34` status `ready` deltaP `2.6094` edge `0.0207` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.282` n `149` status `ready` deltaP `1.8281` edge `0.0006` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6322` n `149` status `ready` deltaP `-0.9543` edge `-0.0126` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.6478` n `34` status `ready` deltaP `-0.1078` edge `-0.0105` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6478` n `34` status `ready` deltaP `-0.1078` edge `-0.0105` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.6787` n `149` status `ready` deltaP `-0.1085` edge `0.0176` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.812` n `149` status `ready` deltaP `2.4213` edge `0.0208` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
