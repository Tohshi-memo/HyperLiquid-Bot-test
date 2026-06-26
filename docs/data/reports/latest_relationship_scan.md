# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T03:37:28.215382+00:00`
- Price records: `672`
- Market context records: `4789`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7510`

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

- `market_context_high->unknown_1h` score `7.674` n `122` status `ready` deltaP `12.8792` edge `0.5954` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.6527` n `122` status `ready` deltaP `18.4152` edge `0.636` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.9856` n `107` status `ready` deltaP `11.52` edge `0.181` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.1681` n `122` status `ready` deltaP `5.8309` edge `0.0339` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.0777` n `122` status `ready` deltaP `11.8153` edge `0.0484` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.2367` n `122` status `ready` deltaP `7.7769` edge `0.0864` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.4142` n `122` status `ready` deltaP `6.5374` edge `0.0102` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4614` n `122` status `ready` deltaP `2.5165` edge `0.0017` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.7187` n `122` status `ready` deltaP `1.4185` edge `0.0074` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.9244` n `122` status `ready` deltaP `-1.3326` edge `-0.0032` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3907` n `122` status `ready` deltaP `-1.497` edge `-0.0055` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.2579` n `122` status `ready` deltaP `-0.7976` edge `-0.0666` maxDD `-14.0715`
- `market_context_high->commodity_24h` score `-2.2769` n `107` status `ready` deltaP `18.8814` edge `0.0931` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-3.0836` n `122` status `ready` deltaP `0.8982` edge `-0.039` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.4398` n `107` status `ready` deltaP `-16.2887` edge `-0.0231` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4047` n `122` status `ready` deltaP `0.6847` edge `-0.0626` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.8433` n `122` status `ready` deltaP `4.4407` edge `-0.0081` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6426` n `107` status `ready` deltaP `-5.1029` edge `-0.1028` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.1374` n `122` status `ready` deltaP `3.2012` edge `-0.1415` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.402` n `122` status `ready` deltaP `5.9251` edge `-0.2926` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
