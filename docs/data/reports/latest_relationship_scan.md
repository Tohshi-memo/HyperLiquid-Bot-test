# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T07:37:32.898365+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3930`

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

- `news_risk_high->crypto_alt_4h` score `-0.4899` n `146` status `ready` deltaP `5.7802` edge `0.1623` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.671` n `146` status `ready` deltaP `1.5831` edge `0.0262` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7082` n `146` status `ready` deltaP `-2.672` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7573` n `146` status `ready` deltaP `2.6946` edge `-0.0011` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5259` n `146` status `ready` deltaP `-8.2417` edge `-0.0185` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5873` n `146` status `ready` deltaP `-9.7561` edge `-0.0133` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.7371` n `146` status `ready` deltaP `1.6037` edge `-0.0033` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.131` n `146` status `ready` deltaP `-7.4297` edge `0.0086` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4312` n `146` status `ready` deltaP `-18.6638` edge `-0.0164` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5994` n `146` status `ready` deltaP `-6.3366` edge `-0.0234` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8772` n `146` status `ready` deltaP `-12.1628` edge `-0.0036` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1345` n `146` status `ready` deltaP `-9.7311` edge `0.0391` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4228` n `146` status `ready` deltaP `-7.7065` edge `-0.0613` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4824` n `146` status `ready` deltaP `-10.1967` edge `-0.0684` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.4271` n `146` status `ready` deltaP `-5.7307` edge `-0.1392` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.5791` n `146` status `ready` deltaP `-12.097` edge `-0.149` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.3198` n `146` status `ready` deltaP `-20.1616` edge `0.1005` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.7637` n `146` status `ready` deltaP `0.994` edge `-0.0675` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.8018` n `146` status `ready` deltaP `9.9778` edge `0.2337` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.3237` n `146` status `ready` deltaP `5.9985` edge `-0.1769` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
