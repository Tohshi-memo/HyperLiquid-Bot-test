# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T09:52:28.629013+00:00`
- Price records: `672`
- Market context records: `6805`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8203` n `176` status `ready` deltaP `-1.5467` edge `0.4907` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3228` n `176` status `ready` deltaP `10.0537` edge `0.1467` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.3125` n `187` status `ready` deltaP `6.1722` edge `0.0188` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.4332` n `187` status `ready` deltaP `3.4984` edge `0.017` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.4529` n `187` status `ready` deltaP `-1.3585` edge `-0.0005` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6547` n `187` status `ready` deltaP `-1.144` edge `-0.008` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6863` n `187` status `ready` deltaP `-2.2991` edge `-0.0011` maxDD `-0.7249`
- `market_context_high->metal_1h` score `-0.7483` n `187` status `ready` deltaP `-5.5942` edge `-0.0039` maxDD `-1.3794`
- `market_context_high->equity_1h` score `-1.3102` n `187` status `ready` deltaP `2.1078` edge `-0.0188` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3825` n `185` status `ready` deltaP `4.7602` edge `-0.0026` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4056` n `185` status `ready` deltaP `-2.5981` edge `-0.0139` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.643` n `185` status `ready` deltaP `1.8375` edge `-0.0269` maxDD `-6.3458`
- `market_context_high->unknown_1h` score `-1.6463` n `187` status `ready` deltaP `-5.8936` edge `-0.0078` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.7766` n `185` status `ready` deltaP `-5.857` edge `-0.0186` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.2698` n `185` status `ready` deltaP `-0.6576` edge `-0.0821` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.4543` n `185` status `ready` deltaP `-1.517` edge `-0.0744` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.4905` n `185` status `ready` deltaP `-14.1175` edge `0.0398` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4996` n `176` status `ready` deltaP `-9.7853` edge `-0.0061` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.969` n `185` status `ready` deltaP `-0.81` edge `-0.1778` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.5037` n `176` status `ready` deltaP `-20.5808` edge `-0.2327` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
