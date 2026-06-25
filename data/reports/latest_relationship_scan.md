# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T23:22:29.067433+00:00`
- Price records: `672`
- Market context records: `4770`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `8.0223` n `124` status `ready` deltaP `12.628` edge `0.6261` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.4014` n `124` status `ready` deltaP `17.6583` edge `0.6201` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.0729` n `109` status `ready` deltaP `12.0859` edge `0.1845` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.0887` n `124` status `ready` deltaP `11.4133` edge `0.0525` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0607` n `124` status `ready` deltaP `4.9981` edge `0.0305` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.4427` n `124` status `ready` deltaP `2.8767` edge `0.0017` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.5182` n `124` status `ready` deltaP `5.6009` edge `0.0031` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.5984` n `124` status `ready` deltaP `6.191` edge `0.0506` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.9116` n `124` status `ready` deltaP `-1.188` edge `-0.0031` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-1.0243` n `124` status `ready` deltaP `0.058` edge `-0.009` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.4604` n `124` status `ready` deltaP `-2.0378` edge `-0.0077` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.0663` n `109` status `ready` deltaP `20.7696` edge `0.1075` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2711` n `124` status `ready` deltaP `-1.0962` edge `-0.0663` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-3.3535` n `109` status `ready` deltaP `-14.1453` edge `-0.0209` maxDD `-3.474`
- `market_context_high->crypto_alt_1h` score `-3.6553` n `124` status `ready` deltaP `-0.6568` edge `-0.0621` maxDD `-16.3838`
- `market_context_high->crypto_major_1h` score `-4.8936` n `124` status `ready` deltaP `-1.13` edge `-0.0854` maxDD `-22.5224`
- `market_context_high->crypto_alt_4h` score `-5.0791` n `124` status `ready` deltaP `3.8356` edge `-0.0343` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.833` n `109` status `ready` deltaP `-6.1147` edge `-0.1057` maxDD `-19.1697`
- `market_context_high->crypto_major_4h` score `-8.3548` n `124` status `ready` deltaP `2.6358` edge `-0.1656` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.5692` n `124` status `ready` deltaP `4.1798` edge `-0.3024` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
