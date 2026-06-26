# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T00:52:26.809069+00:00`
- Price records: `672`
- Market context records: `4777`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7510`

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

- `market_context_high->unknown_1h` score `8.2297` n `122` status `ready` deltaP `12.5798` edge `0.6437` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.3559` n `122` status `ready` deltaP `17.1956` edge `0.6194` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.8488` n `107` status `ready` deltaP `11.52` edge `0.1696` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.1553` n `122` status `ready` deltaP `12.2726` edge `0.0553` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0998` n `122` status `ready` deltaP `5.2321` edge `0.0322` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.4194` n `122` status `ready` deltaP `3.2787` edge `0.002` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.5345` n `122` status `ready` deltaP `5.3179` edge `0.0029` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.5984` n `122` status `ready` deltaP `6.1001` edge `0.0512` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.8609` n `122` status `ready` deltaP `-0.5841` edge `-0.0029` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-0.9669` n `122` status `ready` deltaP `0.3706` edge `-0.0063` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.4902` n `122` status `ready` deltaP `-2.3952` edge `-0.0078` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.0699` n `107` status `ready` deltaP `20.7911` edge `0.1069` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3016` n `122` status `ready` deltaP `-1.2467` edge `-0.0692` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-3.2841` n `107` status `ready` deltaP `-14.5525` edge `-0.0217` maxDD `-3.3968`
- `market_context_high->crypto_alt_1h` score `-3.3162` n `122` status `ready` deltaP `0.0` edge `-0.0524` maxDD `-15.2495`
- `market_context_high->crypto_major_1h` score `-4.6674` n `122` status `ready` deltaP `-0.2135` edge `-0.0785` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.2056` n `122` status `ready` deltaP `3.0688` edge `-0.0454` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6738` n `107` status `ready` deltaP `-5.1029` edge `-0.1054` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.5254` n `122` status `ready` deltaP `1.8293` edge `-0.1821` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.6327` n `122` status `ready` deltaP `4.2483` edge `-0.311` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
