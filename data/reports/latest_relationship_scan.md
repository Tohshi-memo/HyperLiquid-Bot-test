# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T22:22:33.704038+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

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

- `market_context_high->fx_1h` score `0.8386` n `72` status `ready` deltaP `13.5479` edge `0.0017` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.5035` n `69` status `ready` deltaP `10.8673` edge `0.0091` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.2031` n `72` status `ready` deltaP `6.7947` edge `0.0039` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.0553` n `72` status `ready` deltaP `2.9275` edge `0.008` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2321` n `72` status `ready` deltaP `5.7884` edge `-0.0081` maxDD `-2.1532`
- `market_context_high->metal_4h` score `-0.353` n `69` status `ready` deltaP `2.7837` edge `0.0084` maxDD `-0.4441`
- `market_context_high->index_1h` score `-0.4628` n `72` status `ready` deltaP `-1.0479` edge `-0.003` maxDD `-0.2813`
- `market_context_high->crypto_major_1h` score `-1.2236` n `72` status `ready` deltaP `-4.4661` edge `0.0004` maxDD `-7.5329`
- `market_context_high->commodity_4h` score `-2.4245` n `69` status `ready` deltaP `-22.1611` edge `-0.0053` maxDD `-2.9572`
- `market_context_high->equity_4h` score `-3.6479` n `69` status `ready` deltaP `-16.6667` edge `-0.1529` maxDD `-6.9605`
- `market_context_high->index_4h` score `-4.1857` n `69` status `ready` deltaP `-22.9211` edge `-0.0212` maxDD `-0.984`
- `market_context_high->crypto_alt_1h` score `-4.3874` n `72` status `ready` deltaP `-9.3563` edge `-0.1079` maxDD `-11.9607`
- `market_context_high->crypto_major_4h` score `-9.2246` n `69` status `ready` deltaP `-9.1972` edge `-0.2569` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-19.6232` n `69` status `ready` deltaP `-32.3833` edge `-0.6599` maxDD `-49.4247`
- `market_context_high->unknown_4h` score `-555.0166` n `69` status `ready` deltaP `4.4958` edge `-46.2764` maxDD `-0.063`
- `market_context_high->unknown_1h` score `-1301.2111` n `72` status `ready` deltaP `1.4388` edge `-108.4322` maxDD `-0.2652`
- `news_risk_high->unknown_1h` score `2911.3819` n `25` status `thin_sample` deltaP `8.3832` edge `291.0823` maxDD `0.0`
- `news_risk_high->unknown_4h` score `236.2553` n `25` status `thin_sample` deltaP `5.9451` edge `23.5859` maxDD `0.0`
- `risk_on_high->unknown_4h` score `27.4994` n `2` status `thin_sample` deltaP `5.9451` edge `34.3346` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `27.4994` n `2` status `thin_sample` deltaP `5.9451` edge `34.3346` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
