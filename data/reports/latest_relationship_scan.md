# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T12:22:34.097623+00:00`
- Price records: `672`
- Market context records: `5878`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10178`

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

- `news_risk_high->fx_4h` score `3.7752` n `30` status `ready` deltaP `39.3902` edge `0.0566` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5629` n `231` status `ready` deltaP `9.0995` edge `0.1796` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9509` n `30` status `ready` deltaP `11.8363` edge `0.0897` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3167` n `30` status `ready` deltaP `5.6188` edge `0.0493` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.3277` n `236` status `ready` deltaP `4.9528` edge `0.0342` maxDD `-4.5619`
- `news_risk_high->metal_1h` score `-0.4095` n `30` status `ready` deltaP `1.8363` edge `-0.0281` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.4645` n `236` status `ready` deltaP `-1.4691` edge `-0.0009` maxDD `-0.5751`
- `market_context_high->metal_1h` score `-0.5052` n `236` status `ready` deltaP `3.164` edge `0.0039` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5085` n `236` status `ready` deltaP `-1.02` edge `-0.0013` maxDD `-1.9006`
- `market_context_high->index_1h` score `-0.5853` n `236` status `ready` deltaP `0.8449` edge `0.0041` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8398` n `236` status `ready` deltaP `3.5877` edge `0.0382` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9097` n `236` status `ready` deltaP `2.7657` edge `0.0392` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1674` n `231` status `ready` deltaP `0.5636` edge `0.0153` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2409` n `30` status `ready` deltaP `-12.5449` edge `-0.024` maxDD `-1.1161`
- `news_risk_high->commodity_4h` score `-1.8236` n `30` status `ready` deltaP `-13.8821` edge `-0.0537` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-1.9844` n `231` status `ready` deltaP `10.1059` edge `0.2045` maxDD `-25.6458`
- `market_context_high->fx_4h` score `-1.9904` n `231` status `ready` deltaP `-8.1856` edge `-0.0057` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.2809` n `231` status `ready` deltaP `-0.722` edge `-0.0139` maxDD `-6.3754`
- `news_risk_high->index_4h` score `-2.3142` n `30` status `ready` deltaP `-17.0122` edge `-0.0799` maxDD `-2.9371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
