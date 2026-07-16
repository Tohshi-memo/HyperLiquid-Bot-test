# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T15:52:41.006023+00:00`
- Price records: `672`
- Market context records: `6933`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `market_context_high->fx_1h` score `-0.2303` n `230` status `ready` deltaP `2.5306` edge `0.0021` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.42` n `230` status `ready` deltaP `2.9433` edge `0.0218` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5415` n `230` status `ready` deltaP `3.9625` edge `0.0197` maxDD `-4.2991`
- `market_context_high->metal_1h` score `-0.703` n `230` status `ready` deltaP `-2.0021` edge `0.0` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.704` n `230` status `ready` deltaP `0.1002` edge `0.0002` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8218` n `224` status `ready` deltaP `13.6978` edge `0.0097` maxDD `-2.1765`
- `market_context_high->unknown_24h` score `-0.8281` n `213` status `ready` deltaP `-6.8502` edge `0.3527` maxDD `-15.3896`
- `market_context_high->commodity_1h` score `-1.15` n `230` status `ready` deltaP `-2.0528` edge `-0.0133` maxDD `-2.1742`
- `market_context_high->unknown_1h` score `-1.5424` n `230` status `ready` deltaP `-1.924` edge `-0.0256` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.5986` n `224` status `ready` deltaP `-3.8655` edge `-0.0302` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.658` n `230` status `ready` deltaP `3.1294` edge `-0.014` maxDD `-13.221`
- `market_context_high->index_4h` score `-1.6639` n `224` status `ready` deltaP `8.3624` edge `-0.0111` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-1.9206` n `224` status `ready` deltaP `5.368` edge `0.0163` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7554` n `224` status `ready` deltaP `1.753` edge `-0.0066` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7659` n `224` status `ready` deltaP `-0.0871` edge `-0.0213` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9827` n `224` status `ready` deltaP `-7.6655` edge `0.0391` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.2331` n `213` status `ready` deltaP `-3.3157` edge `-0.0605` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.1584` n `213` status `ready` deltaP `-5.1611` edge `-0.0085` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.5134` n `224` status `ready` deltaP `6.0649` edge `-0.081` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.7747` n `213` status `ready` deltaP `-12.8112` edge `-0.1172` maxDD `-33.4554`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
