# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T15:22:35.329483+00:00`
- Price records: `672`
- Market context records: `6829`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `market_context_high->unknown_24h` score `0.9186` n `176` status `ready` deltaP `-1.5467` edge `0.5033` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1925` n `176` status `ready` deltaP `9.8801` edge `0.137` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1678` n `207` status `ready` deltaP `6.0452` edge `0.0317` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.3194` n `207` status `ready` deltaP `3.48` edge `0.0266` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3362` n `207` status `ready` deltaP `0.6906` edge `0.0008` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.8844` n `207` status `ready` deltaP `-3.4395` edge `-0.0053` maxDD `-1.8127`
- `market_context_high->metal_1h` score `-0.9395` n `207` status `ready` deltaP `-5.7255` edge `-0.0084` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.1731` n `207` status `ready` deltaP `-3.1878` edge `-0.0082` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.1985` n `197` status `ready` deltaP `7.7721` edge `0.0009` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4841` n `197` status `ready` deltaP `-3.9123` edge `-0.0152` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.633` n `207` status `ready` deltaP `-4.0925` edge `-0.0187` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.8942` n `197` status `ready` deltaP `1.2628` edge `-0.0302` maxDD `-8.3516`
- `market_context_high->equity_1h` score `-2.4459` n `207` status `ready` deltaP `0.1461` edge `-0.0372` maxDD `-9.0745`
- `market_context_high->metal_4h` score `-2.6611` n `197` status `ready` deltaP `-2.8863` edge `-0.0236` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9239` n `197` status `ready` deltaP `0.3985` edge `-0.0448` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.0862` n `197` status `ready` deltaP `0.5525` edge `-0.041` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2593` n `197` status `ready` deltaP `-10.7032` edge `0.0363` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.454` n `176` status `ready` deltaP `-9.7853` edge `-0.0023` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.9317` n `197` status `ready` deltaP `-1.1212` edge `-0.1865` maxDD `-38.3202`
- `market_context_high->metal_24h` score `-9.4678` n `176` status `ready` deltaP `-20.5808` edge `-0.2281` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
