# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T15:22:29.085230+00:00`
- Price records: `672`
- Market context records: `7262`
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

- `risk_on_high->crypto_major_4h` score `6.2171` n `34` status `ready` deltaP `28.6047` edge `0.3657` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.2171` n `34` status `ready` deltaP `28.6047` edge `0.3657` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.561` n `34` status `ready` deltaP `19.5391` edge `0.2891` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.561` n `34` status `ready` deltaP `19.5391` edge `0.2891` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1134` n `34` status `ready` deltaP `22.7168` edge `0.0397` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1134` n `34` status `ready` deltaP `22.7168` edge `0.0397` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.1242` n `34` status `ready` deltaP `5.7744` edge `0.1395` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.1242` n `34` status `ready` deltaP `5.7744` edge `0.1395` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.3347` n `34` status `ready` deltaP `8.2247` edge `0.0171` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3347` n `34` status `ready` deltaP `8.2247` edge `0.0171` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2942` n `34` status `ready` deltaP `3.5153` edge `0.0311` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2942` n `34` status `ready` deltaP `3.5153` edge `0.0311` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1714` n `34` status `ready` deltaP `2.6094` edge `0.0205` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1714` n `34` status `ready` deltaP `2.6094` edge `0.0205` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2429` n `145` status `ready` deltaP `2.564` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5758` n `145` status `ready` deltaP `0.0393` edge `-0.012` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.6356` n `34` status `ready` deltaP `-0.045` edge `-0.0099` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6356` n `34` status `ready` deltaP `-0.045` edge `-0.0099` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.8064` n `145` status `ready` deltaP `-1.5156` edge `0.0106` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.9465` n `145` status `ready` deltaP `1.1253` edge `0.0122` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
