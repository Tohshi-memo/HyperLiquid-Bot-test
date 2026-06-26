# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T02:07:25.676033+00:00`
- Price records: `672`
- Market context records: `4783`
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

- `market_context_high->unknown_1h` score `8.1157` n `122` status `ready` deltaP `12.7295` edge `0.6332` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.4957` n `122` status `ready` deltaP `17.653` edge `0.628` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.9016` n `107` status `ready` deltaP `11.52` edge `0.174` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.1034` n `122` status `ready` deltaP `11.8153` edge `0.0517` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.083` n `122` status `ready` deltaP `5.0824` edge `0.0318` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.4622` n `122` status `ready` deltaP `2.5165` edge `0.0016` maxDD `-1.5439`
- `market_context_high->equity_4h` score `-0.4823` n `122` status `ready` deltaP `6.8623` edge `0.061` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.4983` n `122` status `ready` deltaP `5.7752` edge `0.0045` maxDD `-5.5505`
- `market_context_high->fx_1h` score `-0.8873` n `122` status `ready` deltaP `-0.8835` edge `-0.0031` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-0.8878` n `122` status `ready` deltaP `0.8197` edge `-0.0027` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.4614` n `122` status `ready` deltaP `-2.0958` edge `-0.0074` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1704` n `107` status `ready` deltaP `19.9231` edge `0.0998` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2922` n `122` status `ready` deltaP `-1.097` edge `-0.069` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.2599` n `122` status `ready` deltaP `0.2994` edge `-0.0497` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.362` n `107` status `ready` deltaP `-15.4206` edge `-0.0224` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.5799` n `122` status `ready` deltaP `0.0859` edge `-0.0732` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.1147` n `122` status `ready` deltaP `3.5261` edge `-0.0368` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6798` n `107` status `ready` deltaP `-5.1029` edge `-0.1059` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.4205` n `122` status `ready` deltaP `2.2866` edge `-0.1717` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.558` n `122` status `ready` deltaP `5.0105` edge `-0.3065` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
