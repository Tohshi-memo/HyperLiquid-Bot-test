# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T07:52:31.524568+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7662`

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

- `market_context_high->commodity_24h` score `0.6086` n `82` status `ready` deltaP `16.5438` edge `0.0753` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.4312` n `37` status `ready` deltaP `12.0044` edge `0.0023` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4312` n `37` status `ready` deltaP `12.0044` edge `0.0023` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4236` n `37` status `ready` deltaP `14.1002` edge `0.0026` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4236` n `37` status `ready` deltaP `14.1002` edge `0.0026` maxDD `-0.7172`
- `risk_on_high->commodity_24h` score `0.2841` n `37` status `ready` deltaP `11.3692` edge `0.0404` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2841` n `37` status `ready` deltaP `11.3692` edge `0.0404` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1546` n `37` status `ready` deltaP `6.4493` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1546` n `37` status `ready` deltaP `6.4493` edge `0.0027` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0669` n `37` status `ready` deltaP `1.8498` edge `0.0055` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0669` n `37` status `ready` deltaP `1.8498` edge `0.0055` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.0945` n `82` status `ready` deltaP `3.6147` edge `0.0035` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.1149` n `82` status `ready` deltaP `5.6402` edge `0.0083` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.3322` n `82` status `ready` deltaP `2.5449` edge `-0.0059` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.4978` n `37` status `ready` deltaP `-3.1721` edge `0.0057` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4978` n `37` status `ready` deltaP `-3.1721` edge `0.0057` maxDD `-0.0831`
- `risk_on_high->index_4h` score `-0.5138` n `37` status `ready` deltaP `4.4002` edge `-0.0107` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.5138` n `37` status `ready` deltaP `4.4002` edge `-0.0107` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.5257` n `82` status `ready` deltaP `-0.084` edge `-0.0001` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6136` n `82` status `ready` deltaP `0.7622` edge `0.015` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
