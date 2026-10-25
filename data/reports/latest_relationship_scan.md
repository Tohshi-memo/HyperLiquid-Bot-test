# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T05:22:35.382103+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7740`

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

- `market_context_high->unknown_4h` score `51.7917` n `95` status `ready` deltaP `-0.0593` edge `4.3499` maxDD `-1.016`
- `market_context_high->unknown_1h` score `18.3871` n `107` status `ready` deltaP `3.7271` edge `1.5563` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `7.7762` n `37` status `ready` deltaP `27.4118` edge `0.6141` maxDD `-10.5732`
- `market_context_high->crypto_major_24h` score `1.5939` n `37` status `ready` deltaP `16.2772` edge `0.1701` maxDD `-8.3301`
- `market_context_high->commodity_24h` score `0.6908` n `37` status `ready` deltaP `14.1705` edge `0.085` maxDD `-3.6055`
- `market_context_high->fx_1h` score `-0.1183` n `107` status `ready` deltaP `2.5267` edge `0.0029` maxDD `-0.1258`
- `market_context_high->fx_24h` score `-0.1414` n `37` status `ready` deltaP `7.6295` edge `0.0052` maxDD `-0.9352`
- `market_context_high->fx_4h` score `-0.3153` n `95` status `ready` deltaP `1.8036` edge `0.0074` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.3424` n `107` status `ready` deltaP `5.8929` edge `-0.004` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3724` n `107` status `ready` deltaP `-0.8073` edge `0.0077` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5297` n `107` status `ready` deltaP `0.3582` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.7518` n `95` status `ready` deltaP `-3.3135` edge `0.0361` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.129` n `107` status `ready` deltaP `3.8293` edge `-0.0122` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.9244` n `95` status `ready` deltaP `5.2006` edge `-0.024` maxDD `-5.3498`
- `market_context_high->equity_1h` score `-2.2989` n `107` status `ready` deltaP `2.7897` edge `-0.086` maxDD `-12.1865`
- `market_context_high->metal_24h` score `-2.3881` n `37` status `ready` deltaP `-3.8992` edge `-0.0319` maxDD `-6.2888`
- `market_context_high->crypto_alt_1h` score `-2.5952` n `107` status `ready` deltaP `0.5079` edge `-0.0406` maxDD `-11.3243`
- `market_context_high->index_4h` score `-3.3253` n `95` status `ready` deltaP `-7.2706` edge `-0.0412` maxDD `-4.3282`
- `market_context_high->crypto_major_4h` score `-5.6843` n `95` status `ready` deltaP `-7.423` edge `-0.1733` maxDD `-33.8105`
- `market_context_high->index_24h` score `-6.6915` n `37` status `ready` deltaP `-33.5117` edge `-0.2007` maxDD `-5.3475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
