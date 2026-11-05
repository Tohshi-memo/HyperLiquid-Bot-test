# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T03:52:26.708709+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3812`

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

- `news_risk_high->crypto_alt_4h` score `-0.4724` n `146` status `ready` deltaP `6.2375` edge `0.1615` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.703` n `146` status `ready` deltaP `1.2837` edge `0.0241` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7339` n `146` status `ready` deltaP `-3.1211` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7957` n `146` status `ready` deltaP `2.3952` edge `-0.0023` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5446` n `146` status `ready` deltaP `-8.5411` edge `-0.0189` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5976` n `146` status `ready` deltaP `-9.9085` edge `-0.0136` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8476` n `146` status `ready` deltaP `0.0793` edge `-0.0073` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1334` n `146` status `ready` deltaP `-7.5794` edge `0.0094` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4359` n `146` status `ready` deltaP `-18.6638` edge `-0.017` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6251` n `146` status `ready` deltaP `-6.4863` edge `-0.0257` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.7468` n `146` status `ready` deltaP `-11.1248` edge `0.0062` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1477` n `146` status `ready` deltaP `-9.7311` edge `0.038` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4839` n `146` status `ready` deltaP `-8.0059` edge `-0.0644` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.36` n `146` status `ready` deltaP `-9.2821` edge `-0.0643` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-5.6339` n `146` status `ready` deltaP `-3.1355` edge `-0.0904` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.759` n `146` status `ready` deltaP `-13.0116` edge `-0.1579` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.8802` n `146` status `ready` deltaP `-20.1616` edge `0.0538` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.9371` n `146` status `ready` deltaP `0.5367` edge `-0.0789` maxDD `-52.2214`
- `news_risk_high->crypto_alt_24h` score `-13.0538` n `146` status `ready` deltaP `8.5937` edge `-0.0314` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-13.315` n `146` status `ready` deltaP `10.4968` edge `0.2708` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
