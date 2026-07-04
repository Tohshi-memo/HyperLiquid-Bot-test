# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T14:37:27.896143+00:00`
- Price records: `672`
- Market context records: `5672`
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

- `market_context_high->equity_24h` score `2.1483` n `196` status `ready` deltaP `16.323` edge `0.5781` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9838` n `246` status `ready` deltaP `11.7378` edge `0.2265` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4896` n `246` status `ready` deltaP `8.7906` edge `0.1632` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.3199` n `246` status `ready` deltaP `6.4532` edge `0.1475` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2621` n `258` status `ready` deltaP `1.938` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4839` n `258` status `ready` deltaP `4.4504` edge `0.0307` maxDD `-5.0555`
- `market_context_high->fx_24h` score `-0.4967` n `196` status `ready` deltaP `16.0431` edge `0.0502` maxDD `-2.8834`
- `market_context_high->crypto_alt_1h` score `-0.5378` n `258` status `ready` deltaP `2.1063` edge `0.0373` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.5821` n `258` status `ready` deltaP `1.0665` edge `0.0051` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7045` n `258` status `ready` deltaP `3.876` edge `0.04` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.784` n `258` status `ready` deltaP `0.3876` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.9112` n `258` status `ready` deltaP `0.5721` edge `-0.0032` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2155` n `246` status `ready` deltaP `3.1504` edge `0.0066` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2659` n `246` status `ready` deltaP `-0.559` edge `0.0086` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.4863` n `196` status `ready` deltaP `6.6681` edge `0.0355` maxDD `-16.8966`
- `market_context_high->metal_4h` score `-2.9208` n `246` status `ready` deltaP `-12.4492` edge `-0.0539` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.7171` n `246` status `ready` deltaP `-1.5752` edge `-0.0317` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5288` n `196` status `ready` deltaP `4.319` edge `0.0395` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3364` n `196` status `ready` deltaP `-12.6453` edge `-0.2499` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.4005` n `196` status `ready` deltaP `-12.5071` edge `-0.0891` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
