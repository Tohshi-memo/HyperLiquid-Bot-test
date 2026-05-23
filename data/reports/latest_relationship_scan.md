# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T14:07:14.387938+00:00`
- Price records: `672`
- Market context records: `1637`
- Flow alert records: `6621`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `9.9895` n `179` status `ready` deltaP `27.3384` edge `0.8928` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.3875` n `179` status `ready` deltaP `19.4234` edge `0.2906` maxDD `-5.3574`
- `market_context_high->crypto_alt_4h` score `2.6166` n `185` status `ready` deltaP `18.1159` edge `0.3637` maxDD `-16.3135`
- `market_context_high->equity_4h` score `1.4351` n `185` status `ready` deltaP `11.5866` edge `0.1518` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.9236` n `179` status `ready` deltaP `17.8819` edge `0.4476` maxDD `-33.1875`
- `market_context_high->crypto_major_4h` score `0.8223` n `185` status `ready` deltaP `13.8756` edge `0.2838` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.1599` n `195` status `ready` deltaP `1.9001` edge `0.0692` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `-0.2676` n `179` status `ready` deltaP `23.4869` edge `0.6797` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.3811` n `179` status `ready` deltaP `7.0428` edge `0.0262` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.554` n `195` status `ready` deltaP `0.7631` edge `0.0296` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6624` n `195` status `ready` deltaP `0.3555` edge `0.0056` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7807` n `195` status `ready` deltaP `0.1896` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.8391` n `195` status `ready` deltaP `-1.2183` edge `0.0335` maxDD `-5.9702`
- `market_context_high->index_4h` score `-0.8557` n `185` status `ready` deltaP `-0.0009` edge `0.0376` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.8679` n `195` status `ready` deltaP `1.986` edge `0.0024` maxDD `-4.7041`
- `market_context_high->crypto_alt_24h` score `-1.2145` n `179` status `ready` deltaP `23.8355` edge `0.9208` maxDD `-88.8062`
- `market_context_high->metal_1h` score `-1.4288` n `195` status `ready` deltaP `1.7726` edge `0.0027` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.5149` n `185` status `ready` deltaP `7.3266` edge `0.0941` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.0077` n `185` status `ready` deltaP `-9.153` edge `-0.0134` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.8237` n `185` status `ready` deltaP `8.0818` edge `-0.1454` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
