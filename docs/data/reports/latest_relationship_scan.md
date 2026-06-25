# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T15:52:26.209399+00:00`
- Price records: `672`
- Market context records: `4737`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7454`

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

- `market_context_high->unknown_1h` score `78.5287` n `142` status `ready` deltaP `14.4619` edge `6.4894` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2659` n `140` status `ready` deltaP `13.9896` edge `0.4666` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.3945` n `131` status `ready` deltaP `16.9967` edge `0.2619` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4565` n `142` status `ready` deltaP `2.528` edge `0.0247` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.5186` n `140` status `ready` deltaP `5.7622` edge `0.0026` maxDD `-5.5999`
- `market_context_high->fx_4h` score `-0.8736` n `140` status `ready` deltaP `-0.3702` edge `-0.0021` maxDD `-1.9274`
- `market_context_high->equity_4h` score `-0.8779` n `140` status `ready` deltaP `3.9808` edge `0.0295` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-0.9525` n `142` status `ready` deltaP `-1.7079` edge `-0.0142` maxDD `-5.3889`
- `market_context_high->fx_1h` score `-1.3456` n `142` status `ready` deltaP `-5.8615` edge `-0.0055` maxDD `-1.0711`
- `market_context_high->commodity_4h` score `-1.5794` n `140` status `ready` deltaP `8.2709` edge `0.024` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5993` n `142` status `ready` deltaP `-3.8037` edge `-0.0075` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.6612` n `142` status `ready` deltaP `-4.4088` edge `-0.0714` maxDD `-15.8975`
- `market_context_high->crypto_alt_1h` score `-2.7758` n `142` status `ready` deltaP `-0.3606` edge `-0.0528` maxDD `-20.053`
- `market_context_high->crypto_major_1h` score `-3.4654` n `142` status `ready` deltaP `-0.5271` edge `-0.0736` maxDD `-26.7065`
- `market_context_high->commodity_24h` score `-4.1066` n `131` status `ready` deltaP `16.4254` edge `0.0607` maxDD `-27.6602`
- `market_context_high->fx_24h` score `-4.7574` n `131` status `ready` deltaP `-14.6376` edge `-0.0203` maxDD `-5.2856`
- `market_context_high->crypto_alt_4h` score `-6.9249` n `140` status `ready` deltaP `-0.723` edge `-0.0928` maxDD `-57.8818`
- `market_context_high->index_24h` score `-8.0931` n `131` status `ready` deltaP `-12.0799` edge `-0.1066` maxDD `-26.6498`
- `market_context_high->metal_4h` score `-8.5304` n `140` status `ready` deltaP `1.5549` edge `-0.2633` maxDD `-62.2565`
- `market_context_high->crypto_major_4h` score `-9.8545` n `140` status `ready` deltaP `-0.3223` edge `-0.2049` maxDD `-79.1746`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
