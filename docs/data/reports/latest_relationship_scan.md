# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T09:37:29.925715+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4448`

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

- `news_risk_high->crypto_alt_4h` score `0.2937` n `146` status `ready` deltaP `6.3899` edge `0.2587` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4791` n `146` status `ready` deltaP `1.7328` edge `0.0498` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6381` n `146` status `ready` deltaP `-1.3247` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9323` n `146` status `ready` deltaP `0.8982` edge `-0.0037` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2416` n `146` status `ready` deltaP `-4.3495` edge `-0.008` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2713` n `146` status `ready` deltaP `-3.9634` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.0261` n `146` status `ready` deltaP `-2.6646` edge `-0.0119` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.2482` n `146` status `ready` deltaP `8.8256` edge `0.112` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-2.292` n `146` status `ready` deltaP `-4.1785` edge `0.0182` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.394` n `146` status `ready` deltaP `-17.3326` edge `-0.0205` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4678` n `146` status `ready` deltaP `-9.8249` edge `-0.0035` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7218` n `146` status `ready` deltaP `-7.0851` edge `-0.0341` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3086` n `146` status `ready` deltaP `-8.7544` edge `-0.0448` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0843` n `146` status `ready` deltaP `-13.9994` edge `-0.0116` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6067` n `146` status `ready` deltaP `-5.776` edge `-0.0249` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.7707` n `146` status `ready` deltaP `18.1531` edge `0.7104` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8802` n `146` status `ready` deltaP `-13.6214` edge `-0.0806` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.2878` n `146` status `ready` deltaP `-0.6828` edge `-0.1` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.4367` n `146` status `ready` deltaP `13.292` edge `0.4135` maxDD `-102.7472`
- `news_risk_high->commodity_24h` score `-13.024` n `146` status `ready` deltaP `-24.4292` edge `-0.0964` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
