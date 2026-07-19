# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T03:52:26.655014+00:00`
- Price records: `672`
- Market context records: `7211`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `12810`

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

- `risk_on_high->crypto_major_4h` score `5.9213` n `34` status `ready` deltaP `27.2328` edge `0.3502` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.9213` n `34` status `ready` deltaP `27.2328` edge `0.3502` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.3968` n `34` status `ready` deltaP `17.8623` edge `0.2866` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.3968` n `34` status `ready` deltaP `17.8623` edge `0.2866` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.0772` n `34` status `ready` deltaP `22.279` edge `0.0396` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.0772` n `34` status `ready` deltaP `22.279` edge `0.0396` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.253` n `34` status `ready` deltaP `6.8149` edge `0.1433` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.253` n `34` status `ready` deltaP `6.8149` edge `0.1433` maxDD `-2.412`
- `risk_on_high->equity_1h` score `0.3286` n `34` status `ready` deltaP `3.7953` edge `0.0321` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3286` n `34` status `ready` deltaP `3.7953` edge `0.0321` maxDD `-0.7345`
- `risk_on_high->crypto_major_1h` score `0.3167` n `34` status `ready` deltaP `8.075` edge `0.0158` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3167` n `34` status `ready` deltaP `8.075` edge `0.0158` maxDD `-0.9888`
- `risk_on_high->unknown_4h` score `-0.274` n `34` status `ready` deltaP `3.9814` edge `-0.0018` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.274` n `34` status `ready` deltaP `3.9814` edge `-0.0018` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.317` n `178` status `ready` deltaP `3.2581` edge `0.0008` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5851` n `178` status `ready` deltaP `-0.259` edge `-0.0112` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.5932` n `178` status `ready` deltaP `1.0849` edge `0.0206` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.5997` n `178` status `ready` deltaP `4.8695` edge `0.0317` maxDD `-7.6171`
- `market_context_high->unknown_1h` score `-0.66` n `178` status `ready` deltaP `-1.201` edge `0.0172` maxDD `-1.4688`
- `risk_on_high->commodity_4h` score `-0.7` n `34` status `ready` deltaP `-0.4753` edge `-0.0124` maxDD `-0.7546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
