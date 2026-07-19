# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T17:07:24.631933+00:00`
- Price records: `672`
- Market context records: `7271`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13775`

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

- `risk_on_high->crypto_major_4h` score `7.1274` n `30` status `ready` deltaP `32.2866` edge `0.4082` maxDD `-0.6931`
- `risk_on_and_context->crypto_major_4h` score `7.1274` n `30` status `ready` deltaP `32.2866` edge `0.4082` maxDD `-0.6931`
- `risk_on_high->crypto_alt_4h` score `5.8689` n `30` status `ready` deltaP `27.3171` edge `0.3292` maxDD `-0.7792`
- `risk_on_and_context->crypto_alt_4h` score `5.8689` n `30` status `ready` deltaP `27.3171` edge `0.3292` maxDD `-0.7792`
- `risk_on_high->commodity_1h` score `1.8529` n `30` status `ready` deltaP `20.03` edge `0.0359` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `1.8529` n `30` status `ready` deltaP `20.03` edge `0.0359` maxDD `-0.2021`
- `risk_on_high->unknown_4h` score `0.6492` n `30` status `ready` deltaP `7.4899` edge `0.0497` maxDD `-0.6423`
- `risk_on_and_context->unknown_4h` score `0.6492` n `30` status `ready` deltaP `7.4899` edge `0.0497` maxDD `-0.6423`
- `risk_on_high->crypto_major_1h` score `0.4644` n `30` status `ready` deltaP `9.8503` edge `0.0225` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `0.4644` n `30` status `ready` deltaP `9.8503` edge `0.0225` maxDD `-0.957`
- `risk_on_high->equity_4h` score `0.4176` n `30` status `ready` deltaP `-0.6728` edge `0.1236` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `0.4176` n `30` status `ready` deltaP `-0.6728` edge `0.1236` maxDD `-2.412`
- `risk_on_high->equity_1h` score `0.2473` n `30` status `ready` deltaP `3.2733` edge `0.0288` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2473` n `30` status `ready` deltaP `3.2733` edge `0.0288` maxDD `-0.7345`
- `market_context_high->fx_1h` score `-0.2734` n `140` status `ready` deltaP `1.9927` edge `0.0006` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6948` n `140` status `ready` deltaP `-1.8747` edge `-0.0145` maxDD `-1.9668`
- `risk_on_high->crypto_alt_1h` score `-0.7446` n `30` status `ready` deltaP `-9.2515` edge `0.0035` maxDD `-0.9826`
- `risk_on_and_context->crypto_alt_1h` score `-0.7446` n `30` status `ready` deltaP `-9.2515` edge `0.0035` maxDD `-0.9826`
- `market_context_high->crypto_alt_1h` score `-0.7466` n `140` status `ready` deltaP `-0.6801` edge `0.0127` maxDD `-5.9775`
- `risk_on_high->commodity_4h` score `-0.7598` n `30` status `ready` deltaP `-5.0765` edge `-0.0208` maxDD `-0.7546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
