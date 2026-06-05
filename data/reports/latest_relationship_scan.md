# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T12:07:21.833824+00:00`
- Price records: `672`
- Market context records: `2967`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.91` n `115` status `ready` deltaP `10.6718` edge `1.7297` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `9.3026` n `115` status `ready` deltaP `16.4674` edge `0.7119` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `8.4597` n `115` status `ready` deltaP `31.5731` edge `0.5648` maxDD `-2.2916`
- `market_context_high->equity_24h` score `7.4855` n `115` status `ready` deltaP `16.7949` edge `0.7122` maxDD `-12.6963`
- `market_context_high->index_24h` score `3.6064` n `115` status `ready` deltaP `15.4061` edge `0.2959` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.2484` n `116` status `ready` deltaP `16.311` edge `0.2009` maxDD `-0.7819`
- `market_context_high->crypto_alt_4h` score `2.6195` n `116` status `ready` deltaP `23.7489` edge `0.5161` maxDD `-30.8239`
- `market_context_high->index_4h` score `1.5145` n `116` status `ready` deltaP `16.3268` edge `0.0962` maxDD `-1.9733`
- `market_context_high->equity_1h` score `0.8172` n `116` status `ready` deltaP `5.9674` edge `0.0618` maxDD `-1.012`
- `market_context_high->crypto_alt_1h` score `0.2426` n `116` status `ready` deltaP `9.0337` edge `0.1235` maxDD `-10.747`
- `market_context_high->unknown_4h` score `0.2112` n `116` status `ready` deltaP `3.8004` edge `0.0976` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.1034` n `116` status `ready` deltaP `6.1119` edge `0.0206` maxDD `-1.1802`
- `market_context_high->crypto_major_1h` score `-0.0399` n `116` status `ready` deltaP `8.5794` edge `0.0913` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-0.2622` n `116` status `ready` deltaP `7.9479` edge `0.0523` maxDD `-7.4453`
- `market_context_high->fx_1h` score `-0.2951` n `116` status `ready` deltaP `0.3046` edge `0.0041` maxDD `-0.1244`
- `market_context_high->commodity_1h` score `-0.5855` n `116` status `ready` deltaP `-1.5331` edge `-0.0023` maxDD `-3.3365`
- `market_context_high->unknown_1h` score `-0.7052` n `116` status `ready` deltaP `2.7772` edge `-0.0042` maxDD `-3.1801`
- `market_context_high->metal_1h` score `-0.729` n `116` status `ready` deltaP `-1.0531` edge `0.0023` maxDD `-3.4325`
- `market_context_high->crypto_major_4h` score `-0.82` n `116` status `ready` deltaP `11.3278` edge `0.3319` maxDD `-33.6701`
- `market_context_high->fx_4h` score `-1.1697` n `116` status `ready` deltaP `-3.7058` edge `0.0051` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
