# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T15:07:26.078303+00:00`
- Price records: `672`
- Market context records: `7261`
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

- `risk_on_high->crypto_major_4h` score `6.1953` n `34` status `ready` deltaP `28.4523` edge `0.3649` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.1953` n `34` status `ready` deltaP `28.4523` edge `0.3649` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.544` n `34` status `ready` deltaP `19.3867` edge `0.2887` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.544` n `34` status `ready` deltaP `19.3867` edge `0.2887` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1254` n `34` status `ready` deltaP `22.867` edge `0.0397` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1254` n `34` status `ready` deltaP `22.867` edge `0.0397` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.1095` n `34` status `ready` deltaP `5.6215` edge `0.1393` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.1095` n `34` status `ready` deltaP `5.6215` edge `0.1393` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.3331` n `34` status `ready` deltaP `8.2247` edge `0.0169` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3331` n `34` status `ready` deltaP `8.2247` edge `0.0169` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.281` n `34` status `ready` deltaP `3.3651` edge `0.031` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.281` n `34` status `ready` deltaP `3.3651` edge `0.031` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1714` n `34` status `ready` deltaP `2.6094` edge `0.0205` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1714` n `34` status `ready` deltaP `2.6094` edge `0.0205` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2546` n `146` status `ready` deltaP `2.3551` edge `0.0006` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5879` n `146` status `ready` deltaP `-0.1789` edge `-0.0121` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.6368` n `34` status `ready` deltaP `-0.045` edge `-0.01` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6368` n `34` status `ready` deltaP `-0.045` edge `-0.01` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.7745` n `146` status `ready` deltaP `-1.1566` edge `0.0123` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.9153` n `146` status `ready` deltaP `1.456` edge `0.014` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
