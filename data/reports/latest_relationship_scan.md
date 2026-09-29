# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T10:37:34.233771+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7522`

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

- `news_risk_high->unknown_24h` score `2602.6764` n `139` status `ready` deltaP `1.2153` edge `216.8816` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.657` n `139` status `ready` deltaP `32.9349` edge `1.5637` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.384` n `139` status `ready` deltaP `34.616` edge `0.8902` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `9.053` n `139` status `ready` deltaP `27.3243` edge `1.0157` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.2827` n `139` status `ready` deltaP `39.0325` edge `0.1662` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.9408` n `139` status `ready` deltaP `31.9332` edge `0.301` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.6928` n `142` status `ready` deltaP `27.9801` edge `0.1988` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0967` n `142` status `ready` deltaP `8.6332` edge `0.2998` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7357` n `142` status `ready` deltaP `6.8209` edge `0.1069` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6757` n `142` status `ready` deltaP `8.4507` edge `0.0661` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4766` n `142` status `ready` deltaP `8.7501` edge `0.0104` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0199` n `142` status `ready` deltaP `8.6826` edge `0.0291` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4429` n `142` status `ready` deltaP `1.3916` edge `0.0622` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5469` n `142` status `ready` deltaP `0.8644` edge `0.0116` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.327` n `142` status `ready` deltaP `-7.5446` edge `0.0296` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.338` n `142` status `ready` deltaP `8.5216` edge `-0.007` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.7298` n `142` status `ready` deltaP `-4.3778` edge `0.0789` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8816` n `142` status `ready` deltaP `-9.7432` edge `-0.0038` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-2.0434` n `142` status `ready` deltaP `-11.8495` edge `-0.0155` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.6468` n `142` status `ready` deltaP `-12.3561` edge `-0.0151` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
