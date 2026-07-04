# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T17:07:29.613590+00:00`
- Price records: `672`
- Market context records: `5684`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8768`

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

- `market_context_high->equity_24h` score `1.7872` n `206` status `ready` deltaP `16.0987` edge `0.5495` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8274` n `256` status `ready` deltaP `11.6426` edge `0.2141` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.3993` n `256` status `ready` deltaP `8.7271` edge `0.1561` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.1706` n `256` status `ready` deltaP `5.907` edge `0.1387` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2729` n `268` status `ready` deltaP `1.716` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.4681` n `268` status `ready` deltaP `2.6767` edge `0.0393` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.4974` n `268` status `ready` deltaP `0.6681` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5668` n `268` status `ready` deltaP `3.7135` edge `0.0287` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6192` n `268` status `ready` deltaP `0.4424` edge `0.0045` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6948` n `268` status `ready` deltaP `4.1022` edge `0.0393` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.9437` n `268` status `ready` deltaP `0.2257` edge `-0.0036` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1491` n `256` status `ready` deltaP `4.3826` edge `0.0069` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2756` n `256` status `ready` deltaP `-0.5811` edge `0.0075` maxDD `-3.04`
- `market_context_high->fx_24h` score `-1.2761` n `206` status `ready` deltaP `13.4928` edge `0.0465` maxDD `-3.0904`
- `market_context_high->index_24h` score `-2.528` n `206` status `ready` deltaP `5.9567` edge `0.0383` maxDD `-17.1688`
- `market_context_high->metal_4h` score `-2.8715` n `256` status `ready` deltaP `-11.5759` edge `-0.0534` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.8152` n `256` status `ready` deltaP `-2.7725` edge `-0.0319` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.9598` n `206` status `ready` deltaP `3.747` edge `0.0074` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.2905` n `206` status `ready` deltaP `-12.1073` edge `-0.2476` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-11.9735` n `206` status `ready` deltaP `-9.5991` edge `-0.0729` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
