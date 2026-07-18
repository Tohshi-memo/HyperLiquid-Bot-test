# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T21:52:30.364907+00:00`
- Price records: `672`
- Market context records: `7185`
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

- `risk_on_high->crypto_major_4h` score `6.3135` n `31` status `ready` deltaP `27.3947` edge `0.3818` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.3135` n `31` status `ready` deltaP `27.3947` edge `0.3818` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.4796` n `31` status `ready` deltaP `15.6865` edge `0.308` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.4796` n `31` status `ready` deltaP `15.6865` edge `0.308` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.04` n `34` status `ready` deltaP `22.1293` edge `0.0375` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.04` n `34` status `ready` deltaP `22.1293` edge `0.0375` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.5174` n `31` status `ready` deltaP `9.82` edge `0.1453` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.5174` n `31` status `ready` deltaP `9.82` edge `0.1453` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.4399` n `34` status `ready` deltaP `9.1229` edge `0.0246` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.4399` n `34` status `ready` deltaP `9.1229` edge `0.0246` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.403` n `34` status `ready` deltaP `4.3941` edge `0.0343` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.403` n `34` status `ready` deltaP `4.3941` edge `0.0343` maxDD `-0.7345`
- `market_context_high->fx_1h` score `-0.3266` n `178` status `ready` deltaP `3.1084` edge `0.001` maxDD `-0.5817`
- `market_context_high->crypto_major_1h` score `-0.4766` n `178` status `ready` deltaP `5.9174` edge `0.0405` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.5441` n `178` status `ready` deltaP `0.9352` edge `0.0279` maxDD `-5.9775`
- `market_context_high->commodity_1h` score `-0.6093` n `178` status `ready` deltaP `-0.4087` edge `-0.0133` maxDD `-1.9668`
- `risk_on_high->unknown_4h` score `-0.7499` n `31` status `ready` deltaP `-1.4063` edge `-0.0269` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.7499` n `31` status `ready` deltaP `-1.4063` edge `-0.0269` maxDD `-1.4561`
- `market_context_high->unknown_1h` score `-0.7559` n `178` status `ready` deltaP `-1.7998` edge `0.0132` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.87` n `178` status `ready` deltaP `-0.3045` edge `-0.004` maxDD `-2.3175`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
