# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T05:07:30.006453+00:00`
- Price records: `672`
- Market context records: `4795`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7548`

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

- `market_context_high->unknown_4h` score `7.7677` n `122` status `ready` deltaP `19.1774` edge `0.6405` maxDD `-4.6834`
- `market_context_high->unknown_1h` score `7.3957` n `122` status `ready` deltaP `12.2804` edge `0.5762` maxDD `-1.674`
- `market_context_high->unknown_24h` score `2.2601` n `112` status `ready` deltaP `12.8968` edge `0.1947` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.1141` n `122` status `ready` deltaP `5.6812` edge `0.0304` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.0519` n `122` status `ready` deltaP `11.8153` edge `0.0451` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.0284` n `122` status `ready` deltaP `8.6915` edge `0.107` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.3237` n `122` status `ready` deltaP `7.4521` edge `0.0157` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4242` n `122` status `ready` deltaP `3.1263` edge `0.0024` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6983` n `122` status `ready` deltaP `1.7179` edge `0.0071` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.8849` n `122` status `ready` deltaP `-0.8835` edge `-0.0029` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3512` n `122` status `ready` deltaP `-1.0479` edge `-0.0052` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.157` n `112` status `ready` deltaP `19.7172` edge `0.1029` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.233` n `122` status `ready` deltaP `-0.6479` edge `-0.0644` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.1136` n `122` status `ready` deltaP `1.1976` edge `-0.0435` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.2353` n `112` status `ready` deltaP `-14.0625` edge `-0.0209` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4564` n `122` status `ready` deltaP `0.9841` edge `-0.0689` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.6974` n `122` status `ready` deltaP `5.3553` edge `0.0045` maxDD `-46.0617`
- `market_context_high->index_24h` score `-6.5392` n `112` status `ready` deltaP `-7.5645` edge `-0.1215` maxDD `-21.8401`
- `market_context_high->crypto_major_4h` score `-7.9915` n `122` status `ready` deltaP `4.1159` edge `-0.1289` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.2686` n `122` status `ready` deltaP `6.8398` edge `-0.2816` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
