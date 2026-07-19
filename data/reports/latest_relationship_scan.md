# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T12:52:29.638130+00:00`
- Price records: `672`
- Market context records: `7251`
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

- `risk_on_high->crypto_major_4h` score `6.0659` n `34` status `ready` deltaP `27.6901` edge `0.3592` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.0659` n `34` status `ready` deltaP `27.6901` edge `0.3592` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.4066` n `34` status `ready` deltaP `18.0147` edge `0.2864` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.4066` n `34` status `ready` deltaP `18.0147` edge `0.2864` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1014` n `34` status `ready` deltaP `22.5667` edge `0.0397` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1014` n `34` status `ready` deltaP `22.5667` edge `0.0397` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.1208` n `34` status `ready` deltaP `5.8374` edge `0.1388` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.1208` n `34` status `ready` deltaP `5.8374` edge `0.1388` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.3276` n `34` status `ready` deltaP `8.2247` edge `0.0162` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3276` n `34` status `ready` deltaP `8.2247` edge `0.0162` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2582` n `34` status `ready` deltaP `3.0648` edge `0.0311` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2582` n `34` status `ready` deltaP `3.0648` edge `0.0311` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1334` n `34` status `ready` deltaP `3.2192` edge `0.0213` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1334` n `34` status `ready` deltaP `3.2192` edge `0.0213` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2253` n `155` status `ready` deltaP `2.9032` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5971` n `155` status `ready` deltaP `-0.3555` edge `-0.0121` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.7209` n `34` status `ready` deltaP `-0.8712` edge `-0.0115` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.7209` n `34` status `ready` deltaP `-0.8712` edge `-0.0115` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.7329` n `155` status `ready` deltaP `-0.7611` edge `0.015` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.8197` n `155` status `ready` deltaP `2.3044` edge `0.0206` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
