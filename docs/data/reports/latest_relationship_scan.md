# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T07:22:34.226636+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3926`

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

- `news_risk_high->crypto_alt_4h` score `-0.522` n `146` status `ready` deltaP `5.6277` edge `0.1592` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.671` n `146` status `ready` deltaP `1.5831` edge `0.0262` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7168` n `146` status `ready` deltaP `-2.8217` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.743` n `146` status `ready` deltaP `2.8443` edge `-0.0009` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5259` n `146` status `ready` deltaP `-8.2417` edge `-0.0185` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5968` n `146` status `ready` deltaP `-9.9085` edge `-0.0135` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.7466` n `146` status `ready` deltaP `1.4513` edge `-0.0035` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1143` n `146` status `ready` deltaP `-7.28` edge `0.009` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4328` n `146` status `ready` deltaP `-18.6638` edge `-0.0166` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5846` n `146` status `ready` deltaP `-6.1869` edge `-0.0225` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8741` n `146` status `ready` deltaP `-12.1628` edge `-0.0032` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1139` n `146` status `ready` deltaP `-9.5786` edge `0.0398` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4228` n `146` status `ready` deltaP `-7.7065` edge `-0.0613` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4836` n `146` status `ready` deltaP `-10.1967` edge `-0.0685` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.3821` n `146` status `ready` deltaP `-5.5577` edge `-0.1366` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.6261` n `146` status `ready` deltaP `-12.2495` edge `-0.1519` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.3546` n `146` status `ready` deltaP `-20.1616` edge `0.0976` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.7903` n `146` status `ready` deltaP `0.8415` edge `-0.0687` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.791` n `146` status `ready` deltaP `9.9778` edge `0.2346` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.2702` n `146` status `ready` deltaP `6.1715` edge `-0.1712` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
