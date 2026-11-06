# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T10:22:24.876994+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4042`

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

- `news_risk_high->crypto_alt_4h` score `-0.4923` n `129` status `ready` deltaP `4.429` edge `0.171` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5801` n `129` status `ready` deltaP `1.5318` edge `0.0382` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6884` n `129` status `ready` deltaP `2.7561` edge `0.0007` maxDD `-1.1151`
- `news_risk_high->index_4h` score `-0.7314` n `129` status `ready` deltaP `5.4831` edge `0.012` maxDD `-2.7189`
- `news_risk_high->fx_1h` score `-0.7669` n `129` status `ready` deltaP `-3.8307` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.1069` n `129` status `ready` deltaP `-6.0148` edge `-0.0096` maxDD `-1.3766`
- `news_risk_high->index_24h` score `-1.163` n `129` status `ready` deltaP `-7.1081` edge `0.1026` maxDD `-6.6786`
- `news_risk_high->crypto_major_1h` score `-1.2273` n `129` status `ready` deltaP `-3.6218` edge `-0.0022` maxDD `-6.1465`
- `news_risk_high->metal_1h` score `-1.2561` n `129` status `ready` deltaP `-6.4661` edge `-0.0177` maxDD `-2.3516`
- `news_risk_high->fx_24h` score `-1.8197` n `129` status `ready` deltaP `-19.7848` edge `-0.0166` maxDD `-1.1167`
- `news_risk_high->equity_1h` score `-1.9492` n `129` status `ready` deltaP `-4.2903` edge `0.0035` maxDD `-12.9841`
- `news_risk_high->equity_24h` score `-2.1905` n `129` status `ready` deltaP `17.289` edge `0.8775` maxDD `-86.0244`
- `news_risk_high->crypto_major_4h` score `-2.7726` n `129` status `ready` deltaP `-5.1167` edge `0.0361` maxDD `-13.31`
- `news_risk_high->commodity_1h` score `-2.7947` n `129` status `ready` deltaP `-13.7156` edge `-0.0048` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-4.0832` n `129` status `ready` deltaP `-9.4725` edge `-0.0644` maxDD `-6.3504`
- `news_risk_high->commodity_4h` score `-4.5493` n `129` status `ready` deltaP `-20.1113` edge `-0.0096` maxDD `-9.5011`
- `news_risk_high->equity_4h` score `-5.518` n `129` status `ready` deltaP `5.9404` edge `0.0622` maxDD `-35.9312`
- `news_risk_high->metal_24h` score `-6.057` n `129` status `ready` deltaP `-10.1164` edge `-0.2477` maxDD `-8.5019`
- `news_risk_high->commodity_24h` score `-10.5812` n `129` status `ready` deltaP `-22.0823` edge `0.0345` maxDD `-42.1907`
- `news_risk_high->crypto_major_24h` score `-12.0676` n `129` status `ready` deltaP `-19.927` edge `0.0307` maxDD `-54.9453`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
