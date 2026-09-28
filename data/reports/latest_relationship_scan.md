# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T06:52:32.973866+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7882`

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

- `news_risk_high->unknown_24h` score `617.8704` n `139` status `ready` deltaP `1.2153` edge `51.4811` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `3.7524` n `139` status `ready` deltaP `16.9627` edge `0.5948` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.0753` n `139` status `ready` deltaP `21.945` edge `0.0779` maxDD `-1.4342`
- `news_risk_high->equity_24h` score `1.2807` n `139` status `ready` deltaP `15.866` edge `0.2566` maxDD `-11.1183`
- `news_risk_high->metal_24h` score `1.1922` n `139` status `ready` deltaP `20.3013` edge `0.159` maxDD `-7.5992`
- `news_risk_high->crypto_major_24h` score `1.0605` n `139` status `ready` deltaP `12.3938` edge `0.4492` maxDD `-26.1424`
- `news_risk_high->equity_4h` score `1.0551` n `139` status `ready` deltaP `19.8566` edge `0.1169` maxDD `-9.2416`
- `news_risk_high->crypto_alt_1h` score `0.3113` n `139` status `ready` deltaP `5.6703` edge `0.0792` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.1737` n `139` status `ready` deltaP `6.2982` edge `0.0045` maxDD `-0.2275`
- `news_risk_high->equity_1h` score `0.0919` n `139` status `ready` deltaP `4.8594` edge `0.0416` maxDD `-1.9736`
- `news_risk_high->crypto_alt_4h` score `-0.1708` n `139` status `ready` deltaP `5.4494` edge `0.2154` maxDD `-15.9436`
- `news_risk_high->index_4h` score `-0.2271` n `139` status `ready` deltaP `7.407` edge `0.0123` maxDD `-1.1153`
- `news_risk_high->metal_1h` score `-0.5984` n `139` status `ready` deltaP `0.742` edge `0.0091` maxDD `-0.7796`
- `news_risk_high->crypto_major_1h` score `-0.8911` n `139` status `ready` deltaP `-1.7986` edge `0.026` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1586` n `139` status `ready` deltaP `-8.6687` edge `-0.0027` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2372` n `139` status `ready` deltaP `9.8296` edge `-0.0028` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.6787` n `139` status `ready` deltaP `-12.0525` edge `0.0196` maxDD `-4.0238`
- `news_risk_high->commodity_1h` score `-1.9625` n `139` status `ready` deltaP `-10.8183` edge `-0.012` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.6186` n `139` status `ready` deltaP `-8.7494` edge `-0.0059` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6344` n `139` status `ready` deltaP `-9.6454` edge `0.0033` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
