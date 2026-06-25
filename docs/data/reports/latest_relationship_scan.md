# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T15:37:31.327747+00:00`
- Price records: `672`
- Market context records: `4736`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7448`

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

- `market_context_high->unknown_1h` score `78.6126` n `142` status `ready` deltaP `15.0165` edge `6.4927` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2657` n `141` status `ready` deltaP `14.2277` edge `0.465` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.4374` n `132` status `ready` deltaP `17.1875` edge `0.2642` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3014` n `142` status `ready` deltaP `2.528` edge `0.0241` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.5633` n `141` status `ready` deltaP `5.3721` edge `0.0014` maxDD `-5.7542`
- `market_context_high->fx_4h` score `-0.8835` n `141` status `ready` deltaP `-0.547` edge `-0.0022` maxDD `-1.9274`
- `market_context_high->equity_1h` score `-0.9552` n `142` status `ready` deltaP `-1.7079` edge `-0.0135` maxDD `-5.4726`
- `market_context_high->equity_4h` score `-0.9741` n `141` status `ready` deltaP `3.5958` edge `0.0239` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.4009` n `142` status `ready` deltaP `-6.4161` edge `-0.006` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.5255` n `141` status `ready` deltaP `8.6457` edge `0.026` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5993` n `142` status `ready` deltaP `-3.8037` edge `-0.0075` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.7066` n `142` status `ready` deltaP `-4.9633` edge `-0.0729` maxDD `-15.9475`
- `market_context_high->crypto_alt_1h` score `-2.9067` n `142` status `ready` deltaP `-0.3606` edge `-0.0557` maxDD `-21.1642`
- `market_context_high->crypto_major_1h` score `-3.5185` n `142` status `ready` deltaP `-0.5271` edge `-0.0735` maxDD `-27.2597`
- `market_context_high->commodity_24h` score `-4.3129` n `132` status `ready` deltaP `16.2405` edge `0.0571` maxDD `-28.6488`
- `market_context_high->fx_24h` score `-4.8072` n `132` status `ready` deltaP `-14.678` edge `-0.0199` maxDD `-5.2943`
- `market_context_high->crypto_alt_4h` score `-7.1872` n `141` status `ready` deltaP `-1.0574` edge `-0.1034` maxDD `-59.5456`
- `market_context_high->index_24h` score `-8.2791` n `132` status `ready` deltaP `-12.2474` edge `-0.1085` maxDD `-27.3155`
- `market_context_high->metal_4h` score `-8.597` n `141` status `ready` deltaP `1.3882` edge `-0.2618` maxDD `-62.6377`
- `market_context_high->crypto_major_4h` score `-10.0739` n `141` status `ready` deltaP `-0.6465` edge `-0.2136` maxDD `-80.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
