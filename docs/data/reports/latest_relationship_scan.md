# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T11:22:29.177546+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `11860.469` n `109` status `ready` deltaP `0.798` edge `988.3869` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7364.0166` n `109` status `ready` deltaP `0.1301` edge `613.6956` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `13.9505` n `95` status `ready` deltaP `41.9463` edge `1.7123` maxDD `-13.9399`
- `market_context_high->crypto_alt_24h` score `11.0122` n `95` status `ready` deltaP `22.6956` edge `1.4334` maxDD `-10.1635`
- `market_context_high->crypto_major_4h` score `0.4554` n `109` status `ready` deltaP `2.1271` edge `0.3417` maxDD `-17.4668`
- `market_context_high->crypto_alt_4h` score `0.1321` n `109` status `ready` deltaP `2.5844` edge `0.2214` maxDD `-13.4025`
- `market_context_high->metal_24h` score `-0.0208` n `95` status `ready` deltaP `16.2902` edge `0.1985` maxDD `-14.7068`
- `market_context_high->metal_4h` score `-0.075` n `109` status `ready` deltaP `14.946` edge `0.0231` maxDD `-5.9858`
- `market_context_high->metal_1h` score `-0.276` n `109` status `ready` deltaP `2.8347` edge `0.0122` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.7397` n `109` status `ready` deltaP `-1.1344` edge `0.0031` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.836` n `109` status `ready` deltaP `2.5353` edge `0.0624` maxDD `-10.2523`
- `market_context_high->crypto_alt_1h` score `-1.1277` n `109` status `ready` deltaP `-2.8004` edge `0.0244` maxDD `-7.6911`
- `market_context_high->index_4h` score `-1.2101` n `109` status `ready` deltaP `-3.0613` edge `-0.0004` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.5234` n `109` status `ready` deltaP `-10.6274` edge `-0.0012` maxDD `-0.392`
- `market_context_high->fx_4h` score `-2.4317` n `109` status `ready` deltaP `-15.4761` edge `-0.0044` maxDD `-2.0011`
- `market_context_high->commodity_1h` score `-2.5036` n `109` status `ready` deltaP `-10.9076` edge `-0.0281` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.6121` n `109` status `ready` deltaP `1.4682` edge `-0.0196` maxDD `-10.9626`
- `market_context_high->fx_24h` score `-6.8068` n `95` status `ready` deltaP `-19.7588` edge `-0.0058` maxDD `-5.7098`
- `market_context_high->commodity_4h` score `-7.6879` n `109` status `ready` deltaP `-25.7063` edge `-0.1074` maxDD `-14.9509`
- `market_context_high->index_24h` score `-9.3638` n `95` status `ready` deltaP `-17.924` edge `-0.1186` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
