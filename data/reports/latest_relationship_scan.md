# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T10:22:14.916788+00:00`
- Price records: `637`
- Market context records: `745`
- Flow alert records: `2103`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `12.8495` n `146` status `ready` deltaP `30.5978` edge `0.9002` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6214` n `146` status `ready` deltaP `7.633` edge `0.5057` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.2406` n `146` status `ready` deltaP `1.8992` edge `0.2069` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.3121` n `163` status `ready` deltaP `4.3198` edge `0.003` maxDD `-0.291`
- `market_context_high->equity_24h` score `-0.4044` n `146` status `ready` deltaP `0.2959` edge `0.2248` maxDD `-10.5047`
- `market_context_high->fx_4h` score `-0.4425` n `156` status `ready` deltaP `6.1308` edge `0.0094` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.5163` n `163` status `ready` deltaP `2.0434` edge `0.0408` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.8765` n `163` status `ready` deltaP `1.2319` edge `0.0041` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.0724` n `163` status `ready` deltaP `-1.1304` edge `-0.0008` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0849` n `163` status `ready` deltaP `5.536` edge `-0.0037` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4314` n `163` status `ready` deltaP `4.4224` edge `-0.0173` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5547` n `163` status `ready` deltaP `-4.4379` edge `-0.0228` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.5802` n `156` status `ready` deltaP `17.3727` edge `0.1231` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7689` n `156` status `ready` deltaP `1.6893` edge `-0.0064` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-2.064` n `163` status `ready` deltaP `-4.4089` edge `-0.0393` maxDD `-9.0076`
- `market_context_high->crypto_alt_4h` score `-2.184` n `156` status `ready` deltaP `2.3969` edge `0.059` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5871` n `156` status `ready` deltaP `-1.228` edge `0.0078` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.6995` n `156` status `ready` deltaP `-5.5791` edge `0.079` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.766` n `156` status `ready` deltaP `5.0074` edge `-0.1594` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.3954` n `146` status `ready` deltaP `-15.7394` edge `-0.0696` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
