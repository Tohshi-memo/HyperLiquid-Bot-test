# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T04:22:25.524153+00:00`
- Price records: `672`
- Market context records: `7213`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13810`

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

- `risk_on_high->crypto_major_4h` score `5.8837` n `34` status `ready` deltaP `26.9279` edge `0.3491` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.8837` n `34` status `ready` deltaP `26.9279` edge `0.3491` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.3932` n `34` status `ready` deltaP `17.8623` edge `0.2863` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.3932` n `34` status `ready` deltaP `17.8623` edge `0.2863` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.0772` n `34` status `ready` deltaP `22.279` edge `0.0396` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.0772` n `34` status `ready` deltaP `22.279` edge `0.0396` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.213` n `34` status `ready` deltaP `6.51` edge `0.142` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.213` n `34` status `ready` deltaP `6.51` edge `0.142` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.3385` n `34` status `ready` deltaP `8.3744` edge `0.0166` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3385` n `34` status `ready` deltaP `8.3744` edge `0.0166` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.3262` n `34` status `ready` deltaP `3.7953` edge `0.0319` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3262` n `34` status `ready` deltaP `3.7953` edge `0.0319` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.267` n `34` status `ready` deltaP `3.9814` edge `-0.0009` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.267` n `34` status `ready` deltaP `3.9814` edge `-0.0009` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.329` n `178` status `ready` deltaP `3.1084` edge `0.0008` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.5768` n `178` status `ready` deltaP `1.2346` edge `0.0217` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.5779` n `178` status `ready` deltaP `5.1689` edge `0.0325` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.5851` n `178` status `ready` deltaP `-0.259` edge `-0.0112` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-0.684` n `178` status `ready` deltaP `-1.3507` edge `0.0162` maxDD `-1.4688`
- `risk_on_high->commodity_4h` score `-0.6866` n `34` status `ready` deltaP `-0.3228` edge `-0.0123` maxDD `-0.7546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
