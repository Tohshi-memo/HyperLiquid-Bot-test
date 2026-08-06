# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T14:37:28.273955+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11797`

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

- `market_context_high->unknown_24h` score `6.8465` n `100` status `ready` deltaP `3.8611` edge `0.5491` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.2959` n `100` status `ready` deltaP `4.0694` edge `0.1977` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.1384` n `112` status `ready` deltaP `13.5888` edge `0.0889` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4728` n `100` status `ready` deltaP `20.3681` edge `0.0454` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3176` n `114` status `ready` deltaP `6.6105` edge `0.024` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0428` n `114` status `ready` deltaP `6.6761` edge `-0.004` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3021` n `112` status `ready` deltaP `7.1646` edge `-0.0005` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5448` n `114` status `ready` deltaP `-2.0091` edge `-0.007` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6839` n `114` status `ready` deltaP `-2.7576` edge `-0.0159` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7521` n `112` status `ready` deltaP `2.9181` edge `0.0076` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-1.1087` n `112` status `ready` deltaP `3.8327` edge `-0.0287` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.1898` n `100` status `ready` deltaP `-3.4583` edge `0.09` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.3088` n `114` status `ready` deltaP `-3.7215` edge `-0.0132` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.4937` n `114` status `ready` deltaP `2.8916` edge `-0.0543` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.6933` n `112` status `ready` deltaP `-7.6873` edge `-0.0404` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.873` n `114` status `ready` deltaP `-8.4725` edge `-0.0456` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.8866` n `100` status `ready` deltaP `-5.3611` edge `-0.0605` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.2624` n `112` status `ready` deltaP `0.0` edge `-0.274` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.5141` n `100` status `ready` deltaP `7.9306` edge `-0.0115` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.4385` n `112` status `ready` deltaP `-6.642` edge `-0.1544` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
