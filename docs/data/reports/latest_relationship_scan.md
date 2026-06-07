# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T11:37:23.751352+00:00`
- Price records: `672`
- Market context records: `3173`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8856`

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

- `market_context_high->commodity_24h` score `13.9111` n `101` status `ready` deltaP `47.2171` edge `0.8873` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.0744` n `101` status `ready` deltaP `20.2643` edge `0.9199` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.5266` n `101` status `ready` deltaP `14.4115` edge `2.3793` maxDD `-71.142`
- `market_context_high->index_24h` score `6.1812` n `101` status `ready` deltaP `29.2216` edge `0.8531` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.4506` n `101` status `ready` deltaP `12.9762` edge `1.3257` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1222` n `134` status `ready` deltaP `19.8125` edge `0.1739` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.7512` n `101` status `ready` deltaP `12.3539` edge `0.003` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.3275` n `138` status `ready` deltaP `5.6474` edge `0.0319` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `0.2646` n `134` status `ready` deltaP `11.0506` edge `0.1706` maxDD `-14.7778`
- `market_context_high->index_1h` score `-0.3734` n `138` status `ready` deltaP `5.821` edge `0.0196` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.4126` n `138` status `ready` deltaP `5.9945` edge `0.1201` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.92` n `134` status `ready` deltaP `15.6238` edge `0.0688` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0374` n `138` status `ready` deltaP `3.0894` edge `0.0727` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2856` n `138` status `ready` deltaP `4.0723` edge `0.0143` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3386` n `134` status `ready` deltaP `-11.4352` edge `-0.0069` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6237` n `138` status `ready` deltaP `-9.199` edge `-0.0053` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0808` n `138` status `ready` deltaP `-3.8749` edge `-0.0082` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.1858` n `134` status `ready` deltaP `17.8127` edge `0.4055` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-2.9973` n `138` status `ready` deltaP `3.0548` edge `-0.0675` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6426` n `134` status `ready` deltaP `10.7504` edge `0.2537` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
