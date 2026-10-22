# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T02:07:27.937889+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8382`

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

- `risk_on_high->equity_1h` score `0.6818` n `37` status `ready` deltaP `16.196` edge `0.0218` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6818` n `37` status `ready` deltaP `16.196` edge `0.0218` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5877` n `37` status `ready` deltaP `14.3996` edge `0.0064` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5877` n `37` status `ready` deltaP `14.3996` edge `0.0064` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.548` n `37` status `ready` deltaP `16.4454` edge `0.0404` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.548` n `37` status `ready` deltaP `16.4454` edge `0.0404` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `0.2538` n `78` status `ready` deltaP `13.3962` edge `0.0508` maxDD `-3.6055`
- `market_context_high->index_1h` score `0.0621` n `78` status `ready` deltaP `6.2222` edge `0.002` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0308` n `37` status `ready` deltaP `4.3535` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0308` n `37` status `ready` deltaP `4.3535` edge `0.0008` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.2204` n `37` status `ready` deltaP `7.5076` edge `0.0062` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2204` n `37` status `ready` deltaP `7.5076` edge `0.0062` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.3346` n `78` status `ready` deltaP `6.0406` edge `0.02` maxDD `-2.9203`
- `risk_on_high->fx_4h` score `-0.3379` n `37` status `ready` deltaP `-2.1022` edge `-0.0029` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3379` n `37` status `ready` deltaP `-2.1022` edge `-0.0029` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3387` n `78` status `ready` deltaP `1.9653` edge `0.01` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.6098` n `78` status `ready` deltaP `-5.681` edge `-0.0028` maxDD `-0.6669`
- `risk_on_high->commodity_1h` score `-0.7685` n `37` status `ready` deltaP `-1.9502` edge `-0.019` maxDD `-0.9891`
- `risk_on_and_context->commodity_1h` score `-0.7685` n `37` status `ready` deltaP `-1.9502` edge `-0.019` maxDD `-0.9891`
- `risk_on_high->metal_1h` score `-0.777` n `37` status `ready` deltaP `-6.1661` edge `0.0024` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
