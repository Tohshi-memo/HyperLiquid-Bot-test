# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T13:22:20.240899+00:00`
- Price records: `672`
- Market context records: `3181`
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

- `market_context_high->commodity_24h` score `13.8178` n `103` status `ready` deltaP `47.2357` edge `0.8794` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.2085` n `103` status `ready` deltaP `19.6905` edge `0.9349` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.4946` n `103` status `ready` deltaP `14.4266` edge `2.3751` maxDD `-71.142`
- `market_context_high->index_24h` score `6.224` n `103` status `ready` deltaP `29.7599` edge `0.855` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.4599` n `103` status `ready` deltaP `12.7798` edge `1.3282` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1126` n `134` status `ready` deltaP `19.8125` edge `0.1731` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.7774` n `134` status `ready` deltaP `11.3555` edge `0.2113` maxDD `-14.7778`
- `market_context_high->fx_24h` score `0.6997` n `103` status `ready` deltaP `11.755` edge `0.0027` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.3456` n `140` status `ready` deltaP `5.9795` edge `0.0312` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3237` n `140` status `ready` deltaP `6.6125` edge `0.0207` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.4408` n `140` status `ready` deltaP `6.0821` edge `0.1159` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.8333` n `134` status `ready` deltaP `16.6909` edge `0.0728` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0212` n `140` status `ready` deltaP `3.58` edge `0.0715` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2214` n `140` status `ready` deltaP `4.6193` edge `0.016` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3457` n `134` status `ready` deltaP `-11.5876` edge `-0.0068` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.612` n `140` status `ready` deltaP `-9.0676` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0714` n `140` status `ready` deltaP `-3.8024` edge `-0.0079` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.2188` n `134` status `ready` deltaP `17.5078` edge `0.4033` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0835` n `140` status `ready` deltaP `2.8016` edge `-0.073` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6257` n `134` status `ready` deltaP `10.4455` edge `0.2579` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
