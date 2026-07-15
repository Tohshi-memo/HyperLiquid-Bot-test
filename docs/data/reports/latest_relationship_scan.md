# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T19:22:26.822497+00:00`
- Price records: `672`
- Market context records: `6846`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `1.034` n `176` status `ready` deltaP `-1.5467` edge `0.5181` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `-0.2117` n `176` status `ready` deltaP `7.7967` edge `0.1172` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2517` n `221` status `ready` deltaP `2.1791` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5918` n `221` status `ready` deltaP `1.9204` edge `0.0143` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6082` n `221` status `ready` deltaP `3.88` edge `0.0136` maxDD `-4.2122`
- `market_context_high->commodity_1h` score `-0.6665` n `221` status `ready` deltaP `-2.0226` edge `-0.0035` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.9066` n `221` status `ready` deltaP `-3.0909` edge `-0.0045` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9795` n `221` status `ready` deltaP `-5.8194` edge `-0.01` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0218` n `211` status `ready` deltaP `10.4807` edge `0.0055` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5171` n `211` status `ready` deltaP `-4.3529` edge `-0.0165` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6898` n `221` status `ready` deltaP `-3.4072` edge `-0.028` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-2.0312` n `221` status `ready` deltaP `-0.6584` edge `-0.038` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.1766` n `211` status `ready` deltaP `1.5035` edge `-0.0311` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.6224` n `211` status `ready` deltaP `-2.3819` edge `-0.022` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9974` n `211` status `ready` deltaP `-0.3092` edge `-0.0495` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1744` n `211` status `ready` deltaP `-0.5448` edge `-0.045` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2584` n `211` status `ready` deltaP `-9.6268` edge `0.0292` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4816` n `176` status `ready` deltaP `-9.7853` edge `-0.0046` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.9364` n `211` status `ready` deltaP `-1.5757` edge `-0.2125` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.1701` n `176` status `ready` deltaP `-18.8447` edge `-0.2015` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
