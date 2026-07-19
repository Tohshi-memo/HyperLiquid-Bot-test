# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T11:52:29.058521+00:00`
- Price records: `672`
- Market context records: `7246`
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

- `risk_on_high->crypto_major_4h` score `5.9595` n `34` status `ready` deltaP `27.0804` edge `0.3544` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.9595` n `34` status `ready` deltaP `27.0804` edge `0.3544` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.3194` n `34` status `ready` deltaP `17.4049` edge `0.2832` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.3194` n `34` status `ready` deltaP `17.4049` edge `0.2832` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1447` n `34` status `ready` deltaP `23.0171` edge `0.0403` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1447` n `34` status `ready` deltaP `23.0171` edge `0.0403` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.0698` n `34` status `ready` deltaP `5.3794` edge `0.1376` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.0698` n `34` status `ready` deltaP `5.3794` edge `0.1376` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.2762` n `34` status `ready` deltaP `7.6259` edge `0.0136` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2762` n `34` status `ready` deltaP `7.6259` edge `0.0136` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2282` n `34` status `ready` deltaP `2.7645` edge `0.0306` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2282` n `34` status `ready` deltaP `2.7645` edge `0.0306` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1334` n `34` status `ready` deltaP `3.2192` edge `0.0213` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1334` n `34` status `ready` deltaP `3.2192` edge `0.0213` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2369` n `159` status `ready` deltaP `2.68` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6547` n `159` status `ready` deltaP `-1.2522` edge `-0.0135` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.6648` n `34` status `ready` deltaP `-0.2605` edge `-0.0109` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6648` n `34` status `ready` deltaP `-0.2605` edge `-0.0109` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.7136` n `159` status `ready` deltaP `-0.5244` edge `0.0159` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.7736` n `159` status `ready` deltaP `2.8905` edge `0.0226` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
