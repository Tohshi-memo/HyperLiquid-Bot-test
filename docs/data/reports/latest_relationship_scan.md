# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T16:22:33.155452+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6666`

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

- `market_context_high->commodity_24h` score `1.229` n `87` status `ready` deltaP `18.4028` edge `0.0873` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.5522` n `37` status `ready` deltaP `14.3996` edge `0.0171` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.5522` n `37` status `ready` deltaP `14.3996` edge `0.0171` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.4803` n `37` status `ready` deltaP `12.6032` edge `0.0046` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4803` n `37` status `ready` deltaP `12.6032` edge `0.0046` maxDD `-0.1637`
- `risk_on_high->fx_1h` score `0.1398` n `37` status `ready` deltaP `6.1499` edge `0.0028` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1398` n `37` status `ready` deltaP `6.1499` edge `0.0028` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.1362` n `37` status `ready` deltaP `11.1956` edge `0.0226` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1362` n `37` status `ready` deltaP `11.1956` edge `0.0226` maxDD `-1.7154`
- `market_context_high->fx_4h` score `-0.037` n `87` status `ready` deltaP `7.0718` edge `0.0104` maxDD `-0.5168`
- `risk_on_high->fx_4h` score `-0.0678` n `37` status `ready` deltaP `1.6974` edge `0.0064` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0678` n `37` status `ready` deltaP `1.6974` edge `0.0064` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1136` n `87` status `ready` deltaP `2.6705` edge `0.0031` maxDD `-0.1712`
- `risk_on_high->index_4h` score `-0.2153` n `37` status `ready` deltaP `7.9063` edge `0.0042` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2153` n `37` status `ready` deltaP `7.9063` edge `0.0042` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4709` n `87` status `ready` deltaP `0.7296` edge `0.0015` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.4863` n `87` status `ready` deltaP `2.569` edge `-0.004` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.5434` n `37` status `ready` deltaP `-3.6212` edge `0.0049` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.5434` n `37` status `ready` deltaP `-3.6212` edge `0.0049` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.6687` n `87` status `ready` deltaP `1.386` edge `0.0082` maxDD `-2.9203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
