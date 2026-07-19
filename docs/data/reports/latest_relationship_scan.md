# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T13:07:31.094800+00:00`
- Price records: `672`
- Market context records: `7252`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13743`

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

- `risk_on_high->crypto_major_4h` score `6.0949` n `34` status `ready` deltaP `27.8426` edge `0.3606` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.0949` n `34` status `ready` deltaP `27.8426` edge `0.3606` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.426` n `34` status `ready` deltaP `18.1671` edge `0.287` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.426` n `34` status `ready` deltaP `18.1671` edge `0.287` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1014` n `34` status `ready` deltaP `22.5667` edge `0.0397` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1014` n `34` status `ready` deltaP `22.5667` edge `0.0397` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.1232` n `34` status `ready` deltaP `5.8374` edge `0.139` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.1232` n `34` status `ready` deltaP `5.8374` edge `0.139` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.337` n `34` status `ready` deltaP `8.3744` edge `0.0164` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.337` n `34` status `ready` deltaP `8.3744` edge `0.0164` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2582` n `34` status `ready` deltaP `3.0648` edge `0.0311` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2582` n `34` status `ready` deltaP `3.0648` edge `0.0311` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1342` n `34` status `ready` deltaP `3.2192` edge `0.0212` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1342` n `34` status `ready` deltaP `3.2192` edge `0.0212` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2074` n `154` status `ready` deltaP `3.2468` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6136` n `154` status `ready` deltaP `-0.6571` edge `-0.0122` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.7075` n `34` status `ready` deltaP `-0.7185` edge `-0.0114` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.7075` n `34` status `ready` deltaP `-0.7185` edge `-0.0114` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.723` n `154` status `ready` deltaP `-0.6008` edge `0.0152` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.8301` n `154` status `ready` deltaP `2.1483` edge `0.0203` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
