# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T13:52:33.237970+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->index_1h` score `0.2116` n `124` status `ready` deltaP `10.8992` edge `0.0048` maxDD `-0.6937`
- `market_context_high->equity_1h` score `0.2088` n `124` status `ready` deltaP `7.8134` edge `0.0468` maxDD `-3.1861`
- `market_context_high->fx_4h` score `0.1831` n `112` status `ready` deltaP `9.5601` edge `0.01` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0879` n `124` status `ready` deltaP `3.0182` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.1791` n `112` status `ready` deltaP `3.5061` edge `0.1166` maxDD `-8.3685`
- `market_context_high->index_4h` score `-0.3377` n `112` status `ready` deltaP `5.1612` edge `0.0147` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3744` n `124` status `ready` deltaP `1.8785` edge `-0.0041` maxDD `-0.503`
- `market_context_high->metal_4h` score `-0.393` n `112` status `ready` deltaP `4.29` edge `-0.0214` maxDD `-1.273`
- `market_context_high->unknown_1h` score `-0.4149` n `124` status `ready` deltaP `10.1314` edge `-0.0794` maxDD `-0.4843`
- `market_context_high->commodity_24h` score `-0.4679` n `105` status `ready` deltaP `4.4147` edge `0.1149` maxDD `-4.666`
- `market_context_high->commodity_4h` score `-0.65` n `112` status `ready` deltaP `-1.3502` edge `0.0107` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6577` n `124` status `ready` deltaP `-4.2496` edge `0.0006` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.93` n `124` status `ready` deltaP `-0.5601` edge `0.0064` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.3604` n `124` status `ready` deltaP `-2.9119` edge `-0.0525` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-2.6404` n `112` status `ready` deltaP `0.1742` edge `-0.0942` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.9951` n `105` status `ready` deltaP `-12.3016` edge `-0.0066` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.1873` n `105` status `ready` deltaP `-5.5953` edge `-0.0493` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.3411` n `112` status `ready` deltaP `-1.0888` edge `-0.2524` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.4933` n `105` status `ready` deltaP `-16.7212` edge `-0.1338` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.1408` n `105` status `ready` deltaP `8.1201` edge `-0.4319` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
