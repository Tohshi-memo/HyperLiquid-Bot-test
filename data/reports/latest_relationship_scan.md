# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T17:52:33.640921+00:00`
- Price records: `672`
- Market context records: `6839`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11802`

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

- `market_context_high->unknown_24h` score `0.9779` n `176` status `ready` deltaP `-1.5467` edge `0.5109` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0276` n `176` status `ready` deltaP `8.8384` edge `0.1302` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.271` n `216` status `ready` deltaP `1.838` edge `0.0015` maxDD `-0.5468`
- `market_context_high->crypto_major_1h` score `-0.525` n `216` status `ready` deltaP `4.3053` edge `0.0177` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.5287` n `216` status `ready` deltaP `2.3037` edge `0.017` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.8934` n `216` status `ready` deltaP `-2.7778` edge `-0.0049` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-1.03` n `216` status `ready` deltaP `-6.5508` edge `-0.0116` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-1.0575` n `216` status `ready` deltaP `-2.2732` edge `-0.0045` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-1.0768` n `205` status `ready` deltaP `9.6341` edge `0.0041` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.6269` n `216` status `ready` deltaP `-3.2962` edge `-0.0235` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9957` n `216` status `ready` deltaP `-0.2301` edge `-0.0363` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.2444` n `205` status `ready` deltaP `0.5488` edge `-0.0351` maxDD `-11.1709`
- `market_context_high->commodity_4h` score `-2.3701` n `205` status `ready` deltaP `-4.9085` edge `-0.0158` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.745` n `205` status `ready` deltaP `-3.7805` edge `-0.0284` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9179` n `205` status `ready` deltaP `0.2439` edge `-0.043` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1092` n `205` status `ready` deltaP `0.2744` edge `-0.0421` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2448` n `205` status `ready` deltaP `-9.7561` edge `0.0312` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4624` n `176` status `ready` deltaP `-9.7853` edge `-0.003` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.8456` n `205` status `ready` deltaP `-1.6768` edge `-0.2206` maxDD `-54.9257`
- `market_context_high->metal_24h` score `-9.2496` n `176` status `ready` deltaP `-18.8447` edge `-0.2117` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
