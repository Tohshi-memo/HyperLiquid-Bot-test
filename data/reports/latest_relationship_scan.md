# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T12:22:26.368811+00:00`
- Price records: `672`
- Market context records: `5662`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.2719` n `190` status `ready` deltaP `15.4386` edge `0.5943` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8849` n `240` status `ready` deltaP `11.128` edge `0.2288` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4814` n `240` status `ready` deltaP `7.6626` edge `0.1529` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.2168` n `240` status `ready` deltaP `7.6321` edge `0.1521` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.1987` n `190` status `ready` deltaP `17.5201` edge `0.0541` maxDD `-2.3472`
- `market_context_high->fx_1h` score `-0.2519` n `252` status `ready` deltaP `2.1338` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4402` n `252` status `ready` deltaP `4.876` edge `0.0315` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5189` n `252` status `ready` deltaP `0.1949` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5499` n `252` status `ready` deltaP `2.015` edge `0.0369` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.8074` n `252` status `ready` deltaP `3.0249` edge `0.0371` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.872` n `252` status `ready` deltaP `1.0479` edge `-0.0031` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.9329` n `252` status `ready` deltaP `0.5846` edge `0.0052` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.2348` n `240` status `ready` deltaP `2.7643` edge `0.0067` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2913` n `240` status `ready` deltaP `-1.0772` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3626` n `190` status `ready` deltaP `8.6824` edge `0.0379` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0233` n `240` status `ready` deltaP `-14.1667` edge `-0.0548` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.7655` n `240` status `ready` deltaP `-1.8801` edge `-0.0337` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.8119` n `190` status `ready` deltaP `3.5453` edge `0.0294` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4292` n `190` status `ready` deltaP `-13.8414` edge `-0.2523` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.5452` n `190` status `ready` deltaP `-13.1908` edge `-0.0966` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
