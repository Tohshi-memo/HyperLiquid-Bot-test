# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T14:22:42.487813+00:00`
- Price records: `672`
- Market context records: `5671`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8686`

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

- `market_context_high->equity_24h` score `2.1738` n `195` status `ready` deltaP `16.2366` edge `0.5808` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9936` n `245` status `ready` deltaP `11.7409` edge `0.2273` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4859` n `245` status `ready` deltaP `8.7905` edge `0.1629` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.3541` n `245` status `ready` deltaP `6.7004` edge `0.1487` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2718` n `257` status `ready` deltaP `1.751` edge `0.0011` maxDD `-0.4764`
- `market_context_high->fx_24h` score `-0.4067` n `195` status `ready` deltaP `16.3675` edge `0.0508` maxDD `-2.8382`
- `market_context_high->equity_1h` score `-0.4964` n `257` status `ready` deltaP `4.2936` edge `0.0307` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.5639` n `257` status `ready` deltaP `1.9298` edge `0.0363` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.5917` n `257` status `ready` deltaP `0.8825` edge `0.0051` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7345` n `257` status `ready` deltaP `3.6965` edge `0.0387` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.7791` n `257` status `ready` deltaP `0.434` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.8959` n `257` status `ready` deltaP `0.7636` edge `-0.0032` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2255` n `245` status `ready` deltaP `2.958` edge `0.0066` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2671` n `245` status `ready` deltaP `-0.5973` edge `0.0087` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.4814` n `195` status `ready` deltaP `6.8189` edge `0.0351` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9259` n `245` status `ready` deltaP `-12.5473` edge `-0.0539` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.7002` n `245` status `ready` deltaP `-1.4093` edge `-0.0314` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.496` n `195` status `ready` deltaP `4.3696` edge `0.0419` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3448` n `195` status `ready` deltaP `-12.7778` edge `-0.2501` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.415` n `195` status `ready` deltaP `-12.508` edge `-0.0903` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
