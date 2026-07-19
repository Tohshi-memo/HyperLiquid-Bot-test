# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T16:39:32.897682+00:00`
- Price records: `672`
- Market context records: `7269`
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

- `risk_on_high->crypto_major_4h` score `6.341` n `32` status `ready` deltaP `27.439` edge `0.3838` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.341` n `32` status `ready` deltaP `27.439` edge `0.3838` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `5.1664` n `32` status `ready` deltaP `22.9421` edge `0.3065` maxDD `-0.9797`
- `risk_on_and_context->crypto_alt_4h` score `5.1664` n `32` status `ready` deltaP `22.9421` edge `0.3065` maxDD `-0.9797`
- `risk_on_high->commodity_1h` score `1.985` n `32` status `ready` deltaP `21.3964` edge `0.0378` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `1.985` n `32` status `ready` deltaP `21.3964` edge `0.0378` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `0.8179` n `32` status `ready` deltaP `2.7714` edge `0.134` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `0.8179` n `32` status `ready` deltaP `2.7714` edge `0.134` maxDD `-2.412`
- `risk_on_high->equity_1h` score `0.5512` n `32` status `ready` deltaP `6.6066` edge `0.0319` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.5512` n `32` status `ready` deltaP `6.6066` edge `0.0319` maxDD `-0.7345`
- `risk_on_high->crypto_major_1h` score `0.2289` n `32` status `ready` deltaP `6.1003` edge `0.0177` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2289` n `32` status `ready` deltaP `6.1003` edge `0.0177` maxDD `-0.9888`
- `risk_on_high->unknown_4h` score `0.1106` n `32` status `ready` deltaP `4.878` edge `0.0327` maxDD `-1.083`
- `risk_on_and_context->unknown_4h` score `0.1106` n `32` status `ready` deltaP `4.878` edge `0.0327` maxDD `-1.083`
- `market_context_high->fx_1h` score `-0.2454` n `142` status `ready` deltaP `2.5166` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6679` n `142` status `ready` deltaP `-1.4909` edge `-0.0136` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.7978` n `142` status `ready` deltaP `-1.3642` edge `0.0107` maxDD `-5.9775`
- `risk_on_high->commodity_4h` score `-0.888` n `32` status `ready` deltaP `-2.4656` edge `-0.0148` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.888` n `32` status `ready` deltaP `-2.4656` edge `-0.0148` maxDD `-0.7546`
- `market_context_high->unknown_4h` score `-0.9072` n `141` status `ready` deltaP `6.5181` edge `0.0761` maxDD `-6.2026`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
