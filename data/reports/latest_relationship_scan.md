# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T16:52:29.881228+00:00`
- Price records: `672`
- Market context records: `7270`
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

- `risk_on_high->crypto_major_4h` score `6.725` n `31` status `ready` deltaP `29.8584` edge `0.3954` maxDD `-0.723`
- `risk_on_and_context->crypto_major_4h` score `6.725` n `31` status `ready` deltaP `29.8584` edge `0.3954` maxDD `-0.723`
- `risk_on_high->crypto_alt_4h` score `5.5249` n `31` status `ready` deltaP `25.059` edge `0.317` maxDD `-0.8923`
- `risk_on_and_context->crypto_alt_4h` score `5.5249` n `31` status `ready` deltaP `25.059` edge `0.317` maxDD `-0.8923`
- `risk_on_high->commodity_1h` score `1.9205` n `31` status `ready` deltaP `20.74` edge `0.0368` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `1.9205` n `31` status `ready` deltaP `20.74` edge `0.0368` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `0.6274` n `31` status `ready` deltaP `1.1098` edge `0.1292` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `0.6274` n `31` status `ready` deltaP `1.1098` edge `0.1292` maxDD `-2.412`
- `risk_on_high->equity_1h` score `0.4101` n `31` status `ready` deltaP `4.9937` edge `0.0309` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.4101` n `31` status `ready` deltaP `4.9937` edge `0.0309` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `0.4075` n `31` status `ready` deltaP `6.1369` edge `0.0412` maxDD `-0.8522`
- `risk_on_and_context->unknown_4h` score `0.4075` n `31` status `ready` deltaP `6.1369` edge `0.0412` maxDD `-0.8522`
- `risk_on_high->crypto_major_1h` score `0.3404` n `31` status `ready` deltaP `7.9148` edge `0.0195` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `0.3404` n `31` status `ready` deltaP `7.9148` edge `0.0195` maxDD `-0.957`
- `market_context_high->fx_1h` score `-0.255` n `141` status `ready` deltaP `2.3321` edge `0.0007` maxDD `-0.5817`
- `risk_on_high->commodity_4h` score `-0.6653` n `31` status `ready` deltaP `-3.724` edge `-0.0177` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6653` n `31` status `ready` deltaP `-3.724` edge `-0.0177` maxDD `-0.7546`
- `market_context_high->commodity_1h` score `-0.6816` n `141` status `ready` deltaP `-1.6805` edge `-0.0141` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.7715` n `141` status `ready` deltaP `-1.0245` edge `0.0118` maxDD `-5.9775`
- `market_context_high->unknown_4h` score `-0.8843` n `140` status `ready` deltaP `6.6899` edge `0.0779` maxDD `-6.2026`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
