# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T18:22:28.943775+00:00`
- Price records: `672`
- Market context records: `5690`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8856`

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

- `market_context_high->equity_24h` score `1.7729` n `207` status `ready` deltaP `16.1761` edge `0.5478` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.6662` n `257` status `ready` deltaP `12.5736` edge `0.2312` maxDD `-9.7608`
- `market_context_high->crypto_alt_4h` score `0.9192` n `257` status `ready` deltaP `9.6612` edge `0.1731` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2254` n `257` status `ready` deltaP `6.5323` edge `0.1391` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2636` n `269` status `ready` deltaP `1.8949` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.3497` n `269` status `ready` deltaP `3.1348` edge `0.0419` maxDD `-4.6885`
- `market_context_high->crypto_major_1h` score `-0.462` n `269` status `ready` deltaP `4.7865` edge `0.0437` maxDD `-6.1289`
- `market_context_high->metal_1h` score `-0.4757` n `269` status `ready` deltaP `1.0691` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5726` n `269` status `ready` deltaP `3.6413` edge `0.0287` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6178` n `269` status `ready` deltaP `0.4703` edge `0.0045` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.8992` n `207` status `ready` deltaP `13.5115` edge `0.0463` maxDD `-3.1322`
- `market_context_high->commodity_1h` score `-0.9419` n `269` status `ready` deltaP `0.2632` edge `-0.0037` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1253` n `257` status `ready` deltaP `4.7956` edge `0.0072` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.291` n `257` status `ready` deltaP `-0.8767` edge `0.0075` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.6776` n `207` status `ready` deltaP `4.5969` edge `0.0333` maxDD `-17.5782`
- `market_context_high->metal_4h` score `-2.812` n `257` status `ready` deltaP `-10.5521` edge `-0.0526` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.8391` n `257` status `ready` deltaP `-3.0102` edge `-0.0323` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4098` n `207` status `ready` deltaP `4.9215` edge `0.0454` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.1959` n `207` status `ready` deltaP `-10.7639` edge `-0.2464` maxDD `-32.6082`
- `market_context_high->commodity_24h` score `-12.1063` n `207` status `ready` deltaP `-10.8394` edge `-0.0757` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
