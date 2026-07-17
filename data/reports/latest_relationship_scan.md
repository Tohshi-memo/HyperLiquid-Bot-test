# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T13:07:31.184950+00:00`
- Price records: `672`
- Market context records: `7031`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_1h` score `-0.2632` n `214` status `ready` deltaP `1.9279` edge `0.0012` maxDD `-0.49`
- `market_context_high->crypto_alt_1h` score `-0.3338` n `214` status `ready` deltaP `1.9419` edge `0.0307` maxDD `-4.5815`
- `market_context_high->fx_4h` score `-0.4636` n `214` status `ready` deltaP `11.99` edge `0.0083` maxDD `-1.4798`
- `market_context_high->metal_1h` score `-0.676` n `214` status `ready` deltaP `-1.6929` edge `0.0014` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.6884` n `214` status `ready` deltaP `0.3987` edge `0.0002` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-1.0055` n `214` status `ready` deltaP `3.4571` edge `0.0284` maxDD `-7.1523`
- `market_context_high->unknown_24h` score `-1.0785` n `201` status `ready` deltaP `-7.4783` edge `0.3666` maxDD `-18.7342`
- `market_context_high->unknown_1h` score `-1.1311` n `214` status `ready` deltaP `-2.6317` edge `0.0035` maxDD `-2.7502`
- `market_context_high->commodity_1h` score `-1.2587` n `214` status `ready` deltaP `-3.8334` edge `-0.0177` maxDD `-1.9306`
- `market_context_high->index_4h` score `-1.9073` n `214` status `ready` deltaP `6.1175` edge `-0.0154` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9951` n `214` status `ready` deltaP `5.0761` edge `0.0087` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.0247` n `214` status `ready` deltaP `-6.0392` edge `0.0836` maxDD `-8.2984`
- `market_context_high->commodity_4h` score `-2.1031` n `214` status `ready` deltaP `-3.9036` edge `-0.0332` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.5008` n `201` status `ready` deltaP `-2.0134` edge `-0.0641` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.685` n `214` status `ready` deltaP `1.352` edge `0.0253` maxDD `-22.2831`
- `market_context_high->equity_1h` score `-2.8666` n `214` status `ready` deltaP `3.3703` edge `-0.0149` maxDD `-15.0497`
- `market_context_high->crypto_major_4h` score `-3.0185` n `214` status `ready` deltaP `2.469` edge `0.025` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7441` n `201` status `ready` deltaP `-2.84` edge `-0.0124` maxDD `-3.7875`
- `market_context_high->equity_4h` score `-7.274` n `214` status `ready` deltaP `4.3609` edge `-0.0746` maxDD `-63.963`
- `market_context_high->metal_24h` score `-13.623` n `201` status `ready` deltaP `-12.2876` edge `-0.0564` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
